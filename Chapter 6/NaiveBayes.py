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
  def _probability_of_each_class_given_data(self, observation, class_a_data, class_b_data):
    p_class_a = len(class_a_data)/(1.0*(len(class_a_data) + len(class_b_data)))
    p_class_b = len(class_b_data)/(1.0*(len(class_a_data) + len(class_b_data)))
    sum_of_probabilities = self.probability_of_data_given_class(observation, class_a_data) * p_class_a \
                           + self.probability_of_data_given_class(observation, class_b_data)*p_class_b 
    class_a_probability = self.probability_of_data_given_class(observation, class_a_data)*p_class_a \
                          / sum_of_probabilities
    class_b_probability = self.probability_of_data_given_class(observation, class_b_data)*p_class_b \
                          / sum_of_probabilities
    return (class_a_probability, class_b_probability)
  def classify(self, observation):
    if self._classification_a_label is None and self._classification_b_label is None:
      return None
    elif self._classification_b_label is None:
      return self._classification_a_label
    elif len(self._classification_a) <= 1 or len(self._classification_b) <= 1:
      return None
    else:
      closest_class = self._classification_a_label
      p_of_A_given_data, p_of_B_given_data = self._probability_of_each_class_given_data(observation, self._classification_a, self._classification_b)
      if p_of_A_given_data > p_of_B_given_data:
        return self._classification_a_label
      else:
        return self._classification_b_label