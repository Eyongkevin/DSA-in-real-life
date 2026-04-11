import os
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from mutagen.mp3 import MP3

from dsa import Playlist


class MusicPlayer:
    def __init__(self, playlist: Playlist):
        self.playlist = playlist
        self.sound = None

    def play_current(self):
        # Stop any currently playing sound
        self.stop()

        song = self.playlist.current

        if song is None:
            print('Unable to play current song')
            return

        if not os.path.exists(song.file_path):
            print(f"File not found: {song.file_path}")
            return
        
        self.sound = SoundLoader.load(song.file_path)
        self.play()

    def play(self):
        if self.sound:
            self.sound.play()

    def stop(self):
        if self.sound:
            self.sound.stop()

    def next(self):
        self.playlist.next_song()
        self.play_current()

    def previous(self):
        self.playlist.prev_song()
        self.play_current()

# UI
class PlayerUI(MDBoxLayout):
    def __init__(self, player: MusicPlayer, **kwargs):
        super().__init__(orientation = 'vertical', padding=20, spacing=20, **kwargs)

        self.player = player
        self.playing_state: bool = False

        # Card
        self.card = MDCard(
            orientation = 'vertical',
            padding=20,
            spacing=10,
            radius=[20],
            elevation=8,
            size_hint=(1, 0.6)
        )

        self.song_title = MDLabel(
            text = "No song playing",
            halign = 'center',
            theme_text_color = 'Secondary'
        )

        self.duration = MDLabel(
            text = "00:00",
            halign = 'center',
            theme_text_color = 'Hint'
        )

        self.next_song = MDLabel(
            text = "",
            halign = 'center',
            theme_text_color = 'Hint'
        )

        self.prev_song = MDLabel(
            text = "",
            halign = 'center',
            theme_text_color = 'Hint'
        )

        self.card.add_widget(self.song_title)
        self.card.add_widget(self.duration)
        self.card.add_widget(self.next_song)
        self.card.add_widget(self.prev_song)

        self.add_widget(self.card)

        # Controls
        controls = MDBoxLayout(
            orientation = 'horizontal',
            spacing=20,
            size_hint=(1, 0.3),
            pos_hint = {'center_x': 0.5}
        )

        btn_prev = MDIconButton(
            icon = 'skip-previous',
            font_size = '48sp',
            on_release = self.prev_song_action,
        )
        btn_play = MDIconButton(
            icon="play-circle",
            font_size="60sp",
            on_release=self.play_song_action,
        )
        btn_stop = MDIconButton(
            icon="stop-circle",
            font_size="40sp",
            on_release=self.stop_song_action,
        )
        btn_next = MDIconButton(
            icon="skip-next",
            font_size="40sp",
            on_release=self.next_song_action,
        )

        controls.add_widget(btn_prev)
        controls.add_widget(btn_play)
        controls.add_widget(btn_stop)
        controls.add_widget(btn_next)

        self.add_widget(controls)
        self.update_ui()

    def update_ui(self):
        song = self.player.playlist.current

        playing_mode = "Playing" if self.playing_state else "Stopped"

        self.song_title.text = f"{playing_mode}: {song.title}" if song else "No song playing"
        self.duration.text = f"Duration: {song.duration}" if song else "00:00"

    def play_song_action(self, _):
        self.player.play_current()
        self.playing_state = True
        self.update_ui()

    def stop_song_action(self, _):
        self.player.stop()
        self.playing_state = False
        self.update_ui()

    def next_song_action(self, _):
        self.player.next()
        self.playing_state = True
        self.update_ui()

    def prev_song_action(self, _):
        self.player.previous()
        self.playing_state = True
        self.update_ui()


class MusicApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"

        playlist = Playlist()

        song1 = MP3("songs/song1.mp3")
        song2 = MP3("songs/song2.mp3")
        song3 = MP3("songs/song3.mp3")
        song4 = MP3("songs/song4.mp3")

        playlist.add_song("Song 1", song1.filename, format_duration(song1.info.length))
        playlist.add_song("Song 2", song2.filename, format_duration(song2.info.length))
        playlist.add_song("Song 3", song3.filename, format_duration(song3.info.length))
        playlist.add_song("Song 4", song4.filename, format_duration(song4.info.length))

        player = MusicPlayer(playlist)
        return PlayerUI(player)

def format_duration(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}:{seconds:02d}"

if __name__ == "__main__":
    MusicApp().run()