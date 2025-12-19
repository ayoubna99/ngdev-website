// NAVBAR SCROLL EFFECT
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
  if (!navbar) return;
  navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// MOBILE MENU TOGGLE
const mobileMenu = document.querySelector('.mobile-menu');
const navLinks = document.querySelector('.nav-links');
const navLinkItems = document.querySelectorAll('.nav-links a');

if (mobileMenu && navLinks) {
  mobileMenu.addEventListener('click', () => {
    navLinks.classList.toggle('mobile-active');
  });

  navLinkItems.forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('mobile-active');
    });
  });
}

// FADE-IN ANIMATIONS
const fadeElements = document.querySelectorAll('.fade-in');

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

  fadeElements.forEach(el => observer.observe(el));
} else {
  fadeElements.forEach(el => el.classList.add('visible'));
}

// LOADING SCREEN (simple)
document.addEventListener('DOMContentLoaded', () => {
  const loading = document.querySelector('.loading');
  if (loading) {
    loading.classList.add('hidden');
    setTimeout(() => {
      if (loading.parentNode) loading.parentNode.removeChild(loading);
    }, 600);
  }
});
