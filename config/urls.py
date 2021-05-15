from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from andr_omeda.andr_update.views.update.views import TelegramView
from django.views.decorators.csrf import csrf_exempt
from andr_omeda.andr_bot.views import Bots
from andr_omeda.andr_moderation.views.moderated_object.views import *
from andr_omeda.andr_moderation.views.moderation_categories.views import *
from andr_omeda.andr_moderation.views.erpuser.views import *

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("andr_omeda.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()


bot_patterns = [
    path('', Bots.as_view(), name='bots'),
]

bots_patterns = [
    path("<user_erp_name>/<token>/", include(bot_patterns)),
]

moderation_moderated_object_patterns = [
    path('', ModeratedObjectItem.as_view(), name='moderated-object'),
    path('approve/', ApproveModeratedObject.as_view(), name='approve-moderated-object'),
    path('reject/', RejectModeratedObject.as_view(), name='reject-moderated-object'),
    path('logs/', ModeratedObjectLogs.as_view(), name='moderated-object-logs'),
]

moderation_moderated_objects_patterns = [
    path('<int:moderated_object_id>/', include(moderation_moderated_object_patterns)),
    #path('global/', GlobalModeratedObjects.as_view(), name='global-moderated-objects'),
]

moderation_patterns = [
    path('<str:erp_name>/moderated-objects/', include(moderation_moderated_objects_patterns), name='moderation-moderated-objects'),
    path('categories/', ModerationCategories.as_view(), name='moderation-categories'),
    #path('is-not-suspended-check/', IsNotSuspendedCheck.as_view(), name='is-not-suspended-check'),
    #path('andruser/penalties/', AndruserModerationPenalties.as_view(), name='user-moderation-penalties'),
    path('<str:erp_name>/pending-moderated-objects-bots/', ChatPendingModeratedObjectsBots.as_view(),
         name='chat-pending-moderated-objects-bots'),
]

erp_patterns = [
    path("bots/", include(bots_patterns)),
    path("moderation/", include(moderation_patterns)),
]

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    path("erp/", include(erp_patterns)),
    path("webhooks/update/<token>/", csrf_exempt(TelegramView.as_view())),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
