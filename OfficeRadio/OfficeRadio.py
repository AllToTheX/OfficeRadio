'''
Created on Aug 18, 2016

@author: aveldman
'''

from pprint import pprint
import sys

import spotipy
import spotipy.util as util


def add_song(username,playlist_id,track_ids,sp):

    sp.trace = False
    sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print("Track Added")

        
def get_playlist_id(username,playlist_name,sp):

    playlists = sp.user_playlists(username)
    playlist = [playlist for playlist in playlists['items'] if playlist['name'] == playlist_name][0]
    playlist_id = playlist['id']
    return playlist_id


def get_song_id(song,sp):

    results = sp.search(q=song, limit=20)
    for i, song in enumerate(results['tracks']['items']):
        print("[%d] : %s - %s" %(i,song['artists'][0]['name'],song['name']))
    choice = int(raw_input("Select track: "))
    return(results['tracks']['items'][choice]['id'])


def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()
    
    song = raw_input("Search: ")
    playlist_name = 'OfficeRadio'
    
    
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username, scope)
    sp = spotipy.Spotify(auth=token)
    
    playlist_id = get_playlist_id(username,playlist_name,sp)
    song_ids = list()
    song_ids.append(get_song_id(song,sp))
    add_song(username, playlist_id, song_ids, sp)
    

if __name__ == '__main__':
    main()