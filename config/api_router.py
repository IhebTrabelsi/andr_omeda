from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from andr_omeda.users.api.views import UserViewSet
from andr_omeda.andr_update.views.update.views import UpdateViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("update/", UpdateViewSet, basename="update")


app_name = "api"
urlpatterns = router.urls
