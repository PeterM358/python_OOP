from project.album import Album
from project.band import Band


class Song:

    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f"{self.name} - {self.length}"


# album = Album("The Sound of Perseverance")
# song = Song("Scavenger of Human Sorrow", 6.56, True)
# album.publish()
# print(album.add_song(song))

# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# # print(album.remove_song("Around the World"))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())