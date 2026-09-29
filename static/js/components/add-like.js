const likeButtons = document.querySelectorAll(".project-like");

async function addLike(projectId, csrf) {
  const response = await fetch(`/add-like/${projectId}`, {
    method: "POST",
    headers: { "X-CSRFTOKEN": csrf },
  });
  if (!response.ok) {
    throw new Error("Failed to add like!");
  }
  window.location.reload();
}

likeButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const projectId = button.dataset.projectId;
    const csrf = button.dataset.csrf;
    addLike(projectId, csrf);
  });
});
