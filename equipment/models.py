# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.html import format_html
from users.models import Group


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    icon = models.ImageField(verbose_name="Иконка")
    description = RichTextField(verbose_name="Описание")

    cost = models.PositiveIntegerField(default=0, verbose_name="Стоимость")
    mass = models.FloatField(default=0, verbose_name="Масса")

    def icon_admin(self):
        return format_html('<center><img href="{0}" src="{0}" /></center>'.format(self.icon.url))

    icon_admin.allow_tags = True
    icon_admin.short_description = 'Иконка'

    def __str__(self):
        return self.name


class Mass(models.Model):
    mass = models.PositiveIntegerField(default=0, verbose_name="Масса")

    class Meta:
        abstract = True


class Ammo(Item, Mass):
    eq_type = "ammo"

    quantity = models.PositiveIntegerField(default=0, verbose_name="Колличество патронов в пачке")

    class Meta:
        verbose_name = "Пачка патронов"
        verbose_name_plural = "Патроны"


class Addon(Item, Mass):
    eq_type = "addon"

    accuracy = models.IntegerField(default=0, verbose_name="Точность")
    damage = models.IntegerField(default=0, verbose_name="Повреждение")
    convenience = models.IntegerField(default=0, verbose_name="Удобность")
    pace_of_fire = models.IntegerField(default=0, verbose_name="Скорострельность")
    capacity = models.IntegerField(default=0, verbose_name="Ёмкость")

    class Meta:
        verbose_name = "Аддон"
        verbose_name_plural = "Аддоны"


class WeaponAbstract(Item):
    WEAPONS_TYPES = [
        ("none", "/* NONE /*"),
        ("melee", "Ножи/Топоры"),
        ("pistols", "Пистолет"),
        ("smg", "Пистолеты-пулеметы"),
        ("shotguns", "Дробовики"),
        ("auto_rifles", "Автоматические винтовки"),
        ("sniper_rifles", "Снайперские винтовки"),
        ("explosive", "Гранатометы"),
        ("gauss", "Винтовка Гаусса"),
    ]

    sort = models.CharField(choices=WEAPONS_TYPES, max_length=100, verbose_name="Тип оружия")

    accuracy = models.IntegerField(default=0, verbose_name="Точность оружия")
    damage = models.IntegerField(default=0, verbose_name="Повреждение оружия")
    convenience = models.IntegerField(default=0, verbose_name="Удобность оружия")
    pace_of_fire = models.IntegerField(default=0, verbose_name="Скорострельность оружия")
    capacity = models.IntegerField(default=0, verbose_name="Ёмкость магазина")

    class Meta:
        abstract = True


class Weapon(WeaponAbstract, Mass):
    eq_type = "weapon"

    one_handed = models.BooleanField(default=False, verbose_name="Однорурчное",
                                     help_text="Является ли оружие одноручным. (Например, нож, пистолет)")
    ammo_type = models.ManyToManyField(Ammo, related_name="ammo_type", verbose_name="Тип боепприпасов",
                                       help_text="Боеприпасы которые используются данным видом оружия", blank=True)

    addons = models.ManyToManyField(Addon, related_name="addon1", verbose_name="1 слот аддонов: Варианты",
                                    help_text="Возможные аддоны для первого слота аддонов", blank=True)
    addon1open = models.BooleanField(default=True, verbose_name="1 слот аддонов: Доступность",
                                     help_text="Отрыт ли слот изначально")
    addon2open = models.BooleanField(default=True, verbose_name="2 слот аддонов: Доступность",
                                     help_text="Отрыт ли слот изначально")
    addon3open = models.BooleanField(default=True, verbose_name="3 слот аддонов: Доступность",
                                     help_text="Отрыт ли слот изначально")

    unique = models.BooleanField(default=False, verbose_name="Уникальное оружие")

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружие"


class WeaponUpgrade(WeaponAbstract):
    pass

    class Meta:
        verbose_name = "Улучшение оружия"
        verbose_name_plural = "Улучшения оружия"


class OutfitAbstract(Item):
    OUTFIT_TYPES = [
        ("none", "/* NONE /*"),
        ("rookie", "Одежда новичка"),
        ("cloak", "Плащи"),
        ("light", "Легкая броня"),
        ("middle", "Средняя броня"),
        ("rhbz", "Комбинезоны РХБЗ (радиоационной, химической и биологической защиты)"),
        ("science_low", "Научные комбинезоны(Низкий уровень)"),
        ("science_high", "Научные комбинезоны(Высокий уровень)"),
        ("seva", "СЕВА"),
        ("heavy", "Тяжелая броня"),
        ("protoexo", "Прототипы экзоскелета"),
        ("exo", "Экзоскелеты"),
        ("heavyexo", "Тяжелые экзоскелеты"),
    ]

    sort = models.CharField(choices=OUTFIT_TYPES, max_length=100, verbose_name="Тип брони")

    ballistic = models.IntegerField(default=0, verbose_name="Балистическая защита уникального костюма")
    burst = models.IntegerField(default=0, verbose_name="Защита от разрыва уникального костюма")
    kick = models.IntegerField(default=0, verbose_name="Гашение удара уникального костюма")
    explosion = models.IntegerField(default=0, verbose_name="Защита от взрыва уникального костюма")
    thermal = models.IntegerField(default=0, verbose_name="Термозащита уникального костюма")
    chemical = models.IntegerField(default=0, verbose_name="Химащита уникального костюма")
    electrical = models.IntegerField(default=0, verbose_name="Электрозащита уникального костюма")
    radioactive = models.IntegerField(default=0, verbose_name="Радиоактивная уникального костюма")
    psi = models.IntegerField(default=0, verbose_name="Пси защита уникального костюма")
    weight = models.IntegerField(default=0, verbose_name="Переносимый вес уникального костюма")

    arts_max = models.IntegerField(default=0, verbose_name="Колличество контейнеров для артефактов")
    modules_max = models.IntegerField(default=0, verbose_name="Колличество контейнеров для модулей")

    running = models.BooleanField(default=True, verbose_name="Возможность бега")

    class Meta:
        abstract = True


class Outfit(OutfitAbstract, Mass):
    eq_type = "outfit"

    equipped_icon = models.ImageField(default="postap.png", verbose_name="Иконка персонажа в костюме")
    helmet_built_in = models.BooleanField(default=False, verbose_name="Шлем",
                                          help_text="Присуствует ли всторенный шлем")
    unique = models.BooleanField(default=False, verbose_name="Уникальный костюм")

    def equipped_icon_admin(self):
        return format_html('<img href="{0}" src="{0}" style="width:75%;height:75%;" />'.format(self.equipped_icon.url))

    equipped_icon_admin.allow_tags = True
    equipped_icon_admin.short_description = 'Icon'

    class Meta:
        verbose_name = "Броня"
        verbose_name_plural = "Броня"


class OutfitUpgrade(OutfitAbstract):
    pass

    class Meta:
        verbose_name = "Улучшение брони"
        verbose_name_plural = "Улучшения брони"


class HelmetAbstract(Item):
    HELMET_TYPES = [
        ("none", "/* NONE /*"),
        ("headdress", "Головные уборы"),
        ("light", "Легкие шлемы"),
        ("middle", "Средние шлемы"),
        ("heavy", "Тяжелые шлемы"),
        ("science", "Научные шлемы"),
        ("exo", "Шлемы экзо"),
    ]

    sort = models.CharField(choices=HELMET_TYPES, max_length=100, verbose_name="Тип оружия")
    ballistic = models.IntegerField(default=0, verbose_name="Балистическая защита уникального шлема")
    burst = models.IntegerField(default=0, verbose_name="Защита от разрыва уникального шлема")
    kick = models.IntegerField(default=0, verbose_name="Гашение удара уникального шлема")
    explosion = models.IntegerField(default=0, verbose_name="Защита от взрыва уникального шлема")
    thermal = models.IntegerField(default=0, verbose_name="Термозащита уникального шлема")
    chemical = models.IntegerField(default=0, verbose_name="Химащита уникального шлема")
    electrical = models.IntegerField(default=0, verbose_name="Электрозащита уникального шлема")
    radioactive = models.IntegerField(default=0, verbose_name="Радиоактивная уникального шлема")
    psi = models.IntegerField(default=0, verbose_name="Пси защита уникального шлема")
    weight = models.IntegerField(default=0, verbose_name="Переносимый вес уникального шлема")

    class Meta:
        abstract = True


class HelmetUpgrade(HelmetAbstract):
    pass

    class Meta:
        verbose_name = "Улучшение шлемов"
        verbose_name_plural = "Улучшения шлемов"


class Helmet(HelmetAbstract, Mass):
    eq_type = "helmet"

    unique = models.BooleanField(default=False, verbose_name="Уникальный шлем")

    class Meta:
        verbose_name = "Шлем"
        verbose_name_plural = "Шлемы"


class Backpack(Item, Mass):
    eq_type = "backpack"

    carry_weight = models.IntegerField(default=0, verbose_name="Максимальный переносимый вес")

    class Meta:
        verbose_name = "Рюкзак"
        verbose_name_plural = "Рюкзаки"


class Device(Item, Mass):
    ACTIONS_FOR_USE = [
        ('use', 'Использовать'),
        ('play', 'Играть'),
    ]
    eq_type = "device"

    slot_setting = models.BooleanField(verbose_name="Возможность установить в слот устройств")

    actions = models.CharField(max_length=10, choices=ACTIONS_FOR_USE, verbose_name="Действия для использования")

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"


class FoodAndMedicine(Item, Mass):
    ACTIONS_FOR_USE = [
        ('use', 'Использовать'),
        ('eat', 'Съесть'),
        ('drink', 'Выпить'),
    ]
    eq_type = "food_medicine"

    ballistic = models.IntegerField(default=0, verbose_name="Балистическая защита")
    burst = models.IntegerField(default=0, verbose_name="Защита от разрыва")
    kick = models.IntegerField(default=0, verbose_name="Гашение удара")
    explosion = models.IntegerField(default=0, verbose_name="Защита от взрыва")
    thermal = models.IntegerField(default=0, verbose_name="Термозащита")
    chemical = models.IntegerField(default=0, verbose_name="Химащита")
    electrical = models.IntegerField(default=0, verbose_name="Электрозащита")
    radioactive = models.IntegerField(default=0, verbose_name="Радиозащита")
    psi = models.IntegerField(default=0, verbose_name="Пси защита")
    weight = models.IntegerField(default=0, verbose_name="Переносимый вес")
    healing = models.IntegerField(default=0, verbose_name="Лечение")
    satiety = models.IntegerField(default=0, verbose_name="Насыщение")
    energy = models.IntegerField(default=0, verbose_name="Восстановление энергии")

    actions = models.CharField(max_length=10, choices=ACTIONS_FOR_USE, verbose_name="Действия для использования")

    class Meta:
        verbose_name = "Пищу и медикаменты"
        verbose_name_plural = "Пища и медикаменты"


class Misc(Item, Mass):
    eq_type = "misc"

    class Meta:
        verbose_name = "Разное"
        verbose_name_plural = "Разное"


class Artifact(Item, Mass):
    eq_type = "artifact"
    HELMET_TYPES = [
        ("rock", "Булыжник"),
        ("first", "I уровня"),
        ("second", "IІ уровня"),
        ("third", "IІІ уровня"),
        ("empty", "Пустышка"),
    ]

    sort = models.CharField(choices=HELMET_TYPES, default="rock", max_length=100, verbose_name="Тип артефакта")
    ballistic = models.IntegerField(default=0, verbose_name="Балистическая защита")
    burst = models.IntegerField(default=0, verbose_name="Защита от разрыва")
    kick = models.IntegerField(default=0, verbose_name="Гашение удара")
    explosion = models.IntegerField(default=0, verbose_name="Защита от взрыва")
    thermal = models.IntegerField(default=0, verbose_name="Термозащита")
    chemical = models.IntegerField(default=0, verbose_name="Химащита")
    electrical = models.IntegerField(default=0, verbose_name="Электрозащита")
    radioactive = models.IntegerField(default=0, verbose_name="Радиозащита")
    psi = models.IntegerField(default=0, verbose_name="Пси защита")
    weight = models.IntegerField(default=0, verbose_name="Переносимый вес")
    healing = models.IntegerField(default=0, verbose_name="Лечение")
    satiety = models.IntegerField(default=0, verbose_name="Насыщение")
    energy = models.IntegerField(default=0, verbose_name="Восстановление энергии")

    class Meta:
        verbose_name = "Артефакт"
        verbose_name_plural = "Артефакты"


class QuestItem(Item, Mass):
    FEATURE_TYPES = [
        ("none", ""),
    ]
    eq_type = "quest_item"

    tradable = models.BooleanField(default=False, verbose_name="Продаваемость", help_text="Возможность "
                                                                                          "продать/выкинуть предмет")
    feature1 = models.CharField(choices=FEATURE_TYPES, verbose_name="Характеристика №1", max_length=100)
    feature_num1 = models.IntegerField(default=0, verbose_name="Значение характеристики №1")
    feature2 = models.CharField(choices=FEATURE_TYPES, verbose_name="Характеристика №2", max_length=100)
    feature_num2 = models.IntegerField(default=0, verbose_name="Значение характеристики №2")
    feature3 = models.CharField(choices=FEATURE_TYPES, verbose_name="Характеристика №3", max_length=100)
    feature_num3 = models.IntegerField(default=0, verbose_name="Значение характеристики №3")
    feature4 = models.CharField(choices=FEATURE_TYPES, verbose_name="Характеристика №4", max_length=100)
    feature_num4 = models.IntegerField(default=0, verbose_name="Значение характеристики №4")
    feature5 = models.CharField(choices=FEATURE_TYPES, verbose_name="Характеристика №5", max_length=100)
    feature_num5 = models.IntegerField(default=0, verbose_name="Значение характеристики №5")

    class Meta:
        verbose_name = "Квестовый предмет"
        verbose_name_plural = "Квестовые предметы"


class EquipItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя предмета")
    limit = models.Q(app_label='equipment', model='ammo') | models.Q(app_label='equipment', model='addon') \
            | models.Q(app_label='equipment', model='weapon') | models.Q(app_label='equipment', model='outfit') \
            | models.Q(app_label='equipment', model='helmet') | models.Q(app_label='equipment', model='backpack') \
            | models.Q(app_label='equipment', model='device') | models.Q(app_label='equipment', model='foodandmedicine') \
            | models.Q(app_label='equipment', model='misc') | models.Q(app_label='equipment', model='artifact') \
            | models.Q(app_label='equipment', model='questitem')

    content_type = models.ForeignKey(ContentType, limit_choices_to=limit, on_delete=models.DO_NOTHING,
                                     verbose_name="Тип предмета")
    object_id = models.PositiveIntegerField(verbose_name="ID предмета")
    content_object = GenericForeignKey('content_type', 'object_id')

    quantity = models.PositiveSmallIntegerField(default=1, verbose_name="Колличество предметов")
    condition = models.PositiveSmallIntegerField(default=100, verbose_name="Состояние предмета")
    cost = models.PositiveIntegerField(default=0, verbose_name="Стоимость предмета")


class Equip(models.Model):
    name = models.CharField(max_length=500, verbose_name="Имя, id профиля")

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
    belt5 = models.ForeignKey(EquipItem, related_name="device4", default=None, verbose_name="Пояс::Устройство №4",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt6 = models.ForeignKey(EquipItem, related_name="device5", default=None, verbose_name="Пояс::Устройство №5",
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
    container6 = models.ForeignKey(EquipItem, related_name="art6", default=None, verbose_name="Артефакт №6",
                                   on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Снаряжение"
        verbose_name_plural = "Снаряжения"
