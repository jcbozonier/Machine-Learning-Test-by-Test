class NoClassifierOptionsException(Exception):
  pass

class ClassifierChooser:
    def __init__(self,
                 classifier_options_list=None,
                 test_label=None,
                 test_input=None):
        if not classifier_options_list is None:
            self._classifier_options_list = classifier_options_list
            for classifier in classifier_options_list:
                predicted_label = classifier.classify(test_input)
                if predicted_label == test_label:
                    self._classifier_options = classifier
        else:
            raise NoClassifierOptionsException()

    @staticmethod
    def create_with_single_classifier_option(classifier_option):
        return ClassifierChooser(classifier_options_list=[classifier_option])

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
