import os
import shutil
import warnings
import urllib.request
import numpy as np
import gtrs.Utilities as Utilities

class SEISCAT():
    """
    A class to process seismic catalog from USGS website
    Attributes:
        header: header of file
        data_str: data in format of string, to preserve info
        data_float: data in format of float, to save actual data
    """
    def __init__(self):
        pass

    def ReadHeader(self, _filename):
        '''
        Read header information from file.
        An example of string is:
        'time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id'
        Args:
            _filename(str):
                filename for data file
        '''
        assert(os.access(_filename, os.R_OK))
        with open(_filename, 'r') as fin:
            _texts = fin.readlines()  # read the text of the file header
        self.header = Utilities.ReadHeader2(_texts, deli=',')
    
    def ReadData(self, _filename):
        '''
        Read Data
        Attributes:
            _filename(string):
                filename for data file
        '''
        assert(os.access(_filename, os.R_OK))  # read in data
        # import data via numpy buid in method
        # catch warning of empty file and return 1
        with warnings.catch_warnings(record=True) as w:
            self.data_str = np.genfromtxt(_filename, skip_header=1, delimiter=',', dtype=str)
            self.data_float = np.genfromtxt(_filename, skip_header=1, delimiter=',', dtype=float)
            if (len(w) > 0):
                assert(issubclass(w[-1].category, UserWarning))
                assert('Empty input file' in str(w[-1].message))
                warnings.warn('ReadData: %s, abort' % str(w[-1].message))
                return 1
        
        if len(self.data_str.shape) == 1:
            # only one row, expand it too 2-d array
            self.data_str = np.array([self.data_str])
            self.data_float = np.array([self.data_float])
        return 0


def url_to_usgs():
    '''
    generate a url to usgs
    Inputs:
    Return:
        url(str): url to usgs website
    '''
    data_site    = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv"
    text_query = "?starttime=1976-01-01%2000:00:00&endtime=2006-05-28%2023:59:59&latitude=-7.526469&longitude=112.711131&maxradiuskm=1500&minmagnitude=4.0&eventtype=earthquake&orderby=time"
    url = data_site + text_query
    return url


def download_from_url(url, ofile):
    '''
    download data from url
    Inputs:
        url(str): url to download from
        ofile(str): filename
    '''
    with urllib.request.urlopen(url) as response, open(ofile, 'wb') as fout:
        shutil.copyfileobj(response, fout)