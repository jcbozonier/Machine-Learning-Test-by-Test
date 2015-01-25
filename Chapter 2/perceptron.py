class Perceptron:
  def __init__(self):
    self._result = None
  def train(self, training_data):
    self._result = { tuple(i[0]):i[1] for i in training_data }
  def predict(self, input=None):
    if input is None:
      return None
    return self._result[tuple(input)]