import pandas as pd
import numpy as np

df = pd.read_excel(r'C:\Users\jezei\OneDrive\Documents\Data Projects\NBA GOAT\StatmuseBookAVG.xlsx')

# Convert the DataFrame into a NumPy array
array_data = df.to_numpy()

print(array_data[1,2])