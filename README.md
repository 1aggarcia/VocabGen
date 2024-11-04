# Untitled Anki Add-on for language learning 

## Overview
Studying vocabulary for a foreign language is difficult for various reasons.
It's impossible to learn every word you see on first occurrence, you you need
to pick and choose which words are worth learning and which are not. Learning
the correct pronunciation is important so that others can understand you. And
most importantly, foreign words almost never map one-to-one with English. You
need to learn not a translation, but rather the word sense(s), correct grammatical
usage, and potential idiomatic phrases.

Repition is essential to internalize new words, and [Anki](https://apps.ankiweb.net/) helps considerably with
this aspect. [Anki](https://apps.ankiweb.net/) is an intelligent flashcard system for web, desktop, iOS and
Android which analyses how easily you remember flashcards and spaces the review
times out accordingly. Anki is highly customizable and unopinionated, allowing
it to be used to study almost anything. However the lack of structure creates
extra work to tailor it to your specific needs, such as studying vocab.

Anki has lots of potential for extension by third-party developers (I guess
that means me now), and they recognize this by providing a platform for
developers to share [Add-ons](https://ankiweb.net/shared/addons).

## Features

**Goal** - Make it easier to create and plan flashcards for foreign words

- Given a word in the target language, create a flashcard in an Anki deck containing:
    - The translation of the word
    - Example sentence of usage
    - IPA transcription
- Nice to haves:
    - Audio of the pronunciation
    - Part of speech
    - Grammatical forms depending on part of speech (e.g. gender of nouns, verb tenses, irregularities especially)

*Note:* These features are biased towards Romance languages (Spanish, Romanian, French, etc)
since those are the only languages I have studied at depth.

## Setup and Build

This add-on is developed in Python 3.9 (the version Anki runs). I recommend working in a virtual enviornment
to keep Anki-related dependencies seperate from the rest of your system

To install dependencies (when cloning repo)
```
pip install -r requirements.txt
```


To install Anki (what I did to get the dependencies, you probably won't have to):
```
python3

import subprocess

subprocess.check_call(["pip3", "install", "--upgrade", "pip"])
subprocess.check_call(["pip3", "install", "mypy", "aqt[qt6]"])
```

add more stuff here ...