const mobileMenuButton = document.querySelector(".mobile-menu-button");

function toggleMobileMenu() {
  if (mobileMenuButton) {
    mobileMenuButton.addEventListener("click", () => {
      mobileMenuButton.classList.toggle("active");
    });
  }
}

toggleMobileMenu();
