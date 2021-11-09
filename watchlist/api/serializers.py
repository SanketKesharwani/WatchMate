from rest_framework import serializers
from watchlist.models import WatchList,StreamPlatform

#MODEL SERIALIZER--------------------------------------------------------------------------------

class WatchListSerializer(serializers.ModelSerializer):
    name_len = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"
    
    def get_name_len(self,object):
        return len(object.title)
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"
#------------------------------------------------------------------END----------------------------

# #VALIDATORS--------------------------------------------------------------------------------------
# def name_length(value):
#      if len(value) < 2:
#         raise serializers.ValidationError("Name too Short")
# #------------------------------------------------------------------------------------------------

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     activate = serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.activate = validated_data.get('activate',instance.activate)
#         instance.save()
#         return instance

# # FIELD LEVEL VALIDATION----------------------------------------------------------------------------
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name too Short")
#         return value
# #--------------------------------------------------------------------------------------------------

# #----------------------------OBJECT LEVEL VALIDATION-----------------------------------------------
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description can not be same")
#         return data
# #------------------------------------------------------------------------------------------------


