"""Dask functions

This module provide helper functions to work with Dask
"""
import dask.dataframe as dd


def read(filePath):
    """Creates Dask dataframe from CSV file

    Keyword arguments:
    filePath -- the path to the CSV file

    Return:
    return -- Dask dataframe
    """
    daskDf = dd.read_csv(filePath)
    return daskDf


def count(daskDf):
    """Counts number of rows in Dask dataframe

    Keyword arguments:
    daskDf -- Dask dataframe

    Return:
    return -- Number of rows
    """
    return daskDf.index.size.compute()


def distinct_count(daskDf, columnName):
    """Counts distint number of values in Dask dataframe

    Keyword arguments:
    daskDf -- Dask dataframe
    columnName -- Column name

    Return:
    return -- Distinct number of values
    """
    return daskDf[columnName].drop_duplicates().size
