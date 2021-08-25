#fileformat example: p1_amae.txt
import os
import re
import numpy as np
import pandas as pd

import csv

df = pd.read_csv('input\Trimed_eGeMAPSv01b_acoustics.csv')


print(df,'df1')
# selecting the column/s
df_selected = df[["Emotion_Category", "12", "14", "15", "23", "26", "28", "30", "41", "43", "47"]]


print(df_selected)

df_selected.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\Output\MfccBackE_Trimed_eGeMAPSv01b_acoustics.csv', index = False)
