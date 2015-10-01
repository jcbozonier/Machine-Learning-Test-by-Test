class Perceptron:
  def __init__(self):
    self._weight_1 = 0.20
    self._weight_2 = 0.20
  def train(self, inputs, label):
    pass
  def predict(self, input):
    if len(input) == 0:
      return None
    return 0 < self._weight_1 * input[0] + self._weight_2 * input[1]

