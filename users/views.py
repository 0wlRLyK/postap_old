import os

from PIL import Image
from cities_light.models import Country
from django.http import HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from guardian.decorators import permission_required_or_403
from postap import settings
from userena.decorators import secure_required

from .forms import EditFormExtra, TransferMoneyForm
from .models import UsersProfiles, MoneyTransaction


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
        country_obj = Country.objects.get(name=form.data["country"])
        form_save.country = country_obj
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
        if 'sign_image' in form.changed_data:
            x_s = form.cleaned_data['x_sign']
            y_s = form.cleaned_data['y_sign']
            w_s = form.cleaned_data['width_sign']
            h_s = form.cleaned_data['height_sign']
            print(x_s, y_s, w_s, h_s)
            image_sign = Image.open(form_save.sign_image)
            cropped_sign = image_sign.crop((x_s, y_s, w_s + x_s, h_s + y_s))
            cropped_sign.save(form_save.sign_image.path, commit=True)
        if 'bg' in form.changed_data:
            xl_bg = form.cleaned_data['x_bg']
            yl_bg = form.cleaned_data['y_bg']
            xr_bg = form.cleaned_data['width_bg']
            yr_bg = form.cleaned_data['height_bg']
            print(xl_bg, yl_bg, xr_bg, xr_bg)
            image_bg = Image.open(form_save.bg)
            cropped_bg = image_bg.crop((xl_bg, yl_bg, xr_bg, yr_bg))
            # resized_bg = cropped_bg.resize((width_bg, h_bg), Image.ANTIALIAS)
            cropped_bg.save(form_save.bg.path, commit=True)

        form_save.save()
        print(self.model.mugshot)
        return super(EditUserProfile, self).form_valid(form)

    @method_decorator(secure_required)
    @method_decorator(permission_required_or_403("change_profile"), (UsersProfiles, "user__username", "username"))
    def dispatch(self, *args, **kwargs):
        return super(EditUserProfile, self).dispatch(*args, **kwargs)


class TransferMoney(CreateView):
    model = MoneyTransaction
    form_class = TransferMoneyForm
    # fields = "__all__"
    template_name = "users/profile/addmoney.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['user'] = UsersProfiles.objects.get(user=self.request.user)
        return context

    def get_success_url(self):
        username = self.request.user
        return "{}".format(reverse("userena_profile_detail", kwargs={"username": username}))

    def form_valid(self, form):
        form.instance.sender = self.request.user
        transfered_money = form.instance.amount
        send_from = UsersProfiles.objects.get(user=self.request.user)
        send_to = UsersProfiles.objects.get(user=form.instance.recipient)
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
