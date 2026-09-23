const nightModeButton = document.querySelector(".dark-mode-button");

function toggleNightMode() {
  if (localStorage.getItem("dark-mode") === "enabled") {
    document.documentElement.classList.add("dark-mode");
    if (nightModeButton) {
      nightModeButton.classList.add("active");
    }
  }
  if (nightModeButton) {
    nightModeButton.addEventListener("click", () => {
      nightModeButton.classList.toggle("active");
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
