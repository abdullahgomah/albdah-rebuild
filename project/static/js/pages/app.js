var swiper = new Swiper(".mySwiper", {
    freeMode: true,
    slidesPerView: 1,
    loop: true, 
    spaceBetween: 40, 
    breakpoints: {
      320: {
        slidesPerView: 4,
        spaceBetween: 20
      },
      640: {
        slidesPerView: 7,
        spaceBetween: 40
      }
    }
    /*pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },*/
  });


// Make navbar responsive 

