import times as times
from times import compute_overlap_time
# Example test case for compute_overlap_time function
import datetime as datetime
def test_given_input():
    result = compute_overlap_time([("2021-05-01 09:00:00", "2021-05-01 10:00:00")],
                                  [("2021-05-01 09:30:00", "2021-05-01 10:30:00")]) 
    expected = [("2021-05-01 09:30:00", "2021-05-01 10:00:00")] 
    assert result == expected
def test_no_overlap():
    result = compute_overlap_time([("2021-05-01 09:00:00", "2021-05-01 10:00:00")],
                                  [("2021-05-01 10:30:00", "2021-05-01 11:30:00")]) 
    expected = [] 
    assert result == expected
def test_full_overlap():
    result = compute_overlap_time([("2021-05-01 09:00:00", "2021-05-01 11:00:00")],
                                  [("2021-05-01 09:30:00", "2021-05-01 10:30:00")]) 
    expected = [("2021-05-01 09:30:00", "2021-05-01 10:30:00")] 
    assert result == expected
    
# how do I run pytest on this direct§ly?
# Save this code in a file named test_times.py and run the following command in the terminal
# pytest test_times.py
#t
# It says there is an assertion error, but I don't see why
# I will add print statements to debug
def test_debug_given_input():
    result = compute_overlap_time([("2021-05-01 09:00:00", "2021-05-01 10:00:00")],
                                  [("2021-05-01 09:30:00", "2021-05-01 10:30:00")]) 
    expected = [("2021-05-01 09:30:00", "2021-05-01 10:00:00")] 
    print("Result:", result)
    print("Expected:", expected)
    assert result == expected
# I see the problem, the compute_overlap_time function is returning invalid overlaps
# I will fix the compute_overlap_time function in times.py  


