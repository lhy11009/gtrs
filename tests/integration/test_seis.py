import os
import filecmp
import gtrs.Seis as Seis

test_dir = '.test'
test_source_dir = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_download_from_url():
    """
    test download_from_url
    """
    # test 1
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=2006-05-27%2000:00:00&endtime=2006-05-28%2023:59:59&latitude=-7.526469&longitude=112.711131&maxradiuskm=1500&minmagnitude=4.0&eventtype=earthquake&orderby=time"
    ofile = os.path.join(test_dir, 'download_from_url_output.txt')
    ofile_std = os.path.join(test_source_dir, 'download_from_url_output_std.txt')
    # remove older file
    if os.path.isfile(ofile):
        os.remove(ofile)
    Seis.download_from_url(url, ofile)
    # assert file exists
    assert(os.path.isfile(ofile))
    # assert file content
    assert(filecmp.cmp(ofile_std, ofile))


def test_seiscat():
    """
    test class SEISCAT
    """

    # test 1
    # download file
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=1976-05-27%2000:00:00&endtime=2006-05-28%2023:59:59&latitude=-7.526469&longitude=112.711131&maxradiuskm=1500&minmagnitude=4.0&eventtype=earthquake&orderby=time"
    datfile = os.path.join(test_dir, 'download_from_url_output.txt')
    # remove older file
    if os.path.isfile(datfile):
        os.remove(datfile)
    Seis.download_from_url(url, datfile)
    assert(os.access(datfile, os.R_OK))
    # initiate a class
    Seiscat = Seis.SEISCAT()
    # read file
    Seiscat.ReadHeader(datfile)
    # plot epicenters in Solomon aera
    ofile = os.path.join(test_dir, 'seiscat_plot.png')
    if os.path.isfile(ofile):
        os.remove(ofile)
    Seiscat.Plot(ofile, lusi_lat=-7.526469, lusi_lon=112.711131)
    assert(os.path.isfile(ofile))