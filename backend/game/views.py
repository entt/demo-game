import json
from django.core.serializers import serialize
from django.shortcuts import HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View

from .forms import PlayerForm
from .models import Player


@method_decorator(csrf_exempt, name='dispatch')
class PlayerList(View):
    def get(self, request):
        players = Player.objects.all()
        return HttpResponse(serialize("json", players),
                            content_type="application/json")


    def post(self, request):
        form = PlayerForm(json.loads(request.body.decode('utf-8')))
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)


class PlayerDetails(View):
    def get(self, request, player_id):
        player = get_object_or_404(Player, pk=player_id)
        return HttpResponse(serialize("json", [player,]),
                            content_type="application/json")


    @csrf_exempt
    def put(self, request):
        pass
