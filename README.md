# Emotion_Recognition_initial_recordings

wav_file_processing.py script helps to standardize the wav name files. 

txt_processing.py script is used over the txt files to merge into a common csv file.

Feature_Extractor.py which executes the opensmile script and gives the path for reading and storing the files.

txt_NametoNumber_transformation.py, which allows the further interpretation of the emotions as labels for the algorithms.

txt_NametoName_transformation.py whose main aim is to standardize all the possible names of the positive emotions.
 
txt_Column_selection.py selects the features (columns) of interest of the excel file.

txt_Row_selection.py makes it possible to select the emotions into a new excel file

txt_column_split.py helps processing the emobase_acoustics_dutch.csv file.

txt_EmotionGrouping_transformation.py to create the numeric labels of the groups.

txt_Gender_assignment.py to assign the gender by participant number.

txt_Gender_Numeric_assignment.py to transform the gender into a number for preparing the file for the MLpositive_emotion algorithm.

txt_grouping_selection.py to select the emotions that create 4 groups: epistemological emotions (amusement, awe, interest, relief), prosocial emotions (amae, gratitude, admiration, elevation), savouring emotions (sensory pleasure, lust), agency-approach emotions (elation/euphoria, pride, excitement, triumph)

txt_Randomnize_dataset.py selects randomly and splits the data in three different datasets: Training, validation and test set.

txt_scale_transformation.py performs the scaling over the data.
