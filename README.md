# Chae's video downloader

## Youtube video downloader project.
___
video_downloader.py is the main file.

filter_streams.py stores the class that checks for correct input and has methods to filter streams using regexes.

down_load.py stores the video downloader class that works the actual stream data. has methods to fetch the streams and downlaod one given the index.


### Installing video downloader
___
```
git clone https://github.com/ChaeDLR/Chaes-video-downloader.git
```
### Mac OS venv
___

#### Create virtual environment files in your current directory

```
python3 -m venv (folder name)
```

#### Activate environment

```
source (folder name)/bin/activate
```

#### To deactivate venv

```
deactivate
```


### Windows 10 venv
___

#### Create virtual environment files in your current directory

```
python -m venv (folder name)
```

#### Activate environment

```
(folder name)/Scripts/activate.bat
```

#### To deactivate venv

```
deactivate
```

### Installing requirements
```
pip install -r requirements.txt
```

## Run the program
___
```
python video_downloader.py
```