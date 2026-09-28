const about = document.querySelector(".about-section");
const intro = document.querySelector(".intro-section");
const projects = document.querySelectorAll(".project");
const contact = document.querySelector(".contact-section");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
      }
    });
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
observer.observe(contact);
