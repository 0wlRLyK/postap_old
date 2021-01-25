function simple_tooltip(target_items, name) {
    $(target_items).each(function (i) {
        $("body").append("<div class='" + name + "' id='" + name + i + "'><p>" + $(this).attr('title') + "</p></div>");
        var my_tooltip = $("#" + name + i);

        if ($(this).attr("title")) { // Проверяем есть ли атрибут title

            $(this).removeAttr("title").mouseover(function () {
                my_tooltip.css({opacity: 0.95, display: "none"}).fadeIn(400);
            }).mousemove(function (e) {
                let $tooltip = $('#' + name + i);
                let wW = $(window).scrollLeft() + $(window).width();
                let wH = $(window).scrollTop() + $(window).height();
                // console.log("wW, wH: ", wW, wH);
                let mouseX = e.pageX + 20;
                let mouseY = e.pageY;
                // console.log("X, Y: ",mouseX, mouseY);
                if (mouseX + $tooltip.outerWidth() > wW) {
                    mouseX = wW - $tooltip.outerWidth();
                    my_tooltip.css({right: mouseX, top: mouseY});
                }

                if (mouseY + $tooltip.outerHeight() > wH) {
                    mouseY = e.pageY - $tooltip.outerHeight();
                    my_tooltip.css({left: mouseX, top: mouseY + 250});
                } else {
                    my_tooltip.css({left: mouseX, top: mouseY});
                }
            }).mouseout(function () {
                my_tooltip.fadeOut(400);
            });

        }
    });
}

$(document).ready(function () {
    simple_tooltip("tip", "tooltip");
});