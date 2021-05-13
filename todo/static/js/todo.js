$(document).ready(function() {
    $('.btn-light').click(function() {
        console.log('1');
        $('li.hide').toggleClass('actv');
        $('li.hide').toggle(400);
        console.log('2');
    });

    // if($('body').height() < $(window).height()) {
    //     $('p.footsy').addClass('posd');
    //     console.log($('body').height(), $(window).height(), 'x');
    // }
    // else {
    //     $('p.footsy').removeClass('posd');
    //     console.log($('body').height(), $(window).height(), 'y');
    // }
});

// if($('body').height() > $(window).height()) {
//     $('p.footsy').addClass('posd');
//     console.log($('body').height(), $(window).height(), 'x');
// }
// if($('body').height() < $(window).height()) {
//     $('p.footsy').removeClass('posd');
//     console.log($('body').height(), $(window).height(), 'y');
// }

// $(window).scroll(function (e) {
//     if(window.scrollY > 150)
//     $('ul.nbar').slideDown();
//     else {
//         $('ul.nbar').slideUp();
//     }
//     console.log(window.scrollY);
// });
