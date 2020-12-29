import gtrs.Seis as Seis

test_dir = '.test'

def test_url_to_usgs():
    """
    test url_to_usgs
    """
    # test 1
    url = Seis.url_to_usgs()
    url_std = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=1976-01-01%2000:00:00&endtime=2006-05-28%2023:59:59&latitude=-7.526469&longitude=112.711131&maxradiuskm=1500&minmagnitude=4.0&eventtype=earthquake&orderby=time"
    assert(url == url_std)
