#fileformat example: p1_amae.txt
import os
import re
import numpy as np
import pandas as pd

import csv
df = pd.read_csv('input\Trimed_eGeMAPSv01b_acoustics.csv')

# updating the column value/data
df.loc[df.Part_number == 6, 'gender'] = 'male'
df.loc[df.Part_number == 9, 'gender'] = 'male'
df.loc[df.Part_number == 28, 'gender'] = 'male'
df.loc[df.Part_number == 31, 'gender'] = 'male'
df.loc[df.Part_number == 43, 'gender'] = 'male'
df.loc[df.Part_number == 50, 'gender'] = 'male'
df.loc[df.Part_number == 51, 'gender'] = 'male'
df.loc[df.Part_number == 53, 'gender'] = 'male'
df.loc[df.Part_number == 59, 'gender'] = 'male'
df.loc[df.Part_number == 60, 'gender'] = 'male'
df.loc[df.Part_number == 61, 'gender'] = 'male'
df.loc[df.Part_number == 66, 'gender'] = 'male'
df.loc[df.Part_number == 70, 'gender'] = 'male'
df.loc[df.Part_number == 72, 'gender'] = 'male'
df.loc[df.Part_number == 82, 'gender'] = 'male'
df.loc[df.Part_number == 99, 'gender'] = 'male'
df.loc[df.Part_number == 112, 'gender'] = 'male'
df.loc[df.Part_number == 114, 'gender'] = 'male'
df.loc[df.Part_number == 116, 'gender'] = 'male'
df.loc[df.Part_number == 118, 'gender'] = 'male'
df.loc[df.Part_number == 123, 'gender'] = 'male'
df.loc[df.Part_number == 130, 'gender'] = 'male'
df.loc[df.Part_number == 139, 'gender'] = 'male'
df.loc[df.Part_number == 141, 'gender'] = 'male'
df.loc[df.Part_number == 144, 'gender'] = 'male'
df.loc[df.Part_number == 145, 'gender'] = 'male'
df.loc[df.Part_number == 148, 'gender'] = 'male'
df.loc[df.Part_number == 153, 'gender'] = 'male'
df.loc[df.Part_number == 155, 'gender'] = 'male'
df.loc[df.Part_number == 159, 'gender'] = 'male'
df.loc[df.Part_number == 160, 'gender'] = 'male'
df.loc[df.Part_number == 161, 'gender'] = 'male'
df.loc[df.Part_number == 165, 'gender'] = 'male'
df.loc[df.Part_number == 168, 'gender'] = 'male'
df.loc[df.Part_number == 180, 'gender'] = 'male'
df.loc[df.Part_number == 183, 'gender'] = 'male'
df.loc[df.Part_number == 184, 'gender'] = 'male'
df.loc[df.Part_number == 199, 'gender'] = 'male'


df.to_csv(r'C:\Users\jesus\Desktop\AMSTERDAM\psychology\Feature-Transformation\Output\Trimed_eGeMAPSv01b_acoustics.csv', index = False)
