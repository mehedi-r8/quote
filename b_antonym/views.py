from rest_framework.views import APIView
from rest_framework.response import Response
from Quote.authentication import ApiKeyAuthentication
from .models import Antonym
from .serializers import AntonymSerializer


class AntonymListView(APIView):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        antonyms = Antonym.objects.all()
        group_size = 30
        groups = []
        group_count = (antonyms.count() // group_size) + (1 if antonyms.count() % group_size else 0)

        for i in range(group_count):
            group_antonyms = antonyms[i * group_size:(i + 1) * group_size]
            group_serializer = AntonymSerializer(group_antonyms, many=True)
            groups.append(
                {'group': [{'word': item['word'], 'antonym': item['antonym']} for item in group_serializer.data]})

        data = {'groups': groups}
        return Response(data)
