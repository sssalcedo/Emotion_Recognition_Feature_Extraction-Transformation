#fileformat example: p1_amae.txt
import os
import re
import numpy as np
import pandas as pd

import csv
df = pd.read_csv('input\BackE_Groups_Trimed_eGeMAPSv01b_acoustics.csv')

# updating the column value/data

df.loc[df.Emotion_Category == 'amusement', 'labels'] = 1
df.loc[df.Emotion_Category == 'awe', 'labels'] = 1
df.loc[df.Emotion_Category == 'interest', 'labels'] = 1
df.loc[df.Emotion_Category == 'relief', 'labels'] = 1
df.loc[df.Emotion_Category == 'admiration', 'labels'] = 2
df.loc[df.Emotion_Category == 'amae', 'labels'] = 2
df.loc[df.Emotion_Category == 'gratitude', 'labels'] = 2
df.loc[df.Emotion_Category == 'elevation', 'labels'] = 2
df.loc[df.Emotion_Category == 'sensorypleasure', 'labels'] = 3
df.loc[df.Emotion_Category == 'lust', 'labels'] = 3
df.loc[df.Emotion_Category == 'elation', 'labels'] = 4
df.loc[df.Emotion_Category == 'pride', 'labels'] = 4
df.loc[df.Emotion_Category == 'excitement', 'labels'] = 4
df.loc[df.Emotion_Category == 'triumph', 'labels'] = 4




df.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\Output\SOM_BackE_Groups_Trimed_eGeMAPSv01b_acoustics.csv', index = False)
