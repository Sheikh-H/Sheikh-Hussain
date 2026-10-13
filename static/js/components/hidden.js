const about = document.querySelector(".about-section");
const intro = document.querySelector(".intro-section");
const projects = document.querySelectorAll(".project");
const skills = document.querySelectorAll(".skill-card");
const projectCards = document.querySelectorAll(".project-item");

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

if (intro) {
  observer.observe(intro);
}

if (about) {
  observer.observe(about);
}

const skillObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        const bar = entry.target.querySelector(".skill-grade-inner");
        const duration = Number(bar.dataset.duration) || 0;
        const percent = Math.min((duration / 36) * 100, 100);
        setTimeout(() => {
          bar.style.width = `${percent}%`;
        }, 800);
        skillObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.1,
  },
);

if (skills) {
  skills.forEach((skill) => {
    skillObserver.observe(skill);
  });
}

if (projects) {
  projects.forEach((project) => {
    observer.observe(project);
  });
}

if (projectCards) {
  projectCards.forEach((item) => {
    observer.observe(item);
  });
}
