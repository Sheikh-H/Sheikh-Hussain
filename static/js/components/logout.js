const logoutButton = document.querySelector("#logout-button");

async function logout(button) {
  const csrf = button.dataset.csrf;
  const response = await fetch(logoutButton.href, {
    method: "POST",
    headers: {
      "X-CSRFTOKEN": csrf,
    },
  });

  if (response.ok) {
    window.location.href = "/";
  }
}

if (logoutButton) {
  logoutButton.addEventListener("click", (event) => {
    event.preventDefault();
    logout(logoutButton);
  });
}
