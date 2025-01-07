
def max_distance_to_closest(seats):
    pass

def test_max_distance_to_closest():
    assert max_distance_to_closest([1,0,0,0,1,0,1]) == 2
    assert max_distance_to_closest([1,0,0,0]) == 3
    assert max_distance_to_closest([0,1]) == 0
    assert max_distance_to_closest([1,0,0,0,1,0,0,0,1]) == 2