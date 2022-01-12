import numpy as np
import random

def create_gaps(data,p,gap_length,gap_ocur):
    """
    Parameters
    ----------
    data : 1D array
        the data which the gaps are created in
    p : Integer
        the amount of gaps that must be created the amount still depends
        on the length and occurence of the gaps 
    gap_length : list
        a list with the start length and the end length of each gap
    gap_ocur : Integer
        how much space there must be between the gaps

    Returns
    -------
    data : 1D array
        returns the 1D array with nan for the gaps
    index_numbers : list
        list with the index numbers that got removed

    """
    #list to store the index numbers that get removed
    index_numbers = []

    #random indexes createad to remove
    indexes = sorted(random.sample(range(len(data)),len(data)//p),reverse=True)
    
    ##goes over every index to see if the next index complies with the space between the gaps
    for i in range(len(indexes)):
        for gap_width in range(len(indexes)):
            if (indexes[gap_width] - indexes[i] <gap_ocur) and (indexes[gap_width] - indexes[i] > 0) :
                indexes[i] = np.nan
            
    #once all indexes are selected the length of the gap gets determined 
    for i in indexes:
        if i != np.nan:
            x = np.arange(1,random.randrange(gap_length[0],gap_length[1]),1)
            #every index gets replaced with a nan
            for a in x:
                index_numbers.append(a+i)
                data[i+a] = np.nan
    print('Total deleted data: ' + str(len(data)-np.count_nonzero(~np.isnan(data))))
    return data , index_numbers
