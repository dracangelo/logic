from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/' , include('contact.urls' , namespace='contact')),
    path('about/', include('about.urls', namespace='about')),
    path('' , include('home.urls' , namespace='home')),
    path('services/', include('services.urls', namespace='services')),
    path('summernote/', include('django_summernote.urls')),    
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "LOGISTICEXPRESS ADMIN"
admin.site.site_title = "LOGISTICEXPRESS ADMIN"
admin.site.site_index_title = "Welcome to LOGISTICEXPRESS ADMIN"