from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from andr_omeda.andr_moderation.models import ModerationCategory
from andr_omeda.andr_moderation.views.moderation_categories.serializers import  \
    ModerationCategorySerializer


class ModerationCategories(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        moderation_categories = ModerationCategory.objects.all().order_by('order')
        serializer = ModerationCategorySerializer(moderation_categories, many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
