#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reads in the JSON files retrieved from the Guardian API which queries the
webpage.

Converts these JSON files - there is one for each day over the time period
concerned - turns it in a pandas dataframe and saves output as csv.

Then dataframe saved in full unprocessed form.

@author: TGreen
"""

import pandas as pd
from glob import glob

year = '2019'

filenames = glob(f'/home/tim/Documents/DataProjects/Guardian/guardiannews/data/raw/{year}/*.json')

# #fpath = '/DataProjects/Guardian/guardiannews/data/raw/20'

#datatypes = {'id':str, 'type':str, 'sectionId':str, 'sectionName':str, 'webPublicationDate':datetime,
       # 'webTitle':str, 'webUrl':str, 'apiUrl':'S10', 'fields':dict, 'isHosted':bool, 'pillarId':str,
       # 'pillarName':str}
df = pd.concat([pd.read_json(f) for f in filenames], ignore_index=True)

# # Expands the fields dictionary into cols
df = df.join(pd.json_normalize(df.fields))
df = df.drop('fields', axis = 1)

df.to_csv(f'/home/tim/Documents/DataProjects/Guardian/guardiannews/data/interim/full_dataframe_{year}.csv')
