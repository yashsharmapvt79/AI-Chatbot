document.addEventListener("DOMContentLoaded", function() {
    const signupForm = document.getElementById("signupForm");
    const signupErrorMessage = document.getElementById("signupErrorMessage");

    signupForm.addEventListener("submit", function(event) {
        event.preventDefault();

        // Retrieve form data
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const confirmPassword = document.getElementById("confirmPassword").value;

        // Perform basic validation
        if (password !== confirmPassword) {
            signupErrorMessage.textContent = "Passwords do not match!";
            return;
        }

        // Send form data to backend for further processing (e.g., saving to a file or database)
        // Here, you can use AJAX, Fetch API, or any other method to send the data to the server

        // For demonstration purposes, we'll just log the data to the console
        console.log("Signup form submitted:");
        console.log("Username:", username);
        console.log("Email:", email);
        console.log("Password:", password);

        // Reset form and error message
        signupForm.reset();
        signupErrorMessage.textContent = "";
    });
});
