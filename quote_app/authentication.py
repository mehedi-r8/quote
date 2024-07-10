from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("API Key:", request.headers.get('API-Key'))
        api_key = request.headers.get('API-Key')
        if not api_key or api_key != 'your':
            raise AuthenticationFailed('Invalid or missing API Key')
        return (None, None)