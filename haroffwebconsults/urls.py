
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('about-blog/', include('about_blog.urls')),
    path('register/', include('register_mail.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
