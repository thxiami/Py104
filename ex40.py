class Song(object):
    
    def __init__(self, title, lyrics):
        self.lyrics = lyrics
        self.title = title
        
    def sing_me_a_song(self):
        print "-"*20
        print "Title:", self.title
        for i in self.lyrics:
            print i
            
happy_bday = Song("Happy birthday",
            ["Happy birthday to you",
            "I don't want to get sued",
            "So I'll stop right there"])

bulls_on_parade = Song("bulls_on_parade",
                        ["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()