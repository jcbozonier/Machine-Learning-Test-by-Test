import nose.tools as nt

def the_easy_test():
  nt.assert_true(True)

from perceptron import *

def no_training_data_supplied_test():
  the_perceptron = Perceptron()
  result = the_perceptron.predict([])
  nt.assert_equal(result, None, 'Should have no result with no training data.')

def train_an_OR_function_test():
  the_perceptron = Perceptron()
  the_perceptron.train([
                           [1,1], 
                           [0,1], 
                           [1,0], 
                           [0,0]
                         ], 
                         [1,1,1,0])
  nt.assert_equal(the_perceptron.predict([1,1]), 1)
  nt.assert_equal(the_perceptron.predict([1,0]), 1)
  nt.assert_equal(the_perceptron.predict([0,1]), 1)
  nt.assert_equal(the_perceptron.predict([0,0]), 0)


def detect_values_greater_than_five_test():
  the_perceptron = Perceptron()
  the_perceptron.train([
                           [ 5], 
                           [ 2], 
                           [ 0],
                           [-2], 
                         ], 
                         [1,0,0,0])
  nt.assert_equal(the_perceptron.predict([ 8]),    1)
  nt.assert_equal(the_perceptron.predict([ 5]),    1)
  nt.assert_equal(the_perceptron.predict([ 2]),    0)
  nt.assert_equal(the_perceptron.predict([ 0]),    0)
  nt.assert_equal(the_perceptron.predict([-2]),    0)
