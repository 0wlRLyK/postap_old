function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Настройка AJAX
$(function () {
    $.ajaxSetup({
        headers: {"X-CSRFToken": getCookie("csrftoken")}
    });
});


/*
 :: AJAX EQUIP functions
 */
function tradeSell(tradeItems) {
    let obj = $(tradeItems),
        objectsArray = [];
    $(tradeItems).children().children().each(function (i, v) {
        objectsArray.push({
            id: ($(v).children().children().last().data("id")),
            quantity: ($(v).children().children().last().data("quantity"))
        })
    })
    let path = window.location.pathname.split("/");
    let data = {
        obj: objectsArray,
        id: path[path.length - 2]
    };
    data["obj"] = JSON.stringify(data['obj'])
    $.ajax({
        url: "/rp/trade/sell/",
        type: 'POST',
        data: data,

        dataType: 'json',

        success: function (json) {
            obj.empty().masonry('layout');
            $("#user_sum_money").text(0);
            $("#user_sum_mass").text("0.0");
            if (json.result === true) {
                $("#user-money").text(json.moneyUser);
                if (json.moneyTrader !== "infinity") {
                    $("#trader-money").text(json.moneyUser);
                }
            }
        }
    });

    return false;
}

function tradeBuy(tradeItems) {
    let obj = $(tradeItems),
        objectsArray = [];
    $(tradeItems).children().children().each(function (i, v) {
        objectsArray.push({
            id: ($(v).children().children().last().data("id")),
            quantity: ($(v).children().children().last().data("quantity")),
            type: ($(v).children().children().last().data("type")),
        })
    })
    let path = window.location.pathname.split("/");
    let dataSet = {
        obj: objectsArray,
        id: path[path.length - 2]
    };
    dataSet["obj"] = JSON.stringify(dataSet['obj'])
    $.ajax({
        url: "/rp/trade/buy/",
        type: 'POST',
        data: dataSet,

        dataType: 'json',

        success: function (json) {


            if (json.result === true) {
                $("#trader_sum_money").text(0);
                $("#trader_sum_mass").text("0.0");
                $("#user-money").text(json.moneyUser);
                obj.empty().masonry('layout');
                $.ajax({
                    url: '/rp/user/items/' + path[path.length - 2] + '/',
                    success: function (data) {

                        let html = $(data).filter('#user_items').html();
                        console.log($(data).filter('#user_items'));
                        let userItems = $('#user_items');
                        userItems.html(html);
                        userItems.imagesLoaded()
                            .done(function () {
                                userItems.masonry({
                                    itemSelector: '.user-item',
                                    gutter: 3,
                                    isResizable: true,
                                    isAnimated: true,
                                    horizontalOrder: true,
                                    // анимируем перестроение блоков
                                    animationOptions: {
                                        queue: false,
                                        duration: 500
                                    }
                                },);
                            });
                        $('#user_items').masonry('reloadItems');
                    }
                });
            }


        }
    });

    return false;
}


/*
:: EQUIP functions
*/

function toField(parent, person, type, fromTrader = false) {

    let item = $(parent).children().children().children().last(),
        id = $(item).attr("data-id"),
        quantity = Number(item.attr("data-quantity")),
        quantityBlock = $(parent).children().children().children().first(),
        newClassName = "",
        postfixOld = "",
        postfixNew = "";
    if (type === "to") {

        $("#" + person + "_sum_money").text(Number($("#" + person + "_sum_money").text()) + Number($(item).attr("data-cost")))
        $("#" + person + "_sum_mass").text((parseFloat($("#" + person + "_sum_mass").text()) + parseFloat($(item).attr("data-mass"))).toFixed(2))
        postfixOld = "";
        postfixNew = "_sell"
        newClassName = person + "-item-trade";
    } else if (type === "from") {
        if (fromTrader === false) {
            $("#" + person + "_sum_money").text(Number($("#" + person + "_sum_money").text()) - Number($(item).attr("data-cost")))
            $("#" + person + "_sum_mass").text((parseFloat($("#" + person + "_sum_mass").text()) - parseFloat($(item).attr("data-mass"))).toFixed(2))
        }
        postfixOld = "_sell";
        postfixNew = "";
        newClassName = person + "-item";
    }
    let toBlock = $("#" + person + "_items" + postfixNew).find(`[data-id='${id}']`);

    if (Number(toBlock.length) == 0) {
        let parentCopy = $(parent).clone();
        parentCopy.attr("class", newClassName);
        $("#" + person + "_items" + postfixNew).append(parentCopy).masonry('appended', parentCopy);
        let newItem = parentCopy.children().children().children(".item_" + person + postfixOld),
            newQuantityBlock = parentCopy.children().children().children(".equip-quantity");
        if (type === "from") {
            let newItem = parentCopy.children().children().children(".item_" + person + postfixOld),
                newQuantityBlock = parentCopy.children().children().children(".equip-quantity");
        }
        newItem.attr("class", "item_" + person + postfixNew);
        newItem.attr("data-quantity", 0);
        newQuantityBlock.text("x0");
        $("#" + person + "_items" + postfixNew).masonry('layout');
    }


    if (quantity <= 1) {
        if (person === "trader" && type === "to") {
            refreshQuantity(item, person, id, postfixOld, postfixNew, (person === "trader") ? "+=" : "--");
        } else if (person === "trader" && type === "from") {
            refreshQuantity(item, person, id, postfixOld, postfixNew, (person === "trader") ? "-=" : "--");
        } else {
            refreshQuantity(item, person, id, postfixOld, postfixNew, "--");
        }

        $(parent).remove();
        $(parent).removeAttr("style");
        $("#" + person + "_items" + postfixOld).masonry('layout');
        $("#" + person + "_items" + postfixNew).masonry('layout');
    } else {

        if (person === "trader" && type === "to") {
            refreshQuantity(item, person, id, postfixOld, postfixNew, "+=");
        } else if (person === "trader" && type === "from") {
            refreshQuantity(item, person, id, postfixOld, postfixNew, "-=");
        } else {
            refreshQuantity(item, person, id, postfixOld, postfixNew, "--");
        }
        $("#" + person + "_items" + postfixOld).masonry('layout');
        $("#" + person + "_items" + postfixNew).masonry('layout');

    }


}

function toFieldByClick(parentItem, person, type) {
    let item = $(parent).children().children().children().last();
    toField(parentItem, person, type);
    let toFirst = (type == "to") ? "_sell" : "",
        toSecond = (type == "to") ? "" : "_sell",
        nextType = (type == "to") ? "from" : "to";
    $(".item_" + person + toFirst).draggable({
        droptarget: "#" + person + "_items" + toSecond,
        revert: true,
        drop: function (evt, droptarget) {
            let parent = $(this).parent().parent().parent();
            toField(parent, person, nextType);
            toFieldDnD(".item_user" + toSecond, "user", type);
        }
    });
}

function toFieldDnD(parentItem, person, type) {
    let dropTargFirst = "",
        dropTargSecond = "",
        newTypeFirst = "",
        newTypeSecond = "",
        postfixFirst = "",
        postfixSecond = "",
        item = $(parentItem).children().children().children().last();
    if (type === "to") {
        dropTargFirst = "#" + person + "_items_sell";
        dropTargSecond = "#" + person + "_items";
        newTypeFirst = "from";
        newTypeSecond = "to";
        postfixFirst = "_sell";
        postfixSecond = "";
    } else if (type === "from") {
        dropTargFirst = "#" + person + "_items";
        dropTargSecond = "#" + person + "_items_sell";
        newTypeFirst = "to";
        newTypeSecond = "from";
        postfixFirst = "";
        postfixSecond = "_sell";
    }

    $(parentItem).draggable({
        droptarget: dropTargFirst,
        revert: true,
        drop: function (evt, droptarget) {
            let parentFirst = $(this).parent().parent().parent();
            toField(parentFirst, person, type);
            $(".item_" + person + postfixFirst).draggable({
                droptarget: dropTargSecond,
                revert: true,
                drop: function (evt, droptarget) {
                    let parentSecond = $(this).parent().parent().parent();
                    toField(parentSecond, "user", newTypeFirst);
                    toFieldDnD(".item_" + person + "-item" + postfixSecond, "user", newTypeSecond);
                }
            });
        }
    });
    return this;
}


function refreshQuantity(item, person, dataId, postfixOld, postfixNew, mode = "--") {
    let fromParent = $("#" + person + "_items" + postfixOld).find(`[data-id='${dataId}']`).parent().parent(),
        fromQuantityBlock = fromParent.children().children().first(".equip-quantity"),
        toParent = $("#" + person + "_items" + postfixNew).find(`[data-id='${dataId}']`).parent().parent(),
        toQuantityBlock = toParent.children().children().first(".equip-quantity"),
        toItem = toParent.children().children().last(),
        quantityFrom = Number($(item).attr("data-quantity")),
        quantityTo = Number($(toItem).attr("data-quantity")),
        resultFrom = 0,
        resultTo = 0;
    $(toQuantityBlock).removeAttr("style");
    // fromParent.css("background", "red");
    // toParent.css("background", "green");
    if (mode === "--") {
        resultFrom = quantityFrom - 1;
        resultTo = quantityTo + 1;
        $(item).attr("data-quantity", resultFrom);
        $(toItem).attr("data-quantity", resultTo);
        fromQuantityBlock.text("x" + (resultFrom));
        toQuantityBlock.text("x" + (resultTo));
    } else if (mode === "++") {
        resultFrom = quantityFrom + 1;
        resultTo = quantityTo - 1;
        $(item).attr("data-quantity", resultFrom);
        $(toItem).attr("data-quantity", resultTo);
        fromQuantityBlock.text("x" + (resultFrom));
        toQuantityBlock.text("x" + (resultTo));
    } else if (mode === "-=") {
        resultFrom = quantityFrom - 1;
        $(item).attr("data-quantity", resultFrom);
        fromQuantityBlock.text("x" + (resultFrom));
    } else if (mode === "+=") {
        resultTo = quantityTo + 1;
        $(toItem).attr("data-quantity", resultTo);
        toQuantityBlock.text("x" + (resultTo));
    } else {
        quantityFrom = quantityFrom;
        quantityTo = quantityTo;
        $(item).attr("data-quantity", quantityFrom);
        $(toItem).attr("data-quantity", quantityTo);
    }


}

