// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form submission handling
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Get form data
        const formData = new FormData(this);
        const data = Object.fromEntries(formData);

        // Here you would typically send the data to your server
        console.log('Form submitted:', data);

        // Show success message
        alert('Thank you for your message! We will get back to you soon.');
        this.reset();
    });
}

// Login/Signup button functionality
const loginBtn = document.querySelector('.login-btn');
const signupBtn = document.querySelector('.signup-btn');

if (loginBtn) {
    loginBtn.addEventListener('click', function () {
        window.location.href = "/login";
    });
}

if (signupBtn) {
    signupBtn.addEventListener('click', function () {
        window.location.href = "/signup";
    });
}

//Toggle password visibility
function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    const toggleIcon = document.querySelector('.toggle-password');

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text'; 
        toggleIcon.classList.remove('fa-eye');  
        toggleIcon.classList.add('fa-eye-slash'); 
        passwordInput.style.paddingLeft = '35px'; 
    } else {
        passwordInput.type = 'password'; 
        toggleIcon.classList.remove('fa-eye-slash'); 
        toggleIcon.classList.add('fa-eye'); 
    }
}

// CTA button functionality
const ctaButton = document.querySelector('.cta-button');
if (ctaButton) {
    ctaButton.addEventListener('click', function () {
        // Here you would typically redirect to signup or show a modal
        alert('Get started with FitPal today!');
    });
}

// Add animation to feature cards when they come into view
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.5s ease-out';
    observer.observe(card);
});

// Mobile menu toggle (to be implemented)
// This would be used when we add a mobile menu button
const mobileMenuToggle = () => {
    const navLinks = document.querySelector('.nav-links');
    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
};

// Add scroll event listener for navbar
window.addEventListener('scroll', function () {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = '0 2px 5px rgba(0,0,0,0.1)';
    } else {
        navbar.style.backgroundColor = 'var(--white)';
        navbar.style.boxShadow = 'none';
    }
}); 
