setTimeout(() => {
  const flashes = document.querySelectorAll(".flash");
  flashes.forEach((flash) => {
    flash.remove();
  });
}, 3000);
