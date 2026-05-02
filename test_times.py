import times 
from times import compute_overlap_time
from times import time_range


import yaml

     
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






def test_from_yaml():
    with open("fixture.yaml", "r") as file:
        test_cases = yaml.safe_load(file)

    for case in test_cases:
        name = list(case.keys())[0]
        data = case[name]

        result = compute_overlap_time(
            data["time_range_1"],
            data["time_range_2"],
        )

        expected = [tuple(interval) for interval in data["expected"]]

        assert result == expected


url ="https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/56/0/0/5/50&apiKey={VJR5AF-GDAKJ5-DFZ7EG-5QEA}"


def iss_passes():
    fake_response = {
    "status_code": 200,
    "json": lambda: {
        "large": [("2010-02-12 10:00:00", "2010-02-12 12:00:00")],
        "short": [("2010-02-12 10:30:00", "2010-02-12 10:45:00")],
        "expected": [("2010-02-12 10:30:00", "2010-02-12 10:45:00")],
    },
    }
    with path("times.get_response") as mock_get:
        mock_get.return_value.json.return_value = fake_response
        result = get_response()

        assert result== fake_response

    mock_get.assert_called_once_with(url)



url ="https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/56/0/0/5/50&apiKey={VJR5AF-GDAKJ5-DFZ7EG-5QEA}"


def iss_passes():
    fake_response = {
    "status_code": 200,
    "json": lambda: {
        "large": [("2010-02-12 10:00:00", "2010-02-12 12:00:00")],
        "short": [("2010-02-12 10:30:00", "2010-02-12 10:45:00")],
        "expected": [("2010-02-12 10:30:00", "2010-02-12 10:45:00")],
    },
    }
    with patch("times.get_response") as mock_get:
        mock_get.return_value.json.return_value = fake_response
        result = get_response()

        assert result== fake_response

    mock_get.assert_called_once_with(url)



from unittest.mock import patch


url ="https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/56/0/0/5/50&apiKey={VJR5AF-GDAKJ5-DFZ7EG-5QEA}"


def test_iss_passes():
    fake_response = {
    "status_code": 200,
    "json": lambda: {
        "large": [("2010-02-12 10:00:00", "2010-02-12 12:00:00")],
        "short": [("2010-02-12 10:30:00", "2010-02-12 10:45:00")],
        "expected": [("2010-02-12 10:30:00", "2010-02-12 10:45:00")],
    },
    }
    with patch("times.get_response") as mock_get:
        mock_get.return_value.json.return_value = fake_response
        result = get_response()

        assert result== fake_response

    mock_get.assert_called_once_with(url)
