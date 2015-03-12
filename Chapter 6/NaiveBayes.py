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
  def classify(self, observation):
    if self._classification_a_label is None and self._classification_b_label is None:
      return None
    elif self._classification_b_label is None:
      return self._classification_a_label
    else:
      closest_class = self._classification_a_label
      closest_observation = abs(observation - self._classification_a[0])
      if abs(observation - self._classification_b[0]) < closest_observation:
        closest_class = self._classification_b_label
    return closest_class