from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.urls import include, path
from django.views.generic.base import RedirectView

from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/login/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('images/favicon.ico'),
        permanent=False)),
    path('robots.txt', lambda x: HttpResponse('User-Agent: *\nDisallow:', content_type='text/plain'),
         name='robots_file'),
    path('api/', include('users.urls')),
    path('api/', include('posts.urls')),
]

if settings.TOOLBAR:
    # noinspection PyPackageRequirements
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
