class NoClassifierOptionsException(Exception):
  pass

class ClassifierChooser:
    def __init__(self):
        raise NoClassifierOptionsException()
