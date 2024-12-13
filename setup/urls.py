from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #indica ao django que tem que usar as inferências la do settings