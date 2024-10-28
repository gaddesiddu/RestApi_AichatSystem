from rest_framework import serializers
from .models import User, Chat
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','tokens']
        extra_kwargs={'password':{'write_only':True},'tokens':{'read_only':True}}  #write_only:True is it should not include in API response
        #extra_kwargs is an option used in meta class to specify additional keyword agrument for fields
        

        
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields=['user','message','response','timestamp']
        