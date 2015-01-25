class Perceptron:
  def __init__(self):
    self._result = None
    self._weights = [0]
  def train(self, training_data):
    for i in range(100000):
      for input_data, label in training_data:
        cross_product = self._weights[0] * input_data[0]
        error = label - cross_product
        self._weights[0] += .1 * error * input_data[0]
  def predict(self, input=None):
    if input is None:
      return None
    return self._weights[0]*input[0] > 0