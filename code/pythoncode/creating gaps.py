import pandas as pd
from gaps import create_gaps
import numpy as np


data = pd.read_csv("cleanKNMIdata.txt",header=0)
print(list(data.columns))


"""
outdoor temp
solar radiation
humidity
"""
temp = data['Temperature']
rad = data['Global Radiation']
hum = data['Relative atmospheric humidity']

temp2 = data['Temperature']
rad2 = data['Global Radiation']
hum2 = data['Relative atmospheric humidity']

temp3 = data['Temperature']
rad3 = data['Global Radiation']
hum3 = data['Relative atmospheric humidity']
"""
small_temp_data , index = create_gaps(temp,4,[1,3],200)

small_rad_data , index = create_gaps(rad,4,[1,3],200)

small_hum_data , index = create_gaps(hum,4,[1,3],200)
np.savetxt("small_temp_data.txt", small_temp_data, delimiter=",", fmt='%s')
np.savetxt("small_rad_data.txt", small_rad_data, delimiter=",", fmt='%s')
np.savetxt("small_hum_data.txt", small_hum_data, delimiter=",", fmt='%s')

med_temp_data , index = create_gaps(temp2,4,[6,12],400)

med_rad_data , index = create_gaps(rad2,4,[6,12],400)

med_hum_data , index = create_gaps(hum2,4,[6,12],400)
np.savetxt("med_temp_data.txt", med_temp_data, delimiter=",", fmt='%s')
np.savetxt("med_rad_data.txt", med_rad_data, delimiter=",", fmt='%s')
np.savetxt("med_hum_data.txt", med_hum_data, delimiter=",", fmt='%s')

"""
large_temp_data , index = create_gaps(temp3,4,[24,72],1200)

large_rad_data , index = create_gaps(rad3,4,[24,72],1200)

large_hum_data , index = create_gaps(hum3,4,[24,72],1200)

np.savetxt("large_temp_data.txt", large_temp_data, delimiter=",", fmt='%s')
np.savetxt("large_rad_data.txt", large_rad_data, delimiter=",", fmt='%s')
np.savetxt("large_hum_data.txt", large_hum_data, delimiter=",", fmt='%s')
