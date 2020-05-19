from datetime import datetime

from cities_light.models import Country, City
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, Group
from django.db import models
from django.utils.translation import gettext as _
from image_cropping import ImageCropField, ImageRatioField
from multiselectfield import MultiSelectField
from postap import settings
from stdimage import StdImageField
from userena import settings as userena_settings
from userena.models import UserenaBaseProfile
from userena.utils import (
    generate_nonce,
    get_datetime_now,
)


def upload_to_mugshot(instance, filename):
    """
    Uploads a mugshot for a user to the ``USERENA_MUGSHOT_PATH`` and saving it
    under unique hash for the image. This is for privacy reasons so others
    can't just browse through the mugshot directory.

    """
    extension = filename.split(".")[-1].lower()
    path = userena_settings.USERENA_MUGSHOT_PATH % {
        "username": instance.user.username,
        "id": instance.user.id,
        "date": instance.user.date_joined,
        "date_now": get_datetime_now().date(),
    }
    return "%(path)s%(hash)s.%(extension)s" % {
        "path": path,
        "hash": generate_nonce()[:10],
        "extension": extension,
    }


class Equipment(models.Model):
    title = models.CharField(max_length=200)


class RplAvatarCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя категории")


class RplAvatar(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название аватара")
    category = models.ForeignKey(RplAvatarCategory, on_delete=models.DO_NOTHING, blank=True, null=True, )
    image = ImageCropField(blank=True, upload_to='avatars/base', verbose_name="Аватар")
    cropping = ImageRatioField('avatar', "{0}x{0}".format(userena_settings.USERENA_MUGSHOT_SIZE))


class Faction(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя категории")
    description = RichTextField(verbose_name="Описание группировки")
    logo = StdImageField(upload_to='users/factions', default='postap.png', verbose_name="Изображение", blank=True,
                         variations={'thumbnail': (120, 90), 'small': (300, 225)})
    image = StdImageField(upload_to='users/factions', default='postap.png', verbose_name="Изображение", blank=True,
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    rel_friends = models.ManyToManyField('self', verbose_name="Союзные группировки", blank=True)
    rel_neutrals = models.ManyToManyField('self', verbose_name="Нейтальные группировки", blank=True)
    rel_enemies = models.ManyToManyField('self', verbose_name="Враждебные", blank=True)

    leader = models.ForeignKey(User, verbose_name="Лидер", on_delete=models.DO_NOTHING, blank=True, null=True,
                               related_name="gr_leader")
    deputy = models.ForeignKey(User, verbose_name="Заместитель", on_delete=models.DO_NOTHING, blank=True, null=True,
                               related_name="gr_deputy")
    trader = models.ForeignKey(User, verbose_name="Торговец", on_delete=models.DO_NOTHING, blank=True, null=True,
                               related_name="gr_trader")
    armourer = models.ForeignKey(User, verbose_name="Оружейник", on_delete=models.DO_NOTHING, blank=True, null=True,
                                 related_name="gr_armourer")
    mechanic = models.ForeignKey(User, verbose_name="Механик", on_delete=models.DO_NOTHING, blank=True, null=True,
                                 related_name="gr_mechanic")
    medic = models.ForeignKey(User, verbose_name="Медик", on_delete=models.DO_NOTHING, blank=True, null=True,
                              related_name="gr_medic")
    barmen = models.ForeignKey(User, verbose_name="Бармен", on_delete=models.DO_NOTHING, blank=True, null=True,
                               related_name="gr_barmen")
    scientist = models.ForeignKey(User, verbose_name="Ученый", on_delete=models.DO_NOTHING, blank=True, null=True,
                                  related_name="gr_scientist")
    headhunter = models.ForeignKey(User, verbose_name="Главный по найму", on_delete=models.DO_NOTHING, blank=True,
                                   null=True, related_name="gr_headhunter")
    guide = models.ForeignKey(User, verbose_name="Проводник", on_delete=models.DO_NOTHING, blank=True, null=True,
                              related_name="gr_guide")

    security_commander = models.ForeignKey(User, verbose_name="Командир охраны", on_delete=models.DO_NOTHING,
                                           blank=True, null=True, related_name="gr_security_com")
    assault_commander = models.ForeignKey(User, verbose_name="Командир штурмовиков", on_delete=models.DO_NOTHING,
                                          blank=True, null=True, related_name="gr_assault_com")
    hunter_commander = models.ForeignKey(User, verbose_name="Командир охотников", on_delete=models.DO_NOTHING,
                                         blank=True, null=True, related_name="gr_hunter_com")
    sniper_commander = models.ForeignKey(User, verbose_name="Командир снайперов", on_delete=models.DO_NOTHING,
                                         blank=True, null=True, related_name="gr_sniper_com")

    trader_assistant = models.ManyToManyField(User, verbose_name="Помощники торговца", blank=True,
                                              related_name="gr_trader_help")
    armourer_assistant = models.ManyToManyField(User, verbose_name="Помощники оружейника",
                                                blank=True, related_name="gr_armourer_help")
    mechanic_assistant = models.ManyToManyField(User, verbose_name="Помощники механика", blank=True,
                                                related_name="gr_mechanic_help")
    medic_assistant = models.ManyToManyField(User, verbose_name="Помощники медика", blank=True,
                                             related_name="gr_medic_help")
    barmen_assistant = models.ManyToManyField(User, verbose_name="Помощиники бармена", blank=True,
                                              related_name="gr_barmen_com")
    scientist_assistant = models.ManyToManyField(User, verbose_name="Помощники ученого", blank=True,
                                                 related_name="gr_scientist_com")

    security = models.ManyToManyField(User, verbose_name="Служба охраны", blank=True, related_name="gr_security")
    assaults = models.ManyToManyField(User, verbose_name="Штурмовики", blank=True, related_name="gr_assaults")
    hunters = models.ManyToManyField(User, verbose_name="Охотники", blank=True, related_name="gr_hunters")
    snipers = models.ManyToManyField(User, verbose_name="Снайперы", blank=True, related_name="gr_snipers")
    legends = models.ManyToManyField(User, verbose_name="Легендарные участники группировки", blank=True,
                                     related_name="gr_legends")


class AvatarCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя категории")


class Avatar(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название аватара")
    category = models.ForeignKey(AvatarCategory, on_delete=models.DO_NOTHING, blank=True, null=True, )
    image = ImageCropField(blank=True, upload_to='avatars/base', verbose_name="Аватар")
    cropping = ImageRatioField('avatar', "{0}x{0}".format(userena_settings.USERENA_MUGSHOT_SIZE))


class UsersProfiles(UserenaBaseProfile):
    SPECIALITIES = (
        ("no", _("Without speciality")),
        ("hunter", _("Hunter")),
        ("warrior", _("Warrior")),
        ("stalker", _("Stalker")),
        ("mechanic", _("Mechanic")),
        ("doctor", _("Doctor")),
        ("trader", _("Trader")),
        ("guide", _("Guide")),
    )

    PERMISIONS = (
        ("faction", _("Faction")),
        ("speciality", _("Faction")),
        ("first_visit", _("First visit")),
        ("last_visit", _("Last visit")),
        ("birthday", _("Birthday")),
        ("gender", _("Gender")),
        ("reputation", _("Reputation")),
        ("money", _("Money")),
        ("xp", _("Experience")),
        ("lvl", _("Level")),
        ("rank", _("Rank")),
    )

    GEO_PERMISSIONS = (
        ("show_all", _("Show all data about your location in your profile ")),
        ("show_no_details", _("Show only data about your country and city, but without details")),
        ("show_country", _("Show only data about your country in your profile")),
        ("show_city", _("Show only data about your city in your profile")),
        ("show_none", _("Doesn't show information about my position in profile")),
    )

    user = models.OneToOneField(User, unique=True, verbose_name=_('user'), related_name='users_profiles',
                                on_delete=models.CASCADE)
    faction = models.ForeignKey(Faction, verbose_name=_('user'), on_delete=models.CASCADE, null=True)

    mugshot = ImageCropField(_("avatar"), blank=True, null=True, upload_to=upload_to_mugshot)
    cropping = ImageRatioField('avatar', "{0}x{0}".format(userena_settings.USERENA_MUGSHOT_SIZE),
                               verbose_name=_("cropping"), )
    avatar = models.ForeignKey(Avatar, on_delete=models.DO_NOTHING, blank=True, null=True, )
    birthday = models.DateField(_('birthday'), default=datetime.strptime('01-06-2020', '%m-%d-%Y').date())
    # objects = BirthdayManager()
    gender = models.CharField(_('gender'), max_length=100, choices=settings.GENDERS, default="None")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True, )
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True, )

    signature = RichTextField(_('signature'), default="")
    sign_image = ImageCropField(_("avatar"), blank=True, null=True, upload_to=upload_to_mugshot)
    sign_image_crop = ImageRatioField('avatar', "600x200", verbose_name=_("cropping"), )

    rpl_nickname = models.CharField(_('Nickname of hero'), max_length=50, default="Stalker", blank=True)
    rpl_first_name = models.CharField(_('First name of hero'), max_length=50, default="", blank=True)
    rpl_second_name = models.CharField(_('Second name of hero'), max_length=50, default="", blank=True)

    rpl_bio = RichTextField(_('biography'), default="", blank=True)
    rpl_avatar = models.ForeignKey(RplAvatar, verbose_name=_('avatar'), on_delete=models.CASCADE, blank=True, null=True)
    speciality = models.CharField(_('Speciality'), max_length=200, choices=SPECIALITIES, default="no")
    rpl_xp = models.IntegerField(_('experience'), default=0)
    rpl_lvl = models.IntegerField(_('level'), default=0)
    rank = models.IntegerField(_('rank'), default=0)

    reputation = models.IntegerField(_('reputation'), default=0)
    money = models.IntegerField(_('reputation'), default=0)
    xp = models.IntegerField(_('experience'), default=0)
    level = models.IntegerField(_('level'), default=0)

    permissions = MultiSelectField(_('permissions'), max_length=200, choices=PERMISIONS, null=True, blank=True)
    geo_permissions = models.CharField(_('Location permissions'), max_length=200, choices=GEO_PERMISSIONS,
                                       default="show_no_details")

    equipment = models.ForeignKey(Equipment, on_delete=models.DO_NOTHING, blank=True, null=True, )
