from NumberGuesser import NumberGuesser

def given_no_information_when_asked_to_guess_test():
  number_guesser = NumberGuesser()
  result = number_guesser.guess()
  assert result is None

def given_one_datapoint_when_asked_to_guess_test():
  #given
  number_guesser = NumberGuesser()
  number_guesser.number_was(5)

  #when
  result = number_guesser.guess()

  #then
  assert type(result) is int, 'then the answer is a number'