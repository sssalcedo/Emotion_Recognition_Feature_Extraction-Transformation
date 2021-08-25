#fileformat example: p1_amae.txt
import os
import re
import numpy as np
import pandas as pd

import csv

df = pd.read_csv('input-Trimed\Triumph_awe_BackE_Trimed_eGeMAPSv01b_acoustics.csv')


print(df,'df1')
# updating the column value/data


df_Training = df.sample(frac=0.70)
#part_1 = df.sample(frac = 0.7)
#part_2 = df.drop(part_1.index)
part_2 = df.drop(df_Training.index)
df_Test = part_2.sample(frac=0.30)
#df_Validation = part_2.sample(frac=0.30)
#df_Test = part_2.drop(df_Validation.index)
print(df_Test)

df_Training.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\output-Trimed\Training_Triumph_awe_BackE_Trimed_eGeMAPSv01b_acoustics.csv', index = False)
#df_Validation.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\output-Trimed\Validation_Triumph_awe_BackE_Trimed_eGeMAPSv01b_acoustics.csv', index = False)
df_Test.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\output-Trimed\Test_Triumph_awe_BackE_Trimed_eGeMAPSv01b_acoustics.csv', index = False)
