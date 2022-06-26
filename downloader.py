# Import libraries
import os, time, eyed3
import requests, urllib, urllib.parse
from datetime import datetime

# Variables, (Lists) and Sets
log = open('log.txt', "a")
moods, genres, tracks, bpm, pages, vocals, order, duration, tagsList  = ([] for i in range(9))
sort = ["neutral-pop91"]
userfolder = "E-Downloader"
Path = "./" 
typed = ""

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
def flog(item,delim="\n",log=log):
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
    case "mood" | "mod" | "md" | "m":
      for item in breadth:
        if item in MOODS:
          moods.append(urllib.parse.quote_plus(item))
        else:
          print("Invalid Mood!")
    case "genre" | "genr" | "gen" | "g":
      for item in breadth:
        if (item in GENRES) | (item in SUBGENRES):
          genres.append(urllib.parse.quote_plus(item))
        else:
          print("Invalid Genre / Subgenre!") 
    case "bpm" | "speed" | "beats" | "b":
      for item in breadth:
        bpm.append(urllib.parse.quote_plus(item))
    case "vocals" | "voice" | "voz" | "v":
      vocals.append(True)
    case "instrumentals" | "novoice" | "instruments" | "sound" | "inst" | "i":
      vocals.append(False)
    case "duration" | "time" | "length" | "len" | "tm" | "dur" | "d" | "l":
      match breadth:
        case [a]:
          duration = [0,a]
        case [a, b]:
          duration = [a,b]
    case "order" | "ord" | "o":
      if isIn(breadth, SORT):
        order = urllib.parse.quote_plus(breadth)
    case "sort" | "srt" | "st" | "s":
      if isIn(breadth, SORT):
        sort = [urllib.parse.quote_plus(breadth)]
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
    case _:
        print("Not Recognized: {}".format(command))

# Create tags for all gathered information
try: tagsList.append("?sort={}".format(sort[-1]));
except IndexError: pass
try: tagsList.append("&vocals={}".format(vocals[-1]))
except IndexError: pass
try: tagsList.append("&order={}".format(order[-1]))
except IndexError: pass
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
    '{} {}'.format(userfolder,' '.join(moods),' '.join(genres)))
try: 
    os.makedirs(Path + folder) 
    flog('Folder Created: {}'.format(folder))
except FileExistsError: pass

# Begin iterating sequences
tracked, paged = 0
curTrack, curPage = 1
for pg in pages:
    paged = int(pg)
for tr in tracks:
    tracked = int(tr)
if (tracked == 0):
    paged = 1
while (curTrack <= tracked) | (curPage <= paged) :
    resp = requests.get(
        'https://www.epidemicsound.com/json/search/tracks/{}&{}'
        .format(tags, "page={}".format(curPage))
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
          os.remove(picFilename)
          ##Will Be Deprecated Soon##
          information = '{} || {} >> {} | {} - {}'.format(curTrack, int(time.time()), datetime.now(), trackAuthor, trackName)
          flog('{}'.format(information))
          curTrack += 1
    curPage += 1
log.close()
print(' ')
