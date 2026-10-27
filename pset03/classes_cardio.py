# ----------------------------------------------------------------------
# This is the file classes_cardio.py
#
# The intent is to give you practice with classes.
#
# Follow the instructions below, adding code where directed.
#
# There are no stubs in this file, so you will need to infer exactly
# how to write each class from the descriptions and the unit tests at
# the bottom of the file. To run the tests, you can use the command
#
#     pytest classes_cardio.py
#
# Remove this comment, and other comments serving as instructions,
# prior to submission. You can, and should, add your own comments,
# but please remove all the comments that are here now.
# ----------------------------------------------------------------------

import math

class Rectangle: 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"


class Circle: 
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return ((math.pi) * (self.radius ** 2))

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"

# Write a class called Song, with attributes title, artist, and
# duration. The duration should be in seconds. The class should
# have a __str__ method that returns a string representation
# according the unit tests below, and a method called play that
# prints a message inferrable from the unit tests below.

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration}s)"

    def play(self):
        print("Playing {self.title} by {self.artist} ({self.duration})s\n")

# Write a class called Playlist, which contains a list of Song
# objects. The class should have methods to add a song, play all
# songs, and a __str__ method that returns a string representation
# of the playlist, with each song represented as "title by artist
# (duration)s" and separated by a pipe character (|). If the playlist
# is empty, the __str__ method should return "Playlist is empty."


def test_rectangle():
    rect = Rectangle(3, 4)
    assert rect.area() == 12
    assert rect.perimeter() == 14
    assert str(rect) == "Rectangle(3 x 4)"


def test_circle():
    circle = Circle(5)
    assert circle.area() == 25*math.pi
    assert circle.circumference() == 10*math.pi
    assert str(circle) == "Circle(radius=5)"


def test_song(capfd):
    song = Song("Night Shift", "Lucy Dacus", 391)
    assert str(song) == "Night Shift by Lucy Dacus (391s)"
    song.play()
    captured_output = capfd.readouterr()
    assert captured_output.out == (
        "Playing Night Shift by Lucy Dacus (391s)\n"
    )


def test_playlist(capfd):
    playlist = Playlist()
    song1 = Song("Night Shift", "Lucy Dacus", 391)
    song2 = Song("I Was Neon", "Julia Jacklin", 243)
    song3 = Song("Forgiveness", "Alice Glass", 191)
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    assert str(playlist) == (
        "Night Shift by Lucy Dacus (391s)|"
        "I Was Neon by Julia Jacklin (243s)|"
        "Forgiveness by Alice Glass (191s)"
    )
    playlist.play_all()
    captured_output = capfd.readouterr()
    assert captured_output.out == (
        "Playing Night Shift by Lucy Dacus (391s)\n"
        "Playing I Was Neon by Julia Jacklin (243s)\n"
        "Playing Forgiveness by Alice Glass (191s)\n"
    )

test_rectangle()
test_circle()
test_song(1)
#test_playlist()

print("All tests passed!")