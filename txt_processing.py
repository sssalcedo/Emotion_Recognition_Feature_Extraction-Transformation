#Processing of the txt files with a  _ format
#fileformat example: p1_amae.txt
import os
import re
import numpy as np
import pandas as pd
txt_path='Speech_Prosody_of_Positive_Emotions/Outputs/'
txt_list=os.listdir(txt_path)
features_list=[]   #list of features
Name_list=[]
name_list=[]
Emotion_list=[]
for txt in txt_list:
    if txt[-4:]=='.txt':
        this_path=os.path.join(txt_path,txt)
        f=open(this_path)
        last_line=f.readlines()[-1]
        f.close()
        features=last_line.split(',')
        features=features[1:-1]
        features_list.append(features)
        Name_list.append(txt[1:-4])
features_array=np.array(features_list)
dataframe = pd.DataFrame(features_array)
for i in Name_list:
    temp = re.compile("([0-9]+)([_]+)([a-zA-Z]+)")  #filename splitter
    res = temp.match(i).groups() 
    name_list.append(int(res[0])) #participant number list
    Emotion_list.append(res[2]) #positive emotion list
dataframe.insert(0, "Part number", name_list) #insetion of participant number
dataframe.insert(1, "Emotion Category", Emotion_list)#insertion of positive emotion
print(dataframe)
dataframe.to_csv(r"Speech_Prosody_of_Positive_Emotions/Merged_outputs/eGeMAPSv01b_acoustics_dutch.csv")