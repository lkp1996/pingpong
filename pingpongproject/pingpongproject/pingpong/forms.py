from django import forms
from pingpong.models import Game, Player
from django.forms.utils import ErrorList


class GameModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs['error_class'] = DivErrorList
        super(GameModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Game
        fields = ('player_one', 'player_two', 'score_one', 'score_two')

    def clean(self):
        player1 = self.cleaned_data.get('player_one')
        player2 = self.cleaned_data.get('player_two')
        score1 = self.cleaned_data.get('score_one')
        score2 = self.cleaned_data.get('score_two')
        all_players = player1 and player2
        scores = score1 is not None and score2 is not None
        if not (all_players and scores):
            raise forms.ValidationError("All fields are required")
        if player1 == player2:
            raise forms.ValidationError("Players need to be different")
        elif score1 == score2:
            raise forms.ValidationError("Scores need to be different")
        elif score1 < 0 or score2 < 0:
            raise forms.ValidationError(
                "Scores must be greater than or equal to 0")
        return self.cleaned_data


class PlayerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs['error_class'] = DivErrorList
        super(PlayerModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Player
        fields = ('name',)

    def clean(self):
        name = self.cleaned_data.get('name')
        players = Player.objects.all()
        for player in players:
            if name == player.name:
                raise forms.ValidationError("This player already exists")
            elif name is None:
                raise forms.ValidationError("This field is required")
        return self.cleaned_data


class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self.data:
            return ''
        for e in self:
            if e == "This field is required.":
                return ''
            if e == "Player with this Name already exists.":
                return ''
        return ''.join(['<div class="error">%s</div>' % e for e in self])
