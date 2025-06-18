# camera_control

To test the relative alignmnet and light-output quality of the collimated light from the LED-FEB system, we take photos of the collimated light projected to a grid with the Sony α7R IV camera. 

This app is a gphoto2 wrapper which allows you to change settings of and capture photos from the Sony α7R IV camera. 

It also allows you to try finding the spots and position of the spots to ensure data quality.

## Repository Structure

The __data\_acquisition.ipynb__ notebook is the basic data-acquisition and visualization of this project. The __tutorial.ipynb__ notebook, in turn, contains examples of how to connect to the camera, change ISO and shutter speed, and take photos.

Both notebooks call the classes and methods defined in the __./utils__ folder. While __camera\_controls.py__ has the basic Camera and GPhoto classes, for camera management and control, __metadata.py__ has classes to manage data-acquisition runs, and __spot\_tools.py__ contains the Photo class, to preprocess images and ensure maximal photo quality during acquisition. 

```text
.
├── utils
│   ├── __init__.py 
│   ├── camera_controls.py
│   ├── metadata.py
│   └── spot_tools.py
├── data_acquisition.ipynb
├── README.md
└── tutorial.ipynb
```


## Data Structure

When initializing a __Run__ object, you must provide __data\_dir__, a path to a directory that will contain three folders: photos, run_info, spots. You do not need to create a new folder for each run. 

```text
data_dir
├── photos
├── run_info
└── spots
```

## Starting a Camera Object

Use `GPhoto.auto_connect()` to automatically look for all the cameras find the Sony Sony α7R IV's __port\_number__.  

Now, initialize the Camera object using this port number. For example:

```python
sony = Camera(port=port_number)
```

## Taking a Photo



`Camera.capture_photo()`

## Changing ISO and Shutter Speed

### ISO Choices

To list all ISO options, please use `Camera.list_iso()` method. Below is a table with all the choices available for the Sony α7R IV camera.

|   Choice | ISO    |
|---------:|:-------|
|        0 | Auto   |
|        1 | 50     |
|        2 | 64     |
|        3 | 80     |
|        4 | 100    |
|        5 | 125    |
|        6 | 160    |
|        7 | 200    |
|        8 | 250    |
|        9 | 320    |
|       10 | 400    |
|       11 | 500    |
|       12 | 640    |
|       13 | 800    |
|       14 | 1000   |
|       15 | 1250   |
|       16 | 1600   |
|       17 | 2000   |
|       18 | 2500   |
|       19 | 3200   |
|       20 | 4000   |
|       21 | 5000   |
|       22 | 6400   |
|       23 | 8000   |
|       24 | 10000  |
|       25 | 12800  |
|       26 | 16000  |
|       27 | 20000  |
|       28 | 25600  |
|       29 | 32000  |
|       30 | 40000  |
|       31 | 51200  |
|       32 | 64000  |
|       33 | 80000  |
|       34 | 102400 |


### Shutter Speed Choices

To list all ISO options, please use `Camera.list_shutterspeed()` method. Below is a table with all the choices available for the Sony α7R IV camera.

|   Choice | Shutter Speed   |
|---------:|:----------------|
|        0 | 0/0             |
|        1 | 30              |
|        2 | 25              |
|        3 | 20              |
|        4 | 15              |
|        5 | 13              |
|        6 | 10              |
|        7 | 8               |
|        8 | 6               |
|        9 | 5               |
|       10 | 4               |
|       11 | 32/10           |
|       12 | 25/10           |
|       13 | 2               |
|       14 | 16/10           |
|       15 | 13/10           |
|       16 | 1               |
|       17 | 8/10            |
|       18 | 6/10            |
|       19 | 5/10            |
|       20 | 4/10            |
|       21 | 1/3             |
|       22 | 1/4             |
|       23 | 1/5             |
|       24 | 1/6             |
|       25 | 1/8             |
|       26 | 1/10            |
|       27 | 1/13            |
|       28 | 1/15            |
|       29 | 1/20            |
|       30 | 1/25            |
|       31 | 1/30            |
|       32 | 1/40            |
|       33 | 1/50            |
|       34 | 1/60            |
|       35 | 1/80            |
|       36 | 1/100           |
|       37 | 1/125           |
|       38 | 1/160           |
|       39 | 1/200           |
|       40 | 1/250           |
|       41 | 1/320           |
|       42 | 1/400           |
|       43 | 1/500           |
|       44 | 1/640           |
|       45 | 1/800           |
|       46 | 1/1000          |
|       47 | 1/1250          |
|       48 | 1/1600          |
|       49 | 1/2000          |
|       50 | 1/2500          |
|       51 | 1/3200          |
|       52 | 1/4000          |
|       53 | 1/5000          |
|       54 | 1/6400          |
|       55 | 1/8000          |
|       56 | Bulb            |