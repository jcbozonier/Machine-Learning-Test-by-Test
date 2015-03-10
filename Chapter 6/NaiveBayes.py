class Classifier:
  def __init__(self):
    self._classifications = {}
  def train(self, classification, observation):
    if not classification in self._classifications:
      self._classifications[classification] = []
    self._classifications[classification].append(observation)
  def classify(self, observation):
    if len(self._classifications.keys()) == 0:
      return None
    else:
      closest_class = self._classifications.keys()[0]
      closest_observation = abs(observation - self._classifications[closest_class][0])
      for the_class, trained_observations in self._classifications.items():
        if abs(observation - trained_observations[0]) < closest_observation:
          closest_class = the_class
          closest_observation = abs(observation - self._classifications[closest_class][0])
    return closest_class