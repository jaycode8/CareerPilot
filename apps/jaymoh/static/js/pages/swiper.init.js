
/************** Testimonial Slider *************/

var swiper = new Swiper(".testimonialSlider", {
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    breakpoints: {
        200: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        992: {
            slidesPerView: 1,
            spaceBetween: 20,
        }
    }
});

var swiper = new Swiper(".homeslider", {
    slidesPerView: "auto",
    loop: true,
    spaceBetween: 20,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    
});