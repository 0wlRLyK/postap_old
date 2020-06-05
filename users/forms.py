from ajax_select.fields import AutoCompleteField
from django import forms
from userena.forms import EditProfileForm


class EditFormExtra(EditProfileForm):
    country = AutoCompleteField('cities_light_country')
    # city = AutoCompleteField('cities_light_city')

    # AVATAR CROPPING params
    x = forms.FloatField(required=False)
    y = forms.FloatField(required=False)
    width = forms.FloatField(required=False)
    height = forms.FloatField(required=False)
    # SIGNATURE CROPPING params
    x_sign = forms.FloatField(required=False)
    y_sign = forms.FloatField(required=False)
    width_sign = forms.FloatField(required=False)
    height_sign = forms.FloatField(required=False)
    # BACKGROUND CROPPING params
    x_bg = forms.FloatField(required=False)
    y_bg = forms.FloatField(required=False)
    width_bg = forms.FloatField(required=False)
    height_bg = forms.FloatField(required=False)

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
