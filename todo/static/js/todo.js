$(document).ready(function() {
    $('.btn-light').click(function() {
        console.log('1');
        $('li.hide').toggleClass('actv');
        $('li.hide').toggle(400);
        console.log('2');
    });
});
//
// $(window).resize(function() {
//     if($(window).width()>=785) {
//         $('li.right').show();
//     }
//     else {
//         $('li.right').hide();
//     }
// });
//
// $(window).scroll(function (e) {
//     if(window.scrollY > 150)
//     $('ul.nbar').slideDown();
//     else {
//         $('ul.nbar').slideUp();
//     }
//     console.log(window.scrollY);
// });
