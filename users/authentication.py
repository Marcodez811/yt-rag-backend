from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication

class MyJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            header = self.get_header(request)
            if header is None:
                # obtain token from cookies
                raw_token = request.COOKIES.get(settings.AUTH_COOKIE)
            else:
                # obtain token from authorization header
                raw_token = self.get_raw_token(header)

            if raw_token is None:
                return None
            
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), validated_token
        except:
            return None