from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class MyJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        """
        Custom authenticate method to support token from both Authorization header and cookies.
        """
        try:
            header = self.get_header(request)
            if header is None:
                raw_token = request.COOKIES.get(settings.AUTH_COOKIE)
            else:
                raw_token = self.get_raw_token(header)

            if raw_token is None:
                return None

            validated_token = self.get_validated_token(raw_token)
            # Return the user and the validated token
            return self.get_user(validated_token), validated_token

        except AuthenticationFailed as e:
            # Specifically catch authentication failures (invalid token, expired token, etc.)
            raise AuthenticationFailed(
                'Authentication failed: {}'.format(str(e)))

        except Exception as e:
            # General catch-all for unexpected errors (for better debugging)
            raise AuthenticationFailed(
                'An error occurred during authentication: {}'.format(str(e)))
