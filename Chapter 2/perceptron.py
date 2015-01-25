class Perceptron:
  def __init__(self):
    self._result = None
  def train(self, training_data):
    weights = [0]
    for input_data, label in training_data:
      cross_product = weights[0] * input_data[0]
      error = label - cross_product
      weights[0] += error
    self._weights = weights
  def predict(self, input=None):
    if input is None:
      return None
    return self._weights[0]*input[0]