# serializer is used to convert model fields into json format so that it can be rendered in API


from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'   # if we want all fields of model to be converted into json file
         # OR
        # fields = ('title', 'content', 'author',) # if u dont want all fields, Mention which fields from model you want in your json file