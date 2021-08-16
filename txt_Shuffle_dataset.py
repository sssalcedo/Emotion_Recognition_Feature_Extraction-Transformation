#fileformat example: p1_amae.txt
import os
import re
import numpy as np
import pandas as pd

import csv

df = pd.read_csv('input\Random_BackE_eGeMAPSv01b_acoustics_dutchFemales.csv')


print(df,'df1')
# updating the column value/data
df_shuffled=df.sample(frac=1).reset_index(drop=True)
print(df_shuffled)

df_shuffled.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\Output\Random_BackE_eGeMAPSv01b_acoustics_dutchFemales.csv', index = False)
