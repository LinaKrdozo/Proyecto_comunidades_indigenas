from authAppComInd.models.produc_comun                import Produc_comun
from rest_framework                                   import serializers
from authAppComInd.models.producto                    import Producto
from authAppComInd.models.comunidad                   import Comunidad

class Produc_comunSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Produc_comun
        fields = ['comunidad', 'producto']
    
    def to_representation(self,obj):
        comunidad    = Comunidad.objects.get(id=obj.comunidad)
        producto     = Producto.objects.get(id=obj.producto)
        produc_comun = Produc_comun.objects.get(id=obj.id)
        return{
            'id'         : Produc_comun.id,
            'comunidad'  : {
                'id'              : comunidad.id,
                'nombreComunidad' : comunidad.nombreComunidad
            },
            'producto'   : {
                 'id'             : producto.id,
                 'nombreProducto' : producto.nombreProducto,
                 'caracteristica' : producto.caracteristica,
                 'cantidad'       : producto.cantidad    
            }
        }