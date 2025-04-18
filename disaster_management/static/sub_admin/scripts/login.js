function validateForm() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var emailInput = document.getElementById("email");
    var passwordInput = document.getElementById("password");
    var emailError = document.getElementById("emailError");
    var passwordError = document.getElementById("passwordError");
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var valid = true;

    // Reset error messages and styles
    emailError.innerHTML = "";
    passwordError.innerHTML = "";
    emailInput.classList.remove("invalid");
    passwordInput.classList.remove("invalid");

    // Validate email format
    if (email.trim() === "") {
        emailError.innerHTML = "Email is required";
        emailInput.classList.add("invalid");
        valid = false;
    } else if (!emailRegex.test(email)) {
        emailError.innerHTML = "Invalid email format";
        emailInput.classList.add("invalid");
        valid = false;
    }

    // Validate password
    if (password.trim() === "") {
        passwordError.innerHTML = "Password is required";
        passwordInput.classList.add("invalid");
        valid = false;
    } 

    return valid;
}