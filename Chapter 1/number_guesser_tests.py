from NumberGuesser import NumberGuesser

def given_no_information_when_asked_to_guess_test():
  # given
  number_guesser = NumberGuesser()
  # when
  guessed_number = number_guesser.guess()
  # then
  assert guessed_number is None, 'there should be no guess.'

def given_one_datapoint_when_asked_to_guess_test():
  #given
  number_guesser = NumberGuesser()
  previously_chosen_number = 5
  number_guesser.number_was(previously_chosen_number)
  #when
  guessed_number = number_guesser.guess()
  #then
  assert type(guessed_number) is int, 'the answer should be a number'
  assert guessed_number == previously_chosen_number, 'the answer should be the previously chosen number.'

def given_multiple_datapoints_when_asked_to_guess_many_times_test():
  #given
  number_guesser = NumberGuesser()
  previously_chosen_numbers = [1,2,5]
  number_guesser.numbers_were(previously_chosen_numbers)
  #when
  guessed_numbers = [number_guesser.guess() for i in range(0,100)]
  #then
  for guessed_number in guessed_numbers:
    assert guessed_number in previously_chosen_numbers, 'every guess should be one of the previously chosen numbers'
  assert len(set(guessed_numbers)) > 1, "It shouldn't always guess the same number."