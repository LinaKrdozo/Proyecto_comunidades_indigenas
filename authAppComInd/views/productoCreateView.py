from rest_framework                               import status,views
from rest_framework                               import Response
from rest_framework_simplejwt                     import TokenObtainPairSerializer
from authAppComInd.serializers.productoSerializer import productoSerializer

class ProductoCreateView(views.APIViews):
    def post(self, request, *args, **kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()