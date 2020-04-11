import pandas as pd
from os import listdir
from os.path import isfile, join
from collections import Counter

source_folder = "/Volumes/Seagate1TB/Capstone/musicnet/capstone_labels/"

def note_to_key(root, notes):
    if root == 'C':
        for n in notes:
            if n[0] == 'D#/Eb':
                return("c minor")
            elif n[0] == 'E':
                return("C Major")
        return ("Key unclear")

    elif root == 'C#/Db':
        for n in notes:
            if n[0] == 'E':
                return("c# minor")
            elif n[0] == 'F':
                return("Db Major")
        return ("Key unclear")


    elif root == 'D':
        for n in notes:
            if n[0] == 'F':
                return("d minor")
            elif n[0] == 'F#/Gb':
                return("D Major")
        return ("Key unclear")


    elif root == 'D#/Eb':
        for n in notes:
            if n[0] == 'F#/Gb':
                return("eb minor")
            elif n[0] == 'G':
                return("Eb Major")
        return ("Key unclear")


    elif root == 'E':
        for n in notes:
            if n[0] == 'G':
                return("e minor")
            elif n[0] == 'G#/Ab':
                return("E Major")
        return ("Key unclear")


    elif root == 'F':
        for n in notes:
            if n[0] == 'G#/Ab':
                return("f minor")
            elif n[0] == 'A':
                return("F Major")
        return ("Key unclear")

    elif root == 'F#/Gb':
        for n in notes:
            if n[0] == 'A':
                return("f# minor")
            elif n[0] == 'A#/Bb':
                return("F# Major or Gb major")
        return ("Key unclear")

    elif root == 'G':
        for n in notes:
            if n[0] == 'A#/Bb':
                return("g minor")
            elif n[0] == 'B':
                return("G Major")
        return ("Key unclear")

    elif root == 'G#/Ab':
        for n in notes:
            if n[0] == 'B':
                return("G# or Ab minor")
            elif n[0] == 'G#/Ab':
                return("E Major")
        return ("Key unclear")

    elif root == 'A':
        for n in notes:
            if n[0] == 'C':
                return("a minor")
            elif n[0] == 'C#/Db':
                return("A Major")
        return ("Key unclear")

    elif root == 'A#/Bb':
        for n in notes:
            if n[0] == 'C#/Db':
                return("Bb minor")
            elif n[0] == 'D':
                return("Bb Major")
        return("Key unclear")

    elif root == 'B':
        for n in notes:
            if n[0] == 'D':
                return("b minor")
            elif n[0] == 'D#/Eb':
                return("B Major")
        return ("Key unclear")

def midi_to_note(x):
    if(x > 20):
        x=(x-20) % 12
    if(x == 1):
        return('A')
    elif(x == 2):
        return('A#/Bb')
    elif(x == 3):
        return('B')
    elif(x == 4):
        return('C')
    elif(x == 5):
        return('C#/Db')
    elif(x == 6):
        return('D')
    elif(x == 7):
        return('D#/Eb')
    elif(x == 8):
        return('E')
    elif(x == 9):
        return('F')
    elif(x == 10):
        return('F#/Gb')
    elif(x == 11):
        return('G')
    elif(x == 0):
        return('G#/Ab')

onlyfiles = [f for f in listdir(source_folder) if isfile(join(source_folder, f))]
for f in onlyfiles:
    data = pd.read_csv(source_folder + f)

    notenames = []

    # printing the most common notes within the last 5 'beats'
    z = len(data.index)

    i = data['start_beat'][0]
    k = max(data['start_beat'])
    y = data.loc[data.start_beat >= i].index[0]

    # printing the lowest of the last notes of the piece
    root_note = midi_to_note(min(data.loc[data.start_beat == k]['note']))

    for x in range(y, z):
        notenames.append(midi_to_note(data.iloc[x]['note']))

    list_freq = Counter(notenames)
    penta = list_freq.most_common(7)

    print(f, note_to_key(root_note, penta))
















