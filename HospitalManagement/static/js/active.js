(function($) {
    "use strict";

    // jquery document ready function
    jQuery(document).on('ready', function() {

        function custom_mediacarea_fn() {

            var welcomeareaS = $('.home-area'),
                version2Home = $('.Modern-Slider.v2'),
                welcomeareaH = welcomeareaS.height(),
                version2HomeH = version2Home.height(),
                welcomeTextS = $('.slider-content-area'),
                version2sliderS = $('.v2.slider-content-area'),
                welcomeTextH = welcomeTextS.height(),
                version2sliderh = version2sliderS.height(),
                imageFillS = $('.img-fill'),
                imageFillv2S = $('.v2 .img-fill'),
                menuS = $('.navbar'),
                v3homeForm = $('.v3-homeform'),
                v3homeFormH = v3homeForm.height(),
                menuH = (menuS.height() / 2),
                verticaly = ((welcomeareaH - welcomeTextH) / 2),
                verticalyF = ((welcomeareaH - v3homeFormH) / 2),
                verticalyv2 = ((version2HomeH - version2sliderh) / 2);

            welcomeTextS.css({
                paddingTop: verticaly + menuH,
                paddingBottom: verticaly + menuH
            });
            v3homeForm.css({
                paddingTop: verticalyF + menuH,
                paddingBottom: verticalyF
            });

            version2sliderS.css({
                paddingTop: verticalyv2,
                paddingBottom: verticalyv2
            });

            imageFillS.css('height', welcomeareaH);
            imageFillv2S.css('height', version2HomeH);

            // jquery stikcy menu script
            jQuery(window).on('scroll', function() {
                if ($(this).scrollTop() > 1) {
                    menuS.addClass("sticky");
                } else {
                    menuS.removeClass("sticky");
                }
            });
        }
        // script for mobile menu click
        $('.nav li a').on('click', function() {
            $('.collapse').removeClass('in');
        });
        // Change navbar header Icon on click
        $(".navbar-toggle").on("click", function() {
            $(this).toggleClass("active");
        });

       
        if ($.fn.slick) {
            $(".Modern-Slider").slick({
                autoplay: true,
                autoplaySpeed: 10000,
                speed: 600,
                slidesToShow: 1,
                slidesToScroll: 1,
                pauseOnHover: false,
                dots: false,
                pauseOnDotsHover: true,
                cssEase: 'linear',
                fade: true,
                draggable: true,
                prevArrow: '<button class="PrevArrow fa fa-angle-left"></button>',
                nextArrow: '<button class="NextArrow fa fa-angle-right"></button>',
            });
        }

        if ($.fn.slick) {
            $('.aboutv2-imaage-slider').slick({
                slidesToShow: 1,
                slidesToScroll: 1,
                prevArrow: '<button class="PrevArrowAbv2 fa fa-angle-left"></button>',
                nextArrow: '<button class="NextArrowAbv2 fa fa-angle-right"></button>',
                centerPadding: '5px',
            });
        }


        // brnad slider
        if ($.fn.slick) {
            $('.active-brand-slider').slick({
                slidesToScroll: 1,
                slidesToShow: 6,
                prevArrow: '<button class="PrevArrowbrand fa fa-angle-left"></button>',
                nextArrow: '<button class="NextArrowbrand fa fa-angle-right"></button>',

                responsive: [{
                    breakpoint: 780,
                    settings: {
                        slidesToShow: 3
                    }
                }, {
                    breakpoint: 500,
                    settings: {
                        slidesToShow: 1
                    }
                }]
            });
        }
        // end of brand slider

        // start testimonial section

        // client slider 
        if ($.fn.slick) {
            $('.detailst-for').slick({
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
                fade: true,
                asNavFor: '.details-nav',
            });
        }
      
        if ($.fn.slick) {
            $('.details-nav').slick({
                slidesToShow: 5,
                slidesToScroll: 1,
                asNavFor: '.detailst-for',
                dots: false,
                centerMode: true,
                focusOnSelect: true,
                arrows: true,
                prevArrow: '<button type="button" class="slick-prev clientprev fa fa-angle-left"></button>',
                nextArrow: '<button type="button" class="slick-next clientnext fa fa-angle-right"></button>',
                responsive: [{
                    breakpoint: 1400,
                    settings: {
                        slidesToShow: 5
                    }
                }, {
                    breakpoint: 1100,
                    settings: {
                        slidesToShow: 3
                    }
                }, {
                    breakpoint: 780,
                    settings: {
                        slidesToShow: 3
                    }
                }, {
                    breakpoint: 500,
                    settings: {
                        slidesToShow: 1
                    }
                }]
            });
        }
          // client slider 
        if ($.fn.slick) {
            $('.detailst-for-2').slick({
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
                fade: true,
                asNavFor: '.details-navv2',
            });
        }




        if ($.fn.slick) {
            $('.details-navv2').slick({
                slidesToShow: 5,
                slidesToScroll: 1,
                asNavFor: '.detailst-for-2',
                dots: true,
                centerMode: true,
                focusOnSelect: true,
                arrows: false,
                vertical: true,
                prevArrow: '<button type="button" class="slick-prev clientprev fa fa-angle-left"></button>',
                nextArrow: '<button type="button" class="slick-next clientnext fa fa-angle-right"></button>',
                
            });
        }
         


        // end of testimonial section
        if ($.fn.slick) {
            $('.testimonial-section').slick({
                slidesToScroll: 1,
                slidesToShow: 2,
                arrows: false,
                responsive: [{
                    breakpoint: 780,
                    settings: {
                        arrows: false,
                        slidesToShow: 2
                    }
                }, {
                    breakpoint: 500,
                    settings: {
                        arrows: false,
                        slidesToShow: 1
                    }
                }]
            });
        }
        if ($.fn.slick) {
            $('.widget-sider').slick({
                infinite: false,
                slidesToShow: 3,
                slidesToScroll: 1,
                autoplay: false,
                vertical: true,
                autoplaySpeed: 4000,
                prevArrow: '<button type="button" class="slick-prev widgetprev fa fa-angle-up"></button>',
                nextArrow: '<button type="button" class="slick-next widgetnext fa fa-angle-down"></button>',
            });
        }
        // jquery window load function
        jQuery(window).on('load', function() {
            $('#preloader').fadeOut('slow', function() {
                $(this).remove();
            });
            custom_mediacarea_fn();
            medicarea_accoirdion();

        });

        function medicarea_accoirdion() {
            var panelHeading   =    $('.panel-heading');
            $('.collapse.in').prev(panelHeading).addClass('active');
            $('#accordion1, #accordion2,#Abaccordion, #accordion4, #accordion3, #accordion5,#accordion6')
                .on('show.bs.collapse', function(a) {
                    $(a.target).prev(panelHeading).addClass('active');
                })
                .on('hide.bs.collapse', function(a) {
                    $(a.target).prev(panelHeading).removeClass('active');
                });
        }
        if ($.fn.slick) {
            $('.news-slider-active').slick({
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: true,
                fade: true,
                prevArrow: '<button type="button" class="slick-prev news-prev fa fa-angle-left"></button>',
                nextArrow: '<button type="button" class="slick-next news-next fa fa-angle-right"></button>',
            });
        }
        if ($.fn.slick) {
            $('.version-second-news-slider').slick({
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: true,
                fade: true,
                prevArrow: '<button type="button" class="slick-prev news-prev fa fa-angle-left"></button>',
                nextArrow: '<button type="button" class="slick-next news-next fa fa-angle-right"></button>',
            });
        }
        // jquery window resize function
        jQuery(window).on('resize', function() {
            custom_mediacarea_fn();
            medicarea_accoirdion();

        });


    });


})(jQuery);
