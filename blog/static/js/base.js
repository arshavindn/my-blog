$(document).ready(function() {
    $search_box = $('.search-box input');
    $search_box.focus(function() {
        $(this).animate({width: "240px"});
    });
    $search_box.blur(function() {
        $(this).animate({width: "150px"});
    });
});
