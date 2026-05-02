import times 
from times import compute_overlap_time
from times import time_range



    
def test_given_input():
    

    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    
    result = compute_overlap_time(large,short)
    expected = [
    ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
    ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
]

    assert result == expected
    


def test_no_overlap():

    large = time_range("2010-02-12 10:00:00", "2010-02-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected=[]
    result= times.compute_overlap_time(large, short)
    assert expected==result



def test_boundaries():

    large = time_range("2010-02-12 10:00:00", "2010-02-12 12:00:00")
    short = time_range("2010-02-12 12:00:00", "2010-02-12 12:04:00", 2, 60)
    expected=[]
    result= times.compute_overlap_time(large, short)
    assert expected==result



def test_several_times_ranges():
    large = time_range("2010-02-12 10:00:00", "2010-02-12 12:00:00", 3, 300)
    short = time_range("2010-02-12 10:20:00", "2010-02-12 11:40:00", 2, 600)

    expected = [
    ("2010-02-12 10:20:00", "2010-02-12 10:36:40"),
    ("2010-02-12 10:41:40", "2010-02-12 10:55:00"),
    ("2010-02-12 11:05:00", "2010-02-12 11:18:20"),
    ("2010-02-12 11:23:20", "2010-02-12 11:40:00"),
    ]
    result= times.compute_overlap_time(large, short)
    assert expected==result




