from dataclasses import dataclass, field, fields, asdict
from .spot_tools import Photo
import json 


@dataclass
class Run:

    run_number:int
    led_serial:int
    date:str
    data_path:str
    camera_port:str
    photos:list | None = None
    prefix:str  | None = None
    info_path:str = field(init=False)
    run_info:str  = field(init=False)
    

    def __post_init__(self) -> None:

        self.info_path = f'{self.data_path}/run_info/run_info_{self.run_number}.json'
        
        self.run_info = {
            'run_number'  : self.run_number,
            'led_serial'  : self.led_serial,
            'date'        : self.date,
            'data_path'   : self.data_path,
            'camera_port ': self.camera_port,
            'photos'      : self.photos
        }

        self.photo_dir = f"{self.data_path}/photos"

        if self.prefix == None:
            self.prefix = f'Run-{self.run_number}'

    def save_run_info(self) -> None:
        print('Run info saved at:', self.info_path)
        with open(self.info_path, 'w') as json_output:
            json.dump(self.run_info, json_output)

    def update_run_info(self, photo_info) -> None:
        
        with open(self.info_path, 'r') as json_input:
            loaded_run_info = json.load(json_input)

        loaded_run_info['photos'].append(photo_info)
        with open(self.info_path, 'w') as json_output:
            json.dump(loaded_run_info, json_output)
            
        
