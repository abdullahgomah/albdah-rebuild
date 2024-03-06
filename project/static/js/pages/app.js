var swiper = new Swiper(".mySwiper", {
    freeMode: true,
    slidesPerView: 1,
    loop: true, 
    spaceBetween: 30, 
    minimumVelocity: 1, 
    momentum: false, 
    sticky: true, 
    breakpoints: {
      320: {
        slidesPerView: 4,
        spaceBetween: 20
      },
      640: {
        slidesPerView: 7,
        spaceBetween: 30
      }
    }
    /*pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },*/
  });


// Make navbar responsive 

