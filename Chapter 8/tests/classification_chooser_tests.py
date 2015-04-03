import nose.tools
from choosey import *

@nose.tools.raises(NoClassifierOptionsException)
def given_no_model_options_test():
    classifier_chooser = ClassifierChooser()

def given_a_single_classifier_option_that_does_not_require_training_test():
    classifier_chooser = ClassifierChooser(classifier_options=CopyCatClassifier())
    input_value = 42
    predicted_label = classifier_chooser.classify(input_value)
    assert predicted_label == input_value, "Should predict input value."

    input_value = 11
    predicted_label = classifier_chooser.classify(input_value)
    assert predicted_label == input_value, "Should predict input value."

def given_a_CopyCatClassifier_test():
    classifier = CopyCatClassifier()
    input_value = 12.5
    predicted_label = classifier.classify(input_value)
    assert predicted_label == input_value, "Should predict the value to be what the input is."

    input_value = 77
    predicted_label = classifier.classify(input_value)
    assert predicted_label == input_value, "Should predict the value to be what the input is."
