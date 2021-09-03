#Processing of the wav files without _ and with wav format
#fileformat example: ppt  1 - admiration.wav
# Execute this code several times until all the input has been processed
import os
import re
import numpy as np
import pandas as pd
wav_path='Trimed_recordings/p1/'
wav_list=os.listdir(wav_path)
Name_list=[]
name_list=[]
print(wav_list,'wav_list')
for wav in wav_list:
    wav = ''.join(wav.split())
    Name_list.append(wav[1:-4])
print(Name_list,'Name_list')
for i,j in zip(Name_list, wav_list):
    os.rename(r'Trimed_recordings\p1\p' + j[1:],r'Output4\p' + i +'.wav')
