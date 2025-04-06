document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');

    fetch('http://127.0.0.1:8000/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Login failed');
        }
        return response.json();
    })
    .then(data => {
        // Store the token in localStorage
        localStorage.setItem('authToken', data.token);
        localStorage.setItem('username', data.username);
        
        // Redirect to home page or dashboard
        window.location.href = 'index.html';
    })
    .catch(error => {
        errorMessage.textContent = 'Invalid username or password';
        console.error('Error:', error);
    });
});

// Function to check if user is logged in
function isLoggedIn() {
    return localStorage.getItem('authToken') !== null;
}

// Function to logout
function logout() {
    localStorage.removeItem('authToken');
    localStorage.removeItem('username');
    window.location.href = 'login.html';
}

// Add this to your existing app.js fetchTeams function
function fetchTeams() {
    const token = localStorage.getItem('authToken');
    
    fetch('http://127.0.0.1:8000/api/teams/', {
        headers: {
            'Authorization': `Token ${token}`
        }
    })
    .then(response => {
        if (!response.ok) {
            if (response.status === 401) {
                // Unauthorized, redirect to login
                window.location.href = 'login.html';
                return;
            }
            throw new Error(`HTTP error: ${response.status}`);
        }
        return response.json();
    })
    // .fetchTeams code ...
}
