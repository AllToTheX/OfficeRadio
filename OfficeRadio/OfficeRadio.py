'''
Created on Aug 18, 2016

@author: aveldman
'''

from pprint import pprint
import sys

import spotipy
import spotipy.util as util

class OfficeRadio(object):
    
    def __init__(self,username):
        scope = 'playlist-modify-public'
        self.username=username
        self.token = util.prompt_for_user_token(username, scope)
        self.sp = spotipy.Spotify(auth=self.token)


    def add_song(self, playlist_id, track_ids):
    
        self.sp.trace = False
        self.sp.user_playlist_add_tracks(self.username, playlist_id, track_ids)
        print("Track Added")

        
    def get_playlist(self, playlist_name):
    
        playlists = self.sp.user_playlists(self.username)
        playlist = [playlist for playlist in playlists['items'] if playlist['name'] == playlist_name][0]
        playlist = self.sp.user_playlist(self.username, playlist['id'], fields="tracks,next")
        return playlist


    def get_song_id(self, song):
    
        results = self.sp.search(q=song, limit=20)
        for i, song in enumerate(results['tracks']['items']):
            print("[%d] : %s - %s" %(i,song['artists'][0]['name'],song['name']))
        choice = int(raw_input("Select track: "))
        return(results['tracks']['items'][choice]['id'])
    
    def search_song(self, song):
        return self.sp.search(q=song, limit=20)['tracks']['items']
        

def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()
    
    office = OfficeRadio(username)
    
    song = raw_input("Search: ")
    playlist_name = 'OfficeRadio'
    
    song = office.search_song(song)
    pl = office.get_playlist(playlist_name)
    track_add_timestamp = pl['tracks']['items'][0]['added_at']
    print track_add_timestamp
#     pprint(pl['tracks']['items'][0])
    exit()
    
    playlist = office.get_playlist( playlist_name )    
    song_ids = list()
    song_ids.append( office.get_song_id(song) )
    office.add_song( playlist['id'], song_ids )
    

if __name__ == '__main__':
    main()