from collect.conf import AppConfig
import spotipy
import pandas   as pd
from datetime import datetime
from spotipy.oauth2 import SpotifyClientCredentials

#définition des variables utilisateur:
ID_CLIENT="93af51f0124c475e882dde858a060f5a"
CODE_CLIENT="739c3c4b28ff4dd1886e3ec83ecb82b5"
#Connection:
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=ID_CLIENT,
                                                           client_secret=CODE_CLIENT))

def todayString():
    return datetime.now().replace(microsecond=0).strftime("%Y-%m-%d")

def new_releases_spotify():
    response = sp.new_releases()
    response_list = []
    while response:
        albums = response['albums']
        for item in (albums['items']):
            # print(item['external_urls'])
            for pays in item['available_markets']:
                # Release:
                release_id = item['id']
                release_name = item['name']
                release_date = item['release_date']
                release_total_tracks = item['total_tracks']
                release_type = item['type']
                release_external_url = item['external_urls']['spotify']
                # album
                album_type = item['album_type']
                # Artist Data:
                artist_id = item['artists'][0]['id']
                response_list.append(
                    [release_id, release_name, release_date, release_total_tracks, release_type, release_external_url,
                     pays, album_type, artist_id])

        if albums['next']:
            response = sp.next(albums)
        else:
            response = None
    release = pd.DataFrame(response_list, columns=['release_id', 'release_name', 'release_date', 'release_total_tracks',
                                                   'release_type', 'release_external_url', 'release_available_market',
                                                   'album_type', 'artist_id'])
    release['collect_date'] = todayString()
    release.to_csv(""+AppConfig.EDGE_TARGET_FOLDER+"/new_release.csv")

def All_playlist():
    user = 'spotify'
    playlists = sp.user_playlists(user)
    playlist_items=[]
    while playlists:

        for i,playlist in enumerate(playlists['items']):
            #print(playlist.keys())
            playlist_collaborative =playlist['collaborative']
            playlist_description   =playlist['description']
            playlist_external_urls =playlist['external_urls']['spotify']
            playlist_id            =playlist['id']
            playlist_name          =playlist['name']
            playlist_public        =playlist['public']
            playlist_snapshot_id   =playlist['snapshot_id']
            playlist_tracks_url    =playlist['tracks']['href']
            playlist_tracks_count  =playlist['tracks']['total']
            playlist_type          =playlist['type']
            playlist_items.append([   playlist_collaborative
                                     ,playlist_description
                                     ,playlist_external_urls
                                     ,playlist_id
                                     ,playlist_name
                                     ,playlist_public
                                     ,playlist_snapshot_id
                                     ,playlist_tracks_url
                                     ,playlist_tracks_count
                                     ,playlist_type])
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    spotify_playlist = pd.DataFrame(playlist_items,columns=['playlist_collaborative','playlist_description','playlist_external_urls',
                                                              'playlist_id','playlist_name','playlist_public','playlist_snapshot_id',
                                                              'playlist_tracks_url','playlist_tracks_count','playlist_type'])
    spotify_playlist['collect_date']=todayString()
    spotify_playlist.to_csv("" + AppConfig.EDGE_TARGET_FOLDER+"/spotify_playlist.csv")
