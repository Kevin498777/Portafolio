// Navbar scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.style.backgroundColor = 'rgba(13, 17, 23, 0.98)';
    } else {
        navbar.style.backgroundColor = 'rgba(13, 17, 23, 0.85)';
    }
});

// Animación de barras de progreso al hacer scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.querySelectorAll('.progress-bar').forEach(bar => {
                bar.style.width = bar.style.width;
            });
        }
    });
}, { threshold: 0.3 });

document.querySelectorAll('.skill-card').forEach(card => observer.observe(card));
