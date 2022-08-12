from rest_framework.views import APIView, Response, status
from rest_framework.permissions import AllowAny

from .serializers import DateOfBirthSerializer
from .helpers import calculate_dob


class AgeView(APIView):
    permission_classes = [AllowAny]
    serializer_class = DateOfBirthSerializer
    throttle_scope = 'howold'

    def get(self, request):
        dob = request.query_params.get('dob')
        dob_serializer = DateOfBirthSerializer(data={'dob': dob})
        dob_serializer.is_valid(raise_exception=True)
        age = calculate_dob(dob_serializer.validated_data.get('dob'))
        return Response({
            'age': age
        }, status=status.HTTP_200_OK)
