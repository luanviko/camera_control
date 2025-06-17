from dataclasses import dataclass, field, fields, asdict
import json 


@dataclass
class Run:

    run_number:int
    led_serial:int
    date:str
    data_path:str
    camera_port:str
    prefix:str | None = None
    info_path:str = field(init=False)
    run_info:str = field(init=False)
    

    def __post_init__(self) -> None:

        self.info_path = f'{self.data_path}/run_info/run_info_{self.run_number}.json'
        
        self.run_info = {
            'run_number'  : self.run_number,
            'led_serial'  : self.led_serial,
            'date'        : self.date,
            'data_path'   : self.data_path,
            'camera_port ': self.camera_port
        }

        self.photo_dir = f"{self.data_path}/photos"

        if self.prefix == None:
            self.prefix = f'Run-{self.run_number}'

    def save_run_info(self) -> None:
        print('Run info saved at:', self.info_path)
        with open(self.info_path, 'w') as json_output:
            json.dump(self.run_info, json_output)
