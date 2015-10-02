class Perceptron:
  def __init__(self):
    self._weight_1 = 0.431
    self._weight_2 = 0.02
  def train(self, inputs, labels):
    for _ in range(4):
      for input, label in zip(inputs, labels):
        label_delta = (label - self.predict(input))
        self._weight_1 = self._weight_1 + .1 * input[0] * label_delta
        self._weight_2 = self._weight_2 + .1 * input[1] * label_delta
  def predict(self, input):
    if len(input) == 0:
      return None
    return int(0 < self._weight_1 * input[0] + self._weight_2 * input[1])

