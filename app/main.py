#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Minu"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/mutiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@app.get("/square/{e}")
def square(e: int):
    return {"square": e**2}

@app.get("/divide/{f}/{g}")
def divide(f: int, g: int):
    return {"divide": f / g}

@app.get("/subtract/{h}/{i}")
def subtract(h: int, i: int):
    return {"subtract": h - i}
