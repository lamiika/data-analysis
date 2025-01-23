# epileptic seizure | CHB-MIT EEG Dataset (.CSV)
import pandas as pd
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

filename = 'epileptic_seizure_CHB-MIT_EEG_Dataset/EEG_Scaled_data.csv'

total_rows = sum(1 for line in open(filename))
rows_to_read = total_rows // 20

df = pd.read_csv(filename, nrows=rows_to_read)

#for chunk in pd.read_csv('epileptic_seizure_CHB-MIT_EEG_Dataset/EEG_Scaled_data.csv', chunksize=chunksize):
    # Process each chunk here
#    print(chunk.shape)
    

