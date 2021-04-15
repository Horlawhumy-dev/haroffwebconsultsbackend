from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    firstname = serializers.CharField(
        max_length=100,
        style={'placeholder': 'FirstName', 'autofocus': True}
    )

    message = serializers.CharField(
        style={'input_type': 'textarea', 'placeholder': 'Comment'}
    )


    # class LoginSerializer(serializers.Serializer):
    #     email = serializers.EmailField(
    #     max_length=100,
    #     style={'placeholder': 'Email', 'autofocus': True}
    # )
    # password = serializers.CharField(
    #     max_length=100,
    #     style={'input_type': 'password', 'placeholder': 'Password'}
    # )