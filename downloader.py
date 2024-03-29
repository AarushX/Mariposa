# Import libraries
import os, time, eyed3
import requests, urllib, urllib.parse
from datetime import datetime

# Variables, (Lists) and Sets
log = open('log.txt', "a")
moods, genres, tracks, bpm, pages, vocals, duration, tagsList  = ([] for i in range(8))
sort = "neutral-pop91"
order = ""
userfolder = "Epidemic"
Path = "./" 
typed = ""
debug = False
persist = False
keepImage = False

MOODS = set([
  "Angry", "Busy & Frantic", "Changing Tempo", "Chasing", "Dark", "Dreamy", "Eccentric", "Elegant", "Epic", "Euphoric", "Fear", "Floating", "Funny", "Glamorous", "Happy", "Heavy & Ponderous", "Hopeful", "Laid Back", "Marching", "Mysterious", "Peaceful", "Quirky", "Relaxing", "Restless", "Romantic", "Running", "Sad", "Scary", "Sentimental", "Sexy", "Smooth", "Sneaking", "Suspense", "Weird"
])
GENRES = set([
  "Acoustic", "Blues", "Brass & Marching Band", "Children", "Circus & Funfair", "Classical", "Comedy", "Country", "Drones", "Electronica & Dance", "Fanfares", "Film", "Funk", "Hip Hop", "Jazz", "Latin", "Muzak", "Pop", "Reggae", "Rnb & Soul", "Rock", "Small Emotions", "Special Occasions", "Spiritual Music", "Traditional Dance", "World & Countries"
])
SUBGENRES = set([
  "1950s Rock", "1960s Pop", "1960s Rock", "1970s Pop", "1970s Rock", "1980s Pop", "1980s Rock", "1990s Pop", "1990s Rock", "2000s Pop", "2000s Rock", "2010s Pop", "2010s Rock", "2020s Pop", "Acid Jazz", "Acoustic Group", "Action", "Adventure", "African Continent", "Afrobeats", "Alternative Hip Hop", "Alternative", "Ambient", "American Roots Rock", "Amusement Park", "Badly Played", "Bagpipes", "Beats", "Beautiful", "Bebop", "Big Band", "Birthdays", "Bloopers", "Bossa Nova", "Build", "Calypso", "Cartoons", "Ceremonial & Olympic", "Cha Cha", "Chamber Music", "Chase", "Choir", "Christmas", "Circus", "Classical Piano", "Classical Waltz", "Comedy", "Crime Scene", "Dance", "Deep House", "Disco", "Drama", "Dramatic Classical", "Drinking Songs", "Drum n Bass", "Dubstep", "Eccentric & Quirky", "Electro", "Epic Classical", "Euro Pop", "Fantasy & Dreamy", "Flamenco", "Folk", "Funerals", "Funk", "Future Bass", "Gospel", "Greece", "Happy", "Hard Rock", "High Drones", "High Non Rhythmic Drones", "High Rhythmic Drones", "Hip Hop", "Horror", "House", "India", "Indie Pop", "Ireland", "Jitterbug", "K-pop", "Low Drones", "Low Non Rhythmic Drones", "Low Rhythmic Drones", "Lullabies", "Main Title", "Mainstream Hip Hop", "Mambo", "Marching Band", "Metal", "Middle East", "Military & Historical", "Modern Blues", "Modern Classical", "Modern Country", "Modern Hymns", "Modern Jazz", "Modern Latin", "Motown & Old School RnB", "Muzak", "Mystery", "Nostalgia", "Old School Funk", "Old School Hip Hop", "Old School RnB", "Oompah", "Other", "Polka", "Post Rock", "Praise & Worship", "Pulses", "Punk", "Reggae", "Religious Theme", "RnB", "Rumba & Beguine", "Sad", "Salsa", "Samba", "Scandinavian", "Scary", "Schlager", "Show Dance", "Ska", "Small Drama", "Small Emotions", "Smooth Jazz", "Sneaky", "Soft House", "Solo Guitar", "Solo Instruments", "Solo Piano", "Soul", "Strange & Weird", "String Quartet", "Supernatural", "Suspense", "Synth Pop", "Tango", "Techno & Trance", "Teen Pop", "The Balkans", "Traditional Blues", "Traditional Country", "Traditional Jazz", "Tragedy", "Trap", "Twist", "Vaudeville & Variety Show", "Video Games", "Waltz", "Weddings"
])
VOCALS = set([
  "Vocals", "Instrumentals"
])
SORT = set([
  "date", "neutral-pop91", "title", "bpm", "duration" 
])
ORDER = set([
  "asc", "desc"
])

# Functions
def formatLog(item,delim="\n",log=log):
    print(item)
    log.write("{}{}".format(item,delim)) 
def removeUnsupportedSymbols(filename):
    for symbol in [':', '?', '/']:
        filename = filename.replace(symbol, '')
    return filename
def isIn(item, set):
  if (item) in (set):
    return True
  else:
    print("Invalid arguments!")

# Create a CLI to gather information
while typed != "run":
  typed = input(">>> ")
  command, *breadth = typed.split() 
  match command:
#   Mood: Sets mood of the matched songs
#     mood (mood1) (mood2) [mood...]
#       Aliases: mod, md, m
    case "mood" | "mod" | "md" | "m":
      for item in breadth:
        if item in MOODS:
          moods.append(urllib.parse.quote_plus(item))
        else:
          print("Invalid Mood!")

#   Genre: Sets the songs' genres
#     genre (genre1) (genre2) [genre...]
#       Aliases: genr, gen, g
    case "genre" | "genr" | "gen" | "g":
      for item in breadth:
        if (item in GENRES) | (item in SUBGENRES):
          genres.append(urllib.parse.quote_plus(item))
        else:
          print("Invalid Genre / Subgenre!") 

#   BPM: Sets the songs' beats per minutes range
#     bpm (bpm min) (bpm max)
#       Aliases: speed, beats, b
    case "bpm" | "speed" | "beats" | "b":
      for item in breadth:
        bpm.append(urllib.parse.quote_plus(item))

#   Find songs with vocals
#     vocals
#       Aliases: voice, voz, v
    case "vocals" | "voice" | "voz" | "v":
      vocals.append(True)

#   Vocals Settings: Find songs without vocals
#     instrumentals
#       Aliases: novoice, instruments, inst, sound, i
    case "instrumentals" | "novoice" | "instruments" | "sound" | "inst" | "i":
      vocals.append(False)

#   Duration: Sets the songs' time range
#     duration (minimum seconds [optional]) (max seconds)
#       Aliases: time, length, len, tm, dur, d, l
    case "duration" | "time" | "length" | "len" | "tm" | "dur" | "d" | "l":
      match breadth:
        case [a]:
          duration = [0,a]
        case [a, b]:
          duration = [a,b]
#   Order: Sets the songs' downloading order
#     order (order type)
#       Aliases: ord, o
    case "order" | "ord" | "o":
      if (breadth[0]) in (ORDER):
        order = urllib.parse.quote_plus(str(breadth[0]))
      else:
        print("Invalid arguments!")

#   Sort: Sets the songs' sorting order
#     sort (sort type)
#       Aliases: srt, st, s
    case "sort" | "srt" | "st" | "s":
      if (breadth[0]) in (SORT):
        sort = urllib.parse.quote_plus(str(breadth[0]))
      else:
        print("Invalid arguments!")

#   Tracks: Sets the amount of songs to download
#     tracks (amount) [-p page amounts] [-t track amounts]
#       Aliases: amount, number, tlen, tamt, t
    case "tracks" | "amount" | "number" | "tlen" | "tamt" | "t":
      match breadth:
        case [a]:
          tracks.append(a)
        case [a, b]:
          match b:
            case "-p" | "pages" | "full":
              pages.append(a)
            case "-t" | "tracks":
              tracks.append(a)
            case _:
              print("Not a valid argument: {}".format(b))
    case "pages" | "pgs" | "pg" | "p":
      pages.append(breadth)
    case "genres" | "gens":
        print(GENRES)
        print("For subgenres, enter \'subs\' or \'flist\'")
    case "moods" | "ms":
      print(MOODS)
    case "subs" | "subgenres":
        print(SUBGENRES)
    case "list" | "flist" | "full" | "all" | "f":
        print("Moods: \n\t{}\n\nGenres: \n\t{}\nSubgenres: \n\t{}\n\nSorts: \n\t{}".format(MOODS,GENRES,SUBGENRES,SORT))
    case "run" | "rn" | "r":
        print("Started operation!")
    case "name" | "nm" | "nam" | "n":
        userfolder = breadth[0]
    case "debug" | "fix" | "json" | "request" | "url":
      debug = True
    case "remain" | "stayopen" | "so" | "persist":
      persist = True
    case _:
        print("Not Recognized: {}".format(command))
    
# Create tags for all gathered information
if (sort != ""): tagsList.append("?sort={}".format(sort));
try: tagsList.append("&vocals={}".format(vocals[-1]))
except IndexError: pass
if (order != ""): tagsList.append("&order={}".format(order))
try: tagsList.append("&bpm={}-{}".format(bpm[-2],bpm[-1]))
except IndexError: pass
try: tagsList.append("&length={}-{}".format(duration[-2],duration[-1]))
except IndexError: pass
for mood in moods:
    tagsList.append("&mood={}".format(mood))
for genre in genres:
    tagsList.append("&genres={}".format(genre))
tags = ''.join(tagsList)

# Create the folder
folder = removeUnsupportedSymbols(
    '{} {} Music'.format(userfolder,' '.join(moods),' '.join(genres)))
try: 
    os.makedirs(Path + folder) 
    formatLog('Folder Created: {}'.format(folder))
except FileExistsError: pass

# Begin iterating sequences
tracked, paged = (0 for i in range(2))
curTrack, curPage = (1 for i in range(2))
for pg in pages:
    paged = int(pg)
for tr in tracks:
    tracked = int(tr)
if (tracked == 0):
    paged = 1
jsonUrl = 'https://www.epidemicsound.com/json/search/tracks/{}&{}'
if (debug):
  print(jsonUrl.format(tags,"debug"))
while (curTrack <= tracked) | (curPage <= paged) :
    resp = requests.get(
        jsonUrl.format(tags, "page={}".format(curPage))
    )
    for track in resp.json()['entities']['tracks'].values():
        if (curTrack <= tracked) | (curPage <= paged):
          # Title
          trackName = removeUnsupportedSymbols(track['title'])
          # Sources
          pictureUrl = "{}{}".format(track['coverArt']['baseUrl'],track['coverArt']['sizes']['L'])
          trackUrl = track['stems']['full']['lqMp3Url']
          # Author
          if len(track['creatives']['mainArtists']) == 0: trackAuthor = 'Unknown'
          else: trackAuthor = track['creatives']['mainArtists'][0]['name']
          # Paths
          mp3Filename = Path + \
              '{}/{} - {}.mp3'.format(folder, trackAuthor, trackName)
          picFilename = Path + \
              '{}/{} - {}.jpg'.format(folder, trackAuthor, trackName)
          # Downloads
          urllib.request.urlretrieve(trackUrl, mp3Filename)
          urllib.request.urlretrieve(pictureUrl, picFilename)
          # Load the new metadata
          audio = eyed3.load(mp3Filename)
          atg = audio.tag
          if (atg == None): audio.initTag()
          atg.title = trackName
          atg.album = "{} - {}".format(trackAuthor,trackName)
          atg.artist = trackAuthor
          atg.images.set(3, open(picFilename, 'rb').read(), 'image/jpeg')
          atg.save(version=eyed3.id3.ID3_V2_3)
          # Remove the un-needed image
          if (keepImage == False): 
            os.remove(picFilename)
          information = '{} || {} >> {} | {} - {}'.format(curTrack, int(time.time()), datetime.now(), trackAuthor, trackName)
          formatLog('{}'.format(information))
          curTrack += 1
    curPage += 1
log.close()
print(' ')
if (persist):
  input("[0/2] Persist Mode selected. Press enter 2 times to exit.")
  input("[1/2] Persist Mode selected. Press enter 1 more time to exit.")
  print("[2/2]")
else: 
  print("Closing in 5 seconds.")
  time.sleep(5)
