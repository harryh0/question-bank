
def max_distance_to_closest(seats):
    
    n = len(seats)
    last = -1
    max_dist = 0
    for i in range(n):
        if seats[i] == 1:
            if last == -1:
                max_dist = i
            else:
                max_dist = max(max_dist, (i - last) // 2)
            last = i
    max_dist = max(max_dist, n - last - 1)
    return max_dist


def test_max_distance_to_closest():
    assert max_distance_to_closest([1,0,0,0,1,0,1]) == 2
    assert max_distance_to_closest([1,0,0,0]) == 3
    assert max_distance_to_closest([0,1]) == 0
    assert max_distance_to_closest([1,0,0,0,1,0,0,0,1]) == 2