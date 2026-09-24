const backToTopButton = document.querySelector(".top-button");

document.addEventListener("scroll", () => {
  backToTopButton.classList.toggle("active");
});
