$(function () {
    reviseMargin();
    $(window).on('resize', reviseMargin);

    function reviseMargin() {
        $('body').css({
            'margin-top': $('header > nav')[0].offsetHeight + 'px'
        });
    }
});