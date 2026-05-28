from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', TemplateView.as_view(template_name='base/sitemap.xml', content_type='application/xml')),
    path('robots.txt', TemplateView.as_view(template_name='base/robots.txt', content_type='text/plain')),
    path('', include('base.urls')),
]

# Serve media files (in production, consider using cloud storage for scale)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
