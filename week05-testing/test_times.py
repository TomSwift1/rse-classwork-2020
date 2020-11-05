from times import time_range, compute_overlap_time

def test_general_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected
    
def test_non_overlapping_input():
    large = time_range("2019-01-10 10:00:00", "2019-01-10 11:00:00")
    short = time_range("2019-01-10 11:20:00", "2019-01-10 11:30:00")
    result = compute_overlap_time(large, short)
    expected =[]
    assert result == expected
    
def test_mult_intervals_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00",2,60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 11:35:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected =[('2010-01-12 10:30:00', '2010-01-12 11:02:00'),
     ('2010-01-12 11:03:00', '2010-01-12 11:29:30'),
     ('2010-01-12 11:30:30', '2010-01-12 11:35:00')]
    assert result == expected
    
def test_start_end_same_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00")
    short = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 13:00:00', '2010-01-12 13:00:00')]
    assert result == expected