# ANGA ⛅

Anga bot keeps you upto date with weather patterns and local climatic changes.

## Description

Here's an FAQ 😃. 

        Weather info: 
        To get weather info for cities around the globe.  
                1. Whats the current weather? 
                2. whats the weather in kisumu tomorrow? 
                3. tell me about weather in mombasa on sunday? 

        climate info: 
        To get local kenya climate news per region , regions: Coast , Central, Riftvalley, WesternNyanza, NorthEasternEastern. 
                1. How is kenya affected by climate change. 
                2. How does climate change affect the kenyan coast?.

## Getting Started

### Dependencies

* windows 10 and newer versions 
* Anaconda
* python 3.8
* All in the requirements.txt file

### Installing 

1. clone the repo

```Bash
git clone https://github.com/CLozy/anga.git
```

2. move into the anga2.0 directory and Install requirements.txt file

```Bash
pip install -r requirements.txt
```

### Executing program

1. Train bot

```Bash
rasa train
```
2. run action server in terminal

```Bash
rasa run actions
```
3. run rasa open source server in another terminal

```Bash
rasa run --enable-api --cors *
```
4. move into the website dir and run server

```Bash
python manage.py runserver
```

### Docker

In the same dir as docker-compose.yml file run 

```Bash
docker compose up
```



