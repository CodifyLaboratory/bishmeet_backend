from rest_framework.serializers import ModelSerializer

from .models import User


class UsersListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'age', 'gender', 'email', 'is_active'
        )


# class UsersCreateSerializer(ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = (
#             'id', 'first_name', 'last_name', 'age', 'gender', 'avatar'
#             'email', 'is_active', 'password'
#         )


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'age', 'gender', 'avatar', 'email',
        )

# class RegisterSerializer(ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'age', 'gender', 'email', 'password', 'password2')
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Пароли не совпадают"})
#
#         return attrs
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             last_name=validated_data['last_name'],
#             first_name=validated_data['first_name'],
#             age=validated_data['age'],
#             gender=validated_data['gender'],
#             email=validated_data['email'],
#         )
#
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
#
#     def email_user(self, subject, message, from_email=settings.DEFAULT_FROM_EMAIL, **kwargs):
#         send_mail(subject, message, from_email, [self.email], fail_silently=False, **kwargs)
