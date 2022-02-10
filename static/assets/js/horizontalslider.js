
//  ************ Swiper Script **************//

  var swiper = new Swiper(".swiper-thumbnail", {
        spaceBetween: 10,
        slidesPerView: 4,
        freeMode: true,
        watchSlidesVisibility: true,
        watchSlidesProgress: true,
      });
      var swiper2 = new Swiper(".swiper-full-image", {
        spaceBetween: 10,
        slidesPerView: 1,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        thumbs: {
          swiper: swiper,
        },
        loop :true,
        //  autoplay: {
        //   delay: 2500,
        //   disableOnInteraction: false,
        // },
      });