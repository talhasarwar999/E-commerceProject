// Front Page Toggle Menu
$(document).ready(function () {
    $(".menu_btn").click(function () {
        $(".toggle").toggle();
        $(".toggle").css("display", "block");
        $("#carouselIndicators1").css("display", "none");
        $(".header").css("position", "relative");
        $(".logo img").css("filter", "invert(1)");
        $(".search_bar img").css("filter", "none");
        $(".burger").css("display", "none");
        $("input").css("border", "1px solid black");
        $(".cross").css({
            "display": "block",
            "-webkit-filter": "none"
        });
        $("#shaded").css('pointer-events', 'none');
        $("#shaded").css('opacity', '0.5');
        $(".home_user_account i").css("color", "black");
        $(".search_home").css("color", "black");

        //  $("#shaded").css('background','lavender'); .search_home
    });

    $(".cross").click(function () {
        $("#carouselIndicators1").css("display", "block");
        $(".header").css("position", "absolute");
        $(".search_bar img").css("filter", "invert(1)");
        $(".toggle").css("display", "none");
        $(".cross").css("display", "none");
        $(".burger").css("display", "block");
        $("input").css("border", "1px solid #fff");
        $(".home_user_account i").css("color", "#fff");
        $(".logo img").css("filter", "none");
        $("#shaded").css('pointer-events', '');
        $("#shaded").css('opacity', '1');
        $(".search_home").css("color", "#fff");
        //  $("#shaded").css('background','none !important');

    });

    // Login form Open
    $(".user_account i").click(function (e) {
        $(".my_account").css("display", "flex"),
            e.preventDefault();
    });

    // Login form Close
    $(".fm-dialog-close").click(function (e) {
        $(".my_account").hide(),
            e.preventDefault();
    });

    // Forgot-Password form open
    $(".forgot-pass").click(function (e) {
        $(".login-form").hide(),
            $(".signup-form").hide(),
            $(".forgot-email-form").show(),
            $("#forgot_pass_tab").show(),
            $("#forgot_pass_tab").addClass('active').siblings().removeClass('active'),
            e.preventDefault();
    });

});

// User Registration Form Content
$(document).ready(function () {
    $(".tabs_content .tab_content").hide();
    $(".tabs_content .tab_content:first-child").show();

    $(".fm-tabs-bar li").click(function () {

        $(".fm-tabs-bar li").removeClass("active");
        $(this).addClass("active");

        var current_tab = $(this).attr("data-list");
        $(".tab_content").hide();
        $("#forgot_pass_tab").hide();
        $("." + current_tab).show();
    })
});

// Show Password
$(document).ready(function () {
    $(".toggle-password").click(function () {

        $(this).toggleClass("fa-eye fa-eye-slash");
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
            input.attr("type", "text");
        } else {
            input.attr("type", "password");
        }
    })
});

$(document).ready(function () {

    // Featured Products
    $('.featured-products').owlCarousel({
        loop: true,
        margin: 30,
        nav: true,
        dots: false,
        navText: [
            '<i class="fa fa-angle-left"></i>',
            '<i class="fa fa-angle-right"></i>',
        ],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 3
            },
            1000: {
                items: 3
            }
        }
    });

    function messageBox(message) {
        console.log(message)
        var alertBox = document.getElementById("msg_alert");
        console.log(alertBox)
        const messageIcon = document.getElementById("alert-icon");
        $('.alert').addClass("show");
        $('.alert').removeClass("hide");
        $('.alert').addClass("showAlert");
        setTimeout(function () {
            $('.alert').removeClass("show");
            $('.alert').addClass("hide");
        }, 7000);


        alertBox.innerHTML = message;

        messageIcon.innerHTML = `<span class="fas fa-check-circle"></span>`
    }

    // // // // Quantity Plus Minus Script START \\ \\ \\
    // addbtns = document.querySelectorAll(".add");
    // subbtns = document.querySelectorAll(".sub");

    // addbtns.forEach(element => {
    //     element.addEventListener("click", () => {
    //         //Target Closest Parent
    //         let main_div = element.closest(".cart-quantity, .quantity-box");
    //         let qty = main_div.querySelector('#root');

    //         //Increment in value on click of add btn
    //         qty.value = parseInt(qty.value) + 1;
    //         var product_id = qty.getAttribute('product_id')
    //         // Setting cart count in cookies for guest account
    //         // if (user.is_authenticated == false) 
    //         setCookie("product-" + product_id, qty.value);

    //         $.ajax({
    //             url: '/changeQuantity/',
    //             data: {
    //                 'product_id': product_id,
    //                 'quantity': qty.value
    //             },
    //             dataType: 'json',
    //             success: function (data) {
    //                 $('#product_sum').html('')
    //                 $('#product_sum').html(data['product_sum'])
    //                 $('#tax').html('')
    //                 $('#tax').html(data['tax'])
    //                 $('#total').html('')
    //                 $('#total').html(data['total'])
    //                 $('#coupon-discount').html(data['coupon_discount'])
    //                 $(qty).parent().parent().parent().parent().next().html(`<p> AED ${data['price']} </p>`)
    //                 messageBox(data['message'])
    //             },
    //             error: function (data) {
    //                 console.log('not okk')

    //             }
    //         });

    //     })
    // });

    // subbtns.forEach(element => {
    //     element.addEventListener("click", () => {
    //         //Target Closest Parent
    //         let main_div = element.closest(".cart-quantity, .quantity-box");
    //         let qty = main_div.querySelector('#root');

    //         //Decrement if value greater than 1 (At least one product in cart must exist)
    //         if (parseInt(qty.value) > 1)
    //             qty.value = parseInt(qty.value) - 1;

    //         var product_id = qty.getAttribute('product_id')

    //         // Setting cart count in cookies for guest account
    //         // if (`{{user.is_authenticated}}` == "False") 
    //         setCookie("product-" + product_id, qty.value);

    //         console.log(product_id, qty)
    //         console.log(product_id)
    //         $.ajax({
    //             url: '/changeQuantity/',
    //             data: {
    //                 'product_id': product_id,
    //                 'quantity': qty.value
    //             },
    //             dataType: 'json',
    //             success: function (data) {
    //                 console.log('okk')
    //                 console.log(data)
    //                 $('#product_sum').html('')
    //                 $('#product_sum').html(data['product_sum'])
    //                 $('#tax').html('')
    //                 $('#tax').html(data['tax'])
    //                 $('#total').html('')
    //                 $('#total').html(data['total'])
    //                 $(qty).parent().parent().parent().parent().next().html(`<p> AED ${data['price']} </p>`)
    //                 messageBox(data['message'])

    //             },
    //             error: function (data) {
    //                 console.log('not okk')

    //             }
    //         });

    //     })
    // });

    // // // // Quantity Plus Minus Script END \\ \\ \\

    // Update Cart Count for Guest User
    $("#guest_checkout_items").text(getCartCount());

});

// Sub Pages Hamburger Menu / Mobile Menu
window.onload = function () {

    const menu_btn = document.querySelector('.hamburger');
    const mobile_menu = document.querySelector('.mobile-nav');
    const body = document.querySelector('body');

    menu_btn.addEventListener('click', function () {
        menu_btn.classList.toggle('is-active');
        body.classList.toggle('scroll');
        mobile_menu.classList.toggle('is-active');

    });
}

// More Categories in Category Pages
$('.question').click(function (e) {
    e.preventDefault();
    var notthis = $('.activee').not(this);
    notthis.toggleClass('activee').next('.answer').slideToggle(500);
    $(this).toggleClass('activee').next().slideToggle(500);
});


$(document).ready(function () {
    // List and Grip Toggle in Category Pages
    const list = document.querySelector(".list_icon");
    const grid = document.querySelector(".grid");
    const ltg = document.querySelector(".ltg");

    list.addEventListener("click", () => {
        ltg.classList.add("list");
    });
    grid.addEventListener("click", () => {
        ltg.classList.remove("list");
    });
});

// // List and Grid
$('.left_options i, .page-item, .box-size-tabs a,.option-box').click(function () {
    $(this).addClass('active').siblings().removeClass('active');
});

// FIlter By Box and More Categories Toggle
$(document).ready(function () {
    $('.answer > ul > li').click(function () {
        const value = $(this).attr('data-filter');
        if (value == 'all') {
            // $('.product').show('1000');
            $('.product, .item').show();
        } else {
            $(this).addClass('active').siblings().removeClass('active');
            $('.product, .item').filter('.' + value).show().addClass('active');
            $('.product, .item').not('.' + value).hide().removeClass('active');

        }

        $(".filter").removeClass('active');
        $("body").removeClass('scroll');

    });
});

$(document).ready(function () {
    $('.option-box').click(function () {
        const value = $(this).attr('data-filter');
        if (value == 'all') {
            // $('.product').show('1000');
            $('.product, .item').show();

        } else if ($('.answer > ul > li').hasClass('active')) {
            $('.product.active, .item').filter('.' + value).show();
            $('.product.active, .item').not('.' + value).hide();

        } else {
            $('.product, .item').filter('.' + value).show();
            $('.product, .item').not('.' + value).hide();
        }

        $(".filter").removeClass('active');
        $("body").removeClass('scroll');

    });
});

$(document).ready(function () {
    $('.reset_btn').click(function () {
        const value = $(this).attr('data-filter');
        if (value == 'all') {
            // $('.product').show('1000');
            $('.product, .item').show().removeClass('active');
            $('.answer > ul > li').removeClass('active');
        } else {
            $('.product, .item').filter('.' + value).show().removeClass('active');;
            $('.product, .item').not('.' + value).hide();

        }

        $(".option-box").removeClass('active');
        $(".filter").removeClass('active');
        $("body").removeClass('scroll');

    });
});

// // Products SOrt By Price
$(document).on("change", ".price-sorting", function () {

    var sortingMethod = $(this).val();

    if (sortingMethod == 'l2h') {
        sortProductsPriceAscending();
    } else if (sortingMethod == 'h2l') {
        sortProductsPriceDescending();
    }

});


function sortProductsPriceAscending() {
    var products = $('.product');
    products.sort(function (a, b) {
        return $(a).data("price") - $(b).data("price")
    });
    $(".ltg").html(products);
}

function sortProductsPriceDescending() {
    var products = $('.product');
    products.sort(function (a, b) {
        return $(b).data("price") - $(a).data("price")
    });
    $(".ltg").html(products);

}

// // Sub Pages Filter Button Only For Mobile
$(document).ready(function () {

    $(".filter_icon i").click(function () {
        $(".filter").addClass('active').show(1000);
        $("body").addClass('scroll');
    });

    $(".cross_icon").click(function () {
        $(".filter").removeClass('active').show(1000);
        $("body").removeClass('scroll');
    });

});

// // Payment Billing Form Show and Hide
$(document).ready(function () {
    $("#billing-check").click(function () {
        $(".shipping-info").toggle(1000);
    });
});


function openSearch() {
    document.getElementById("myOverlay").style.display = "block";
}

function closeSearch() {
    document.getElementById("myOverlay").style.display = "none";
}



// Blog Post Text Limit ...

$(".blog-post .blog-text").text(function(index, currentText) {
    var maxLength = $(this).parent().attr('data-maxlength');
    if(currentText.length >= maxLength) {
      return currentText.substr(0, maxLength) + "...";
    } else {
      return currentText
    } 
  });