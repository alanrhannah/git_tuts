test = 'A test variable on b'
test2 = 'Another test variable'

additional_line_or_change = 'a new var to merge into master'

def feature_b():
	test3 = '{} {}'.format(test, test2)
	return test3

test3 = feature_b

some_new_var_that_i_want = 'this is good'

git_reset = True

foo = 'Oh, I should have added something else to that last commit, this!'