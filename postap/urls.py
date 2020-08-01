"""postap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
                  path('ajax_select/', include('ajax_select.urls')),
                  path('admin/', admin.site.urls),
                  path('', include('entries.urls')),
                  path('users/', include('users.urls')),
                  path('polls/', include('voting.urls')),
                  path(r'comments/', include('django_comments_xtd.urls')),
                  path('tinymce/', include('tinymce.urls')),
                  path('likes/', include('favorites.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  re_path(r'^uploads/', include('ckeditor_uploader.urls')),
                  # !| TEMPORARY APPS AND PATHS |!
                  #    ! DELETE BEFORE DEPLOY !

              ] + static(settings.STATIC_URL, docuent_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
