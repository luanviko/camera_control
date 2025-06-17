__version__ = '0.1.1'

__doc__ = 'Classes to control camera, change capture settings, find spots and test fitting conversion.'

from .metadata import Run
from .camera_controls import Camera, gphoto2
from .spot_tools import Photo, Spot

__all__ = [
    'Run', 
    'Camera',
    'gphoto2',
    'Photo',
    'Spot'
]

print(f"Initializing utils packages v{__version__}")