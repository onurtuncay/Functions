## Basic Flatten Function

import numpy as np
a = np.matrix('2,3,4;5,6,7;8,9,10')

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


print('Original List', a)
print('Flattened List', flatten_list(a.tolist()))
