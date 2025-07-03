from datetime import datetime
import numpy as np, sys, argparse
from time import sleep


# Load classes from the utils folder
from utils import Run, Photo, Camera, gphoto2, LED

def argv_manager():

    parser = argparse.ArgumentParser(description="LED-FEB Power Up")

    parser.add_argument('--parameters', 
                        type=str,   
                        required=True, 
                        help='Path to yaml file containing run\'s parameters.'
                        )

    parser.add_argument('--calibration', 
                    type=str,   
                    required=True, 
                    help='Path to yaml file containing calibration parameters.'
                    )

    parser.add_argument('--plot-spots',
                    action='store_true', 
                    default=False,       
                    help='Plot spots and save images in the data_dir/spots folder.')

    parser.add_argument('--debug',
                    action='store_true', 
                    default=False,       
                    help='Create and store gphoto2\'s debug files in data_dir/debug')

    return parser.parse_args()


def main():

    argvs = argv_manager()

    run = Run(params_path = argvs.parameters)
    run.save_run_info()
    run.print_summary()

    # ledfeb = LED()

    if argvs.debug:
        print(f"Debugging log files will be saved in: {run.data_path}/debug")

    print(run.channels)

    # gphoto = gphoto2()
    # port = gphoto.find_port()
    # print('Port:', port)

    # sony = Camera(port=port)

    # print(run.iso, run.shutterspeed)
    
    # ret = sony.change_iso(run.iso)
    # sony.print_return(ret)

    # print(sony.get_iso(), sony.get_shutterspeed())
    # sys.exit()

    # print("prefix: ", run.prefix)

    for i, distance in enumerate(run.distances):
        for j, CH in enumerate(run.channels):
            
            # ledfeb.turn_on(channel = CH)
            
            for k in range(0,run.n_photos):
        
                debug_log_dir = ""
                if argvs.debug == True:
                    debug_log_dir = f'{run.data_path}/debug'

                # process_output, photo_paths = sony.capture_photo(photo_dir = run.photo_dir, 
                #                                                  prefix = run.prefix, 
                #                                                  debug_dir = debug_log_dir
                #                                                 )

                # print(photo_paths)

                photo_paths = ('/home/lkoerich/Dropbox/Work/LED_FEB/camera_control/data/photos/Run-9998_2025-06-24-T161125.ARW', '/home/lkoerich/Dropbox/Work/LED_FEB/camera_control/data/photos/Run-9998_2025-06-24-T161126.JPG')

                photo = Photo(run = run, 
                            photo_path = photo_paths,
                            iso = run.iso, 
                            shutterspeed = run.shutterspeed, 
                            calibration_path = argvs.calibration,
                            plot = argvs.plot_spots,
                            data_dir = run.data_path
                            )

                photo.fit()
                photo.save_info()
                            
                print('Waiting 5 seconds between shots.')
                sleep(5)
                print("\n")

                # ledfeb.disable('all')
        

if __name__ == '__main__':
    main()