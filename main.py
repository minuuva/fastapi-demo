#!/usr/local/bin/python3.12

from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import os
import json
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
DB = os.getenv('DB')

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

@app.get("/genres")
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(headers, result)))
        return json_data  # Return directly without json.dumps
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        return {"error": "Failed to fetch genres"}

@app.get("/songs")
def get_songs():
    query = """
    SELECT songs.title, songs.album, songs.artist, songs.year,
           songs.file, songs.image, genres.genre
    FROM songs
    JOIN genres ON songs.genre = genres.genreid
    ORDER BY songs.title;
    """
    try:
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = []
        for result in results:
            json_data.append(dict(zip(headers, result)))
        return json_data  # Return directly without json.dumps
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        return {"error": "Failed to fetch songs"}

