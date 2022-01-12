from missingpy import MissForest
import pandas as pd
import numpy as np

data = pd.read_csv('med_hum_data.txt' , header=None)
clean_data = pd.read_csv('cleanKNMIdata.txt')
npdata = np.array(data)
clean_hum = clean_data['Relative atmospheric humidity']
newdata = npdata.reshape(-1,1)
imputer = MissForest()
X = newdata
X_imputed = imputer.fit_transform(X)
