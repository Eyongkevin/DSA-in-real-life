class SongNode:
    def __init__(self, title: str, file_path: str, duration: str = "--:--"):
        self.title: str = title
        self.file_path: str = file_path
        self.duration: str = duration
        self.next: SongNode | None = None
        self.prev: SongNode | None = None


class Playlist:
    """TODO: Implement data structures and algorithms for the music player application

    Algirithm should support the following operations:
    - Add a song to the playlist
    - Get current song
    - Skip to the next song
    - Go back to the previous song
    """

    def __init__(self):
        self.head: SongNode | None = None
        self.current: SongNode | None = None

    def add_song(self, title: str, file_path: str, duration: str = "--:--"):
        new_song = SongNode(title, file_path, duration)

        if not self.head:
            self.head = new_song
            self.head.next = self.head
            self.head.prev = self.head
            self.current = self.head
        else:
            tail = self.head.prev

            tail.next = new_song
            new_song.prev = tail

            new_song.next = self.head
            self.head.prev = new_song

    def next_song(self):
        if self.current:
            self.current = self.current.next

    def prev_song(self):
        if self.current:
            self.current = self.current.prev
