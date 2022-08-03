$('.minus, .plus').click(function (e) {
    e.preventDefault();
    var $input = $(this).siblings('.value-number');
    var val = parseInt($input.val(), 10);
    var x;

    if(val == 0) x = 0;
    else x = -1;

    $input.val(val + ($(this).hasClass('minus') ? x : 1));
});
