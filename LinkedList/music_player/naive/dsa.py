class Song:
    def __init__(self, title: str, file_path: str, duration: str):
        self.title = title
        self.file_path = file_path
        self.duration = duration

class Playlist:
    """TODO: Implement data structures and algorithms for the music player application

    Algirithm should support the following operations:
    - Add a song to the playlist
    - Get current song
    - Skip to the next song
    - Go back to the previous song
    """
    def __init__(self):
        self.current = None
        self.song_list: list[Song] = []
        self.current_index: int = 0

    def add_song(self, title: str, file_path: str, duration: str):
        song = Song(title, file_path, duration)
        self.song_list.append(song)
        if self.current is None:
            self.current = song

    def next_song(self):
        self.current_index = (self.current_index + 1) % len(self.song_list)
        self.current = self.song_list[self.current_index]

    def prev_song(self):
        self.current_index = (self.current_index - 1) % len(self.song_list)
        self.current = self.song_list[self.current_index]

