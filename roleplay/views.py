import json
import random

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import generic
from equipment import models as equip
from users import models as users_m

from . import models


class LocationView(generic.DetailView):
    model = models.Location
    template_name = "rp/location.html"
    context_object_name = "location"


class AreaView(generic.DetailView):
    model = models.Area
    template_name = "rp/area.html"
    context_object_name = "area"


class SubLocationView(generic.DetailView):
    model = models.SubLocation
    template_name = "rp/sublocation.html"
    context_object_name = "subloc"


class TraderView(generic.DetailView):
    model = models.Trader
    template_name = "rp/trade.html"
    context_object_name = "trader"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['user'] = users_m.SiteUser.objects.get(id=self.request.user.id)
        context['user_equip'] = equip.EquipItem.objects.filter(profile=self.request.user.id)
        context['weapons'] = equip.Weapon.objects.filter(id__in=self.object.items.all())
        context['addons'] = equip.Addon.objects.filter(id__in=self.object.items.all())
        context['ammo'] = equip.Ammo.objects.filter(id__in=self.object.items.all())
        context['outfits'] = equip.Outfit.objects.filter(id__in=self.object.items.all())
        context['helmets'] = equip.Helmet.objects.filter(id__in=self.object.items.all())
        context['backpacks'] = equip.Backpack.objects.filter(id__in=self.object.items.all())
        context['devices'] = equip.Device.objects.filter(id__in=self.object.items.all())
        context['food_and_medicine'] = equip.FoodAndMedicine.objects.filter(id__in=self.object.items.all())
        context['artifacts'] = equip.Artifact.objects.filter(id__in=self.object.items.all())
        context['quest_items'] = equip.QuestItem.objects.filter(id__in=self.object.items.all())
        context['misc'] = equip.Misc.objects.filter(id__in=self.object.items.all())
        return context


class TradeSell(generic.View):
    def post(self, request, *args, **kwargs):
        user = users_m.SiteUser.objects.get(id=request.user.id)
        trader = models.Trader.objects.get(id=int(json.loads([el for el in request.POST.values()][1])))

        slots = [[user.slot1.id if user.slot1 else -1, "slot1"],
                 [user.slot2.id if user.slot2 else -1, "slot2"],
                 [user.slot3.id if user.slot3 else -1, "slot3"],
                 [user.armor.id if user.armor else -1, "armor"],
                 [user.helmet.id if user.helmet else -1, "helmet"],
                 [user.backpack.id if user.backpack else -1, "backpack"],
                 [user.device1.id if user.device1 else -1, "device1"],
                 [user.device2.id if user.device2 else -1, "device2"],
                 [user.device3.id if user.device3 else -1, "device3"],
                 [user.container1.id if user.container1 else -1, "container1"],
                 [user.container2.id if user.container2 else -1, "container2"],
                 [user.container3.id if user.container3 else -1, "container3"],
                 [user.container4.id if user.container4 else -1, "container4"],
                 [user.container5.id if user.container5 else -1, "container5"],
                 [user.belt1.id if user.belt1 else -1, "belt1"],
                 [user.belt2.id if user.belt2 else -1, "belt2"],
                 [user.belt3.id if user.belt3 else -1, "belt3"],
                 [user.belt4.id if user.belt4 else -1, "belt4"]]

        objects_set = sorted(json.loads([el for el in request.POST.values()][0]), key=lambda k: k['id'])
        items = equip.EquipItem.objects.filter(id__in=[i["id"] for i in objects_set], profile=request.user.id)
        cost, del_objects_set, update_objects_set = 0, [], []
        if items.exists():
            for count, item in enumerate(items.iterator()):
                obj_dict = objects_set[count]
                cost += (round(item.c_obj.cost * obj_dict["quantity"] * trader.coef_buy))
                print(item.id, cost, item.cost, obj_dict["quantity"], obj_dict)
                if cost > trader.money and not trader.inf:
                    return HttpResponse(
                        json.dumps({
                            "result": False,
                            "cause": "Недостаточно средств для совершения операции"
                            # "result": str(items.aggregate(Sum('cost'))),
                        }),
                        content_type="application/json", )

                if obj_dict["quantity"] == item.quantity:
                    del_objects_set.append(item.id)
                    for slot in slots:

                        if item.id == slot[0]:
                            print(slot[0], slot[1])
                            field = getattr(user, slot[1])
                            print(setattr(user, slot[1], None))
                            setattr(user, slot[1], None)
                            user.save()
                else:
                    setattr(item, "quantity", item.quantity - obj_dict["quantity"])
                    update_objects_set.append(item)

        items = items.exclude(id__in=del_objects_set)
        equip.EquipItem.objects.bulk_update(update_objects_set, ['quantity'])
        equip.EquipItem.objects.filter(id__in=del_objects_set).delete()
        setattr(user, "money", user.money + cost)
        user.save()
        return HttpResponse(
            json.dumps({
                "result": True,
                "moneyUser": user.money,
                "moneyTrader": trader.money if not trader.inf else "infinity",
                # "result": str(items.aggregate(Sum('cost'))),
            }),
            content_type="application/json", )


class TradeBuy(generic.View):
    def post(self, request, *args, **kwargs):
        user = users_m.SiteUser.objects.get(id=request.user.id)
        trader = models.Trader.objects.get(id=int(json.loads([el for el in request.POST.values()][1])))

        objects_set = sorted(json.loads([el for el in request.POST.values()][0]), key=lambda k: k['id'])
        user_items = user.get_equip_items
        trader_items = equip.Item.objects.filter(id__in=sorted([i["id"] for i in objects_set]))
        cost, create_objects_set, update_objects_set, update_objects_ids = 0, [], [], []
        if trader_items.exists():
            for count, item in enumerate(trader_items.iterator()):
                obj_dict = objects_set[count]
                cost += ((item.cost * trader.coef_trade) * obj_dict["quantity"])
                if cost > user.money:
                    return HttpResponse(
                        json.dumps({
                            "result": False,
                            "cause": "Недостаточно средств для совершения операции"
                        }),
                        content_type="application/json", )

                if user_items.filter(object_id=item.id, condition=100).exists():
                    user_item = user_items.filter(object_id=item.id, condition=100)[0]
                    setattr(user_item, "quantity", user_item.quantity + obj_dict["quantity"])
                    setattr(user_item, "mass", user_item.c_obj.mass * (user_item.quantity + obj_dict["quantity"]))
                    update_objects_set.append(user_item)
                    user_item.save()


                else:
                    # setattr(item, "quantity", item.quantity - obj_dict["quantity"])
                    create_objects_set.append(
                        {"id": item.id, "name": item.name, "type": obj_dict["type"], "quantity": obj_dict["quantity"],
                         "mass": item.mass * obj_dict["quantity"]})

        trader_items = trader_items.exclude(id__in=update_objects_ids)
        equip.EquipItem.objects.bulk_update(update_objects_set, ['quantity'])
        objects_for_create = []
        for el in create_objects_set:
            objects_for_create.append(equip.EquipItem(
                name=el["name"], content_type=ContentType.objects.get(model=el["type"]),
                object_id=el["id"], profile=user, quantity=el["quantity"],
                condition=100, cost=0, mass=el["mass"]
            ))
        equip.EquipItem.objects.bulk_create(objects_for_create)
        # setattr(user, "money", user.money - cost)
        user.save()
        return HttpResponse(
            json.dumps({
                "result": True,
                "moneyUser": user.money,
                "moneyTrader": trader.money if not trader.inf else "infinity",
                # "result": str(create_objects_set),
            }),
            content_type="application/json", )


class UserItemView(generic.DetailView):
    template_name = "rp/user_items.html"
    model = models.Trader
    context_object_name = "trader"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = users_m.SiteUser.objects.get(id=self.request.user.id)
        trader = models.Trader.objects.get()
        context['user_equip'] = user.get_equip_items
        return context


class MiniGameView(generic.DetailView):
    model = models.NPCMinigame
    template_name = "rp/minigame.html"
    context_object_name = "npc_player"


class RollTheDice(generic.View):

    def post(self, request, *args, **kwargs):
        npc = models.NPCMinigame.objects.get(id=int(json.loads([el for el in request.POST.values()][0])))
        user = users_m.SiteUser.objects.get(id=self.request.user.id)
        if user.money < 1000:
            return HttpResponse(
                json.dumps({
                    "result": False,
                    "cause": "У пользователя недостаточно денег"
                }),
                content_type="application/json",
            )
        if npc.money < 1000:
            setattr(npc, "money", npc.money + 5000)
        user_nums = [random.randint(1, 6), random.randint(1, 6)]
        npc_nums = [random.randint(1, 6), random.randint(1, 6)]
        winner = None
        if sum(user_nums) > sum(npc_nums):
            setattr(user, "money", user.money + 1000)
            setattr(npc, "money", npc.money - 1000)
            winner = "user"
        elif sum(user_nums) == sum(npc_nums):
            pass
            winner = "none"
        else:
            setattr(user, "money", user.money + 1000)
            setattr(npc, "money", npc.money + 1000)
            winner = "npc"
        user.save()
        npc.save()

        return HttpResponse(
            json.dumps({
                "result": True,
                "user_dice1": user_nums[0],
                "user_dice2": user_nums[1],
                "npc_dice1": npc_nums[0],
                "npc_dice2": npc_nums[1],
                "winner": winner,
                "user_money": user.money,
                "npc_money": npc.money
                # "result": str(create_objects_set),
            }),
            content_type="application/json",
        )


class MechanicView(generic.DetailView):
    model = models.Mechanic
    template_name = "rp/repair.html"
    context_object_name = "mechanic"


class RepairView(generic.View):
    def post(self, request, *args, **kwargs):
        json_data = [el for el in request.POST.values()]
        item = equip.EquipItem.objects.get(id=int(json_data[0]))
        mode = json_data[1]
        mechanic = models.Mechanic.objects.get(id=int(json_data[2]))
        user = users_m.SiteUser.objects.get(id=self.request.user.id)
        repair_cost = (item.c_obj.cost * (100 - item.condition) / 100) * mechanic.coef_repair
        print(user.money, repair_cost)
        if item.condition >= 100:
            return HttpResponse(
                json.dumps({
                    "result": False,
                    "cause": "Предмет уже находится в исправном состоянии. Ремонт не требуется!"
                })
            )
        if repair_cost > user.money:
            return HttpResponse(
                json.dumps({
                    "result": False,
                    "cause": "Недостаточно денег"
                })
            )
        if mode == "one":
            if equip.EquipItem.objects.filter(object_id=item.object_id, condition=100).exists():
                repeared_item = equip.EquipItem.objects.get(object_id=item.object_id, condition=100)
                setattr(repeared_item, "quantity", repeared_item.quantity + 1)
                repeared_item.save()
            else:
                new_item = equip.EquipItem(content_type=item.content_type,
                                           object_id=item.object_id, profile=user, quantity=1,
                                           condition=100, cost=0)
                new_item.save()
            if item.quantity <= 1:
                item.delete()
            else:
                setattr(item, "quantity", item.quantity - 1)
                item.save()
        elif mode == "all":
            setattr(item, "condition", 100)
            item.save()
        else:
            return HttpResponse(
                json.dumps({
                    "result": False,
                    "cause": "Error"
                })
            )
        setattr(user, "money", user.money - repair_cost)
        setattr(mechanic, "money", mechanic.money + repair_cost)
        user.save()
        mechanic.save()
        return JsonResponse({
            "result": True,
            "user_money": user.money,
            "mechanic_money": mechanic.money,
        })


class UserItemsRepairView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, "rp/user_items_repair.html", {'user_equip': self.request.user.get_equip_items})
        # return HttpResponse(users_m.SiteUser.objects.get(id=self.request.user.id))
