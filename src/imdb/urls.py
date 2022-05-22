from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from filme.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmes/', include('filme.urls', namespace='filmes')),
    path('', HomeView.as_view() ,name='home'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
