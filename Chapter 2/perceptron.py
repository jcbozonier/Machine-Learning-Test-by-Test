class Perceptron:
  def __init__(self, bias=0, training_rate=0.1):
    self._result = None
    self._bias = bias
    self._training_rate = training_rate
  def train(self, training_data):
    self._weights = len(training_data[0][0])*[0]
    labels = []
    for i in range(10000):
      for input_data, label in training_data:
        cross_product = sum(weight_i * input_i for weight_i, input_i in zip(self._weights, input_data))
        error = label - cross_product
        for index, input_i in enumerate(input_data):
          self._weights[index] += self._training_rate * error * input_i
  def predict(self, input=None):
    if input is None:
      return None
    result = sum([weight_i * input_i for weight_i, input_i in zip(self._weights, input)])
    print result
    return (result - self._bias) > 0