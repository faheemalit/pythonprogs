#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:00:34 2019

@author: faheem
"""

import speech_recognition as sr
goodwill=sr.AudioFile('Tyrionspeech.wav')
r=sr.Recognizer()
with goodwill as source:
    rec=r.record(source)
try:
    print("Transcribed Audio:"+r.recognize_google(rec))
except sr.UnknownValuesError:
    print("Google recognition could not understand audio.")
except sr.RequestError:
    print("Could not get the results from Google Speech")