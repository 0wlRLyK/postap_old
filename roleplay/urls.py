from django.urls import path

from . import views

app_name = "rp"
urlpatterns = [
    path("user/items/{}/".format("<slug:pk>"), views.UserItemView.as_view(), name="user_items"),
    path("user/items_repair/", views.UserItemsRepairView.as_view(), name="user_items_repair"),

    path("trader/{}/".format("<slug:pk>"), views.TraderView.as_view(), name="trader"),
    path("trade/sell/", views.TradeSell.as_view(), name="sell"),
    path("trade/buy/", views.TradeBuy.as_view(), name="buy"),

    path("minigames/{}/".format("<slug:pk>"), views.MiniGameView.as_view(), name="minigame"),
    path("minigame/roll_dice/", views.RollTheDice.as_view(), name="roll_the_dice"),

    path("mechanic/{}/".format("<slug:pk>"), views.MechanicView.as_view(), name="mechanic"),
    path("repair/", views.RepairView.as_view(), name="repair")
]
