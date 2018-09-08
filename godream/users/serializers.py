from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.exceptions import (
    ParseError
)


class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        assert self.required_user_type is not None, (
            "'%s' should either include a `required_user_type` attribute."
            % self.__class__.__name__
        )

        email = attrs.get('email')
        password = attrs.get('password')

        if not email and not password:
            msg = _('Must include "email" and "password".')
            raise ParseError(msg)

        user = self.get_user(email, password)
        if not user:
            msg = _("Oops, the email or password entered don't match. Please try again")
            raise ParseError(msg)

        self.validate_user(user)

        attrs['user'] = user
        return attrs

    def get_user(self, email, password):
        return authenticate(email=email, password=password)
