const about = document.querySelector(".about-section");
const intro = document.querySelector(".intro-section");

const projects = document.querySelectorAll(".project");

const observer = new IntersectionObserver(
  (entry) => {
    if (entry[0].intersectionRatio >= 0.1) {
      entry[0].target.classList.add("active");
    }
  },
  {
    threshold: 0.1,
  },
);

observer.observe(intro);
observer.observe(about);

projects.forEach((project) => {
  observer.observe(project);
});
