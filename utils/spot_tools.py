from dataclasses import dataclass, field
from typing import Dict, Any
from .metadata import Run


@dataclass()
class Photo:

    run:Run
    photo_path:str
    iso:str
    shutterspeed:str
    channel:str    | None = None
    distance:float | None = None
    voltage:float  | None = None
    photo_info:Dict[str, Any]    = field(init=False)
    photo_summary:Dict[str, Any] = field(init=False)

    def __post_init__(self):

        self.photo_info = {
            'run_number'  : self.run.run_number,
            'led_serial'  : self.run.led_serial,
            'date'        : self.run.date,
            'photo_path'  : self.photo_path,
            'channel'     : self.channel,
            'distance'    : self.distance,
            'voltage'     : self.voltage,
            'iso'          : self.iso,
            'shutterspeed' : self.shutterspeed
        }

        self.photo_summary = {
            'photo_path'   : self.photo_path,
            'channel'      : self.channel,
            'distance'     : self.distance,
            'voltage'      : self.voltage,
            'iso'          : self.iso,
            'shutterspeed' : self.shutterspeed
        }

