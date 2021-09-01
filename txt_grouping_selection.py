#fileformat example: p1_amae.txt
import os
import re
import numpy as np
import pandas as pd

import csv

df = pd.read_csv('input\Trimed_eGeMAPSv01b_acoustics.csv')


print(df,'df1')
# updating the column value/data
df_grouped = df[df["labels"].isin(['admiration', 'awe', 'amusement','amae','admiration','interest','relief','gratitude','elevation','sensorypleasure','lust','elation','pride','excitement','triumph'])]
print(df_grouped)

df_grouped.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\Output\Groups_Trimed_eGeMAPSv01b_acoustics.csv', index = False)
