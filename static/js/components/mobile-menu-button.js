const mobileMenuButton = document.querySelector(".mobile-menu-button");
const mobileMenuNav = document.querySelector(".menu-nav");
const mobileMenuItem = document.querySelector(".menu-item");
const mobileMenuHeader = document.querySelector(".header");

const menuItems = document.querySelectorAll(".menu-item");

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

function menuClose() {
  menuItems.forEach((item) => {
    item.addEventListener("click", () => {
      if (mobileMenuButton.classList.contains("active")) {
        mobileMenuButton.classList.remove("active");
        mobileMenuNav.classList.remove("active");
        mobileMenuItem.classList.remove("active");
        mobileMenuHeader.classList.remove("active");
      }
    });
  });
}

toggleMobileMenu();
menuOpen();
menuClose();
