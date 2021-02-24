let inv = $('#inventory');

inv.imagesLoaded()
    .done(function () {
        inv.masonry({
            itemSelector: '.eq-inv',
            isResizable: true,
            isAnimated: true,
// анимируем перестроение блоков
            animationOptions: {
                queue: false,
                duration: 500
            }
        });
    });

function defineSlot(equipType, mode = "str") {
    let slot_to = "";
    if (equipType === "weapon") {
        if (mode === "str") {
            slot_to = "#equipped_slot1, #equipped_slot2, #equipped_slot3";
        } else if (mode === "array") {
            slot_to = ["slot1", "slot2", "slot3"];
        }

    } else if (equipType === "outfit") {
        if (mode === "str") {
            slot_to = "#equipped_armor";
        } else if (mode === "array") {
            slot_to = ["armor"];
        }
    } else if (equipType === "helmet") {
        if (mode === "str") {
            slot_to = "#equipped_helmet";
        } else if (mode === "array") {
            slot_to = ["helmet"];
        }

    } else if (equipType === "device") {
        if (mode === "str") {
            // slot_to = "#equipped_device1, #equipped_device2, #equipped_device3";
            slot_to = "#equipped_device2";
        } else if (mode === "array") {
            slot_to = ["device2"];
            // slot_to = ["device1", "device2", "device3"];
        }
    } else if (equipType === "backpack") {
        if (mode === "str") {
            slot_to = "#equipped_backpack";
        } else if (mode === "array") {
            slot_to = ["backpack"];
        }
    } else if (equipType === "artifact") {
        if (mode === "str") {
            slot_to = "#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5";
        } else if (mode === "array") {
            slot_to = ["container1", "container2", "container3", "container4", "container5"];
        }
    } else if (equipType === "ammo") {
        if (mode === "str") {
            slot_to = "#equipped_belt1, #equipped_belt2, #equipped_belt3, #equipped_belt4";
        } else if (mode === "array") {
            slot_to = ["belt1", "belt2", "belt3", "belt4"];
        }
    }
    return slot_to;
}

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
function removeFromSlot(removeObject, pk) {
    let obj = removeObject,
        dataSlot = removeObject.attr("data-slot");
    if (dataSlot === "armor") {
        $("#equipped_outfit_icon").attr("src", "/static/img/equip/icons/sviter_visual.png");
    }

    $.ajax({
        url: "/users/equip/remove/" + pk + "/",
        type: 'POST',
        data: {'obj': pk},

        success: function (json) {
            console.log("Remove From slot\nRESULT: ", json.result, "\n----------------");
            if (dataSlot == "armor") {
                $("#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5").children().css("display", "none");
                $("#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5").attr("class", "eq empty_container");
                $("#os_ballistic").fadeIn(200).text(0);
                $("#os_burst").fadeIn(200).text(0);
                $("#os_chemical").fadeIn(200).text(0);
                $("#os_electrical").fadeIn(200).text(0);
                $("#os_explosion").fadeIn(200).text(0);
                $("#os_kick").fadeIn(200).text(0);
                $("#os_psi").fadeIn(200).text(0);
                $("#os_radioactive").fadeIn(200).text(0);
                $("#os_thermal").fadeIn(200).text(0);
                $("#os_weight").fadeIn(200).text(0);

                $("#equip_weight").fadeIn(200).text(parseFloat($("#equip_weight").text()) - parseFloat(json.object.weight));
                if (parseFloat($("#equip_mass").text()) > parseFloat($("#equip_weight").text())) {
                    $("#equip_mass").attr({
                        class: "txt_blink-red",
                        style: "color:red;"
                    })
                } else {
                    $("#equip_mass").attr({
                        class: "txt_blink",
                        style: ""
                    })
                }

            } else if (dataSlot == "helmet") {
                $("#hs_ballistic").fadeIn(200).text(0);
                $("#hs_burst").fadeIn(200).text(0);
                $("#hs_chemical").fadeIn(200).text(0);
                $("#hs_electrical").fadeIn(200).text(0);
                $("#hs_explosion").fadeIn(200).text(0);
                $("#hs_kick").fadeIn(200).text(0);
                $("#hs_psi").fadeIn(200).text(0);
                $("#hs_radioactive").fadeIn(200).text(0);
                $("#hs_thermal").fadeIn(200).text(0);
                $("#hs_weight").fadeIn(200).text(0);
            } else if (dataSlot === "backpack") {
                $("#equip_weight").fadeIn(200).text(parseFloat($("#equip_weight").text()) - parseFloat(json.object.weight));
                if (parseFloat($("#equip_mass").text()) > parseFloat($("#equip_weight").text())) {
                    $("#equip_mass").attr({
                        class: "txt_blink-red",
                        style: "color:red;"
                    })
                } else {
                    $("#equip_mass").attr({
                        class: "txt_blink",
                        style: ""
                    })
                }
            } else if (["container1", "container2", "container3", "container4", "container5"].includes(dataSlot)) {
                let containersQuantity = Number($("#containers").attr("data-containers")),
                    mode = dataSlot;
                $("#ballistic_art").attr("data-" + mode, 0.0);
                $("#ballistic_art").text(containersSum(containersQuantity, "ballistic"));

                $("#burst_art").attr("data-" + mode, 0.0);
                $("#burst_art").text(containersSum(containersQuantity, "burst"));

                $("#chemical_art").attr("data-" + mode, 0.0);
                $("#chemical_art").text(containersSum(containersQuantity, "chemical"));

                $("#electrical_art").attr("data-" + mode, 0.0);
                $("#electrical_art").text(containersSum(containersQuantity, "electrical"));

                $("#explosion_art").attr("data-" + mode, 0.0);
                $("#explosion_art").text(containersSum(containersQuantity, "explosion"));

                $("#kick_art").attr("data-" + mode, 0.0);
                $("#kick_art").text(containersSum(containersQuantity, "kick"));

                $("#psi_art").attr("data-" + mode, 0.0);
                $("#psi_art").text(containersSum(containersQuantity, "psi"));

                $("#radioactive_art").attr("data-" + mode, 0.0);
                $("#radioactive_art").text(containersSum(containersQuantity, "radioactive"));

                $("#thermal_art").attr("data-" + mode, 0.0);
                $("#thermal_art").text(containersSum(containersQuantity, "thermal"));

                $("#weight_art").attr("data-" + mode, 0.0);
                $("#weight_art").text(containersSum(containersQuantity, "weight"));

            }
            let ballisticSum = specificationsSum("ballistic"),
                burstSum = specificationsSum("burst"),
                chemicalSum = specificationsSum("chemical"),
                electricalSum = specificationsSum("electrical"),
                explosionSum = specificationsSum("explosion"),
                kickSum = specificationsSum("kick"),
                psiSum = specificationsSum("psi"),
                radioactiveSum = specificationsSum("radioactive"),
                thermalSum = specificationsSum("thermal");

            $("#sum_ballistic").fadeIn(200).text(ballisticSum);
            $("#sum_burst").fadeIn(200).text(burstSum);
            $("#sum_chemical").fadeIn(200).text(chemicalSum);
            $("#sum_electrical").fadeIn(200).text(electricalSum);
            $("#sum_explosion").fadeIn(200).text(explosionSum);
            $("#sum_kick").fadeIn(200).text(kickSum);
            $("#sum_psi").fadeIn(200).text(psiSum);
            $("#sum_radioactive").fadeIn(200).text(radioactiveSum);
            $("#sum_thermal").fadeIn(200).text(thermalSum);
            $("#sum_weight").fadeIn(200).text(parseFloat($("#equip_weight").text()));

            $("#slot_outfit_ballistic").fadeIn(200).attr("style", "width:" + ballisticSum + "%");
            $("#slot_outfit_burst").fadeIn(200).attr("style", "width:" + burstSum + "%");
            $("#slot_outfit_chemical").fadeIn(200).attr("style", "width:" + chemicalSum + "%");
            $("#slot_outfit_electrical").fadeIn(200).attr("style", "width:" + electricalSum + "%");
            $("#slot_outfit_explhsion").fadeIn(200).attr("style", "width:" + explosionSum + "%");
            $("#slot_outfit_kick").fadeIn(200).attr("style", "width:" + kickSum + "%");
            $("#slot_outfit_psi").fadeIn(200).attr("style", "width:" + psiSum + "%");
            $("#slot_outfit_radioactive").fadeIn(200).attr("style", "width:" + radioactiveSum + "%");
            $("#slot_outfit_thermal").fadeIn(200).attr("style", "width:" + thermalSum + "%");
        }
    });

    return false;
}

function setInSlot(set_object, mode) {
    let obj = set_object,
        pk = obj.data('id'),
        result = {"success": "", "cause": ""},
        dataType = set_object.attr("data-type");

    $.ajax({
        url: "/users/equip/set/" + mode + "/" + pk + "/",
        type: 'POST',
        data: {'obj': pk},

        error: function (json) {
            console.log("SET in slot\nFAIL CAUSE:", json.result, "\n----------------");
        },
        success: function (json) {
            console.log("SET in slot\nResult: ", json.result, "\n----------------");
            result.success = json.result;
            result.cause = json.cause;
            if (dataType == "outfit") {
                Number($("#containers").attr("data-containers", json.object.containers));
                let containersQuantity = Number(json.object.containers);

                if (containersQuantity >= 5) {
                    $("#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5").children().css("display", "initial");
                    $("#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5").attr("class", "eq");
                } else if (containersQuantity >= 4) {
                    $("#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4").children().css("display", "initial");
                    $("#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4").attr("class", "eq");
                    $("#equipped_container5").children().css("display", "none");
                    $("#equipped_container5").attr("class", "eq empty_container");
                } else if (containersQuantity >= 3) {
                    $("#equipped_container1, #equipped_container2, #equipped_container3").children().css("display", "initial");
                    $("#equipped_container1, #equipped_container2, #equipped_container3").attr("class", "eq");
                    $("#equipped_container4, #equipped_container5").children().css("display", "none");
                    $("#equipped_container4, #equipped_container5").attr("class", "eq empty_container");
                } else if (containersQuantity >= 2) {
                    $("#equipped_container1, #equipped_container2").children().css("display", "initial");
                    $("#equipped_container1, #equipped_container2, #equipped_container3").attr("class", "eq");
                    $("#equipped_container3, #equipped_container4, #equipped_container5").children().css("display", "none");
                    $("#equipped_container3, #equipped_container4, #equipped_container5").attr("class", "eq empty_container");
                } else if (containersQuantity >= 1) {
                    $("#equipped_container1").children().css("display", "initial");
                    $("#equipped_container1").attr("class", "eq");
                    $("#equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5").children().css("display", "none");
                    $("#equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5").attr("class", "eq empty_container");
                } else if (containersQuantity >= 0) {
                    $("#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5").children().css("display", "none");
                    $("#equipped_container1, #equipped_container2, #equipped_container3, #equipped_container4, #equipped_container5").attr("class", "eq empty_container");
                }
                $("#os_ballistic").fadeIn(200).text(json.object.ballistic);
                $("#os_burst").fadeIn(200).text(json.object.burst);
                $("#os_chemical").fadeIn(200).text(json.object.chemical);
                $("#os_electrical").fadeIn(200).text(json.object.electrical);
                $("#os_explosion").fadeIn(200).text(json.object.explosion);
                $("#os_kick").fadeIn(200).text(json.object.kick);
                $("#os_psi").fadeIn(200).text(json.object.psi);
                $("#os_radioactive").fadeIn(200).text(json.object.radioactive);
                $("#os_thermal").fadeIn(200).text(json.object.thermal);
                $("#os_weight").fadeIn(200).text(json.object.weight);

                $("#equip_weight").fadeIn(200).text(parseFloat($("#equip_weight").text()) + parseFloat(json.object.weight));
                if (parseFloat($("#equip_mass").text()) > parseFloat($("#equip_weight").text())) {
                    $("#equip_mass").attr({
                        class: "txt_blink-red",
                        style: "color:red;"
                    })
                } else {
                    $("#equip_mass").attr({
                        class: "txt_blink",
                        style: ""
                    })
                }
            } else if (dataType == "helmet") {
                $("#hs_ballistic").fadeIn(200).text(json.object.ballistic);
                $("#hs_burst").fadeIn(200).text(json.object.burst);
                $("#hs_chemical").fadeIn(200).text(json.object.chemical);
                $("#hs_electrical").fadeIn(200).text(json.object.electrical);
                $("#hs_explosion").fadeIn(200).text(json.object.explosion);
                $("#hs_kick").fadeIn(200).text(json.object.kick);
                $("#hs_psi").fadeIn(200).text(json.object.psi);
                $("#hs_radioactive").fadeIn(200).text(json.object.radioactive);
                $("#hs_thermal").fadeIn(200).text(json.object.thermal);
                $("#hs_weight").fadeIn(200).text(json.object.weight);
            } else if (dataType == "backpack") {
                $("#equip_weight").fadeIn(200).text(parseFloat($("#equip_weight").text()) + parseFloat(json.object.weight));
                if (parseFloat($("#equip_mass").text()) > parseFloat($("#equip_weight").text())) {
                    $("#equip_mass").attr({
                        class: "txt_blink-red",
                        style: "color:red;"
                    })
                } else {
                    $("#equip_mass").attr({
                        class: "txt_blink",
                        style: ""
                    })
                }
            } else if (dataType == "artifact") {
                let containersQuantity = Number($("#containers").attr("data-containers"));
                $("#ballistic_art").attr("data-" + mode, json.object.ballistic);
                $("#ballistic_art").text(containersSum(containersQuantity, "ballistic"));

                $("#burst_art").attr("data-" + mode, json.object.burst);
                $("#burst_art").text(containersSum(containersQuantity, "burst"));

                $("#chemical_art").attr("data-" + mode, json.object.chemical);
                $("#chemical_art").text(containersSum(containersQuantity, "chemical"));

                $("#electrical_art").attr("data-" + mode, json.object.electrical);
                $("#electrical_art").text(containersSum(containersQuantity, "electrical"));

                $("#explosion_art").attr("data-" + mode, json.object.explosion);
                $("#explosion_art").text(containersSum(containersQuantity, "explosion"));

                $("#kick_art").attr("data-" + mode, json.object.kick);
                $("#kick_art").text(containersSum(containersQuantity, "kick"));

                $("#psi_art").attr("data-" + mode, json.object.psi);
                $("#psi_art").text(containersSum(containersQuantity, "psi"));

                $("#radioactive_art").attr("data-" + mode, json.object.radioactive);
                $("#radioactive_art").text(containersSum(containersQuantity, "radioactive"));

                $("#thermal_art").attr("data-" + mode, json.object.thermal);
                $("#thermal_art").text(containersSum(containersQuantity, "thermal"));

                $("#weight_art").attr("data-" + mode, json.object.weight);
                $("#weight_art").text(containersSum(containersQuantity, "weight"));

            }
            let ballisticSum = specificationsSum("ballistic"),
                burstSum = specificationsSum("burst"),
                chemicalSum = specificationsSum("chemical"),
                electricalSum = specificationsSum("electrical"),
                explosionSum = specificationsSum("explosion"),
                kickSum = specificationsSum("kick"),
                psiSum = specificationsSum("psi"),
                radioactiveSum = specificationsSum("radioactive"),
                thermalSum = specificationsSum("thermal");
            $("#sum_ballistic").fadeIn(200).text(ballisticSum);
            $("#sum_burst").fadeIn(200).text(burstSum);
            $("#sum_chemical").fadeIn(200).text(chemicalSum);
            $("#sum_electrical").fadeIn(200).text(electricalSum);
            $("#sum_explosion").fadeIn(200).text(explosionSum);
            $("#sum_kick").fadeIn(200).text(kickSum);
            $("#sum_psi").fadeIn(200).text(psiSum);
            $("#sum_radioactive").fadeIn(200).text(radioactiveSum);
            $("#sum_thermal").fadeIn(200).text(thermalSum);
            $("#sum_weight").fadeIn(200).text(parseFloat($("#equip_weight").text()));

            $("#slot_outfit_ballistic").fadeIn(200).attr("style", "width:" + ballisticSum + "%");
            $("#slot_outfit_burst").fadeIn(200).attr("style", "width:" + burstSum + "%");
            $("#slot_outfit_chemical").fadeIn(200).attr("style", "width:" + chemicalSum + "%");
            $("#slot_outfit_electrical").fadeIn(200).attr("style", "width:" + electricalSum + "%");
            $("#slot_outfit_explhsion").fadeIn(200).attr("style", "width:" + explosionSum + "%");
            $("#slot_outfit_kick").fadeIn(200).attr("style", "width:" + kickSum + "%");
            $("#slot_outfit_psi").fadeIn(200).attr("style", "width:" + psiSum + "%");
            $("#slot_outfit_radioactive").fadeIn(200).attr("style", "width:" + radioactiveSum + "%");
            $("#slot_outfit_thermal").fadeIn(200).attr("style", "width:" + thermalSum + "%");


        }
    });

    return false;
}

/*
:: EQUIP functions
*/
function setUpSlot(invItem, slot, dragAndDrop = false) {
    let dataId = invItem.attr("data-id"),
        dataWeight = parseFloat(invItem.attr("data-weight")) || 0,
        invItemCount = Number(invItem.attr("data-count")),
        invCurrentQuantity = Number(invItem.attr("data-current-count")),
        invItemParent = invItem.parent().parent(),
        slotItem = $("#e-" + slot),
        slotItemCount = Number(slotItem.attr("data-count")),
        slotCurrentQuantity = Number(slotItem.attr("data-current-count")),
        slotParent = slotItem.parent().parent(),
        check = Number(slotItem.length),
        dataIdTo = slotItem.attr("data-id"),
        dataTypeTo = slotItem.attr("data-type"),
        dataWeightTo = parseFloat(slotItem.attr("data-weight")) || 0,
        equipType = invItem.attr("data-type");

    let slot_to = defineSlot(equipType);
    if (equipType === "outfit") {
        $("#equipped_outfit_icon").attr("src", invItem.attr("data-imgpath"));
    }
    if (invCurrentQuantity - 1 < 1) {

        invItemParent.parent().remove();

    }
    if (check > 0) {
        fromSlot(slotItem, "#inventory", dataIdTo, dataTypeTo, slot);
        toSlot(invItemParent, slot, slot_to, dataId, invCurrentQuantity, invItemCount, equipType);

        if (["outfit", "backpack", "artifact"].includes(equipType)) {
            $("#equip_weight").fadeIn(200).text(parseFloat($("#equip_weight").text()) - dataWeightTo - dataWeight + dataWeight);
            if (Number($("#equip_mass").text()) > Number($("#equip_weight").text())) {
                $("#equip_mass").attr({
                    class: "txt_blink-red",
                    style: "color:red;"
                })
            } else {
                $("#equip_mass").attr({
                    class: "txt_blink",
                    style: ""
                })
            }
        }
        if (dragAndDrop) {
            $(slotItem).draggable('destroy');
            setInSlotDnD(slotItem, slot_to, equipType);

        }

    } else {

        toSlot(invItemParent, slot, slot_to, dataId, invCurrentQuantity, invItemCount, equipType);

    }
}

function setUpAmmo(invItem, slot, dragAndDrop = false) {
    let dataId = invItem.attr("data-id"),
        dataWeight = parseFloat(invItem.attr("data-weight")) || 0,
        invItemCount = Number(invItem.attr("data-count")),
        invCurrentQuantity = Number(invItem.attr("data-current-count")),
        ammoQuantity = Number(invItem.attr("data-ammo-count")),
        slotQuantity = Number($("#e-slot" + slot.slice(-1)).attr("data-capacity")) || 0,
        ammoId = Number(invItem.attr("data-ammo-id")) || 0,
        invItemParent = invItem.parent().parent(),
        equipType = invItem.attr("data-type"),
        checkSlot = Number($("#e-" + slot).length),
        ammoContainer = $("#e-" + slot).parent().parent().parent().parent(),
        slot_to = "#equipped_belt1, #equipped_belt2, #equipped_belt3, #equipped_belt4, #equipped_belt5";
    toSlot(invItemParent, slot, slot_to, dataId, invCurrentQuantity, invItemCount, equipType, ammo = true);
    let itemAmmoIds = [];
    if (Number(slot.slice(-1)) <= 3) {
        itemAmmoIds = $("#e-slot" + slot.slice(-1)).attr("data-ammo-types").split(/\s*,\s*/g).map(d => Number(d) || d);
    } else {
        slotQuantity = ammoQuantity;
    }


    if (checkSlot > 0) {
        if (itemAmmoIds.includes(ammoId)) {
            ammoContainer.children().children(".belt_type").attr("src", "/static/img/icons/ok.png");
        } else {
            ammoContainer.children().children(".belt_type").attr("src", "/static/img/icons/er.png");
        }
        ammoContainer.children().children(".belt_one").text(slotQuantity);
        ammoContainer.children().children(".slash").css("display", "initial");
        ammoContainer.children().children(".belt_all").text(ammoQuantity * invCurrentQuantity);
    } else {
        ammoContainer = $("#e-" + slot).parent().parent().parent().parent();
        if (itemAmmoIds.includes(ammoId)) {
            ammoContainer.children().children(".belt_type").attr("src", "/static/img/icons/ok.png");
        } else {
            ammoContainer.children().children(".belt_type").attr("src", "/static/img/icons/er.png");
        }
        ammoContainer.children().children(".belt_one").text(slotQuantity);
        ammoContainer.children().children(".slash").css("display", "initial");
        ammoContainer.children().children(".belt_all").text(ammoQuantity * invCurrentQuantity);
    }
}
/*
 :: DRAG and DROP functions
 */
function replaceInInventoryDnD(from) {
    $(from).draggable({
        droptarget: '#inventory',
        revert: true,
        drop: function (evt, droptarget) {
            let slotItem = this.parent().parent(),
                slotItemParent = slotItem.children().children(),
                invItem = slotItemParent.last(".equip_slot"),
                invItem__q = slotItemParent.first(".equip-quantity");

            let dataId = this.attr("data-id"),
                dataSlot = this.attr("data-slot"),
                dataType = this.attr("data-type"),
                dataQuantity = Number(this.attr("data-count")),
                dataCurrentQuantity = Number(this.attr("data-current-count"));
            let slot_inv = invItem,
                slot_to = defineSlot(dataType);


            $(this).draggable('destroy');
            removeFromSlot(this, dataSlot + "_" + dataId);
            fromSlot(this, droptarget, dataId, dataType, slot_to, true);
            setInSlotDnD(slot_inv, slot_to, dataType);
        }
    });
    return this;
}

function setInSlotDnD(from, to, equipType) {
    $(from).draggable({
        revert: true,
        placeholder: true,
        droptarget: $(to),
        drop: function (evt, droptarget) {
            let this_element = this,
                slot = $(droptarget).attr("id").replace("equipped_", ""),
                dropTgEquipType = $(from).attr("data-type");
            if (equipType !== dropTgEquipType) {
                console.log("This is an incorrect type");
            } else {

                setInSlot(this, slot,);
                setUpSlot(this, slot, true);

            }


        }
    });
    return this;
}

function setInAmmoDnD(from, to, equipType) {
    $(from).draggable({
        revert: true,
        placeholder: true,
        droptarget: $(to),
        drop: function (evt, droptarget) {
            let this_element = this,
                slot = $(droptarget).attr("id").replace("equipped_", ""),
                dropTgEquipType = $(from).attr("data-type");
            if (equipType !== dropTgEquipType) {
                console.log("This is an incorrect type");
            } else {

                setInSlot(this, slot,);
                setUpAmmo(this, slot, true);

            }


        }
    });
    return this;
}

/*
    EXTRA FUNCTIONS
 */
function refreshQuantity(item, slotTo, dataId, quantity, mode = "--") {
    let currentQuantity = quantity;
    if (mode === "--") {
        currentQuantity = --quantity;
    } else if (mode === "++") {
        currentQuantity = ++quantity;
    } else {
        currentQuantity = quantity;
    }
    let inventoryQuantityElement = $("#inventory").find(`[data-id='${dataId}']`).parent().parent(),
        inventoryQuantity = inventoryQuantityElement.children().children().first(".equip-quantity"),
        inventoryItem = inventoryQuantityElement.children().children().last();
    $(slotTo).find(`[data-id='${dataId}']`).attr("data-current-count", currentQuantity);
    inventoryQuantity.text("x" + (currentQuantity));
    $(item).attr("data-current-count", currentQuantity);
    inventoryItem.attr("data-current-count", currentQuantity);

}

function clearEmptyBlocks(block, length = 1) {
    $(block).each(function () {
        if (Number($(this).text().length) < length) {
            $(this).remove();
        }
    });
}

function toSlot(parentItem, slot, slot_to, dataId, currentQuantity, invItemCount, equipType, ammo = false) {
    $("#equipped_" + slot).empty();
    let invItemParentCopy = parentItem.clone(),
        newSlotItem = invItemParentCopy.children().children().last(),
        newInvItem = parentItem.children().children().last(),
        newSlotItem_q = invItemParentCopy.children().children().first();
    if (invItemCount == 1) {
        parentItem.parent().remove();
    } else if (ammo) {
    } else {
        refreshQuantity(newSlotItem, slot_to, dataId, currentQuantity, "--");
    }
    if (equipType === "weapon" && Number(slot.slice(-1)) <= 3) {
        let ammoId = Number($("#e-belt" + slot.slice(-1)).attr("data-ammo-id")) || 0,
            itemAmmoIds = newSlotItem.attr("data-ammo-types").split(/\s*,\s*/g).map(d => Number(d) || d),
            beltParent = $("#container_belt" + slot.slice(-1)).children();
        if (itemAmmoIds.includes(ammoId)) {
            beltParent.children(".belt_type").attr("src", "/static/img/icons/ok.png");
        } else {
            beltParent.children(".belt_type").attr("src", "/static/img/icons/er.png");
        }
        if (beltParent.children(".belt_one").text() != "") {
            beltParent.children(".belt_one").text(newSlotItem.attr("data-capacity"));
        }
    }
    invItemParentCopy.appendTo($("#equipped_" + slot));
    newSlotItem_q.css("display", "none");
    newSlotItem.attr({
        "data-id": dataId.replace(slot + "_", ""),
        "data-slot": slot,
        "class": "equip_slot",
        "id": "e-" + slot
    });

    $(newSlotItem).draggable('destroy');
    replaceInInventoryDnD(newSlotItem);
    $("#inventory").masonry('remove', invItemParentCopy).masonry('layout');
}

function fromSlot(item, target, dataId, dataType, slot_to) {
    let slotItem = $(item).parent().parent(),
        slotItemParent = slotItem.children().children(),
        invItem = slotItemParent.last(".equip_slot"),
        invItem__q = slotItemParent.first(".equip-quantity");
    $("#container_belt" + item.attr("id").slice(-1)).children().children(".belt_type").attr("src", "");
    if (dataType === "weapon" && $("#container_belt" + item.attr("id").slice(-1)).children().children(".belt_one").text() != "") {

        $("#container_belt" + item.attr("id").slice(-1)).children().children(".belt_one").text(0);
    }
    if (Number($("#inventory").find(`[data-id='${dataId}']`).length) === 0) {
        // $('<div/>', {class: 'eq-inv'}).appendTo($(target)).append($(slotItem));
        var $div = $("<div/>")
            .attr("class", "eq-inv")
            .html(slotItem);

        $(target).append($div).masonry('appended', $div);
        invItem__q.css("display", "block").text("");
        invItem.attr({
                "data-id": dataId,
                "data-slot": "",
                "class": "equip_inv_" + dataType,
                "data-current-count": 1
            }
        );
        invItem.removeAttr("id");
        // $(".equip_inv_" + dataType).dblclick(function () {setInSlotClick(this, dataType, defineSlot(dataType, mode="array"))});
    } else if (dataType === "ammo") {
        slotItem.empty();
        let ammoContainer = slotItem.parent().parent();
        ammoContainer.children().children(".belt_one").text("");
        ammoContainer.children().children(".slash").css("display", "none");
        ammoContainer.children().children(".belt_all").text("");
        // ammoContainer.children().children().last().css("color","yellow");
    } else {
        let inventoryItemQ = Number($("#inventory").find(`[data-id='${dataId}']`).attr("data-current-count"));
        dataCurrentQuantity = Number(invItem.attr("data-current-count"));
        refreshQuantity(invItem, slot_to, dataId, inventoryItemQ, "++");
        slotItem.empty();
    }

    $(item).draggable('destroy');
    setInSlotDnD(item, slot_to, dataType);
    inv.masonry('appended', slotItem).masonry('layout');
    ;
    // setInSlotClick(dataType, defineSlot(dataType, mode="array"));

}

function containersSum(containersQuantity, specification) {
    let art1 = 0.0,
        art2 = 0.0,
        art3 = 0.0,
        art4 = 0.0,
        art5 = 0.0;
    if (containersQuantity >= 5) {
        art5 = parseFloat($("#" + specification + "_art").attr("data-container5")) || 0;
    }
    if (containersQuantity >= 4) {
        art4 = parseFloat($("#" + specification + "_art").attr("data-container4")) || 0;
    }
    if (containersQuantity >= 3) {
        art3 = parseFloat($("#" + specification + "_art").attr("data-container3")) || 0;
    }
    if (containersQuantity >= 2) {
        art2 = parseFloat($("#" + specification + "_art").attr("data-container2")) || 0;
    }
    if (containersQuantity >= 1) {
        art1 = parseFloat($("#" + specification + "_art").attr("data-container1")) || 0;
    }
    return art1 + art2 + art3 + art4 + art5;

}

function specificationsSum(specification) {
    let armorSpec = parseFloat($("#os_" + specification).text()) || 0,
        helmetSpec = parseFloat($("#hs_" + specification).text()) || 0,
        artSpec = parseFloat($("#" + specification + "_art").text()) || 0;
    return armorSpec + helmetSpec + artSpec;
}

function containersSet(containersQuantity, specification) {
    if (containersQuantity >= 5) {
        $("#equipped_container1")
    }
    if (containersQuantity >= 4) {
        art4 = parseFloat($("#" + specification + "_art").attr("data-container4")) || 0;
    }
    if (containersQuantity >= 3) {
        art3 = parseFloat($("#" + specification + "_art").attr("data-container3")) || 0;
    }
    if (containersQuantity >= 2) {
        art2 = parseFloat($("#" + specification + "_art").attr("data-container2")) || 0;
    }
    if (containersQuantity >= 1) {
        art1 = parseFloat($("#" + specification + "_art").attr("data-container1")) || 0;
    }
}

function removeFromSlotClick(from) {
    $("#equipped_" + from).dblclick(function () {
        let slotParent = $("#equipped_" + from),
            slotItem = $("#e-" + from);
        let invItem__q = slotItem.children(".equip-quantity");

        let dataId = slotItem.attr("data-id"),
            dataSlot = slotItem.attr("data-slot"),
            dataType = slotItem.attr("data-type"),
            dataQuantity = Number(slotItem.attr("data-count")),
            dataCurrentQuantity = Number(slotItem.attr("data-current-count")),
            slot_inv = slotItem;
        $(slotItem).draggable('destroy');
        removeFromSlot(slotItem, dataSlot + "_" + dataId);
        fromSlot(slotItem, "#inventory", dataId, dataType, defineSlot(dataType), true);
        setInSlotDnD(slot_inv, defineSlot(dataType), dataType);
    });
}

function setInSlotClick(setItem, equipType, to, ammo = false) {
    let toItems = to,
        slot = "",
        found = false,
        equipItem = $(setItem),
        dropTgEquipType = $(setItem).attr("data-type");
    for (const item of toItems) {
        console.log(item, Number($("#e-" + item).length));
        if (Number($("#e-" + item).length) === 0) {
            slot = item;
            found = true;
            break;
        }
    }
    if (!found) {
        slot = toItems[0];
        console.log("  ", false, toItems[0]);
    }

    if (equipType !== dropTgEquipType) {
        console.log("This is an incorrect type");
    } else {
        if (equipItem.attr("data-id") !== $("#e-" + slot).attr("data-id")) {
            setInSlot(equipItem, slot,);
            if (ammo) {
                setUpAmmo(equipItem, slot, true);
            } else {
                setUpSlot(equipItem, slot, true);
            }
        }
    }

}