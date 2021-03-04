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

function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

/**
 * Returns a random integer between min (inclusive) and max (inclusive).
 * The value is no lower than min (or the next integer greater than min
 * if min isn't an integer) and no greater than max (or the next integer
 * lower than max if max isn't an integer).
 * Using Math.round() will give you a non-uniform distribution!
 */
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/*
 :: AJAX EQUIP functions
 */
function rollDice() {
    let user_money = Number($("#user-money").text()),
        npc_money = Number($("#npc-money").text()),
        npc_id = Number($("#npc-name").attr("data-id")),
        path = "/static/img/roleplay/minigame/dice/",
        randomNum = getRandomInt(1, 6);
    $("#round").text("");
    $("#user_dice1").text(0);
    $("#user_dice2").text(0);
    $("#user_sum").text(0);
    $("#npc_dice1").text(0);
    $("#npc_dice2").text(0);
    $("#npc_sum").text(0);
    $("#dice1").addClass('animate' + randomNum);
    $("#dice2").addClass('animate' + (randomNum - 1));
    $("#round").text("РАУНД 1");
    $("#playButton").attr("disabled", true);
    $("#winner").text("");
    $("#error-cause").text();
    $.ajax({
        url: "/rp/minigame/roll_dice/",
        type: 'POST',
        data: {
            id: npc_id
        },

        dataType: 'json',

        success: function (json) {
            $("#error-cause").text(json.cause);
            if (json.result == true) {
                $("#dice1").removeClass('animate' + randomNum);
                $("#dice2").removeClass('animate' + (randomNum - 1));
                $("#user_dice1").text(json.user_dice1);
                $("#user_dice2").text(json.user_dice2);
                $("#user_sum").text(json.user_dice1 + json.user_dice2);
                $("#dice1").css("background-image", "url('" + path + "dice" + json.user_dice1 + ".svg'");
                $("#dice2").css("background-image", "url('" + path + "dice" + json.user_dice2 + ".svg'");

                function npcRolledDice() {

                    let randomNumber = getRandomInt(1, 6);
                    $("#dice1").addClass('animate' + randomNumber);
                    $("#dice2").addClass('animate' + (randomNumber - 1));

                    function npcResult(randomNum) {
                        $("#dice1").removeClass('animate' + randomNum);
                        $("#dice2").removeClass('animate' + (randomNum - 1));
                        $("#npc_dice1").text(json.npc_dice1);
                        $("#npc_dice2").text(json.npc_dice2);
                        $("#npc_sum").text(json.npc_dice1 + json.npc_dice2);
                        $("#dice1").css("background-image", "url('" + path + "dice" + json.npc_dice1 + ".svg'");
                        $("#dice2").css("background-image", "url('" + path + "dice" + json.npc_dice2 + ".svg'");
                        if (json.winner == "user") {
                            $("#winner").text($("#user-name").text());
                        } else if (json.winner == "npc") {
                            $("#winner").text($("#npc-name").text());
                        } else if (json.winner == "none") {
                            $("#winner").text("Ничья");
                        }
                        $("#user-money").text(json.user_money);
                        $("#npc-money").text(json.npc_money);
                        $("#playButton").attr("disabled", false);

                    }

                    $("#round").text("РАУНД 2");
                    setTimeout(npcResult, 3000, randomNumber);
                }

                $("#round").text("ПЕРЕРЫВ");
                setTimeout(npcRolledDice, 5000);

            } else {
                $("#round").text("");
                $("#dice1").removeClass('animate' + randomNum);
                $("#dice2").removeClass('animate' + (randomNum - 1));
                $("#playButton").attr("disabled", false);
            }
        },
        error: function (json) {
            $("#playButton").attr("disabled", false);
        }
    });

    return false;
}

