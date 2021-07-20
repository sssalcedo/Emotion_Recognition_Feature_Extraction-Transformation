# MFCCs processing .wav files to .txt files
#Code comes from:
#https://gist.githubusercontent.com/fedden/213201d5d64dc8b6cff38c5aba5611bc/raw/365ec32f234da3bb32b670d306aed857b5a007b4/librosa_audio.py
#https://gist.githubusercontent.com/fedden/445137b26930dd80da0d66451b303e61/raw/50418e93c1fdbd73e7c5e3a9a5b7292a6384e7c0/mfcc.py
import os
import librosa
import numpy as np
import numpy as num
sample_rate = 44100
mfcc_size = 13
# Load the audio
file_path='Speech_Prosody_of_Positive_Emotions/Speech_Prosody_of_Positive_Emotions/'
file_list=os.listdir(file_path)
for file in file_list:
    audio_path=os.path.join('Speech_Prosody_of_Positive_Emotions/Speech_Prosody_of_Positive_Emotions/p'+file[1:]+'/') 
    audio_list=os.listdir(audio_path)
    for audio in audio_list:
        if audio[-4:] =='.wav':
            print(audio)
            file_path = os.path.join(audio_path,audio)
            print(file_path)
            audio_data, _ = librosa.load(file_path)
            pcm_data, _ = librosa.load(file_path)
            mfccs = librosa.feature.mfcc(pcm_data, 
                                 sample_rate, 
                                 n_mfcc=mfcc_size)
            mfccs_transpose = mfccs.transpose()
            # Get the standard deviation
            stddev_features = np.std(mfccs_transpose, axis=0)
            # Get the mean
            mean_features = np.mean(mfccs_transpose, axis=0)
            # Get the average difference of the features
            average_difference_features = np.zeros((13,))
            for i in range(0, len(mfccs_transpose) - 2, 2):
                average_difference_features += mfccs_transpose[i] - mfccs_transpose[i+1]
            average_difference_features /= (len(mfccs_transpose) // 2)   
            average_difference_features = np.array(average_difference_features)
            # Concatenate the features to a single feature vector
            concat_features_features = np.hstack((stddev_features, mean_features))
            concat_features_features = np.hstack((concat_features_features, average_difference_features))
            num.savetxt('./Speech_Prosody_of_Positive_Emotions/Output/' + audio[:-4] +'.txt',concat_features_features, delimiter=",", fmt="%s") 


