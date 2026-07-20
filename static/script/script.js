const checkbox = document.querySelector(".hamburger input");
const slider = document.querySelector(".mobile-menu-slider");
const mobileNavItem = document.querySelectorAll(".mobile-nav-item");

checkbox.addEventListener("change", () => {
  slider.classList.toggle("active", checkbox.checked);
  document.body.classList.toggle("menu-open", checkbox.checked);
});

mobileNavItem.forEach((item) => {
  item.addEventListener("click", () => {
    if (document.body.classList.contains("menu-open")) {
      document.body.classList.remove("menu-open");
      slider.classList.remove("active");
      checkbox.checked = false;
    }
  });
});

document.querySelectorAll(".project-tags").forEach((container) => {
  const track = container.querySelector(".project-tags-track");

  const overflow = track.scrollWidth - container.clientWidth;

  if (overflow > 0) {
    let timeout;

    container.addEventListener("mouseenter", () => {
      timeout = setTimeout(() => {
        track.style.transform = `translateX(-${overflow}px)`;
      }, 300);
    });

    container.addEventListener("mouseleave", () => {
      clearTimeout(timeout);

      track.style.transform = "translateX(0)";
    });
  }
});

const observer = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.2,
  },
);

const elements = document.querySelectorAll(
  ".hidden-right, .hidden-left, .hidden-up",
);
elements.forEach((element) => observer.observe(element));

const skillCards = document.querySelectorAll(".skill-card");

skillCards.forEach((card, index) => {
  card.style.transitionDelay = `${index * 500}ms`;
});

const projectCards = document.querySelectorAll(".project-card");

projectCards.forEach((card, index) => {
  card.style.transitionDelay = `${index * 500}ms`;
});

setTimeout(() => {
  const flashes = document.querySelectorAll(".flash");

  flashes.forEach((flash) => {
    flash.remove();
  });
}, 3000);

const themeSwitch = document.querySelector("#dark-switch input");

themeSwitch.addEventListener("change", () => {
  document.documentElement.classList.toggle("dark-mode");

  const theme = document.documentElement.classList.contains("dark-mode")
    ? "light"
    : "dark";

  localStorage.setItem("theme", theme);
});
