from authAppComInd.models.tipo_producto import Tipo_producto
from authAppComInd.models.producto      import Producto
from rest_framework                     import serializers

class Tipo_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Tipo_producto
        fields = ['nombre_tipo_prod']
    
    def to_representation(self, obj):
        tipo_producto   = Tipo_producto.objects.get(id=obj.id)
        producto        = Producto.objects.get(id=obj.producto)
        return {
            'id'               : tipo_producto.id,
            'nombre_tipo_prod' : nombre_tipo_prod.nombre_tipo_prod,
            'producto'         : {
                  'id'             : producto.id,
                  'nombreProducto' : producto.nombreComunidad,
                  'caracteristica' : producto.caracteristica,
                  'cantidad'       : producto.cantidad

            }
        }