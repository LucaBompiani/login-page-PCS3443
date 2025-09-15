// API Configuration
const API_BASE_URL = 'http://localhost:8000/api/v1';

// DOM Elements
const authSection = document.getElementById('auth-section');
const dashboardSection = document.getElementById('dashboard-section');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');
const messageDiv = document.getElementById('message');
const userLoginSpan = document.getElementById('userLogin');
const userEmailSpan = document.getElementById('userEmail');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    // Check if user is already logged in
    const token = localStorage.getItem('access_token');
    if (token) {
        // Verify token and get user info
        getUserInfo();
    } else {
        showAuthSection();
    }

    // Add form event listeners
    loginForm.addEventListener('submit', handleLogin);
    registerForm.addEventListener('submit', handleRegister);
});

// Form switching functions
function showLoginForm() {
    document.getElementById('login-form').classList.add('active');
    document.getElementById('register-form').classList.remove('active');
}

function showRegisterForm() {
    document.getElementById('register-form').classList.add('active');
    document.getElementById('login-form').classList.remove('active');
}

// Show/hide sections
function showAuthSection() {
    authSection.classList.remove('hidden');
    dashboardSection.classList.add('hidden');
}

function showDashboardSection() {
    authSection.classList.add('hidden');
    dashboardSection.classList.remove('hidden');
}

// Message display functions
function showMessage(text, type = 'success') {
    messageDiv.textContent = text;
    messageDiv.className = `message ${type}`;
    messageDiv.classList.remove('hidden');
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        messageDiv.classList.add('hidden');
    }, 5000);
}

// API Functions
async function makeApiRequest(url, options = {}) {
    try {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            },
            ...options
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Erro na requisição');
        }

        return data;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// Login function
async function handleLogin(event) {
    event.preventDefault();
    
    const formData = new FormData(loginForm);
    const loginData = {
        username: formData.get('username'),
        password: formData.get('password')
    };

    try {
        // Create FormData for OAuth2PasswordRequestForm
        const oauthFormData = new FormData();
        oauthFormData.append('username', loginData.username);
        oauthFormData.append('password', loginData.password);

        const response = await fetch(`${API_BASE_URL}/auth/token`, {
            method: 'POST',
            body: oauthFormData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Erro no login');
        }

        // Store token
        localStorage.setItem('access_token', data.access_token);
        
        // Get user info and show dashboard
        await getUserInfo();
        showMessage('Login realizado com sucesso!');
        
    } catch (error) {
        showMessage(error.message, 'error');
    }
}

// Register function
async function handleRegister(event) {
    event.preventDefault();
    
    const formData = new FormData(registerForm);
    const userData = {
        login: formData.get('login'),
        email: formData.get('email'),
        password: formData.get('password')
    };

    try {
        await makeApiRequest(`${API_BASE_URL}/users/`, {
            method: 'POST',
            body: JSON.stringify(userData)
        });

        showMessage('Usuário cadastrado com sucesso! Faça login para continuar.');
        showLoginForm();
        registerForm.reset();
        
    } catch (error) {
        showMessage(error.message, 'error');
    }
}

// Get user info function
async function getUserInfo() {
    const token = localStorage.getItem('access_token');
    if (!token) {
        showAuthSection();
        return;
    }

    try {
        // Since there's no specific endpoint to get current user info,
        // we'll decode the token to get the username and show it
        // In a real application, you'd have a /me endpoint
        
        // For now, we'll show a simple message with the token info
        // You can decode the JWT token on the client side to get the username
        const tokenParts = token.split('.');
        const payload = JSON.parse(atob(tokenParts[1]));
        const username = payload.sub;

        // Display user info (we now have both login and email from the token)
        userLoginSpan.textContent = username;
        userEmailSpan.textContent = payload.email || 'Email não disponível';
        
        showDashboardSection();
        
    } catch (error) {
        console.error('Error getting user info:', error);
        // If token is invalid, remove it and show auth section
        localStorage.removeItem('access_token');
        showAuthSection();
        showMessage('Sessão expirada. Faça login novamente.', 'error');
    }
}

// Logout function
function logout() {
    localStorage.removeItem('access_token');
    showAuthSection();
    showMessage('Logout realizado com sucesso!');
    
    // Reset forms
    loginForm.reset();
    registerForm.reset();
    showLoginForm();
}

// Utility function to decode JWT token (for demonstration)
function decodeJWT(token) {
    try {
        const parts = token.split('.');
        if (parts.length !== 3) {
            throw new Error('Invalid token format');
        }
        
        const payload = parts[1];
        const decoded = atob(payload);
        return JSON.parse(decoded);
    } catch (error) {
        console.error('Error decoding token:', error);
        return null;
    }
}
