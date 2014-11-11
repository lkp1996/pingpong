from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, CreateView, ListView
from pingpong.forms import GameModelForm, PlayerModelForm
from pingpong.models import Game, Player
from django.db.models import Q
from operator import itemgetter
from datetime import datetime


class IndexView(ListView):
    model = Game
    template_name = 'pingpong/index.html'
    context_object_name = 'todays_games'

    def get_queryset(self):
        today = datetime.now()
        return Game.objects.filter(
            created__day=today.day, created__month=today.month,
            created__year=today.year
        ).order_by('-created')


class AddGameCreateView(SuccessMessageMixin, CreateView):
    form_class = GameModelForm
    template_name = 'pingpong/add_games.html'
    success_url = 'add_games'
    success_message = "Game added"


class AddPlayerCreateView(SuccessMessageMixin, CreateView):
    form_class = PlayerModelForm
    template_name = 'pingpong/add_players.html'
    success_url = 'add_players'
    success_message = "Player added"


class ScoreboardListView(ListView):
    model = Game
    template_name = 'pingpong/scoreboard.html'
    context_object_name = 'scoreboard'

    def get_queryset(self):
        query = self.request.REQUEST.get("q")
        if not query:
            return self.model.objects.all().order_by('-created')
        players = Player.objects.filter(name__icontains=query)
        games = self.model.objects.filter(
            Q(player_one__in=players) | Q(player_two__in=players)
        ).order_by('-created')
        return games


class RankingView(TemplateView):
    template_name = 'pingpong/ranking.html'

    def get_context_data(self, **kwargs):
        players = Player.objects.all()
        ranking = []
        context = super(RankingView, self).get_context_data(**kwargs)
        for plr in players:

            total = Game.objects.filter(
                Q(player_one=plr) | Q(player_two=plr)
            ).count()

            wins = Game.objects.filter(winner=plr).count()
            looses = total - wins
            points = wins - looses
            ranking.append({
                "Player": plr.name, "Wins": wins,
                "Looses": looses, "Total": total, "Points": points
                })
        context['ranking'] = sorted(
            ranking, reverse=True, key=itemgetter('Points'))
        return context
