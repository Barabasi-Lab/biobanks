from genericpath import isdir
#! usr/bin/env python3
"""Fetch the last version of the manually curated list of biobanks.

creator: Rodrigo Dorantes Gilardi (rodgdor@gmail.com)
"""

import os.path
import pandas as pd
import gspread as gc

OUT = '../data/biobanks.csv'

if not os.path.isdir('../data'):
    raise Exception("You should have a ../data directory.")


sheet_id = "1uAdz6b5EbjXevMQAKBKDkvOH6YtdUyMjl20_maOroSo"
url = (f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit#gid=0")
csv = url.replace('/edit#gid=', '/export?format=csv&gid=')

table = pd.read_csv(csv)

table.to_csv(OUT, index=False)