class Perceptron:
  def __init__(self):
    self._result = None
  def train(self, input, correct_output):
    self._result = correct_output
  def predict(self, input=None):
    return self._result