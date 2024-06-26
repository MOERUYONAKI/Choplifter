import pygame as py

class Vehicule():
    def get_parts(self):
        pass
    
    def get_collid(self):
        pass
    
    def get_left(self):
        pass
    
    def get_top(self):
        pass

    def set_center(self, center : tuple):
        pass
    
    def move_left(self, px : int):
        pass

    def move_top(self, px : int):
        pass

class Music():
    def __init__(self, path : str, volume : float = 0.25):
        self.song = py.mixer.music
        self.volume = volume
        self.playing = False

        self.song.load(path)

    def is_playing(self):
        return self.playing

    def play(self):
        self.playing = True
        self.song.play(loops = -1)

    def pause(self):
        self.playing = False
        self.song.pause()

    def unpause(self):
        self.playing = True
        self.song.unpause()

    def stop(self):
        self.playing = False
        self.song.stop()

    def set_volume(self, volume : float):
        self.song.set_volume(volume if volume >= 0 else 0.25)

def add_asset(image_path : str): # Add an asset by an image - return an image and the image's rect
    try:
        image = py.image.load(image_path).convert_alpha()
        rect = image.get_rect()

        return image, rect
    
    except:
        print("Erreur de génération")
        return False, False