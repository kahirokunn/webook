$(function () {
    reviseMargin();
    $('main').css({
        'display': 'block'
    });
    $(window).on('resize', reviseMargin);

    function reviseMargin() {
        const header_dom = $('header > nav');
        if (header_dom.length > 0) {
            $('body').css({
                'margin-top': header_dom[0].offsetHeight + 'px'
            });
        }
    }
});