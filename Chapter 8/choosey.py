class NoClassifierOptionsException(Exception):
  pass

class ClassifierChooser:
    def __init__(self, classifier_options=None):
        if classifier_options is None:
            raise NoClassifierOptionsException()
        else:
            self._classifier_options = classifier_options
    def classify(self, input):
        return self._classifier_options.classify(input)

class AlwaysTrueClassifier:
    def classify(self, input):
        return 1

class AlwaysFalseClassifier:
    def classify(self, input):
        return 0

class CopyCatClassifier:
    def classify(self, input):
        return input
