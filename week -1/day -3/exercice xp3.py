class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
my_song = Song([
    "Don't say you’re sorry",
    "Cause I’m not even breaking",

])

my_song.sing_me_a_song()
