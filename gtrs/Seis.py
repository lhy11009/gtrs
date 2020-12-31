import os
import shutil
import warnings
import urllib.request
import numpy as np
import cartopy.crs as ccrs
import gtrs.Utilities as Utilities
from matplotlib import pyplot as plt

class SEISCAT():
    """
    A class to process seismic catalog from USGS website
    Attributes:
        header: header of file
        data_str: data in format of string, to preserve info
        data_float: data in format of float, to save actual data
    """
    def __init__(self):
        self.header = []
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
        # create self.format
        self.GenerateFormat()
        self.datfile = _filename

    def GenerateFormat(self):
        """
        Generate a format array to formatting data
        Return:
            format of data
        """
        _str = ['time', 'magType', 'net', 'id', 'updated', 'place', 'type',\
                'status', 'locationSource', 'magSource']
        _float = ['latitude', 'longitude', 'depth', 'mag', 'nst', 'gap',\
                   'dmin', 'rms', 'depthError', 'horizontalError', 'magError',\
                   'magNst']
        _format = [float for i in range(self.header['total_col'])]
        for key, value in self.header.items():
            if type(value) is not dict:
                continue
            if key in _str:
                _format[value['col']] = "|S10"
        # add self.format
        self.format = _format
        pass
    
    def ReadData(self, cols):
        '''
        Read Data
        Attributes:
            _filename(string):
                filename for data file
        '''
        # check self.datfile
        Utilities.my_assert(self.datfile != '', AssertionError, "ReadData: Call read header first")
        assert(os.access(self.datfile, os.R_OK))  # read in data

        # if header is vacant, read header first
        if self.header == []:
            self.ReadHeader(_filename)

        # _format = self.GenerateFormat()
        _format = [self.format[col] for col in cols]
       
        # import data via numpy buid in method
        # catch warning of empty file and return 1
        with warnings.catch_warnings(record=True) as w:
            data = np.genfromtxt(self.datfile, skip_header=1, delimiter=',', dtype=_format, usecols=cols)
            if (len(w) > 0):
                assert(issubclass(w[-1].category, UserWarning))
                assert('Empty input file' in str(w[-1].message))
                warnings.warn('ReadData: %s, abort' % str(w[-1].message))
                return 1
        
        if len(data.shape) == 1:
            # only one row, expand it too 2-d array
            data = np.array([data])
        return data
    
    def Plot(self, ofile, **kwargs):
        """
        inputs:
            ofile(str): output filename
            kwargs(dict):
                'lusi_lon': longitude
                'lusi_lat': latitude
        """
        plt.figure()
        ax = plt.axes(projection=ccrs.PlateCarree())
        # plot earthquake epicenters
        col_lat = self.header['latitude']['col']
        col_lon = self.header['longitude']['col']
        data = self.ReadData((col_lat, col_lon))
        eq_lat = data['f0']
        eq_lon = data['f1']
        plt.scatter(eq_lon,eq_lat,marker='.',transform=ccrs.PlateCarree())
        # plot central point
        lusi_lon = kwargs.get('lusi_lon', 0.0)
        lusi_lat = kwargs.get('lusi_lat', 0.0)
        plt.plot(lusi_lon,lusi_lat,'r^',transform=ccrs.PlateCarree())
        ax.coastlines(resolution='50m', color='black', linewidth=1)
        plt.savefig(ofile)


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