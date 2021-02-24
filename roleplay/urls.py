from django.urls import path

from . import views

app_name = "rp"
urlpatterns = [
    path("user/items/{}/".format("<slug:pk>"), views.UserItemView.as_view(), name="user_items"),
    path("trader/{}/".format("<slug:pk>"), views.TraderView.as_view(), name="trader"),
    path("trade/sell/", views.TradeSell.as_view(), name="sell"),
    path("trade/buy/", views.TradeBuy.as_view(), name="buy"),
]
