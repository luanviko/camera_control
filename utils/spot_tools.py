from dataclasses import dataclass
import rawpy

@dataclass()
class Photo:

    photo_path:str
    run_number:int
    led_serial:int
    channel:str    | None = None
    distance:float | None = None
    voltage:float  | None = None

