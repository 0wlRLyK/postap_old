import os

from PIL import Image
from cities_light.models import Country
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from guardian.decorators import permission_required_or_403
from postap import settings
from userena.decorators import secure_required

from .forms import EditFormExtra
from .models import UsersProfiles


class EditUserProfile(UpdateView):
    model = UsersProfiles
    form_class = EditFormExtra
    template_name = "userena/profile_form.html"
    slug_field = "slug"
    context_extra = dict()

    # def get_slug_field(self):
    #     return self.request.user
    # def get_object(self, queryset=None):
    #     return self.request.user

    def get_success_url(self):
        username = self.request.user
        return reverse("userena_profile_detail", kwargs={"username": username})

    def form_valid(self, form):
        form_save = form.save(commit=False)
        if 'mugshot' in form.changed_data:
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            w = form.cleaned_data['width']
            h = form.cleaned_data['height']
            print(x, y, w, h)
            image = Image.open(form_save.mugshot)
            cropped_image = image.crop((x, y, w + x, h + y))
            resized_image = cropped_image.resize((settings.AVATAR_PROPORTIONS, settings.AVATAR_PROPORTIONS),
                                                 Image.ANTIALIAS)
            resized_image.save(form_save.mugshot.path, commit=True)
            for variation, value in zip(settings.AVATAR_VARIATIONS, settings.ratio_ava):
                cropped_image = image.crop((x, y, w + x, h + y))
                resized_image = cropped_image.resize((value, value), Image.ANTIALIAS)
                file_path = os.path.splitext(form_save.mugshot.path)
                path = "{0}.{1}{2}".format(file_path[0], variation, file_path[1])
                # print(form_save.mugshot, ":", os.path.splitext(form_save.mugshot.path))
                resized_image.save(path, commit=True)

        country_obj = Country.objects.get(name=form.data["country"])
        form_save.country = country_obj
        form_save.save()
        print(self.model.mugshot)
        return super(EditUserProfile, self).form_valid(form)

    @method_decorator(secure_required)
    @method_decorator(permission_required_or_403("change_profile"), (UsersProfiles, "user__username", "username"))
    def dispatch(self, *args, **kwargs):
        return super(EditUserProfile, self).dispatch(*args, **kwargs)

# @secure_required
# @permission_required_or_403("change_profile", (UsersProfiles, "user__username", "username"))
# def profile_edit(
#         request,
#         username,
#         edit_profile_form=EditFormExtra,
#         template_name="userena/profile_form.html",
#         success_url=None,
#         extra_context=None,
#         **kwargs
# ):
#     user = get_object_or_404(get_user_model(), username__iexact=username)
#
#     profile = get_user_profile(user=user)
#
#     user_initial = {"first_name": user.first_name, "last_name": user.last_name}
#
#     form = edit_profile_form(instance=profile, initial=user_initial)
#
#     if request.method == "POST":
#         form = edit_profile_form(
#             request.POST, request.FILES, instance=profile, initial=user_initial
#         )
#         # country_obj = Country.objects.get(name=form.country)
#         profile.country = form.country
#         profile = form.save()
#
#         if form.is_valid():
#
#             if userena_settings.USERENA_USE_MESSAGES:
#                 messages.success(
#                     request, _("Your profile has been updated."), fail_silently=True
#                 )
#
#             if success_url:
#                 # Send a signal that the profile has changed
#                 userena_signals.profile_change.send(sender=None, user=user)
#                 redirect_to = success_url
#             else:
#                 redirect_to = reverse(
#                     "userena_profile_detail", kwargs={"username": username}
#                 )
#             return redirect(redirect_to)
#
#     if not extra_context:
#         extra_context = dict()
#     extra_context["form"] = form
#     extra_context["profile"] = profile
#     return ExtraContextTemplateView.as_view(
#         template_name=template_name, extra_context=extra_context
#     )(request)
