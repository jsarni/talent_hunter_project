import spotipy
import pandas   as pd
from datetime import datetime
from spotipy.oauth2 import SpotifyClientCredentials


EDGE_TARGET_FOLDER = "/home/talenthunter/spotify"
PLAYLISTS_FILE = "spotify_playlist.csv"
NEW_RELEASES_CSV = "new_release.csv"
ARTIST_FILE="artist"

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
    release.to_csv(f"{EDGE_TARGET_FOLDER}/{NEW_RELEASES_CSV}",index=False)


def get_artist_information(id_artist):
    results               = sp.artist(id_artist)
    artist_name           =results['name']
    artist_total_followers=results['followers']['total']
    artist_popularity     =results['popularity']
    artist_uri            =results['uri']
    return [artist_name,artist_total_followers,artist_popularity,artist_uri]
def GetTopsTodayTracks():
    playlist='37i9dQZF1DXcBWIGoYBM5M'
    tracks_list=[]
    tracks=sp.playlist_tracks(playlist)['items']
    #get information about tracks
    for i,track in enumerate(tracks):
        print("****-Track number :",i,"-***")
        print("\n")
        track_added_date        =track['added_at']
        track_artist_id         =track['track']['album']['artists'][0]['id']
        track_artist_information=get_artist_information(track_artist_id)
        track_album_id          =track['track']['album']['id']
        track_album_name        =track['track']['album']['name']
        track_album_date        =track['track']['album']['release_date']
        track_album_total_track =track['track']['album']['total_tracks']
        track_disc_number        =track['track']['disc_number']
        track_duration           =track['track']['duration_ms']
        track_externel_ids       =track['track']['external_ids']['isrc']
        track_href               =track['track']['href']
        track_id                 =track['track']['id']
        track_name               =track['track']['name']
        track_popularity         =track['track']['popularity']
        track_number             =track['track']['track_number']
        track_type               =track['track']['type']
        track_uri                =track['track']['uri']
        #------------------------------------------------------------------------
        tracks_list.append([track_added_date,
                               track_album_id,track_album_name,
                               track_album_date,track_album_total_track,
                               track_disc_number,track_id,track_duration,
                               track_externel_ids,track_href
                               ,track_name, track_popularity,track_number ,
                                track_type ,track_uri,
                                track_artist_id,track_artist_information[0],track_artist_information[1],track_artist_information[2],track_artist_information[3]] )

    TodayHits=pd.DataFrame(tracks_list,columns=[
                                                "track_added_date",
                                                "track_album_id",
                                                "track_album_name",
                                                "track_album_date",
                                                "track_album_total_track",
                                                "track_disc_number",
                                                "track_id",
                                                "track_duration",
                                                "track_externel_ids",
                                                "track_href",
                                                "track_name",
                                                "track_popularity",
                                                "track_number" ,
                                                "track_type" ,
                                                "track_uri",
                                                "track_artist_id",
                                                "track_artist_name",
                                                "track_artist_nbr_follow",
                                                "track_artist_popularity",
                                                "track_artist_uri"])
    TodayHits['collect_date'] = todayString()
    TodayHits.to_csv(f"{EDGE_TARGET_FOLDER}/TopHits_{todayString()}.csv",index=False)



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
    spotify_playlist.to_csv(f"{EDGE_TARGET_FOLDER}/{PLAYLISTS_FILE}",index=False)





if __name__ == '__main__':
    new_releases_spotify()
    All_playlist()
    GetTopsTodayTracks()


