import nose.tools
from choosey import *

@nose.tools.raises(NoClassifierOptionsException)
def given_no_model_options_test():
    classifier_chooser = ClassifierChooser()
