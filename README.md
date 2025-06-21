# 🛠️ Functions Repository

This repository is intended to serve as a collection of reusable Python functions.

The goal is to organize, document, and store small utility functions that can be used across different projects or scripts. Each function will be maintained in its own file with example usage and explanations where necessary.

Documentation will be updated progressively as functions are added.

---

## 🔹 flatten_list(): Flatten a 2D List

The `flatten_list()` function, located in the `Flatten.py` file, takes a two-dimensional Python list (e.g. list of lists) and returns a one-dimensional, flat list.

It is useful for flattening data structures where elements may be nested inconsistently, and it operates safely without relying on external libraries.

### 📁 File: `Flatten.py`

```python
def flatten_list(_2d_list):
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list
```

### 🧪 Example Usage

import numpy as np
from Flatten import flatten_list

a = np.matrix('2,3,4;5,6,7;8,9,10')

flattened = flatten_list(a.tolist())

print("Original List:", a)

print("Flattened List:", flattened)

### ✅ Output

Original List: [[ 2  3  4]
                [ 5  6  7]
                [ 8  9 10]]

Flattened List: [2, 3, 4, 5, 6, 7, 8, 9, 10]

