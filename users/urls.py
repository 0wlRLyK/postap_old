from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy
from userena import settings as userena_settings
from userena import views as userena_views

from . import forms
from . import views as u_views

urlpatterns = [
    # Signup, signin and signout
    url(r"^signup/$", userena_views.signup, name="userena_signup"),
    url(r"^signin/$", userena_views.signin, name="userena_signin"),
    url(r"^signout/$", userena_views.SignoutView.as_view(), name="userena_signout"),
    # Reset password
    url(
        r"^password/reset/$",
        auth_views.PasswordResetView.as_view(
            template_name="userena/password_reset_form.html",
            email_template_name="userena/emails/password_reset_message.txt",
            extra_context={
                "without_usernames": userena_settings.USERENA_WITHOUT_USERNAMES
            },
            success_url=reverse_lazy("userena_password_reset_done"),
        ),
        name="userena_password_reset",
    ),
    url(
        r"^password/reset/done/$",
        auth_views.PasswordResetDoneView.as_view(
            template_name="userena/password_reset_done.html"
        ),
        name="userena_password_reset_done",
    ),
    url(
        r"^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="userena/password_reset_confirm_form.html",
            success_url=reverse_lazy("userena_password_reset_complete"),
        ),
        name="userena_password_reset_confirm",
    ),
    url(
        r"^password/reset/confirm/complete/$",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="userena/password_reset_complete.html"
        ),
        name="userena_password_reset_complete",
    ),
    # Signup
    url(
        r"^(?P<username>[\@\.\+\w-]+)/signup/complete/$",
        userena_views.direct_to_user_template,
        {
            "template_name": "userena/signup_complete.html",
            "extra_context": {
                "userena_activation_required": userena_settings.USERENA_ACTIVATION_REQUIRED,
                "userena_activation_days": userena_settings.USERENA_ACTIVATION_DAYS,
            },
        },
        name="userena_signup_complete",
    ),
    # Activate
    url(
        r"^activate/(?P<activation_key>\w+)/$",
        userena_views.activate,
        name="userena_activate",
    ),
    # Retry activation
    url(
        r"^activate/retry/(?P<activation_key>\w+)/$",
        userena_views.activate_retry,
        name="userena_activate_retry",
    ),
    # Activate pending
    url(
        r"^(?P<username>[\@\.\+\w-]+)/pending/$",
        userena_views.activate_pending,
        name="userena_activate_pending",
    ),
    # Change email and confirm it
    url(
        r"^(?P<username>[\@\.\+\w-]+)/email/$",
        userena_views.email_change,
        name="userena_email_change",
    ),
    url(
        r"^(?P<username>[\@\.\+\w-]+)/email/complete/$",
        userena_views.direct_to_user_template,
        {"template_name": "userena/email_change_complete.html"},
        name="userena_email_change_complete",
    ),
    url(
        r"^(?P<username>[\@\.\+\w-]+)/confirm-email/complete/$",
        userena_views.direct_to_user_template,
        {"template_name": "userena/email_confirm_complete.html"},
        name="userena_email_confirm_complete",
    ),
    url(
        r"^confirm-email/(?P<confirmation_key>\w+)/$",
        userena_views.email_confirm,
        name="userena_email_confirm",
    ),
    # Disabled account
    url(
        r"^(?P<username>[\@\.\+\w-]+)/disabled/$",
        userena_views.disabled_account,
        name="userena_disabled",
    ),
    # Change password
    url(
        r"^(?P<username>[\@\.\+\w-]+)/password/$",
        userena_views.password_change,
        name="userena_password_change",
    ),
    url(
        r"^(?P<username>[\@\.\+\w-]+)/password/complete/$",
        userena_views.direct_to_user_template,
        {"template_name": "userena/password_complete.html"},
        name="userena_password_change_complete",
    ),

    url(r"^(?P<username>[\@\.\+\w-]+)/edit/$", userena_views.profile_edit,
        {"edit_profile_form": forms.EditFormExtra}, name="userena_profile_edit"),
    # path("<slug:slug>/edit/", EditUserProfile.as_view(), name="userena_profile_edit", ),
    # View profiles
    url(
        r"^(?P<username>(?!(signout|signup|signin)/)[\@\.\+\w-]+)/$",
        u_views.profile_detail,
        name="userena_profile_detail",
    ),
    url(
        r"^page/(?P<page>[0-9]+)/$",
        userena_views.ProfileListView.as_view(),
        name="userena_profile_list_paginated",
    ),
    url(r"^$", userena_views.ProfileListView.as_view(), name="userena_profile_list"),

    path("transfer/money/", u_views.TransferMoney.as_view(), name="transfer_money"),
    path("equip/remove/{}/".format("<slug:pk>"), u_views.RemoveFromSlot.as_view(), name="eq_remove"),
    path("equip/set/slot1/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="slot1"), name="eq_set__slot1"),
    path("equip/set/slot2/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="slot2"), name="eq_set__slot2"),
    path("equip/set/slot3/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="slot3"), name="eq_set__slot3"),
    path("equip/set/armor/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="armor"), name="eq_set__armor"),
    path("equip/set/helmet/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="helmet"),
         name="eq_set__helmet"),
    path("equip/set/device1/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="device1"),
         name="eq_set__device1"),
    path("equip/set/device2/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="device2"),
         name="eq_set__device2"),
    path("equip/set/device3/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="device3"),
         name="eq_set__device3"),
    path("equip/set/backpack/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="backpack"),
         name="eq_set__backpack"),
    path("equip/set/container1/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="container1"),
         name="eq_set__container1"),
    path("equip/set/container2/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="container2"),
         name="eq_set__container2"),
    path("equip/set/container3/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="container3"),
         name="eq_set__container3"),
    path("equip/set/container4/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="container4"),
         name="eq_set__container4"),
    path("equip/set/container5/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="container5"),
         name="eq_set__container5"),
    path("equip/set/belt1/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="belt1"), name="eq_set__belt1"),
    path("equip/set/belt2/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="belt2"), name="eq_set__belt2"),
    path("equip/set/belt3/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="belt3"), name="eq_set__belt3"),
    path("equip/set/belt4/{}/".format("<slug:pk>"), u_views.SetInSlot.as_view(slot_name="belt4"), name="eq_set__belt4"),
]
