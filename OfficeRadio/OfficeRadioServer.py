'''
Created on Aug 18, 2016

@author: aveldman
'''

import web
from web import form
from OfficeRadio import OfficeRadio

radio = OfficeRadio('11127572347')
render = web.template.render('templates/')

urls = (
        '/callback/(.*)', 'callback',
        '/(.*)', 'index'
        )

myform = form.Form(
                   form.Textbox('Search:'),
                   form.Button('Search',)
                   )

class index:
    def GET(self,index):
        song_list=None
        song_repr=None
        i = web.input(song=None,choice=None)
        
        if i.song is not None:
            song_list = radio.search_song(i.song)
            
            if i.choice is not None:
                playlist = radio.get_playlist('OfficeRadio')
                song = song_list[int(i.choice)]['id']
                song_repr = "%s - %s" %(song_list[int(i.choice)]['artists'][0]['name'], song_list[int(i.choice)]['name'])
                radio.add_song(playlist['id'], (song,))
        else:
            form = myform()
            return render.formtest(form)       
        
        return render.index(i.song,song_list,song_repr)
    
    def POST(self,url):
        form = myform() 
        if not form.validates(): 
            return form.render()
        else:
            song = form['Search:'].value
            song_list = radio.search_song(song)
            return render.index(song,song_list,None)

class callback(object):
    def GET(self,url):
        print url
        
        return(url)

def main():
    
    app = web.application(urls, globals())
    app.run()

if __name__ == '__main__':
    main()