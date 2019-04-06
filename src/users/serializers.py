import os
from rest_framework.serializers import ImageField
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers as rs

from posts.serializers import SimpleLikeSerializer


# noinspection PyAbstractClass
class CustomRegisterSerializer(RegisterSerializer):  # Inherit RegisterSerializer
    profile_pic = ImageField(required=False)

    def custom_signup(self, request, user):
        if self.validated_data.get('profile_pic', ''):
            user.profile_pic = self.validated_data.get('profile_pic', '')
        user.save(update_fields=['profile_pic', ])


# noinspection PyAbstractClass
class CustomUserDetailsSerializer(UserDetailsSerializer):
    user_likes = SimpleLikeSerializer(many=True, read_only=True)

    profile_pic_thumb = rs.SerializerMethodField(read_only=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = ('id', 'username', 'profile_pic', 'profile_pic_thumb', 'user_likes',)
        read_only_fields = ('id', 'username', 'profile_pic', 'profile_pic_thumb', 'user_likes',)

    @staticmethod
    def get_profile_pic_thumb(user):
        if user.profile_pic:
            name, ext = os.path.splitext(user.profile_pic.url)
            return name + '.thumbnail' + ext
        return None
