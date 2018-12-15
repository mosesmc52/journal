from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.signin,  name='signin'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^signup/$',views.signup),
    url(r'^forgot/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/', views.forgot_change, name='forgot_change'),
    url(r'^forgot/$',views.forgot, name='forgot'),
    url(r'^compose/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/', views.compose_entry, name='compose_token'),
    url(r'^compose/$',views.compose_entry, name='compose'),
    url(r'^done/',views.entry_submitted, name='submitted'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
