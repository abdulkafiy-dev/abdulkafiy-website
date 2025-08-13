let loginForm = document.getElementById('loginForm');
const username = document.getElementById('username');
const password = document.getElementById('password');

loginForm = document.addEventListener('submit', validateForm);

function validateForm(event) {
    if (username.value.trim() === '' && password.value.trim() === '') {
        alert('Username & Password Required!');
        event.preventDefault();
    }

    else if (username.value.trim() !== '' && password.value.trim() === '') {
        alert('Password Required!')
        event.preventDefault();
    }

    else if (password.value.trim() !== '' && username.value.trim() === '') {
        alert('Username Required!')
        event.preventDefault();
    }

    else if (password.value.trim().length < 8) {
        alert('Password must be at least 8 characters in length!');
        event.preventDefault();
    }
}
