var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 10, 

    /*pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },*/
  });


// Make navbar responsive 

var headerSlider = new Swiper('.slider', {
  slidesPerView: 3,
  spaceBetween: 10,
  loop: true,
  breakpoints: {
    // when window width is <= 640px
    640: {
      slidesPerView: 1,
      spaceBetween: 10
    },


  }
});