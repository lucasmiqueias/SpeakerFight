from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = (
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^', include('core.urls')),
    url(r'^', include('deck.urls')),
    url(r'^', include('jury.urls')),
    url(r'^api/', include('api.urls')),
)

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += (
            url(r'^__debug__/', include(debug_toolbar.urls)),
        )
