from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle


class SearchWordsView(APIView):
    throttle_classes = (UserRateThrottle,)

    def get(self, request):
        word_to_search = request.GET.get('words')
        print('word_to_search = {}'.format(word_to_search))
        return Response({'yes!':1})

