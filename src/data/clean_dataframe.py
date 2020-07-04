
"""
Opens, and cleans the raw dataframe file, removing unneccessary fields and
sets the datatypes.

@author: tim
"""

import pandas as pd
from pathlib import Path

filename = Path.cwd().parent.parent.joinpath('data',
                                             'interim',
                                             'full_dataframe_2017_2020.csv')

def open_csvfile(filename):
    if filename.exists():
        print(f'\nOpening file {filename} ...\n')
        df = pd.read_csv(filename)
        print(f'\nFile opened.\n')
    else:
        raise NameError(f'Could not find file "{filename}".')
    return df


df = open_csvfile(filename)

def trim_df(dataframe, columns_keep):
    '''
    Take a large dataframe and return the columns given in the list
    provided.


    Parameters
    ----------
    dataframe : dataframe
        The dataframe to be reduced in size
    columns_keep : list
        List of column names to be kept in dataframe

    Returns
    -------
    dataframe of columns specified

    '''
    print(f'\nTrimming dataframe..')
    return dataframe[columns_keep]


col_keep = ['type', 'sectionName', 'webPublicationDate', 'webTitle',
            'pillarName', 'headline', 'byline', 'webUrl', 'bodyText',
            'wordcount', 'publication', 'charCount', 'productionOffice']

df = trim_df(df, col_keep)

def change_datatypes(dataframe, datatypes):
    """
    Change the datatypes in a dataframe and check the number of null values
    before and after and flag any inconsistancy.

    Parameters
    ----------
    dataframe : dataframe
        Dataframe to be acted on.
    datatypes : dict
        Dictionary of datatypes and associated columns.

    Returns
    -------
    Dataframe with changed datatypes.

    """
    print('\nChanging data types..')
    pre_nans = dataframe.isnull().sum()
    dataframe = dataframe.astype(datatypes)
    if dataframe.isnull().sum().equals(pre_nans):
        pass
    else:
        print('The number of nan values has increased, check data type conversion')
    print('Changing data types complete.\n')
    return dataframe



datatypes = {'charCount': 'int32',
             'wordcount': 'int32',
             'productionOffice': 'category',
             'pillarName': 'category',
             'type': 'category',
             'publication': 'category',
             'sectionName': 'category'}

df = change_datatypes(df, datatypes)

df['webPublicationDate'] = pd.to_datetime(df['webPublicationDate'])

save_filename = Path.cwd().parent.parent.joinpath('data',
                                                  'interim',
                                                 'cleaned_2017_2020.csv')
print(f'\nSaving file: {save_filename} ...')
df.to_csv(save_filename)
print(f'Saving file complete.\n')
