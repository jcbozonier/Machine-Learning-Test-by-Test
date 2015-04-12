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
    classification_model = SimplisticClasses.DumbClassifier({
        ('control', '60602', 'male'): 0.50,
        ('variant', '60602', 'male'): 0.45,
    })
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    customer = ('60602', 'male')
    ad_name = SimplisticClasses.assign_ad_for(customer, classification_model, regression_model)
    assert ad_name == 'control', "Should let sleeping dogs lie."

def given_a_variant_that_improves_on_probability_of_ordering_over_control_test():
    classification_model = SimplisticClasses.DumbClassifier({
        ('control', '60626', 'female'): 0.60,
        ('variant', '60626', 'female'): 0.65,
    })
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    customer = ('60626', 'female')
    ad_name = SimplisticClasses.assign_ad_for(customer, classification_model, regression_model)
    assert ad_name == 'variant', "Should choose to advertise"

def given_a_variant_that_does_NOT_improve_on_probability_of_ordering_over_control_test():
    classification_model = SimplisticClasses.VariantImprovesAndFemaleMoreSoClassifier()
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    customer = ('60626', 'male')
    ad_name = SimplisticClasses.assign_ad_for(customer, classification_model, regression_model)
    assert ad_name == 'control', "Should choose to NOT advertise"

def given_variant_improves_over_control_but_not_enough_to_warrant_advertising_cost_test():
    classification_model = SimplisticClasses.VariantImprovesAndFemaleMoreSoClassifier()
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    customer = ('60626', 'female')
    ad_name = SimplisticClasses.assign_ad_for(customer, classification_model, regression_model, ad_cost=0.61)
    assert ad_name == 'control', "Should choose to NOT advertise"

def given_variant_improves_over_control_just_enough_to_warrant_advertising_cost_test():
    classification_model = SimplisticClasses.VariantImprovesAndFemaleMoreSoClassifier()
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    customer = ('60626', 'female')
    ad_name = SimplisticClasses.assign_ad_for(customer, classification_model, regression_model, ad_cost=0.60)
    assert ad_name == 'variant', "Should choose to advertise"

def given_probability_to_order_remains_constant_but_expected_profit_increases():
    classification_model = SimplisticClasses.VariantImprovesAndFemaleMoreSoClassifier()
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    customer = ('60626', 'male')
