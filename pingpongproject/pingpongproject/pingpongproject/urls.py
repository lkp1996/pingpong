from django.conf.urls import include, url
from django.contrib import admin
from pingpong import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'pingpongproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_games/', views.AddGameCreateView.as_view(), name='add_games'),
    url(
        r'^add_players/', views.AddPlayerCreateView.as_view(),
        name='add_players'
        ),
    url(
        r'^scoreboard/', views.ScoreboardListView.as_view(),
        name='scoreboard'
        ),
    url(r'^ranking/', views.RankingView.as_view(), name='ranking'),
]
