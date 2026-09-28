const about = document.querySelector(".about-section");
const intro = document.querySelector(".intro-section");
const projects = document.querySelectorAll(".project");
const contact = document.querySelector(".contact-section");
const skills = document.querySelectorAll(".skill-card");

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

const skillCards = document.querySelectorAll(".skill-card");

const skillObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const bar = entry.target.querySelector(".skill-grade-inner");
        const duration = Number(bar.dataset.duration);
        const percent = Math.min((duration / 36) * 100, 100);
        entry.target.classList.add("active");
        setTimeout(() => {
          bar.style.width = `${percent}%`;
        }, 200);
        skillObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.2,
  },
);

skillCards.forEach((card) => {
  skillObserver.observe(card);
});

skills.forEach((skill) => {
  skillObserver.observe(skill);
});

projects.forEach((project) => {
  observer.observe(project);
});
observer.observe(contact);
