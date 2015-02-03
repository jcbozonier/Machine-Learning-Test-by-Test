import perceptron, numpy

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

def when_used_on_a_linearly_seperable_dataset_test():
  # Given a perceptron trained on a linearly seperable dataset
  number_correct = 0
  simulations_to_run = 100
  datapoints_per_sim = 100
  for i in range(simulations_to_run):
    x = numpy.random.uniform(0,10,size=datapoints_per_sim)
    y = .75*x + 5.0*numpy.random.normal(loc=0.0, scale=2.0, size=datapoints_per_sim)
    classification = map(lambda t: 1 if t[1] > .75*t[0] else 0, zip(x,y)) 
    training_dataset = zip(zip(x,y),classification)
    the_perceptron = perceptron.Perceptron(max_iterations=200, bias=0.5, training_rate=.001) #, training_rate=.01
    the_perceptron.train(training_dataset)

    # When predicting
    test_results = [(the_perceptron.predict(i[0]), i[1]) for i in training_dataset]
    number_correct += len(filter(lambda x: x[0]==x[1], test_results))
  print number_correct/(1.0*simulations_to_run*datapoints_per_sim)
  assert number_correct/(1.0*simulations_to_run*datapoints_per_sim) >= 0.8, "Then it should have much better than random performance."


def when_trained_on_test_dataset_and_then_cross_validated_test():
  # Given a perceptron trained on a linearly seperable dataset
  number_correct = 0
  simulations_to_run = 100
  datapoints_per_sim = 100
  for i in range(simulations_to_run):
    test_x = numpy.random.uniform(0,10,size=datapoints_per_sim)
    test_y = .75*test_x + 5.0*numpy.random.normal(loc=0.0, scale=2.0, size=datapoints_per_sim)
    test_classification = map(lambda t: 1 if t[1] > .75*t[0] else 0, zip(test_x,test_y))

    training_dataset = zip(zip(test_x,test_y),test_classification)
    the_perceptron = perceptron.Perceptron(max_iterations=150, bias=0.5, training_rate=.001) #, training_rate=.01
    the_perceptron.train(training_dataset)

    # When predicting
    cv_x = numpy.random.uniform(0,10,size=datapoints_per_sim)
    cv_y = .75*cv_x + 5.0*numpy.random.normal(loc=0.0, scale=2.0, size=datapoints_per_sim)
    cv_classification = map(lambda t: 1 if t[1] > .75*t[0] else 0, zip(cv_x,cv_y))
    cv_dataset = zip(zip(cv_x,cv_y),cv_classification)

    test_results = [(the_perceptron.predict(i[0]), i[1]) for i in cv_dataset]
    number_correct += len(filter(lambda x: x[0]==x[1], test_results))
  print number_correct/(1.0*simulations_to_run*datapoints_per_sim)
  assert number_correct/(1.0*simulations_to_run*datapoints_per_sim) >= 0.75, "Then it should have much better than random performance."
