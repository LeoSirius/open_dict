import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

from words_memo.models import Word

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

        if not res:
            return Response('no res')

        try:
            word = Word.objects.get(word=word_to_search, language='EN')
        except Word.DoesNotExist:
            word = Word.objects.create(word=word_to_search,
                                       language='EN',
                                       meaning=json.dumps(res))


        return Response({"word": word.to_dict()})

