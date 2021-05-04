import gtrs.Utilities as Utilities

test_dir = '.test'

def test_read_header2():
    """
    test ReadHeader2
    """
    texts = ['time,latitude,longitude,depth,mag,magType']
    header = Utilities.ReadHeader2(texts, deli=',')
    header_std = {
        'total_col': 6, 
        'time': {'col': 0, 'unit': None}, 
        'latitude': {'col': 1, 'unit': None}, 
        'longitude': {'col': 2, 'unit': None}, 
        'depth': {'col': 3, 'unit': None}, 
        'mag': {'col': 4, 'unit': None}, 
        'magType': {'col': 5, 'unit': None}
    }
    assert(header == header_std)