import shutil
import urllib.request


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