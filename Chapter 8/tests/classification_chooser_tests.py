import nose.tools
from choosey import *

@nose.tools.raises(Exception)
def given_no_model_options_test():
    classifier_chooser = ClassifierChooser()

def given_a_single_classifier_option_that_does_not_require_training_test():
    classifier_chooser = ClassifierChooser.create_with_single_classifier_option(CopyCatClassifier())
    input_value = 42
    predicted_label = classifier_chooser.classify(input_value)
    assert predicted_label == input_value, "Should predict input value."

    input_value = 11
    predicted_label = classifier_chooser.classify(input_value)
    assert predicted_label == input_value, "Should predict input value."

def given_a_different_single_classifier_option_that_does_not_require_training_test():
    classifier_chooser = ClassifierChooser.create_with_single_classifier_option(AlwaysTrueClassifier())
    input_value = 42
    predicted_label = classifier_chooser.classify(input_value)
    assert predicted_label, "Should always predict True."

def given_a_CopyCatClassifier_test():
    classifier = CopyCatClassifier()
    input_value = 12.5
    predicted_label = classifier.classify(input_value)
    assert predicted_label == input_value, "Should predict the value to be what the input is."

    input_value = 77
    predicted_label = classifier.classify(input_value)
    assert predicted_label == input_value, "Should predict the value to be what the input is."

def given_an_AlwaysTrueClassifier_test():
    classifier = AlwaysTrueClassifier()
    predicted_label = classifier.classify(55)
    assert predicted_label == 1, "Should always predict one."

def given_an_AlwaysFalseClassifier_test():
    classifier = AlwaysFalseClassifier()
    predicted_label = classifier.classify(55)
    assert predicted_label == 0, "Should always predict zero."

def given_multiple_classifier_options_test():
    classifier_chooser = ClassifierChooser(classifier_options_list=[
            AlwaysTrueClassifier(),
            AlwaysFalseClassifier()
        ],
        test_input=78,
        test_label=1)
    predicted_label = classifier_chooser.classify(0)
    assert predicted_label == 1, "Should choose best classifier option to classify with."
