class Perceptron:
  def __init__(self):
    self._result = None
  def train(self, training_data):
    self._weights = len(training_data[0][0])*[0]
    for i in range(100000):
      for input_data, label in training_data:
        cross_product = sum(weight_i * input_i for weight_i, input_i in zip(self._weights, input_data))
        error = label - cross_product
        for index, input_i in enumerate(input_data):
          self._weights[index] += .1 * error * input_i
  def predict(self, input=None):
    if input is None:
      return None
    return sum([weight_i * input_i for weight_i, input_i in zip(self._weights, input)]) > 0