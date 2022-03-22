from ast import Is
from django.shortcuts import HttpResponse, get_object_or_404
from .models import Rank
from .serializer import RankSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .funcs import isgame, isRank, rankOrder
import json
# Create your views here.


@api_view(['GET'])
def main(request):
    urls = {
        "/api/leaderboard/<str:game>/": "to get all the ranks for a leaderboard ",
        "/api/rank/": "to add or update a rank for a user",
        "/api/rank/<str:rankHolder>/": " to get the rank for a user ",
    }
    return Response(urls)


@api_view(['GET'])
def getLeaderboardByGame(request, game):
    if not isgame(game):
        return Response(data=json.dumps({"message": "game not found"}), status=404)

    ranks = Rank.objects.filter(game=game)\
        .exclude(rank="NA")\
        .order_by('rankOrdered')

    ranks = RankSerializer(ranks, many=True)
    return Response(ranks.data)


@api_view(['GET'])
def getRankForUser(request, rankHolder):
    ranks = Rank.objects.filter(rankHolder=rankHolder)
    ranks = RankSerializer(ranks, many=True)
    return Response(ranks.data)


@api_view(['POST'])
def AddorUpdateRankForUser(request):
    if isgame(request.data['game']) and isRank(request.data['rank']):
        rank = Rank.objects.filter(
            rankHolder=request.data['rankHolder'], game=request.data['game'])

        if rank:
            rank.update(rank=request.data['rank'], rankOrdered=rankOrder(
                request.data['rank']))
            return HttpResponse("rank updated success")

        else:
            Rank.objects.create(
                rankHolder=request.data['rankHolder'],
                game=request.data['game'],
                rank=request.data['rank'],
                rankOrdered=rankOrder(request.data['rank'])
            )
            return HttpResponse("rank added success")

    return Response("fail")
