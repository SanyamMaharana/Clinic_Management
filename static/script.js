document.querySelector("form").addEventListener("submit", function(event) {
  const username = document.getElementById("username") || document.getElementById("newUsername");
  const password = document.getElementById("password") || document.getElementById("newPassword");
  const confirmPassword = document.getElementById("confirmPassword");

  if (username.value === "" || password.value === "") {
      alert("Please fill in both fields");
      event.preventDefault();
  }

  if (confirmPassword && password.value !== confirmPassword.value) {
      alert("Passwords do not match");
      event.preventDefault();
  }
});