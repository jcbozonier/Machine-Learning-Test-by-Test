import NaiveBayes

def no_observations_test():
  classifier = NaiveBayes.Classifier()
  classification = classifier.classify(observation=23.2)
  assert classification is None, "Should not classify observations without training examples."

def given_an_observation_for_a_single_class_test():
  classifier = NaiveBayes.Classifier()
  classifier.train(classification='a class', observation=0)
  classification = classifier.classify(observation=23.2)
  assert classification == 'a class', "Should always classify as given class if there is only one."

def given_one_observation_for_two_classes_test():
  classifier = NaiveBayes.Classifier()
  classifier.train(classification='a class', observation=0)
  classifier.train(classification='b class', observation=100)
  classification = classifier.classify(observation=23.2)
  assert classification == 'a class', "Should classify as the nearest class."
  classification = classifier.classify(observation=73.2)
  assert classification == 'b class', "Should classify as the nearest class."

def given_multiple_observations_for_two_classes_test():
  classifier = NaiveBayes.Classifier()
  classifier.train(classification='a class', observation=0.0)
  classifier.train(classification='a class', observation=1.0)
  classifier.train(classification='a class', observation=0.5)
  classifier.train(classification='b class', observation=50)
  classifier.train(classification='b class', observation=15)
  classifier.train(classification='b class', observation=100)
  classification = classifier.classify(observation=23.2)
  assert classification == 'b class', "Should classify as the best fit class."
  classification = classifier.classify(observation=2.0)
  assert classification == 'a class', "Should classify as the best fit class."
