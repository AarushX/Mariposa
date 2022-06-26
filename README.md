# E-Downloader
A quick and easy CLI (currently) downloader based in python.

## Installation 
Download and unzip zip file into a folder.
Then, run:
```python
pip install -r requirements.txt
```
Run **downloader.py**!

**Mood:**
Sets mood of the matched songs
```bash
mood (mood1) (mood2) [mood...]
```
*Aliases*: mod, md, m

**Genre:**
Sets the songs' genres
```bash
genre (genre1) (genre2) [genre...]
```
*Aliases*: genr, gen, g

**BPM:**
Sets the songs' beats per minutes range
```bash 
bpm (bpm min) (bpm max)
```
*Aliases*: speed, beats, b

**Vocals Settings:**
*Find songs without vocals*
```bash 
instrumentals
```
*Aliases*: novoice, instruments, inst, sound, i

*Find songs with vocals*
```bash 
vocals
```
*Aliases*: voice, voz, v

**Duration:**
Sets the songs' time range
```bash 
duration (minimum seconds [optional]) (max seconds)
```
*Aliases*: time, length, len, tm, dur, d, l

**Order:**
Sets the songs' downloading order
```bash 
order (order type)
```
*Aliases*: ord, o

**Sort:**
Sets the songs' sorting order
```bash 
sort (sort type)
```
*Aliases*: srt, st, s

**Tracks:**
Sets the amount of songs to download
```bash 
tracks (amount) [-p page amounts] [-t track amounts]
```
*Aliases*: amount, number, tlen, tamt, t

**Pages:**
Sets the amount of pages of songs to download (pages * 60 available tracks)
```bash 
pages (amount of pages)
```
*Aliases*: pgs pg p

**BPM:**
Sets the songs' beats per minutes range
```bash 
bpm (bpm min) (bpm max)
```
*Aliases*: speed, beats, b

## Informational Stats
Print genres
```bash 
genres
```
Print moods
```bash 
moods
```
Print subgenres
```bash 
subgenres
```
Print *all available arguments*
```bash 
list / flist / all / full / f
```
## Essential Commands
**Run:**
Sets the project up, downloads files, and imports metadata
```bash 
run
```
*Aliase*: rn, r

**Name:**
Name the folder identifier that the folder is named
```bash 
name (folder name)
```
*Aliases*: nam, nm, n

## Full lists of everything
### Moods:
```bash
"Angry", "Busy & Frantic", "Changing Tempo", "Chasing", "Dark", "Dreamy", "Eccentric", "Elegant", "Epic", "Euphoric", "Fear", "Floating", "Funny", "Glamorous", "Happy", "Heavy & Ponderous", "Hopeful", "Laid Back", "Marching", "Mysterious", "Peaceful", "Quirky", "Relaxing", "Restless", "Romantic", "Running", "Sad", "Scary", "Sentimental", "Sexy", "Smooth", "Sneaking", "Suspense", "Weird"
```
### Genres:
```bash
"Acoustic", "Blues", "Brass & Marching Band", "Children", "Circus & Funfair", "Classical", "Comedy", "Country", "Drones", "Electronica & Dance", "Fanfares", "Film", "Funk", "Hip Hop", "Jazz", "Latin", "Muzak", "Pop", "Reggae", "Rnb & Soul", "Rock", "Small Emotions", "Special Occasions", "Spiritual Music", "Traditional Dance", "World & Countries"
```
### Subgenres:
```bash
"1950s Rock", "1960s Pop", "1960s Rock", "1970s Pop", "1970s Rock", "1980s Pop", "1980s Rock", "1990s Pop", "1990s Rock", "2000s Pop", "2000s Rock", "2010s Pop", "2010s Rock", "2020s Pop", "Acid Jazz", "Acoustic Group", "Action", "Adventure", "African Continent", "Afrobeats", "Alternative Hip Hop", "Alternative", "Ambient", "American Roots Rock", "Amusement Park", "Badly Played", "Bagpipes", "Beats", "Beautiful", "Bebop", "Big Band", "Birthdays", "Bloopers", "Bossa Nova", "Build", "Calypso", "Cartoons", "Ceremonial & Olympic", "Cha Cha", "Chamber Music", "Chase", "Choir", "Christmas", "Circus", "Classical Piano", "Classical Waltz", "Comedy", "Crime Scene", "Dance", "Deep House", "Disco", "Drama", "Dramatic Classical", "Drinking Songs", "Drum n Bass", "Dubstep", "Eccentric & Quirky", "Electro", "Epic Classical", "Euro Pop", "Fantasy & Dreamy", "Flamenco", "Folk", "Funerals", "Funk", "Future Bass", "Gospel", "Greece", "Happy", "Hard Rock", "High Drones", "High Non Rhythmic Drones", "High Rhythmic Drones", "Hip Hop", "Horror", "House", "India", "Indie Pop", "Ireland", "Jitterbug", "K-pop", "Low Drones", "Low Non Rhythmic Drones", "Low Rhythmic Drones", "Lullabies", "Main Title", "Mainstream Hip Hop", "Mambo", "Marching Band", "Metal", "Middle East", "Military & Historical", "Modern Blues", "Modern Classical", "Modern Country", "Modern Hymns", "Modern Jazz", "Modern Latin", "Motown & Old School RnB", "Muzak", "Mystery", "Nostalgia", "Old School Funk", "Old School Hip Hop", "Old School RnB", "Oompah", "Other", "Polka", "Post Rock", "Praise & Worship", "Pulses", "Punk", "Reggae", "Religious Theme", "RnB", "Rumba & Beguine", "Sad", "Salsa", "Samba", "Scandinavian", "Scary", "Schlager", "Show Dance", "Ska", "Small Drama", "Small Emotions", "Smooth Jazz", "Sneaky", "Soft House", "Solo Guitar", "Solo Instruments", "Solo Piano", "Soul", "Strange & Weird", "String Quartet", "Supernatural", "Suspense", "Synth Pop", "Tango", "Techno & Trance", "Teen Pop", "The Balkans", "Traditional Blues", "Traditional Country", "Traditional Jazz", "Tragedy", "Trap", "Twist", "Vaudeville & Variety Show", "Video Games", "Waltz", "Weddings"
```
### Sort
```bash
"date", "neutral-pop91", "title", "bpm", "duration"
```
### Order
```bash
"asc", "desc"
```
