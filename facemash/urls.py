from django.conf.urls import include, url
from facemash.views import ratings_calculator, play, ratings_page, create_game, add_facemash

urlpatterns = [
    url(r'^create_game/$', create_game, name='create_game'),
    url(r'^play/$', play, name="play"),
    url(r'^calcultor/(?P<winner_id>\d+)-(?P<loser_id>\d+)/$', ratings_calculator, name="calculator"),
    url(r'^add_facemash/(?P<game_id>\d+)/$', add_facemash, name='add_facemash'),
    url(r'^ratings/$', ratings_page, name="ratings"),
]
