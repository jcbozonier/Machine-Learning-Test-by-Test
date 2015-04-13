import SimplisticClasses

def given_a_dumb_classifer_that_says_what_I_want_test():
    classifier = SimplisticClasses.DumbClassifier({
        ('control', '60626', 'female'): 0.60,
    })
    order_probability = classifier.probability(('control', '60626', 'female'))
    assert order_probability == 0.60, "Should return probability I told it to."

def given_a_never_before_seen_observation_test():
    classifier = SimplisticClasses.DumbClassifier({})
    probability = classifier.probability(('boo', 'bibbit'))
    assert probability == None, "Should return None"

def given_any_input_test():
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    results = regression_model.predict(input=(42,'hai'))
    assert results == 12.25, "Should be a constant amount regardless of the input."

def given_a_sleeping_dog_test():
    customer_segment = ('60602', 'male')
    classification_model = SimplisticClasses.DumbClassifier({
        ('control',) + customer_segment: 0.50,
        ('variant',) + customer_segment: 0.45,
    })
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    ad_name = SimplisticClasses.assign_ad_for(customer_segment, classification_model, regression_model)
    assert ad_name == 'control', "Should let sleeping dogs lie."

def given_a_variant_that_improves_on_probability_of_ordering_over_control_test():
    customer_segment = ('60626', 'female')
    classification_model = SimplisticClasses.DumbClassifier({
        ('control',) + customer_segment: 0.60,
        ('variant',) + customer_segment: 0.65,
    })
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    ad_name = SimplisticClasses.assign_ad_for(customer_segment, classification_model, regression_model)
    assert ad_name == 'variant', "Should choose to advertise"

def given_a_variant_that_does_NOT_improve_on_probability_of_ordering_over_control_test():
    customer_segment = ('60626', 'male')
    classification_model = SimplisticClasses.DumbClassifier({
        ('control',) + customer_segment: 0.45,
        ('variant',) + customer_segment: 0.45,
    })
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    ad_name = SimplisticClasses.assign_ad_for(customer_segment, classification_model, regression_model)
    assert ad_name == 'control', "Should choose to NOT advertise"

def given_variant_improves_over_control_but_not_enough_to_warrant_advertising_cost_test():
    customer_segment = ('60626', 'female')
    classification_model = SimplisticClasses.DumbClassifier({
        ('control',) + customer_segment: 0.60,
        ('variant',) + customer_segment: 0.65,
    })
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    ad_name = SimplisticClasses.assign_ad_for(customer_segment, classification_model, regression_model, ad_cost=0.6126)
    assert ad_name == 'control', "Should choose to NOT advertise"

def given_variant_improves_over_control_just_enough_to_warrant_advertising_cost_test():
    customer_segment = ('60626', 'female')
    classification_model = SimplisticClasses.DumbClassifier({
        ('control',) + customer_segment: 0.60,
        ('variant',) + customer_segment: 0.65,
    })
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    ad_name = SimplisticClasses.assign_ad_for(customer_segment, classification_model, regression_model, ad_cost=0.60)
    assert ad_name == 'variant', "Should choose to advertise"

def given_probability_to_order_remains_constant_but_expected_profit_increases_test():
    customer_segment = ('60626', 'female')
    classification_model = SimplisticClasses.DumbClassifier({
        ('control',) + customer_segment: 0.65,
        ('variant',) + customer_segment: 0.65,
    })
    regression_model = SimplisticClasses.DumbClassifier({
        ('control',) + customer_segment: 12.25,
        ('variant',) + customer_segment: 15.50,
    })
    ad_name = SimplisticClasses.assign_ad_for(customer_segment, classification_model, regression_model)
    assert ad_name == 'variant', "Should recommend using ad"

class DummySklearnModel():
    def __init__(self):
        self.predict_proba_call_arguments = None
    def predict_proba(self, input):
        self.predict_proba_call_arguments = input

def logistic_regression_test():
    dummy_sklearn_model = DummySklearnModel()
    model = SimplisticClasses.LogisticModel(dummy_sklearn_model)
    model.predict([1,2,3])
    assert dummy_sklearn_model.predict_proba_call_arguments == [1,2,3]
