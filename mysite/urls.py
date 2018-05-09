from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'', include('eventos.urls')),
    url(r'', include('enquete.urls')),
=======
    url(r'^evento/', include('eventos.urls')),
>>>>>>> 2f2f61dff847480f167f9a4901b2143a76b1505c
]
