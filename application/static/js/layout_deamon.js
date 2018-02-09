$(function () {
    reviseMargin();
    $(window).on('resize', reviseMargin);

    function reviseMargin() {
        $('main').css({
            'margin-top': $('header > nav')[0].offsetHeight + 'px',
            'margin-bottom': $('footer')[0].offsetHeight + 'px'
        });
    }
});