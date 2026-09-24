const nightModeButton = document.querySelector(".dark-mode-button");
const nightModeInnerButton = document.querySelector(".dark-mode-inner-button");
function toggleNightMode() {
  if (localStorage.getItem("dark-mode") === "enabled") {
    document.documentElement.classList.add("dark-mode");
    if (nightModeButton) {
      nightModeButton.classList.add("active");
      nightModeInnerButton.classList.add("active");
    }
  }
  if (nightModeButton) {
    nightModeButton.addEventListener("click", () => {
      nightModeButton.classList.toggle("active");
      nightModeInnerButton.classList.toggle("active");
      document.documentElement.classList.toggle("dark-mode");
      if (document.documentElement.classList.contains("dark-mode")) {
        localStorage.setItem("dark-mode", "enabled");
      } else {
        localStorage.setItem("dark-mode", "disabled");
      }
    });
  }
}
toggleNightMode();
