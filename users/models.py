from datetime import datetime

from cities_light.models import Country, City
from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, Group
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from equipment.models import EquipItem
from multiselectfield import MultiSelectField
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
    username = "{}/".format(instance.username)
    date = "{}/".format(get_datetime_now().date())
    path = userena_settings.USERENA_MUGSHOT_PATH % {
        "username": instance.username,
        "id": instance.id,
        "date": instance.date_joined,
        "date_now": get_datetime_now().date(),
    }
    return "%(path)s%(username)s%(date)s%(hash)s.%(extension)s" % {
        "username": username,
        "date": date,
        "path": path,
        "hash": generate_nonce()[:10],
        "extension": extension,
    }


def upload_to_avatar(instance, filename):
    extension = filename.split(".")[-1].lower()
    type_img = "avatars/"
    username = "{}/".format(instance.username)
    date = "{}/".format(get_datetime_now().date())
    path = userena_settings.USERENA_MUGSHOT_PATH % {
        "username": instance.username,
        "id": instance.id,
        "date": instance.date_joined,
        "date_now": get_datetime_now().date(),
    }
    return "%(path)s%(type_img)s%(username)s%(date)s%(hash)s.%(extension)s" % {
        "path": path,
        "type_img": type_img,
        "username": username,
        "date": date,
        "hash": generate_nonce()[:10],
        "extension": extension,
    }


def upload_to_sign(instance, filename):
    extension = filename.split(".")[-1].lower()
    type_img = "signs/"
    username = "{}/".format(instance.username)
    date = "{}/".format(get_datetime_now().date())
    path = userena_settings.USERENA_MUGSHOT_PATH % {
        "username": instance.username,
        "id": instance.id,
        "date": instance.date_joined,
        "date_now": get_datetime_now().date(),
    }
    return "%(path)s%(type_img)s%(username)s%(date)s%(hash)s.%(extension)s" % {
        "path": path,
        "type_img": type_img,
        "username": username,
        "date": date,
        "hash": generate_nonce()[:10],
        "extension": extension,
    }


def upload_to_bg(instance, filename):
    extension = filename.split(".")[-1].lower()
    type_img = "bg/"
    username = "{}/".format(instance.user.username)
    date = "{}/".format(get_datetime_now().date())
    path = userena_settings.USERENA_MUGSHOT_PATH % {
        "username": instance.user.username,
        "id": instance.user.id,
        "date": instance.user.date_joined,
        "date_now": get_datetime_now().date(),
    }
    return "%(path)s%(type_img)s%(username)s%(date)s%(hash)s.%(extension)s" % {
        "path": path,
        "type_img": type_img,
        "username": username,
        "date": date,
        "hash": generate_nonce()[:10],
        "extension": extension,
    }





class Faction(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя категории")
    description = RichTextField(verbose_name="Описание группировки")
    logo = models.FileField(upload_to='users/factions', default='postap.png',
                            validators=[FileExtensionValidator(['png', 'gif', 'svg'])],
                            verbose_name="Логотип", help_text="Форматы svg, png, gif", blank=True)
    image = StdImageField(upload_to='users/factions', default='postap.png', verbose_name="Изображение", blank=True,
                          variations={'thumbnail': (120, 90), 'small': (300, 225), 'middle': (600, 450),
                                      'big': (800, 600), })
    rel_friends = models.ManyToManyField('self', verbose_name="Союзные группировки", blank=True)
    rel_neutrals = models.ManyToManyField('self', verbose_name="Нейтальные группировки", blank=True)
    rel_enemies = models.ManyToManyField('self', verbose_name="Враждебные", blank=True)

    leader = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Лидер", on_delete=models.DO_NOTHING, blank=True,
                               null=True,
                               related_name="gr_leader")
    deputy = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Заместитель", on_delete=models.DO_NOTHING,
                               blank=True, null=True,
                               related_name="gr_deputy")
    trader = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Торговец", on_delete=models.DO_NOTHING,
                               blank=True, null=True,
                               related_name="gr_trader")
    armourer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Оружейник", on_delete=models.DO_NOTHING,
                                 blank=True, null=True,
                                 related_name="gr_armourer")
    mechanic = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Механик", on_delete=models.DO_NOTHING,
                                 blank=True, null=True,
                                 related_name="gr_mechanic")
    medic = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Медик", on_delete=models.DO_NOTHING, blank=True,
                              null=True,
                              related_name="gr_medic")
    barmen = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Бармен", on_delete=models.DO_NOTHING, blank=True,
                               null=True,
                               related_name="gr_barmen")
    scientist = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Ученый", on_delete=models.DO_NOTHING,
                                  blank=True, null=True,
                                  related_name="gr_scientist")
    headhunter = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Главный по найму",
                                   on_delete=models.DO_NOTHING, blank=True,
                                   null=True, related_name="gr_headhunter")
    guide = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Проводник", on_delete=models.DO_NOTHING,
                              blank=True, null=True,
                              related_name="gr_guide")

    security_commander = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Командир охраны",
                                           on_delete=models.DO_NOTHING,
                                           blank=True, null=True, related_name="gr_security_com")
    assault_commander = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Командир штурмовиков",
                                          on_delete=models.DO_NOTHING,
                                          blank=True, null=True, related_name="gr_assault_com")
    hunter_commander = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Командир охотников",
                                         on_delete=models.DO_NOTHING,
                                         blank=True, null=True, related_name="gr_hunter_com")
    sniper_commander = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Командир снайперов",
                                         on_delete=models.DO_NOTHING,
                                         blank=True, null=True, related_name="gr_sniper_com")

    trader_assistant = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Помощники торговца", blank=True,
                                              related_name="gr_trader_help")
    armourer_assistant = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Помощники оружейника",
                                                blank=True, related_name="gr_armourer_help")
    mechanic_assistant = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Помощники механика", blank=True,
                                                related_name="gr_mechanic_help")
    medic_assistant = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Помощники медика", blank=True,
                                             related_name="gr_medic_help")
    barmen_assistant = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Помощиники бармена", blank=True,
                                              related_name="gr_barmen_com")
    scientist_assistant = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Помощники ученого", blank=True,
                                                 related_name="gr_scientist_com")

    security = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Служба охраны", blank=True,
                                      related_name="gr_security")
    assaults = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Штурмовики", blank=True,
                                      related_name="gr_assaults")
    hunters = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Охотники", blank=True,
                                     related_name="gr_hunters")
    snipers = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Снайперы", blank=True,
                                     related_name="gr_snipers")
    legends = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Легендарные участники группировки",
                                     blank=True,
                                     related_name="gr_legends")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группировка"
        verbose_name_plural = "Группировки"


class AvatarCategory(models.Model):
    AVATAR_TYPES = [
        ("user", "Пользовательский"),
        ("role", "Для ролевой"),
    ]
    name = models.CharField(max_length=200, verbose_name="Имя категории")
    sort = models.CharField(max_length=10, choices=AVATAR_TYPES, default="user", verbose_name="Тип аватара")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория аватаров"
        verbose_name_plural = "Категории аватаров"


class Avatar(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название аватара")
    category = models.ForeignKey(AvatarCategory, on_delete=models.DO_NOTHING, blank=True, null=True, )
    image = models.ImageField(blank=True, upload_to='avatars/base', verbose_name="Аватар")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аватар"
        verbose_name_plural = "Аватары"


class SiteUser(AbstractUser):
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
    avatar = models.ImageField(_("Avatar"), blank=True, null=True, upload_to=upload_to_avatar, default="postap.png")
    faction = models.ForeignKey(Faction, verbose_name=_('Faction'), on_delete=models.CASCADE, null=True)
    birthday = models.DateField(_('Birthday'), default=datetime.strptime('01-06-1990', '%m-%d-%Y').date())
    # objects = BirthdayManager()
    gender = models.CharField(_('Gender'), max_length=100, choices=settings.GENDERS, default="None")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True, )
    # OLD: city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True, )
    city = models.CharField(_('City'), max_length=50, default=" ", blank=True)

    signature = RichTextField(_('Signature'), default="", blank=True)
    sign_image = models.ImageField(_("Signature image"), blank=True, null=True, upload_to=upload_to_sign,
                                   default="postap.png")

    rpl_nickname = models.CharField(_('Nickname of hero'), max_length=50, default="Stalker", blank=True)
    rpl_first_name = models.CharField(_('First name of hero'), max_length=50, default="", blank=True)
    rpl_second_name = models.CharField(_('Second name of hero'), max_length=50, default="", blank=True)

    rpl_bio = RichTextField(_('Biography of hero'), default="", blank=True)
    rpl_avatar = models.ForeignKey(Avatar, verbose_name=_('avatar'), default='img/profile/no_data.gif',
                                   on_delete=models.CASCADE, blank=True, null=True)
    speciality = models.CharField(_('Speciality of hero'), max_length=200, choices=SPECIALITIES, default="no")
    rpl_xp = models.IntegerField(_('Experience of hero'), default=0)
    rpl_lvl = models.IntegerField(_('Level of hero'), default=0)
    rpl_rank = models.PositiveSmallIntegerField(_('Rank of user'), default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(10)])

    hp = models.PositiveSmallIntegerField(_('Health points'), default=100)
    rad = models.SmallIntegerField(_('Radiation points'), default=0)
    satiety = models.SmallIntegerField(_('Satiety points'), default=20)

    reputation = models.IntegerField(_('Reputation'), default=0)
    money = models.IntegerField(_('Money'), default=0)
    xp = models.IntegerField(_('Experience'), default=0)
    level = models.IntegerField(_('Level'), default=0)
    rank = models.PositiveSmallIntegerField(_('Rank of hero'), default=1,
                                            validators=[MinValueValidator(1), MaxValueValidator(5)])

    # EQUIPMENT

    slot1 = models.ForeignKey(EquipItem, related_name="weapons1", default=None, verbose_name="Первый слот",
                              on_delete=models.CASCADE, null=True, blank=True)
    slot2 = models.ForeignKey(EquipItem, related_name="weapons2", default=None, verbose_name="Второй слот",
                              on_delete=models.CASCADE, null=True, blank=True)
    slot3 = models.ForeignKey(EquipItem, related_name="weapons3", default=None, verbose_name="Третий слот",
                              on_delete=models.CASCADE, null=True, blank=True)
    armor = models.ForeignKey(EquipItem, related_name="armor", default=None, verbose_name="Броня",
                              on_delete=models.CASCADE, null=True, blank=True)
    helmet = models.ForeignKey(EquipItem, related_name="helmet", default=None, verbose_name="Шлем",
                               on_delete=models.CASCADE, null=True, blank=True)
    backpack = models.ForeignKey(EquipItem, related_name="backpack", default=None, verbose_name="Устройство №1",
                                 on_delete=models.CASCADE, null=True, blank=True)

    device1 = models.ForeignKey(EquipItem, related_name="device1", default=None, verbose_name="Устройство №1",
                                on_delete=models.CASCADE, null=True, blank=True)
    device2 = models.ForeignKey(EquipItem, related_name="device2", default=None, verbose_name="Устройство №2",
                                on_delete=models.CASCADE, null=True, blank=True)
    device3 = models.ForeignKey(EquipItem, related_name="device3", default=None, verbose_name="Устройство №3",
                                on_delete=models.CASCADE, null=True, blank=True)

    belt1 = models.ForeignKey(EquipItem, related_name="ammo1", default=None, verbose_name="Боеприпасы №1",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt2 = models.ForeignKey(EquipItem, related_name="ammo2", default=None, verbose_name="Боеприпасы №2",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt3 = models.ForeignKey(EquipItem, related_name="ammo3", default=None, verbose_name="Боеприпасы №3",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt4 = models.ForeignKey(EquipItem, related_name="ammo4", default=None, verbose_name="Боеприпасы №4",
                              on_delete=models.CASCADE, null=True, blank=True)

    container1 = models.ForeignKey(EquipItem, related_name="art1", default=None, verbose_name="Артефакт №1",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container2 = models.ForeignKey(EquipItem, related_name="art2", default=None, verbose_name="Артефакт №2",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container3 = models.ForeignKey(EquipItem, related_name="art3", default=None, verbose_name="Артефакт №3",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container4 = models.ForeignKey(EquipItem, related_name="art4", default=None, verbose_name="Артефакт №4",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container5 = models.ForeignKey(EquipItem, related_name="art5", default=None, verbose_name="Артефакт №5",
                                   on_delete=models.CASCADE, null=True, blank=True)

    last_online = models.DateTimeField(blank=True, null=True)

    @property
    def get_equip_items(self):
        return self.equip_items.all()

    @property
    def full_rank(self):
        return settings.LEVELS[self.rank]

    @property
    def full_rpl_rank(self):
        return settings.RANKS_ROLEPLAY[self.rpl_rank]

    def clean(self, *args, **kwargs):
        if self.slot1 and self.slot1.content_type.model != "weapon":
            raise ValidationError('В слоте №1 должны быть обьекты типа WEAPON')
        elif self.slot2 and self.slot2.content_type.model != "weapon":
            raise ValidationError('В слоте №2 должны быть обьекты типа WEAPON')
        elif self.slot3 and self.slot3.content_type.model != "weapon":
            raise ValidationError('В слоте №3 должны быть обьекты типа WEAPON')
        elif self.armor and self.armor.content_type.model != "outfit":
            raise ValidationError('В слоте брони должны быть обьекты типа OUTFIT')
        elif self.helmet and self.helmet.content_type.model != "helmet":
            if self.armor.c_obj and self.armor.c_obj.helmet_built_in:
                raise ValidationError('В используемом костюме уже имеется встроенный шлем')
            raise ValidationError('В слоте шлемов должны быть обьекты типа HELMET')
        elif self.backpack and self.backpack.content_type.model != "backpack":
            raise ValidationError('В слоте рюкзаков должны быть обьекты типа BACKPACK')
        elif self.device1 and self.device1.content_type.model != "device":
            raise ValidationError('В слоте устройств должны быть обьекты типа DEVICE')
        elif self.device2 and self.device2.content_type.model != "device":
            raise ValidationError('В слоте устройств должны быть обьекты типа DEVICE')
        elif self.device3 and self.device3.content_type.model != "device":
            raise ValidationError('В слоте устройств должны быть обьекты типа DEVICE')
        elif self.belt1 and self.belt1.content_type.model != "ammo":
            raise ValidationError('На поясе [1] должны быть обьекты типа AMMO')
        elif self.belt2 and self.belt2.content_type.model != "ammo":
            raise ValidationError('На поясе [2] должны быть обьекты типа AMMO')
        elif self.belt3 and self.belt3.content_type.model != "ammo":
            raise ValidationError('На поясе  [3]должны быть обьекты типа AMMO')
        elif self.belt4 and self.belt4.content_type.model != "ammo":
            raise ValidationError('На поясе [4] должны быть обьекты типа AMMO')

    def full_clean(self, *args, **kwargs):
        return self.clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(SiteUser, self).save(*args, **kwargs)

    # В данном методе проверяем, что дата последнего посещения не старше 15 минут
    def is_online(self):
        if self.last_online:
            return (timezone.now() - self.last_online) < timezone.timedelta(minutes=15)
        return False

    # Если пользователь посещал сайт не более 15 минут назад,
    def get_online_info(self):
        if self.is_online():
            # то возвращаем информацию, что он онлайн
            return _('Online')
        if self.last_online:
            # иначе пишем сообщение о последнем посещении
            return _('Last visit {}').format(naturaltime(self.last_online))
            # Если вы только недавно добавили информацию о посещении пользователем сайта
            # то для некоторых пользователей инфомации о посещении может и не быть, вернём информацию, что последнее посещение неизвестно
        return _('Unknown')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UsersProfiles(UserenaBaseProfile):
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

    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, verbose_name=_('user'),
                                related_name='users_profiles',
                                on_delete=models.CASCADE)
    slug = models.SlugField(_("Slug"), unique=True, null=True, editable=False, blank=True, max_length=300)
    bg = models.ImageField(_("Background image"), blank=True, null=True, upload_to=upload_to_bg)
    quote = models.CharField(_("Status"), max_length=100, blank=True, default="")
    permissions = MultiSelectField(_('permissions'), max_length=200, choices=PERMISIONS, null=True, blank=True)
    mugshot = None

    def save(self, *args, **kwargs):
        self.slug = self.user.get_username()
        super(UsersProfiles, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"


class MoneyTransaction(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name="Отправитель",
                               related_name="money_from")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name="Получатель",
                                  related_name="money_to")
    amount = models.IntegerField(verbose_name="Сумма")
    comment = RichTextField(max_length=250)

    class Meta:
        verbose_name = "Денежная транзакции"
        verbose_name_plural = "Денежные транзакции"


class ReputationTransaction(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name="Отправитель",
                               related_name="rep_from")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name="Получатель",
                                  related_name="rep_to")
    amount = models.IntegerField(verbose_name="Сумма")
    comment = RichTextField(max_length=250)

    class Meta:
        verbose_name = "Репутационная транзакции"
        verbose_name_plural = "Репутационные транзакции"
