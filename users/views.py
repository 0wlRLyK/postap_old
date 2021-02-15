import json

from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic as v
from equipment import models as equip
from userena import settings as userena_settings
from userena.utils import get_user_profile
from userena.views import ExtraContextTemplateView

from . import models as m
from .forms import TransferMoneyForm


def profile_detail(
        request,
        username,
        template_name=userena_settings.USERENA_PROFILE_DETAIL_TEMPLATE,
        extra_context=None,
        **kwargs
):
    """
    Detailed view of an user.

    :param username:
        String of the username of which the profile should be viewed.

    :param template_name:
        String representing the template name that should be used to display
        the profile.

    :param extra_context:
        Dictionary of variables which should be supplied to the template. The
        ``profile`` key is always the current profile.

    **Context**

    ``profile``
        Instance of the currently viewed ``Profile``.

    """
    user = get_object_or_404(get_user_model(), username__iexact=username)
    profile = get_user_profile(user=user)
    if not profile.can_view_profile(request.user):
        raise PermissionDenied
    if not extra_context:
        extra_context = dict()
    equip_items = equip.EquipItem.objects.filter(profile=user)
    weights = [
        user.armor.c_obj.weight if user.armor else 0,
        user.backpack.c_obj.weight if user.backpack else 0,
        user.container1.c_obj.weight if user.container1 else 0,
        user.container2.c_obj.weight if user.container2 else 0,
        user.container3.c_obj.weight if user.container3 else 0,
        user.container4.c_obj.weight if user.container4 else 0,
        user.container5.c_obj.weight if user.container5 else 0,
    ]
    ballistic_art = sum([
        user.container1.c_obj.ballistic if user.container1 else 0,
        user.container2.c_obj.ballistic if user.container2 else 0,
        user.container3.c_obj.ballistic if user.container3 else 0,
        user.container4.c_obj.ballistic if user.container4 else 0,
        user.container5.c_obj.ballistic if user.container5 else 0,
    ])
    burst_art = sum([
        user.container1.c_obj.burst if user.container1 else 0,
        user.container2.c_obj.burst if user.container2 else 0,
        user.container3.c_obj.burst if user.container3 else 0,
        user.container4.c_obj.burst if user.container4 else 0,
        user.container5.c_obj.burst if user.container5 else 0,
    ])
    kick_art = sum([
        user.container1.c_obj.kick if user.container1 else 0,
        user.container2.c_obj.kick if user.container2 else 0,
        user.container3.c_obj.kick if user.container3 else 0,
        user.container4.c_obj.kick if user.container4 else 0,
        user.container5.c_obj.kick if user.container5 else 0,
    ])
    explosion_art = sum([
        user.container1.c_obj.explosion if user.container1 else 0,
        user.container2.c_obj.explosion if user.container2 else 0,
        user.container3.c_obj.explosion if user.container3 else 0,
        user.container4.c_obj.explosion if user.container4 else 0,
        user.container5.c_obj.explosion if user.container5 else 0,
    ])
    thermal_art = sum([
        user.container1.c_obj.thermal if user.container1 else 0,
        user.container2.c_obj.thermal if user.container2 else 0,
        user.container3.c_obj.thermal if user.container3 else 0,
        user.container4.c_obj.thermal if user.container4 else 0,
        user.container5.c_obj.thermal if user.container5 else 0,
    ])
    chemical_art = sum([
        user.container1.c_obj.chemical if user.container1 else 0,
        user.container2.c_obj.chemical if user.container2 else 0,
        user.container3.c_obj.chemical if user.container3 else 0,
        user.container4.c_obj.chemical if user.container4 else 0,
        user.container5.c_obj.chemical if user.container5 else 0,
    ])
    electrical_art = sum([
        user.container1.c_obj.electrical if user.container1 else 0,
        user.container2.c_obj.electrical if user.container2 else 0,
        user.container3.c_obj.electrical if user.container3 else 0,
        user.container4.c_obj.electrical if user.container4 else 0,
        user.container5.c_obj.electrical if user.container5 else 0,
    ])
    radioactive_art = sum([
        user.container1.c_obj.radioactive if user.container1 else 0,
        user.container2.c_obj.radioactive if user.container2 else 0,
        user.container3.c_obj.radioactive if user.container3 else 0,
        user.container4.c_obj.radioactive if user.container4 else 0,
        user.container5.c_obj.radioactive if user.container5 else 0,
    ])
    psi_art = sum([
        user.container1.c_obj.psi if user.container1 else 0,
        user.container2.c_obj.psi if user.container2 else 0,
        user.container3.c_obj.psi if user.container3 else 0,
        user.container4.c_obj.psi if user.container4 else 0,
        user.container5.c_obj.psi if user.container5 else 0,
    ])
    weight_art = sum([
        user.container1.c_obj.weight if user.container1 else 0,
        user.container2.c_obj.weight if user.container2 else 0,
        user.container3.c_obj.weight if user.container3 else 0,
        user.container4.c_obj.weight if user.container4 else 0,
        user.container5.c_obj.weight if user.container5 else 0,
    ])
    ballistic_sum = round(sum([
        user.armor.c_obj.ballistic if user.armor else 0,
        user.helmet.c_obj.ballistic if user.armor else 0,
        ballistic_art if user.container1 else 0,
    ]), 2)
    burst_sum = round(sum([
        user.armor.c_obj.burst if user.armor else 0,
        user.helmet.c_obj.burst if user.armor else 0,
        burst_art if user.container1 else 0,
    ]), 2)
    kick_sum = round(sum([
        user.armor.c_obj.kick if user.armor else 0,
        user.helmet.c_obj.kick if user.armor else 0,
        kick_art if user.container1 else 0,
    ]), 2)
    explosion_sum = round(sum([
        user.armor.c_obj.explosion if user.armor else 0,
        user.helmet.c_obj.explosion if user.armor else 0,
        explosion_art if user.container1 else 0,
    ]), 2)
    thermal_sum = round(sum([
        user.armor.c_obj.thermal if user.armor else 0,
        user.helmet.c_obj.thermal if user.armor else 0,
        thermal_art if user.container1 else 0,
    ]), 2)
    chemical_sum = round(sum([
        user.armor.c_obj.chemical if user.armor else 0,
        user.helmet.c_obj.chemical if user.armor else 0,
        chemical_art if user.container1 else 0,
    ]), 2)
    electrical_sum = round(sum([
        user.armor.c_obj.electrical if user.armor else 0,
        user.helmet.c_obj.electrical if user.armor else 0,
        electrical_art if user.container1 else 0,
    ]), 2)
    radioactive_sum = round(sum([
        user.armor.c_obj.radioactive if user.armor else 0,
        user.helmet.c_obj.radioactive if user.armor else 0,
        radioactive_art if user.container1 else 0,
    ]), 2)
    psi_sum = round(sum([
        user.armor.c_obj.psi if user.armor else 0,
        user.helmet.c_obj.psi if user.armor else 0,
        psi_art if user.container1 else 0,
    ]), 2)
    extra_context["profile"] = profile
    extra_context["hide_email"] = userena_settings.USERENA_HIDE_EMAIL
    extra_context["equip"] = equip_items
    extra_context["mass"] = equip_items.aggregate(Sum('mass'))
    extra_context["weight"] = sum(weights)

    extra_context["ballistic"] = ballistic_sum
    extra_context["burst"] = burst_sum
    extra_context["kick"] = kick_sum
    extra_context["explosion"] = explosion_sum
    extra_context["thermal"] = thermal_sum
    extra_context["electrical"] = electrical_sum
    extra_context["radioactive"] = radioactive_sum
    extra_context["psi"] = psi_sum

    extra_context["ballistic_art"] = ballistic_art
    extra_context["burst_art"] = burst_art
    extra_context["kick_art"] = kick_art
    extra_context["explosion_art"] = explosion_art
    extra_context["thermal_art"] = thermal_art
    extra_context["electrical_art"] = electrical_art
    extra_context["radioactive_art"] = radioactive_art
    extra_context["psi_art"] = psi_art
    extra_context["weight_art"] = weight_art
    return ExtraContextTemplateView.as_view(
        template_name=template_name, extra_context=extra_context
    )(request)


class RemoveFromSlot(v.View):
    model = m.SiteUser
    slot_name = None

    def post(self, request, pk):
        self.slot_name, obj_id = pk.split("_")
        item = self.model.objects.get(id=request.user.id)
        slot = getattr(item, self.slot_name)
        cause = None
        item_outfit = None
        if slot.content_type.model in ["outfit", "helmet", "backpack", "artifact"]:
            item_obj = slot.c_obj
            if slot.content_type.model != "backpack":
                item_outfit = {
                    "ballistic": item_obj.ballistic,
                    "burst": item_obj.burst,
                    "kick": item_obj.kick,
                    "explosion": item_obj.explosion,
                    "thermal": item_obj.thermal,
                    "electrical": item_obj.electrical,
                    "chemical": item_obj.chemical,
                    "radioactive": item_obj.radioactive,
                    "psi": item_obj.psi,
                    "weight": item_obj.weight,
                }
            else:
                item_outfit = {"weight": item_obj.weight}
        if slot is not None:
            setattr(item, self.slot_name, None)
            result = True
        else:
            result = False
            cause = "Slot is already empty"
        item.save()
        return HttpResponse(
            json.dumps({
                "result": "True",
                "cause": cause,
                "object": item_outfit
            }),
            content_type="application/json")


class SetInSlot(v.View):
    model = m.SiteUser
    slot_name = None

    def post(self, request, pk):
        result = True
        cause = None
        item_outfit = "None"
        try:
            item = equip.EquipItem.objects.get(pk=pk)
            user = self.model.objects.get(id=request.user.id)
            if item.content_type.model in ["outfit", "helmet", "backpack", "artifact"]:
                item_obj = item.c_obj
                if item.content_type.model != "backpack":
                    item_outfit = {
                        "ballistic": item_obj.ballistic,
                        "burst": item_obj.burst,
                        "kick": item_obj.kick,
                        "explosion": item_obj.explosion,
                        "thermal": item_obj.thermal,
                        "electrical": item_obj.electrical,
                        "chemical": item_obj.chemical,
                        "radioactive": item_obj.radioactive,
                        "psi": item_obj.psi,
                        "weight": item_obj.weight,
                    }
                if item.content_type.model == "outfit":
                    item_outfit.update({"containers": item_obj.containers})
                else:
                    item_outfit = {"weight": item_obj.weight}
            setattr(user, self.slot_name, item)
            user.save()
        except equip.EquipItem.DoesNotExist:
            result = False
            item_obj = None
            cause = "Item doesn't exist!"

        return HttpResponse(
            json.dumps({
                "result": result,
                "cause": cause,
                "object": item_outfit
            }),
            content_type="application/json")


class TransferMoney(v.CreateView):
    model = m.MoneyTransaction
    form_class = TransferMoneyForm
    # fields = "__all__"
    template_name = "users/profile/addmoney.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['user'] = m.SiteUser.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        username = self.request.user
        return "{}".format(reverse("userena_profile_detail", kwargs={"username": username}))

    def form_valid(self, form):
        form.instance.sender = self.request.user
        transfered_money = form.instance.amount
        send_from = m.SiteUser.objects.get(user=self.request.user)
        send_to = m.SiteUser.objects.get(user=form.instance.recipient)
        if send_from == send_to:
            return HttpResponse("Вы не можете переводить деньги самому себе")
        # if form.instance.sender != send_from:
        #     return HttpResponse("Вы не можете переводить деньги с чужого аккаунта")
        elif transfered_money > send_from.money:
            return HttpResponse("Недостаточно денег на вашем счету")
        else:
            send_from.money -= transfered_money
            send_to.money += transfered_money
            send_from.save()
            send_to.save()
            return super(TransferMoney, self).form_valid(form)
