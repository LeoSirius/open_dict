from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from word_scraper import word_scraper


class SearchWordsView(APIView):
    throttle_classes = (UserRateThrottle,)

    def get(self, request):
        word_to_search = request.GET.get('words')
        print('word_to_search = {}'.format(word_to_search))
        try:
            res = word_scraper(word_to_search)
        except Exception as e:
            print("E = {}".format(e))
        return Response(res)

