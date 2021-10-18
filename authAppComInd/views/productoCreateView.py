from rest_framework                                     import status,views, generics
from rest_framework.response                            import Response
from rest_framework_simplejwt.serializers               import TokenObtainPairSerializer
from authAppComInd.serializers.productoSerializer       import ProductoSerializer
from authAppComInd.models.producto                      import Producto
from rest_framework                                     import serializers

class ProductoCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response("producto creado", status=status.HTTP_201_CREATED)


class ProductoListView(generics.ListAPIView):
    serializer_class = ProductoSerializer
    def get_queryset(self):
        queryset = Producto.objects.all()
        return queryset

