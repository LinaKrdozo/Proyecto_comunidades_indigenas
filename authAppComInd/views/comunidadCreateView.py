from rest_framework                                     import status,views, generics
from rest_framework.response                            import Response
from rest_framework_simplejwt.serializers               import TokenObtainPairSerializer
from authAppComInd.serializers.comunidadSerializer      import ComunidadSerializer
from authAppComInd.models.comunidad                     import Comunidad
from rest_framework                                     import serializers

class ComunidadCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ComunidadSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
    
        return Response("comunidad creada", status=status.HTTP_201_CREATED)


class ComunidadListView(generics.ListAPIView):
    serializer_class = ComunidadSerializer
    def get_queryset(self):
        queryset = Comunidad.objects.all()
        return queryset
