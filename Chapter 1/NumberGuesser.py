class NumberGuesser:
  """Guesses numbers based on the history of your input"""
  _guessed_number = None
  def number_was(self, guessed_number):
    self._guessed_number = guessed_number
  def guess(self):
    return self._guessed_number