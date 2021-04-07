from django.urls import path

from . import views

app_name = "rp"
urlpatterns = [
    path("user/items/<slug:pk>/", views.UserItemView.as_view(), name="user_items"),
    path("user/items_repair/", views.UserItemsRepairView.as_view(), name="user_items_repair"),

    path("location/<slug:pk>/", views.LocationView.as_view(), name="location"),
    path("area/<slug:pk>/", views.AreaView.as_view(), name="area"),
    path("subloc/<slug:pk>/", views.SubLocationView.as_view(), name="sublocation"),

    path("campfire/<slug:pk>/", views.CampFireView.as_view(), name="campfire"),

    path("trader/<slug:pk>/", views.TraderView.as_view(), name="trader"),
    path("trade/sell/", views.TradeSell.as_view(), name="sell"),
    path("trade/buy/", views.TradeBuy.as_view(), name="buy"),

    path("minigames/<slug:pk>/", views.MiniGameView.as_view(), name="minigame"),
    path("minigame/roll_dice/", views.RollTheDice.as_view(), name="roll_the_dice"),

    path("mechanic/<slug:pk>/", views.MechanicView.as_view(), name="mechanic"),
    path("repair/", views.RepairView.as_view(), name="repair")
]
