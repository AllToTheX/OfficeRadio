'''
Created on Aug 18, 2016

@author: aveldman
'''

import web
from OfficeRadio import OfficeRadio

radio = OfficeRadio('11127572347')

urls = (
        '/(.*)','index')

class index:
    def GET(self,index):
        song_list=None
        song_repr=None
        i = web.input(song=None,choice=None)
        render = web.template.render('templates/')
        
        if i.song is not None:
            song_list = radio.search_song(i.song)
            
            if i.choice is not None:
                playlist = radio.get_playlist('OfficeRadio')
                song = song_list[int(i.choice)]['id']
                song_repr = "%s - %s" %(song_list[int(i.choice)]['artists'][0]['name'], song_list[int(i.choice)]['name'])
                radio.add_song(playlist['id'], (song,))
                
        
        return render.index(i.song,song_list,song_repr)

def main():
    
    app = web.application(urls, globals())
    app.run()

if __name__ == '__main__':
    main()