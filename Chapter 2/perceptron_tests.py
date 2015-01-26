import perceptron

def no_training_data_supplied_test():
  the_perceptron = perceptron.Perceptron()
  result = the_perceptron.predict()
  assert result is None, 'Should have no result with no training data.'

def simplest_training_set_and_prediction_test():
  the_perceptron = perceptron.Perceptron()
  the_perceptron.train([([0], 0)])
  result = the_perceptron.predict([0])
  assert result == 0.0, 'Should return the only result it learned.'

def predict_what_weve_seen_in_the_past_test():
  the_perceptron = perceptron.Perceptron()
  the_perceptron.train([([0], 0),([1], 1)])
  result = the_perceptron.predict([0])
  assert result == 0

  result = the_perceptron.predict([1])
  assert result == 1

def seperate_one_dimensional_data_that_generalizes_to_unseen_data_test():
  the_perceptron = perceptron.Perceptron()
  the_perceptron.train([([-2], 0),([1], 1),([-1], 0),([2], 1)])
  print the_perceptron._weights

  result = the_perceptron.predict([-3])
  assert not result, "-3 didn't get classified correctly"

  result = the_perceptron.predict([1])
  assert result, "1 didn't get classified correctly"

  result = the_perceptron.predict([3])
  assert result, "3 didn't get classified correctly"

def learn_AND_with_zero_as_activation_test():
  the_perceptron = perceptron.Perceptron()
  the_perceptron.train([([1,-1], 0), ([1,1], 1), ([-1,1], 0), ([-1,-1], 0)])
  result = the_perceptron.predict([-1,1])
  assert not result, "should be false"
  result = the_perceptron.predict([1,1])
  assert result, "should be true"

def learn_NAND_with_zero_as_activation_test():
  the_perceptron = perceptron.Perceptron()
  the_perceptron.train([([1,-1], 1), ([1,1], 0), ([-1,1], 1), ([-1,-1], 1)])
  result = the_perceptron.predict([-1,1])
  assert result, "should be true"
  result = the_perceptron.predict([1,1])
  assert not result, "should be false"

def learn_AND_with_one_half_as_bias_test():
  the_perceptron = perceptron.Perceptron(bias=0.5)
  the_perceptron.train([([1,0], 0), ([1,1], 1), ([0,1], 0), ([0,0], 0)])

  result = the_perceptron.predict([0,1])
  assert not result, "should be false"

  result = the_perceptron.predict([1,1])
  assert result, "should be true"

  result = the_perceptron.predict([0,0])
  assert not result, "should be false"

  result = the_perceptron.predict([1,0])
  assert not result, "should be false"

def learn_AND_with_big_training_rate_test():
  the_perceptron = perceptron.Perceptron(training_rate=10)
  the_perceptron.train([([1,0], 0), ([1,1], 1), ([0,1], 0), ([0,0], 0)])

  result = the_perceptron.predict([0,1])
  assert not result, "should not predict correctly"


def enable_configuring_number_of_iterations_test():
  the_perceptron = perceptron.Perceptron(bias=0.5, max_iterations=1)
  the_perceptron.train([([1,0], 0), ([1,1], 1), ([0,1], 0), ([0,0], 0)])
  result = the_perceptron.predict([1,1])
  assert not result, "should be misclassified"