from dataclasses import dataclass

@dataclass
class Run:
    run_number:int
    led_serial:int
    date:str
    photo_path:str
    spot_path:str

    def create_metadata(self) -> None:
        pass

    def create_folders(self) -> None:
        pass