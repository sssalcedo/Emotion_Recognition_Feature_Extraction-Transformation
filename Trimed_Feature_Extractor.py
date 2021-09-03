import os
output_path='Trimed_recordings/Output/'
file_path='Trimed_recordings/Trimed_recordings2/'
file_list=os.listdir(file_path)
for file in file_list:
    #print(file[1:])
    audio_path=os.path.join('Trimed_recordings/Trimed_recordings2/p'+file[1:]+'/') 
    audio_list=os.listdir(audio_path)
    for audio in audio_list:
        if audio[-4:] =='.wav':
            this_path_input=os.path.join(audio_path,audio)
            this_path_output=os.path.join(output_path,audio[:-4]+'.txt')     
            cmd ="SMILExtract -C config/egemaps/v01b/eGeMAPSv01b.conf -I " + this_path_input + " -O " + this_path_output
            print(this_path_output)
            os.system(cmd)
            