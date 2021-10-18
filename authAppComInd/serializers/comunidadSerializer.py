from authAppComInd.models.comunidad import Comunidad
from authAppComInd.models.region    import Region
from rest_framework                 import serializers
 

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Comunidad
        fields = ['id','nombreComunidad','region']

    def create(self, validated_data):
        regionData = validated_data.pop('region')
        comunidadInstance = Comunidad.object.create(**validated_data)
        Region.objects.create(comunidad = comunidadInstance, **regionData)
        return comunidadInstance

    def to_representation(self,obj):
        comunidad = Comunidad.objects.get(id=obj.id)
        region    = Region.objects.get(id=obj.region)
        return{
            'id'              : comunidad.id,
            'nombreComunidad' : comunidad.nombreComunidad,
            'region'  : {
                'id'           : region.id,
                'nombreRegion' : region.nombreRegion
            }
        }

    
    