
from django.contrib import admin
from django.urls import path
from team2app.views import show_registration_form, show_login_form, show_product
from team2.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', show_registration_form, name = 'register'),
    path('login/', show_login_form, name = 'login'),
    path('', show_product, name = 'product')
]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)