from chat.models import Chat
from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.html import format_html
from equipment import models as equip
from users import models as user


def upload_to(instance, filename):
    return '/'.join(['roleplay', str(instance._meta.model_name), filename])


class AbstractLocation(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = RichTextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Иконка", upload_to=upload_to)

    def icon_admin(self):
        return format_html('<center><img href="{0}" src="{0}" /></center>'.format(self.image.url))

    icon_admin.allow_tags = True
    icon_admin.short_description = 'Иконка'

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Location(AbstractLocation):
    transitions = models.ManyToManyField('self', verbose_name="Переходы", blank=True)
    map = models.ImageField(upload_to="roleplay/location/maps/", default="postap.png")

    @property
    def get_areas(self):
        return self.areas.all()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Area(AbstractLocation):
    x_coord = models.FloatField(default=0, verbose_name="X координата",
                                help_text="Расположение элемента по X координате")
    y_coord = models.FloatField(default=0, verbose_name="Y координата",
                                help_text="Расположение элемента по Y координате")
    transitions = models.ManyToManyField('self', verbose_name="Переходы", blank=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="areas",
                                 verbose_name="Локация")

    @property
    def get_sublocations(self):
        return self.sublocations.all()

    class Meta:
        verbose_name = "Территория"
        verbose_name_plural = "Территории"


class SubLocation(AbstractLocation):
    TYPES_OF_SUBLOCATIONS = (
        ("none", "Подлокация"),
        ("trader", "Лавка торговца"),
        ("mechanic", "Рабочее место механика"),
        ("bar", "Бар"),
        ("medic", "Медпункт"),
        ("abandoned", "Заброшка"),
    )
    type_of_subloc = models.CharField(max_length=100, choices=TYPES_OF_SUBLOCATIONS, default="none",
                                      verbose_name="Тип подлокации")
    transitions = models.ManyToManyField('self', verbose_name="Переходы", blank=True)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="sublocations",
                             verbose_name="Локация")

    @property
    def get_traders(self):
        return self.npc_traders.all()

    @property
    def get_mechanics(self):
        return self.npc_mechanics.all()

    @property
    def get_npc_minimage(self):
        return self.npc_minigames.all()

    class Meta:
        verbose_name = "Подлокация"
        verbose_name_plural = "Подлокации"


class CampFire(models.Model):
    """
    CampFire - Roleplay chat
    """
    name = models.CharField(max_length=70, verbose_name="Название чата")
    area = models.ForeignKey(Area, verbose_name="Територия", null=True, on_delete=models.SET_NULL,
                             related_name="campfires")
    chat = models.ForeignKey(Chat, verbose_name="Чат", null=True, on_delete=models.SET_NULL)
    image = models.ImageField(verbose_name="Превью", upload_to="roleplay/campfire/preview/", null=True)
    bg = models.ImageField(verbose_name="Фон", upload_to="roleplay/campfire/bg/", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Костер (ролевой чат)"
        verbose_name_plural = "Костры (ролевые чаты)"


def npc_upload_to_ava(instance, filename):
    return '/'.join(['roleplay', "npc", str(instance._meta.model_name), "avatar", filename])


def npc_upload_to_img(instance, filename):
    return '/'.join(['roleplay', "npc", str(instance._meta.model_name), "image", filename])


class AbstractNPC(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    full_name = models.CharField(max_length=150, verbose_name="Полное Имя")
    bio = RichTextField(verbose_name="Описание", blank=True)
    spec = "NPC"
    rank = models.PositiveSmallIntegerField(verbose_name="Ранг", default=1,
                                            validators=[MinValueValidator(1), MaxValueValidator(10)])
    sublocation = models.ForeignKey(SubLocation, related_name="npc", on_delete=models.DO_NOTHING, blank=True,
                                    null=True,
                                    verbose_name="Локация")
    avatar = models.ImageField(verbose_name="Аватар", default="img/profile/no_data.gif", upload_to=npc_upload_to_ava)
    image = models.ImageField(verbose_name="Изображение персонажа", help_text="(Желательно в полный рост и по центру)",
                              upload_to=npc_upload_to_img)

    money = models.IntegerField(verbose_name="Деньги", default=0)
    inf = models.BooleanField(default=False, verbose_name="Бесконечны ли деньги")

    def avatar_adm(self):
        return format_html('<center><img href="{0}" src="{0}" /></center>'.format(self.avatar.url))

    avatar_adm.allow_tags = True
    avatar_adm.short_description = 'Иконка'

    @property
    def full_rank(self):
        return settings.RANKS_ROLEPLAY[self.rank if self.rank <= 5 else 5]

    class Meta:
        abstract = True

    def __str__(self):
        return self.name + self.spec



class Trader(AbstractNPC):
    faction = models.ForeignKey(user.Faction, on_delete=models.DO_NOTHING, blank=True, null=True,
                                verbose_name="Группировка", related_name="rp_npc_trader")
    spec = "Торговец"
    sublocation = models.ForeignKey(SubLocation, related_name="npc_traders", on_delete=models.DO_NOTHING, blank=True,
                                    null=True,
                                    verbose_name="Локация")
    items = models.ManyToManyField(equip.Item, verbose_name="Предметы на продажу", blank=True)
    coef_trade = models.FloatField(verbose_name="Коєфициент продажи", default=1,
                                   validators=[MinValueValidator(0.2), MaxValueValidator(5)])
    coef_buy = models.FloatField(verbose_name="Коєфициент покупки", default=1,
                                 validators=[MinValueValidator(0.2), MaxValueValidator(5)])

    @property
    def spec_icon(self):
        return "/static/img/roleplay/npc/specialities/trader.svg"

    class Meta:
        verbose_name = "Торговец"
        verbose_name_plural = "Торговцы"


class Mechanic(AbstractNPC):
    faction = models.ForeignKey(user.Faction, on_delete=models.DO_NOTHING, blank=True, null=True,
                                verbose_name="Группировка", related_name="rp_npc_mechanic")
    spec = "Механик"
    sublocation = models.ForeignKey(SubLocation, related_name="npc_mechanics", on_delete=models.DO_NOTHING, blank=True,
                                    null=True, verbose_name="Локация")
    items = models.ManyToManyField(equip.Item, verbose_name="Предметы на продажу", blank=True)
    coef_trade = models.FloatField(verbose_name="Коєфициент продажи", default=1,
                                   validators=[MinValueValidator(0.2), MaxValueValidator(5)])
    coef_buy = models.FloatField(verbose_name="Коєфициент покупки", default=1,
                                 validators=[MinValueValidator(0.2), MaxValueValidator(5)])
    coef_repair = models.FloatField(verbose_name="Коєфициент починки", default=1,
                                    validators=[MinValueValidator(0.2), MaxValueValidator(5)])

    @property
    def spec_icon(self):
        return "/static/img/roleplay/npc/specialities/mechanic.svg"


class Meta:
    verbose_name = "Механик"
    verbose_name_plural = "Механики"


class NPCMinigame(AbstractNPC):
    SPECIALTIES = (
        ("trader", "Торговец"),
        ("mechanic", "Механик"),
        ("medic", "Медик"),
        ("barmen", "Бармен"),
        ("npc", "Сталкер"),
    )
    sublocation = models.ForeignKey(SubLocation, related_name="npc_minigames", on_delete=models.DO_NOTHING, blank=True,
                                    null=True, verbose_name="Локация")
    faction = models.ForeignKey(user.Faction, on_delete=models.DO_NOTHING, blank=True, null=True,
                                verbose_name="Группировка", related_name="rp_npc_minigame")
    spec = models.CharField(choices=SPECIALTIES, verbose_name="Специальность", max_length=25, default="npc")
    items = models.ManyToManyField(equip.Item, verbose_name="Предметы на продажу", blank=True)
    coef_trade = models.FloatField(verbose_name="Коєфициент продажи", default=1,
                                   validators=[MinValueValidator(0.2), MaxValueValidator(5)])
    coef_buy = models.FloatField(verbose_name="Коєфициент покупки", default=1,
                                 validators=[MinValueValidator(0.2), MaxValueValidator(5)])

    @property
    def spec_icon(self):
        return "/static/img/roleplay/npc/specialities/minigame.svg"

    class Meta:
        verbose_name = "NPC с миниигрой"
        verbose_name_plural = "NPC`s с миниигрой"
