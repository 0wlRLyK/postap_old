import os

from PIL import Image
from ajax_select.fields import AutoCompleteField
from cities_light.models import Country
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from postap import settings
from userena.forms import EditProfileForm

from .models import MoneyTransaction, SiteUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = SiteUser
        fields = ('username', 'email', 'avatar', 'birthday', 'gender', 'country', 'city', 'signature', 'sign_image',
                  'rpl_nickname', 'rpl_first_name', 'rpl_second_name', 'rpl_avatar', 'rpl_bio', 'speciality', 'rpl_xp',
                  'rpl_lvl', 'rpl_rank', 'hp', 'rad', 'satiety', 'reputation', 'money', 'xp', 'level', 'rank', 'slot1',
                  'slot2', 'slot3', 'armor', 'helmet', 'backpack', 'device1', 'device2', 'device3', 'belt1', 'belt2',
                  'belt3', 'belt4', 'container1', 'container2', 'container3', 'container4', 'container5')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'email', 'avatar', 'birthday', 'gender', 'country', 'city', 'signature', 'sign_image',
                  'rpl_nickname', 'rpl_first_name', 'rpl_second_name', 'rpl_avatar', 'rpl_bio', 'speciality', 'rpl_xp',
                  'rpl_lvl', 'rank', 'hp', 'rad', 'satiety', 'reputation', 'money', 'xp', 'level', 'slot1',
                  'slot2', 'slot3', 'armor', 'helmet', 'backpack', 'device1', 'device2', 'device3', 'belt1', 'belt2',
                  'belt3', 'belt4', 'container1', 'container2', 'container3', 'container4', 'container5')


class EditFormExtra(forms.ModelForm):
    first_name = forms.CharField(label="Имя", max_length=30, required=False)
    last_name = forms.CharField(label="Фамилия", max_length=30, required=False)
    avatar = forms.ImageField(required=False)
    birthday = forms.DateField(label="День рождения", required=False)
    gender = forms.ChoiceField(label="Пол", choices=settings.GENDERS, required=False)
    country = AutoCompleteField('cities_light_country')
    city = forms.CharField(label="City", max_length=30, required=False)
    signature = forms.CharField(widget=CKEditorWidget(), required=False)

    # city = AutoCompleteField('cities_light_city')  # NOT USED - CITIES FIELD NOT PROVIDED

    # AVATAR CROPPING params
    # forms.FloatField( required=False)
    x = forms.FloatField(required=False)
    y = forms.FloatField(required=False)
    width = forms.FloatField(required=False)
    height = forms.FloatField(required=False)
    # SIGNATURE CROPPING params
    sign_image = forms.ImageField(required=False)
    x_sign = forms.FloatField(required=False)
    y_sign = forms.FloatField(required=False)
    width_sign = forms.FloatField(required=False)
    height_sign = forms.FloatField(required=False)
    # BACKGROUND CROPPING params
    x_bg = forms.FloatField(required=False)
    y_bg = forms.FloatField(required=False)
    width_bg = forms.FloatField(required=False)
    height_bg = forms.FloatField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_valid():
            self.profile = super().save(commit=False)
            self.user = self.profile.user
            self.fields['signature'] = forms.ChoiceField(
                required=False,
                widget=CKEditorWidget(),
                initial=self.user.signature,
            )

    def clean_country(self):
        data = self.data.copy()
        self.data = data

    def save(self, force_insert=False, force_update=False, commit=True):
        profile = super().save(commit=False)
        profile.save()
        if 'bg' in self.changed_data:
            xl_bg = self.cleaned_data['x_bg']
            yl_bg = self.cleaned_data['y_bg']
            xr_bg = self.cleaned_data['width_bg']
            yr_bg = self.cleaned_data['height_bg']
            print(profile.bg, profile.bg.path)
            print(xl_bg, yl_bg, xr_bg, xr_bg)
            image_bg = Image.open(profile.bg)
            size = 1920, 400
            cropped_bg = image_bg.crop((xl_bg, yl_bg, xr_bg, yr_bg))
            resized_bg = cropped_bg.resize((1920, 400), Image.ANTIALIAS)
            resized_bg.save(profile.bg.path, commit=True)
        # Save first and last name
        user = profile.user

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.birthday = self.cleaned_data["birthday"]
        user.gender = self.cleaned_data["gender"]
        country_obj = Country.objects.get(name=self.data["country"])
        user.country = country_obj
        user.city = self.cleaned_data["city"]
        user.signature = self.cleaned_data["signature"]
        if 'avatar' in self.changed_data:
            x = self.cleaned_data['x']
            y = self.cleaned_data['y']
            w = self.cleaned_data['width']
            h = self.cleaned_data['height']
            print(x, y, w, h)
            print(user.avatar, user.avatar.path)
            image = Image.open(self.cleaned_data['avatar'])
            cropped = image.crop((x, y, w + x, h + y))
            cropped.save(user.avatar.path)
            print(user.avatar, user.avatar.path, cropped)
            for variation, value in zip(settings.AVATAR_VARIATIONS, settings.ratio_ava):
                cropped_image = image.crop((x, y, w + x, h + y))
                resized_image = cropped_image.resize((value, value), Image.ANTIALIAS)
                file_path = os.path.splitext(user.avatar.path)
                path = "{0}.{1}{2}".format(file_path[0], variation, file_path[1])
                resized_image.save(path, commit=True)
        if 'sign_image' in self.changed_data:
            x_s = self.cleaned_data['x_sign']
            y_s = self.cleaned_data['y_sign']
            w_s = self.cleaned_data['width_sign']
            h_s = self.cleaned_data['height_sign']
            print(x_s, y_s, w_s, h_s)
            # print(self.cleaned_data['sign_image'], self.cleaned_data['sign_image'].path)
            image_sign = Image.open(self.cleaned_data['sign_image'])
            cropped_sign = image_sign.crop((x_s, y_s, w_s + x_s, h_s + y_s))
            cropped_sign.save(user.sign_image.path, commit=True)
        user.save()

        return profile

    class Meta(EditProfileForm.Meta):

        exclude = EditProfileForm.Meta.exclude + ["mugshot", "slug", "quote", "permissions", ]
        fields = ["first_name", "last_name", "privacy", "birthday", "gender", "country", "city", "signature",
                  "avatar", "x", "y", "width", "height",
                  "sign_image", "x_sign", "y_sign", "width_sign", "height_sign",
                  "bg", "x_bg", "y_bg", "width_bg", "height_bg", ]


class TransferMoneyForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=0)

    class Meta:
        model = MoneyTransaction
        fields = '__all__'
