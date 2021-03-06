## Functions to clean datasets.
# ------------------------------

import pandas as pd


def droping_columns(data, lst):
    ''' 
    Function to drop columns from a dataset.
    input = dataframe, list of columns names
    output = draframe 
    '''
    new_data = data.drop(lst, axis=1)
    return new_data

def droping_rows(data, lst):
    ''' 
    Function to drop columns from a dataset.
    input = dataframe, list of columns names
    output = draframe 
    '''
    new_data = data.drop(lst, axis=0)
    return new_data


def sort_by_elements(data, serie, lst):
    ''' 
    Function to sort a dataframe by specific values.
    input = serie, list of values
    output = dataframe
    '''
    new_data = data[serie.isin(lst)]
    return new_data


def new_index(data):
    ''' 
    Function that resets the index of a dataframe.
    input = dataframe
    output = dataframe
    '''
    new_data = data.reset_index(drop=True)
    return new_data


def re_label(data, dictionary):
    '''
    Function that re-label a column based on a dictionary's keys and values.
    input = dataframe, dictionary
    output = dataframe
    '''
    for k,v in dictionary.items():
        data = data.replace(k,v)
    return data



def rename_columns(data, dic):
    ''' 
    Function to rename columns
    input = dataframe, dictionary where the keys equals the old name and the values equals the new name
    ouput = dataframe
    '''
    data_back_up = data.copy()
    data = data.rename(columns=dic)
    return data


def order(data, lst):
    '''
    Function that changes the order of the series within a dataframe.
    input = dataframe
    output = dataframe
    '''
    data_back_up = data.copy()
    data = data[lst]
    return data


def concating_by_column(lst):
    '''
    Function that concatenates multiples dataframes.
    input = list of dataframes
    output = final dataframe
    '''
    new_data = pd.concat(lst, axis=1)
    return new_data

def concating_by_row(lst):
    '''
    Function that concatenates multiples dataframes.
    input = list of dataframes
    output = final dataframe
    '''
    new_data = pd.concat(lst, axis=0)
    return new_data








































