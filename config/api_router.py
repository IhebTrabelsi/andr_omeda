from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from andr_omeda.users.api.views import UserViewSet
from andr_omeda.andr_update.views.update.views import UpdateViewSet
from django.views.decorators.csrf import csrf_exempt

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("update/", csrf_exempt(UpdateViewSet))


app_name = "api"
urlpatterns = router.urls
