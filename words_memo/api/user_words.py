import json
import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated

from words_memo.models import UserWord, Word

from word_scraper import word_scraper


class UserWordsView(APIView):
    throttle_classes = (UserRateThrottle,)
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user_vid = request.user.username
        word_id = request.GET.get('word_id')
        if not word_id:
            return Response('word_id invalid')

        if not Word.objects.filter(id=word_id).exists():
            return Response('word not found')

        UserWord.objcts.create(user_vid=user_vid,
                               circle_stage=1,
                               last_op_time=int(time.time()),
                               word_id=word_id)

        return Response({'success': True})


