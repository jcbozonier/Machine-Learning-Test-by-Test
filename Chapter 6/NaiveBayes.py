import numpy as np

class Classifier:
  def __init__(self):
    self._classification_a_label = None
    self._classification_a = None
    self._classification_b_label = None
    self._classification_b = None
  def train(self, classification, observation):
    if classification == self._classification_a_label:
      self._classification_a.append(observation)
    elif classification == self._classification_b_label:
      self._classification_b.append(observation)
    elif self._classification_a is None:
      self._classification_a_label = classification
      self._classification_a = [observation]
    elif self._classification_b is None:
      self._classification_b_label = classification
      self._classification_b = [observation]
  def probability_of_data_given_class(self, observation, class_observations):
    mean = np.mean(class_observations)
    variance = np.var(class_observations)
    p_data_given_class = 1/np.sqrt(2*np.pi*variance)*np.exp(-0.5*((observation - mean)**2)/variance)
    return p_data_given_class
  def classify(self, observation):
    if self._classification_a_label is None and self._classification_b_label is None:
      return None
    elif self._classification_b_label is None:
      return self._classification_a_label
    elif len(self._classification_a) == 1 or len(self._classification_b) == 1:
      return None
    else:
      closest_class = self._classification_a_label
      sum_of_probabilities = self.probability_of_data_given_class(observation, self._classification_a) +\
                             self.probability_of_data_given_class(observation, self._classification_b) 
      closest_observation = self.probability_of_data_given_class(observation, self._classification_a)/sum_of_probabilities
      if self.probability_of_data_given_class(observation, self._classification_b)/sum_of_probabilities > closest_observation:
        closest_class = self._classification_b_label
    return closest_class