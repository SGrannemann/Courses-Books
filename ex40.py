#!/usr/bin/python3
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

first_song = ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]
second_song = ["They rally around tha familiy",
                        "With pockets full of shells"]
happy_bday = Song(first_song)

bulls_on_parade = Song(second_song)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
