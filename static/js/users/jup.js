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
function removeFromSlot(rem_object, pk) {
    let obj = rem_object,
        data_slot = rem_object.attr("data-slot");
    ;
    if (data_slot === "armor") {
        $("#equipped_outfit_icon").attr("src", "/static/img/equip/icons/sviter_visual.png");
    }

    $.ajax({
        url: "/users/equip/remove/" + pk + "/",
        type: 'POST',
        data: {'obj': pk},

        success: function (json) {
            console.log("RESULT: ", json.result);
            if (data_slot == "armor") {
                $("#slot_outfit_ballistic").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_burst").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_chemical").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_electrical").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_explosion").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_kick").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_psi").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_radioactive").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_thermal").fadeOut(200).attr("style", "width: 0;");
                $("#slot_outfit_weight").fadeOut(200).attr("style", "width: 0;");
            }
        }
    });

    return false;
}

function setInSlot(set_object, mode) {
    let obj = set_object,
        pk = obj.data('id'),
        result = {"success": "", "cause": ""};
    data_type = set_object.attr("data-type");
    console.log("data-slot: ", data_type);

    $.ajax({
        url: "/users/equip/set/" + mode + "/" + pk + "/",
        type: 'POST',
        data: {'obj': pk},

        error: function (json) {
            console.log("CAUSE", json.result);
        },
        success: function (json) {
            result.success = json.result;
            result.cause = json.cause;
            if (data_type == "outfit") {
                $("#slot_outfit_ballistic").fadeIn(200).attr("style", "width:" + json.object.ballistic + "%");
                $("#slot_outfit_burst").fadeIn(200).attr("style", "width:" + json.object.burst + "%");
                $("#slot_outfit_chemical").fadeIn(200).attr("style", "width:" + json.object.chemical + "%");
                $("#slot_outfit_electrical").fadeIn(200).attr("style", "width:" + json.object.electrical + "%");
                $("#slot_outfit_explosion").fadeIn(200).attr("style", "width:" + json.object.explosion + "%");
                $("#slot_outfit_kick").fadeIn(200).attr("style", "width:" + json.object.kick + "%");
                $("#slot_outfit_psi").fadeIn(200).attr("style", "width:" + json.object.psi + "%");
                $("#slot_outfit_radioactive").fadeIn(200).attr("style", "width:" + json.object.radioactive + "%");
                $("#slot_outfit_thermal").fadeIn(200).attr("style", "width:" + json.object.thermal + "%");
                $("#slot_outfit_weight").fadeIn(200).attr("style", "width:" + json.object.weight + "%");
            }


        }
    });

    return false;
}

/*
:: EQUIP functions
*/
function setUpSlot(invItem, slot, dragAndDrop = false) {
    let dataId = invItem.attr("data-id"),
        invItemCount = Number(invItem.attr("data-count")),
        invCurrentQuantity = Number(invItem.attr("data-current-count")),
        invItemParent = invItem.parent().parent(),
        slotItem = $("#e-" + slot),
        slotItemCount = Number(slotItem.attr("data-count")),
        slotCurrentQuantity = Number(slotItem.attr("data-current-count")),
        slotParent = slotItem.parent().parent(),
        check = Number(slotItem.length),
        dataIdTo = slotItem.attr("data-id"),
        slot_to = "",
        equipType = invItem.attr("data-type");
    if (equipType === "weapon") {
        slot_to = "#equipped_slot1, #equipped_slot2, #equipped_slot3";
    } else if (equipType === "outfit") {
        slot_to = "#equipped_armor";
        $("#equipped_outfit_icon").attr("src", invItem.attr("data-imgpath"));
    }
    if (invCurrentQuantity - 1 < 1) {
        invItemParent.remove();
    }
    if (check > 0) {
        let fromCopyItem = invItemParent.clone(),
            toCopyItem = slotParent.clone();

        if (invItemCount <= 1) {
            invItemParent.replaceWith(toCopyItem);
        }
        slotParent.replaceWith(fromCopyItem);

        // ITEM THAT REPLACE IN slot
        let newItemSlot = fromCopyItem.children().children().last(),
            newItemSlot__q = fromCopyItem.children().children().first(".newItemSlot");
        newItemSlot__q.css("display", "none");
        newItemSlot.attr({
            "data-id": dataId.replace(slot + "_", ""),
            "data-slot": slot,
            "class": "equip_slot",
            "id": "e-" + slot
        });

        if (invItemCount != 1 && dataIdTo !== dataId) {
            refreshQuantity(newItemSlot, slot_to, dataId, invCurrentQuantity, "--");
            clearEmptyBlocks('.eq-inv', 20);
        }


        // ITEM THAT REPLACE IN inventory
        let newItemInv = toCopyItem.children().children().last(),
            newItemInv__q = toCopyItem.children().children().first(".newItemSlot");
        let inventoryItemQ = Number($("#inventory").find(`[data-id='${dataIdTo}']`).attr("data-current-count"));
        if (!inventoryItemQ) {
            let toCopyItemCopy = toCopyItem.clone(),
                replacement = $('<div/>', {class: 'eq-inv'}).appendTo($('#inventory')).append(toCopyItemCopy),
                replToInvItem = replacement.children().children().children().last(),
                replToInvItem__q = replacement.children().children().children().first();
            replToInvItem__q.css("display", "block", "background-color", "aqua");
            replToInvItem.attr({
                "id": "",
                "data-id": dataIdTo,
                "data-slot": "",
                "class": "equip_inv_" + slotItem.attr("data-type")
            });
            replToInvItem.removeAttr("id");
            refreshQuantity(replToInvItem, slot_to, dataIdTo, slotCurrentQuantity, "else");
            clearEmptyBlocks('.eq-inv', 20);

            if (dragAndDrop) {
                $(replToInvItem).draggable('destroy');
                setInSlotDnD(replToInvItem, slot_to, equipType);
                clearEmptyBlocks('.eq-inv', 20);
            }

        } else {
            if (dataIdTo !== dataId) {
                refreshQuantity(newItemInv, slot_to, dataIdTo, slotCurrentQuantity, "++");
                clearEmptyBlocks('.eq-inv', 20);
            }
        }
        if (slotCurrentQuantity == 1) {
            newItemInv__q.css("display", "block");
            newItemInv.attr({
                "id": "",
                "data-id": dataIdTo,
                "class": "equip_inv_weapon"
            });
            newItemInv.removeAttr("id");
        } else {
            if (dataIdTo !== dataId) {
                refreshQuantity(newItemInv, slot_to, dataIdTo, slotCurrentQuantity, "++");
                clearEmptyBlocks('.eq-inv', 20);
                toCopyItem.remove();
            }
        }
        // refreshQuantity(newItemInv, slot_to,dataIdTo, slotCurrentQuantity, "--");


        if (dragAndDrop) {

            $(newItemInv).draggable('destroy');
            $(newItemSlot).draggable('destroy');
            setInSlotDnD(newItemInv, slot_to, equipType);
            replaceInInventoryDnD(newItemSlot);
            clearEmptyBlocks('.eq-inv', 20);
        }


    } else {
        $("#equipped_" + slot).empty();

        let invItemParentCopy = invItemParent.clone(),
            newSlotItem = invItemParentCopy.children().children().last(),
            newInvItem = invItemParent.children().children().last(),
            newSlotItem_q = invItemParentCopy.children().children().first();
        if (invItemCount == 1) {
            invItemParent.parent().remove();
        } else {
            refreshQuantity(newSlotItem, slot_to, dataId, invCurrentQuantity, "--");
        }

        invItemParentCopy.appendTo($("#equipped_" + slot));
        newSlotItem_q.css("display", "none");
        newSlotItem.attr({
            "data-id": dataId.replace(slot + "_", ""),
            "data-slot": slot,
            "class": "equip_slot",
            "id": "e-" + slot
        });
        if (dragAndDrop) {
            $(newSlotItem).draggable('destroy');
            replaceInInventoryDnD(newSlotItem);
            setInSlotDnD(newInvItem, slot_to, equipType);
            clearEmptyBlocks('.eq-inv', 20);
        }

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
                slot_to = "";
            if (dataType === "weapon") {
                slot_to = "#equipped_slot1, #equipped_slot2, #equipped_slot3";
            } else if (dataType === "outfit") {
                slot_to = "#equipped_armor";
            }
            $(this).draggable('destroy');
            removeFromSlot(this, dataSlot + "_" + dataId);
            if (Number($("#inventory").find(`[data-id='${dataId}']`).length) === 0) {
                $('<div/>', {class: 'eq-inv'}).appendTo(droptarget).append($(slotItem));
                invItem__q.css("display", "block").text("");
                invItem.attr("data-id", dataId, "data-slot", "", "class", "equip_inv_" + dataType, "data-current-count", 1);
                invItem.removeAttr("id");
                // this.draggable('destroy');

            } else {
                let inventoryItemQ = Number($("#inventory").find(`[data-id='${dataId}']`).attr("data-current-count"));
                dataCurrentQuantity = Number(invItem.attr("data-current-count"));
                refreshQuantity(invItem, slot_to, dataId, inventoryItemQ, "++");
                slotItem.empty();
            }
            clearEmptyBlocks('.eq-inv', 20);

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

                setInSlot(this, slot);

                setUpSlot(this, slot, true);


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
        currentQuantity = quantity - 1;
    } else if (mode === "++") {
        currentQuantity = quantity + 1;
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