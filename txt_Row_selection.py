#fileformat example: p1_amae.txt
import os
import re
import numpy as np
import pandas as pd

import csv

df = pd.read_csv('input-Trimed\PCA_BackE_Trimed_eGeMAPSv01b_acoustics.csv')


print(df,'df')
# selecting the column/s
select_color = df.loc[df['Emotion_Category'].isin(['hope', 'tenderness'])]
print(select_color)



select_color.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\output-Trimed\Hope_Tenderness_PCA_BackE_Trimed_eGeMAPSv01b_acoustics.csv', index = False)
