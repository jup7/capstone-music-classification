import pandas as pd
from os import listdir
from os.path import isfile, join


source_folder = "/Volumes/Seagate1TB/Capstone/musicnet/capstone_labels/"

fs = 44100 #samples/second

onlyfiles = [f for f in listdir(source_folder) if isfile(join(source_folder, f))]

for f in onlyfiles:
  data = pd.read_csv(source_folder + f)

  index = abs(data['end_beat'] - 1).idxmin()
  beat, noteval = (data.loc[index]['end_beat'], data.loc[index]['note_value'])

  mus_start = data.iloc[1]['start_time']
  mus_end = data.iloc[-1]['end_time']

  piece_length = (mus_end - mus_start) / fs

  beat_start = data.iloc[1]['start_beat']
  beat_end = data.iloc[-1]['start_beat'] + data.iloc[-1]['end_beat']

  tot_beats = beat_end - beat_start
  bpm = ((tot_beats  * 60) / piece_length) / beat

  print(f, bpm)







