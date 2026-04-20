// Auto-dismiss flash messages after 4 seconds
document.addEventListener("DOMContentLoaded", () => {
  const flashes = document.querySelectorAll(".flash");
  flashes.forEach((flash) => {
    setTimeout(() => {
      flash.style.opacity = "0";
      flash.style.transform = "translateX(20px)";
      flash.style.transition = "all 0.3s ease";
      setTimeout(() => flash.remove(), 300);
    }, 4000);
  });
});
