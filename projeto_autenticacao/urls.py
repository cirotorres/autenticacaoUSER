
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('appusuarios.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('appusuarios.urls'))

]
