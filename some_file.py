test = 'A test variable on b'
test2 = 'Another test variable'

additional_line_or_change = 'a new var to merge into master'

def feature_b():
	test3 = '{} {}'.format(test, test2)
	return test3

test3 = feature_b

