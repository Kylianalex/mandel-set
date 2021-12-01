from kfractal.mandel import suite

def test_suite():
	assert suite(0.5, 0.5, 0.1, 0.1) == -1
	assert suite(1, 1, 1, 1) == 1
