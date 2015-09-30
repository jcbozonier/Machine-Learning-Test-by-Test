import nose.tools as nt

def the_easy_test():
  nt.assert_true(True)

from perceptron import *

def no_training_data_supplied_test():
  the_perceptron = Perceptron()
  result = the_perceptron.predict()
  nt.assert_equal(result, None, 'Should have no result with no training data.')
