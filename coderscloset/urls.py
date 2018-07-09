
from django.contrib import admin
from django.urls import path,include
from accounts.views import get_home
from accounts import urls as accounts_urls
from products import urls as products_urls
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name="get_home"),
    path('accounts/', include(accounts_urls)),
    path('products/', include(products_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
