from mlproject.distance import haversine


def test_type_of_haversine():
    assert type(haversine(48.865,2.380,48.235,2.393)) == float
    assert haversine(48.865, 2.380, 48.235, 2.393) >= 0
