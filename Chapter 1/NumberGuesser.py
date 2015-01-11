import random
class NumberGuesser:
  """Guesses numbers based on the history of your input"""
  _guessed_numbers = None
  def numbers_were(self, guessed_numbers):
    self._guessed_numbers = guessed_numbers
  def number_was(self, guessed_number):
    self._guessed_numbers = [guessed_number]
  def guess(self):
    if self._guessed_numbers == None:
      return None
    return random.choice(self._guessed_numbers)