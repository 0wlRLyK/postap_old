# Create your models here.
from ckeditor.fields import RichTextField
from django.db import models
from users.models import Group


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    icon = models.ImageField(verbose_name="Иконка")
    description = RichTextField(verbose_name="Описание")

    cost = models.PositiveIntegerField(default=0, verbose_name="Стоимость")

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Mass(models.Model):
    mass = models.PositiveIntegerField(default=0, verbose_name="Масса")

    class Meta:
        abstract = True


class Ammo(Item, Mass):
    quantity = models.PositiveIntegerField(default=0, verbose_name="Колличество патронов в пачке")

    class Meta:
        verbose_name = "Пачка патронов"
        verbose_name_plural = "Патроны"


class Addon(Item, Mass):
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
    one_handed = models.BooleanField(default=False, verbose_name="Является оружие одноручным",
                                     help_text="Например нож, пистолет")

    addon1 = models.ManyToManyField(Addon, related_name="addon1", verbose_name="1 слот аддонов: Варианты",
                                    help_text="Возможные аддоны для первого слота аддонов")
    addon1open = models.BooleanField(default=True, verbose_name="1 слот аддонов: Доступность",
                                     help_text="Отрыт ли слот изначально")
    addon2 = models.ManyToManyField(Addon, related_name="addon2", verbose_name="2 слот аддонов: Варианты",
                                    help_text="Возможные аддоны для первого слота аддонов")
    addon2open = models.BooleanField(default=True, verbose_name="2 слот аддонов: Доступность",
                                     help_text="Отрыт ли слот изначально")
    addon3 = models.ManyToManyField(Addon, related_name="addon3", verbose_name="3 слот аддонов: Варианты",
                                    help_text="Возможные аддоны для первого слота аддонов")
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
    helmet = models.BooleanField(default=False, verbose_name="Шлем", help_text="Присуствует ли всторенный шлем")
    unique = models.BooleanField(default=False, verbose_name="Уникальный костюм")

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
    unique = models.BooleanField(default=False, verbose_name="Уникальный шлем")

    class Meta:
        verbose_name = "Шлем"
        verbose_name_plural = "Шлемы"


class Backpack(Item, Mass):
    carry_weight = models.IntegerField(default=0, verbose_name="Максимальный переносимый вес")

    class Meta:
        verbose_name = "Рюкзак"
        verbose_name_plural = "Рюкзаки"


class Device(Item, Mass):
    ACTIONS_FOR_USE = [
        ('use', 'Использовать'),
        ('play', 'Играть'),
    ]

    slot_setting = models.BooleanField(verbose_name="Возможность установить в слот устройств")

    actions = models.CharField(max_length=10, choices=ACTIONS_FOR_USE, verbose_name="Действия для использования")

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"


class FoodAndMedical(Item, Mass):
    ACTIONS_FOR_USE = [
        ('use', 'Использовать'),
        ('eat', 'Съесть'),
        ('drink', 'Выпить'),
    ]

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
    name = models.CharField(max_length=200, verbose_name="Название")
    icon = models.ImageField(verbose_name="Иконка")
    description = RichTextField(verbose_name="Описание")

    mass = models.IntegerField(default=0, verbose_name="Масса")

    class Meta:
        verbose_name = "Разное"
        verbose_name_plural = "Разное"


class Artifact(Item, Mass):
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


class Equip(models.Model):
    name = models.CharField(max_length=500, verbose_name="Имя, id профиля")

    slot1 = models.ForeignKey(Weapon, related_name="weapons1", default=None, verbose_name="Первый слот",
                              on_delete=models.CASCADE, null=True, blank=True)
    slot1_condition = models.PositiveSmallIntegerField(default=100, verbose_name="Состояние первого слота")
    slot1_ups = models.ManyToManyField(WeaponUpgrade, related_name="weapons_ups1", verbose_name="Улучшения слота №1")

    slot2 = models.ForeignKey(Weapon, related_name="weapons2", default=None, verbose_name="Второй слот",
                              on_delete=models.CASCADE, null=True, blank=True)
    slot2_condition = models.PositiveSmallIntegerField(default=100, verbose_name="Состояние второго слота")
    slot2_ups = models.ManyToManyField(WeaponUpgrade, related_name="weapons_ups2", verbose_name="Улучшения слота №2")

    slot3 = models.ForeignKey(Weapon, related_name="weapons3", default=None, verbose_name="Третий слот",
                              on_delete=models.CASCADE, null=True, blank=True)
    slot3_condition = models.PositiveSmallIntegerField(default=100, verbose_name="Состояние третьего слота")
    slot3_ups = models.ManyToManyField(WeaponUpgrade, related_name="weapons_ups3", verbose_name="Улучшения слота №3")

    armor = models.ForeignKey(Outfit, related_name="armor", default=None, verbose_name="Броня",
                              on_delete=models.CASCADE, null=True, blank=True)
    armor_condition = models.PositiveSmallIntegerField(default=100, verbose_name="Состояние брони")
    armor_ups = models.ManyToManyField(OutfitUpgrade, related_name="armor_ups", verbose_name="Улучшения брони")

    helmet = models.ForeignKey(Helmet, related_name="helmet", default=None, verbose_name="Шлем",
                               on_delete=models.CASCADE, null=True, blank=True)
    helmet_condition = models.PositiveSmallIntegerField(default=100, verbose_name="Состояние шлема")
    helmet_ups = models.ManyToManyField(HelmetUpgrade, related_name="helmet_ups1", verbose_name="Улучшения шлема")

    backpack = models.ForeignKey(Backpack, related_name="backpack", default=None, verbose_name="Устройство №1",
                                 on_delete=models.CASCADE, null=True, blank=True)

    device1 = models.ForeignKey(Device, related_name="device1", default=None, verbose_name="Устройство №1",
                                on_delete=models.CASCADE, null=True, blank=True)
    device2 = models.ForeignKey(Device, related_name="device2", default=None, verbose_name="Устройство №2",
                                on_delete=models.CASCADE, null=True, blank=True)
    device3 = models.ForeignKey(Device, related_name="device3", default=None, verbose_name="Устройство №3",
                                on_delete=models.CASCADE, null=True, blank=True)

    belt1 = models.ForeignKey(Ammo, related_name="ammo1", default=None, verbose_name="Боеприпасы №1",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt2 = models.ForeignKey(Ammo, related_name="ammo2", default=None, verbose_name="Боеприпасы №2",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt3 = models.ForeignKey(Ammo, related_name="ammo3", default=None, verbose_name="Боеприпасы №3",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt4 = models.ForeignKey(Ammo, related_name="ammo4", default=None, verbose_name="Боеприпасы №4",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt5 = models.ForeignKey(Device, related_name="device4", default=None, verbose_name="Пояс::Устройство №4",
                              on_delete=models.CASCADE, null=True, blank=True)
    belt6 = models.ForeignKey(Device, related_name="device5", default=None, verbose_name="Пояс::Устройство №5",
                              on_delete=models.CASCADE, null=True, blank=True)

    container1 = models.ForeignKey(Artifact, related_name="art1", default=None, verbose_name="Артефакт №1",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container2 = models.ForeignKey(Artifact, related_name="art2", default=None, verbose_name="Артефакт №2",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container3 = models.ForeignKey(Artifact, related_name="art3", default=None, verbose_name="Артефакт №3",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container4 = models.ForeignKey(Artifact, related_name="art4", default=None, verbose_name="Артефакт №4",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container5 = models.ForeignKey(Artifact, related_name="art5", default=None, verbose_name="Артефакт №5",
                                   on_delete=models.CASCADE, null=True, blank=True)
    container6 = models.ForeignKey(Artifact, related_name="art6", default=None, verbose_name="Артефакт №6",
                                   on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Снаряжение"
        verbose_name_plural = "Снаряжения"
