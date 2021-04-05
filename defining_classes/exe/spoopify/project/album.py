class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.songs = [song for song in args]
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."

        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        return f"Song is already in the album."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."
        for song in self.songs:
            if song == song_name:
                self.songs.remove(song)
            return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        album_details = f"Album {self.name}\n"
        for s in self.songs:
            album_details += f"== {s.name} - {s.length}\n"
        return album_details

