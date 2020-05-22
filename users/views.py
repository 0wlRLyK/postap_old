from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from guardian.decorators import permission_required_or_403
from userena import settings as userena_settings
from userena import signals as userena_signals
from userena.decorators import secure_required
from userena.utils import get_user_profile
from userena.views import ExtraContextTemplateView

from .forms import EditFormExtra
from .models import UsersProfiles


@secure_required
@permission_required_or_403("change_profile", (UsersProfiles, "user__username", "username"))
def profile_edit(
        request,
        username,
        edit_profile_form=EditFormExtra,
        template_name="userena/profile_form.html",
        success_url=None,
        extra_context=None,
        **kwargs
):
    user = get_object_or_404(get_user_model(), username__iexact=username)

    profile = get_user_profile(user=user)

    user_initial = {"first_name": user.first_name, "last_name": user.last_name}

    form = edit_profile_form(instance=profile, initial=user_initial)

    if request.method == "POST":
        form = edit_profile_form(
            request.POST, request.FILES, instance=profile, initial=user_initial
        )
        # country_obj = Country.objects.get(name=form.country)
        profile.country = form.country
        profile = form.save()

        if form.is_valid():

            if userena_settings.USERENA_USE_MESSAGES:
                messages.success(
                    request, _("Your profile has been updated."), fail_silently=True
                )

            if success_url:
                # Send a signal that the profile has changed
                userena_signals.profile_change.send(sender=None, user=user)
                redirect_to = success_url
            else:
                redirect_to = reverse(
                    "userena_profile_detail", kwargs={"username": username}
                )
            return redirect(redirect_to)

    if not extra_context:
        extra_context = dict()
    extra_context["form"] = form
    extra_context["profile"] = profile
    return ExtraContextTemplateView.as_view(
        template_name=template_name, extra_context=extra_context
    )(request)
