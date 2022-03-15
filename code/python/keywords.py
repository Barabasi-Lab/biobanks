#!/usr/bin/env python3
"""
Produce a table of biobanks based on some keywords.

Creator: Rodrigo Dorantes Gilardi <rodgdor@gmail.com>
"""

import os
import os.path
import pandas as pd
from serendipity import read_chunks

# This is where the preliminary data is going to be stored
OUT = '../../data/raw/initial.csv'

if not os.path.isdir('../../headers'):
    raise Exception("You should have the MAG headers in '../../headers")

if not os.path.isdir('../../data'):
    raise Exception("Please have a ../../data directory.")

if not os.path.isdir('../../data/biobanks'):
    os.mkdir('../../data/biobanks')

keywords = {
    'cohort': ['cohort', 'baseline', ':'],
    'health_study': ['health study'],
    'biobank': ['biobank', ':'],
    'mega_biobank': ['mega biobank', ':'],
    'cohort_profile': ['^cohort profile:'],
    'epidemiological_study': ['epidemiological', 'study', ':'],
    'prospective': ['prospective' , 'study', 'rationale', ':'],
    'longitudinal': ['longitudinal', 'study', 'rationale', 'design', ':']}


tables = []
i = 0
for chunk in read_chunks('Papers.txt'):
    i += 1
    print(f"Processing the first {i} millions rows.")
    for kw in keywords:
        temp = []
        for k in keywords[kw]:
            chunk = chunk[chunk['OriginalTitle'].str.contains(k, case=False)]
        temp.append(chunk)
        temp = pd.concat(temp)
        temp['keyword'] = kw
        tables.append(temp)
tables = pd.concat(tables)


tables.to_csv(OUT, index=False)