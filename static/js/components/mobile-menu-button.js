const mobileMenuButton = document.querySelector(".mobile-menu-button");
const mobileMenuNav = document.querySelector(".menu-nav");
const mobileMenuItem = document.querySelector(".menu-item");
const mobileMenuHeader = document.querySelector(".header");

function toggleMobileMenu() {
  if (mobileMenuButton) {
    mobileMenuButton.addEventListener("click", () => {
      mobileMenuButton.classList.toggle("active");
      mobileMenuNav.classList.toggle("active");
      mobileMenuItem.classList.toggle("active");
      mobileMenuHeader.classList.toggle("active");
    });
  }
}

function menuOpen() {
  document.addEventListener("click", (event) => {
    if (
      mobileMenuButton.classList.contains("active") &&
      !mobileMenuNav.contains(event.target) &&
      !mobileMenuButton.contains(event.target)
    ) {
      mobileMenuButton.classList.remove("active");
      mobileMenuNav.classList.remove("active");
      mobileMenuItem.classList.remove("active");
      mobileMenuHeader.classList.remove("active");
    }
  });
}

toggleMobileMenu();
