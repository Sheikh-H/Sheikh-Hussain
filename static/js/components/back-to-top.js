const backToTopButton = document.querySelector(".back-to-top-button");
const topViewer = document.querySelector(".screen-view");

const observer = new IntersectionObserver(
  (entry) => {
    if (entry[0].intersectionRatio >= 0.5) {
      backToTopButton.classList.remove("active");
    } else {
      backToTopButton.classList.add("active");
    }
  },
  {
    threshold: [0, 0.5],
  },
);

observer.observe(topViewer);

backToTopButton.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});
