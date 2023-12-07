// Your JavaScript code goes here
document.addEventListener("DOMContentLoaded", function () {

  const hambuger = document.querySelector('.hambuger');
  const navMenu = document.querySelector('.nav-menu');
  hambuger.addEventListener("click", mobileMenu);

  function mobileMenu() {
    hambuger.classList.toggle("active");
    navMenu.classList.toggle("active");
  }

  const navLink = document.querySelectorAll('.nav-link');

  navLink.forEach((n) => n.addEventListener("click", closeMenu));

  function closeMenu() {
    hambuger.classList.remove("active");
    navMenu.classList.remove("active");
  }
});
