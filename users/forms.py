from ajax_select.fields import AutoCompleteField
from django import forms
from userena.forms import EditProfileForm

from .models import MoneyTransaction


class EditFormExtra(EditProfileForm):
    country = AutoCompleteField('cities_light_country')
    # city = AutoCompleteField('cities_light_city')  # NOT USED - CITIES FIELD NOT PROVIDED

    # AVATAR CROPPING params
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # SIGNATURE CROPPING params
    x_sign = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y_sign = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width_sign = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height_sign = forms.FloatField(widget=forms.HiddenInput(), required=False)
    # BACKGROUND CROPPING params
    x_bg = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y_bg = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width_bg = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height_bg = forms.FloatField(widget=forms.HiddenInput(), required=False)

    def clean_country(self):
        data = self.data.copy()
        self.data = data

    class Meta(EditProfileForm.Meta):
        fields = ("mugshot", "sign_image", "bg", "x", "y", "width", "height",
                  "x_sign", "y_sign", "width_sign", "height_sign",
                  "x_bg", "y_bg", "width_bg", "height_bg",
                  "country", "city", "gender", "birthday", "signature", "quote")
        widgets = {
            'mugshot': forms.FileInput(attrs={
                'accept': 'image/*'  # this is not an actual validation! don't rely on that!
            })
        }
        # exclude = EditProfileForm.Meta.exclude
        # fields = ["country", "city"]

    def save(self, commit=False, *args, **kwargs):
        photo = super(EditFormExtra, self).save(commit=True, *args, **kwargs)

        return photo


class TransferMoneyForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=0)

    class Meta:
        model = MoneyTransaction
        fields = '__all__'
