## How to yse this repo 

Install dependencies
```
make install
```

#### Make
for simple hello world app :
```
make helloworld
```

for message app, runi in separate terminal :
```
make message_server
make message_terminal
```

#### To clean repo
```
make clean
```

## CREATE FLASK APP Guide

#### Create a virtual environnement named `venv`
``` 
python3 -m venv venv
```

#### Activate the virtual environnement
- On Windows, use  
```
venv\Scripts\activate
```
- On Unix or MacOS, use 
```
source venv/bin/activate
```

#### Install Flask 
```
pip3 install Flask
```

Check helloworld app for basic python code. 

#### Run Your Flask App
In your terminal, with the virtual environment activated, run 
```
python app.py
```
This will start a development server on localhost (usually on port 5000).

#### How to freeze requirement
```
python -m pip freeze > requirements.txt
```# Flask_Example
