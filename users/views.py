import json

from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
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
    extra_context["profile"] = profile
    extra_context["hide_email"] = userena_settings.USERENA_HIDE_EMAIL
    extra_context["equip"] = equip.EquipItem.objects.filter(profile=user)
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
            if item.content_type.model == "outfit":
                item_obj = item.c_obj
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
