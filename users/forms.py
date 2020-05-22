from ajax_select.fields import AutoCompleteSelectMultipleField
from userena.forms import EditProfileForm


class EditFormExtra(EditProfileForm):
    country = AutoCompleteSelectMultipleField('cities_light_country')
    city = AutoCompleteSelectMultipleField('cities_light_city')
