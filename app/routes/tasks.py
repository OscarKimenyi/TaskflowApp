from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import db, csrf
from app.models import Task
from app.forms import TaskForm
from datetime import datetime

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("tasks.dashboard"))
    return render_template("index.html")


@tasks_bp.route("/dashboard")
@login_required
def dashboard():
    filter_status = request.args.get("status", "all")
    filter_priority = request.args.get("priority", "all")
    filter_category = request.args.get("category", "all")
    sort_by = request.args.get("sort", "created_at")
    search_query = request.args.get("q", "")

    query = Task.query.filter_by(user_id=current_user.id)

    if search_query:
        query = query.filter(Task.title.ilike(f"%{search_query}%"))

    if filter_status == "active":
        query = query.filter_by(completed=False)
    elif filter_status == "completed":
        query = query.filter_by(completed=True)

    if filter_priority != "all":
        query = query.filter_by(priority=filter_priority)

    if filter_category != "all":
        query = query.filter_by(category=filter_category)

    if sort_by == "due_date":
        query = query.order_by(Task.due_date.asc().nullslast())
    elif sort_by == "priority":
        priority_order = db.case({"high": 1, "medium": 2, "low": 3}, value=Task.priority)
        query = query.order_by(priority_order)
    elif sort_by == "title":
        query = query.order_by(Task.title.asc())
    else:
        query = query.order_by(Task.created_at.desc())

    tasks = query.all()

    all_tasks = Task.query.filter_by(user_id=current_user.id).all()
    categories = list(set(t.category for t in all_tasks if t.category))
    total = len(all_tasks)
    completed = sum(1 for t in all_tasks if t.completed)
    overdue = sum(1 for t in all_tasks if t.is_overdue())

    return render_template(
        "tasks/dashboard.html",
        tasks=tasks,
        categories=categories,
        total=total,
        completed=completed,
        overdue=overdue,
        filter_status=filter_status,
        filter_priority=filter_priority,
        filter_category=filter_category,
        sort_by=sort_by,
        search_query=search_query,
    )


@tasks_bp.route("/tasks/new", methods=["GET", "POST"])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            category=form.category.data.strip() if form.category.data else None,
            due_date=form.due_date.data,
            user_id=current_user.id,
        )
        db.session.add(task)
        db.session.commit()
        flash("Task created!", "success")
        return redirect(url_for("tasks.dashboard"))

    return render_template("tasks/task_form.html", form=form, title="New Task", action="Create")


@tasks_bp.route("/tasks/<int:task_id>/edit", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    form = TaskForm(obj=task)

    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.priority = form.priority.data
        task.category = form.category.data.strip() if form.category.data else None
        task.due_date = form.due_date.data
        task.updated_at = datetime.utcnow()
        db.session.commit()
        flash("Task updated!", "success")
        return redirect(url_for("tasks.dashboard"))

    return render_template("tasks/task_form.html", form=form, title="Edit Task", action="Update", task=task)


@tasks_bp.route("/tasks/<int:task_id>/toggle", methods=["POST"])
@login_required
@csrf.exempt
def toggle_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"completed": task.completed, "id": task.id})


@tasks_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "info")
    return redirect(url_for("tasks.dashboard"))
