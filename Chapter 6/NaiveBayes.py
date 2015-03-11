import numpy as np

class Classifier:
  def __init__(self):
    self._classifications = {}
  def train(self, classification, observation):
    if not classification in self._classifications:
      self._classifications[classification] = []
    self._classifications[classification].append(observation)
  def _probability_given_class(self, trained_observations, observation):
    variance = np.var(trained_observations)
    mean = np.mean(trained_observations)
    return 1/np.sqrt(2*np.pi*variance) * np.exp(-0.5*((observation - mean)**2)/variance)
  def _probability_of_class_given_observation(self, the_class, other_classes, p_of_observation_given_class):
    return p_of_observation_given_class[the_class]/(p_of_observation_given_class[the_class] + sum([p_of_observation_given_class[other_class] for other_class in other_classes]))
  def classify(self, observation):
    if len(self._classifications.keys()) == 0:
      return None
    else:
      classes = set(self._classifications.keys())
      highest_probability = 0
      best_class = self._classifications.keys()[0]
      probability_of_observation_given_class={}
      for the_class, trained_observations in self._classifications.items():
        if len(trained_observations) <= 1:
          return None
        probability_of_observation_given_class[the_class] = self._probability_given_class(trained_observations, observation)
      print probability_of_observation_given_class
      for the_class in probability_of_observation_given_class:
        candidate_probability = self._probability_of_class_given_observation(the_class, classes-set(the_class), probability_of_observation_given_class)
        candidate_class = the_class
        print candidate_probability
        if candidate_probability > highest_probability:
          highest_probability = candidate_probability
          best_class = candidate_class
    return best_class