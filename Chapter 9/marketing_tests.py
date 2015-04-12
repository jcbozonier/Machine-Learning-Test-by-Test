import SimplisticClasses

def given_a_classifier_where_the_variant_improves_and_females_more_so_test():
    classifier = SimplisticClasses.VariantImprovesAndFemaleMoreSoClassifier()

    # Our persuadables
    order_probability = classifier.probability(('control', '60626', 'female'))
    assert order_probability == 0.60, "Females should have a base probability of ordering."
    order_probability = classifier.probability(('variant', '60626', 'female'))
    assert order_probability == 0.65, "Females should be more likely to order with the new campaign"

    # Our no effects
    order_probability = classifier.probability(('control', '60626', 'male'))
    assert order_probability == 0.45, "Males should have a base probability of ordering."
    order_probability = classifier.probability(('variant', '60626', 'male'))
    assert order_probability == 0.45, "Males should be equally likely to order with the new campaign"
    # More no effects
    order_probability = classifier.probability(('control', '60602', 'female'))
    assert order_probability == 0.70, "Females should have a base probability of ordering."
    order_probability = classifier.probability(('variant', '60602', 'female'))
    assert order_probability == 0.70, "Females should be equally likely to order with the new campaign"

    # Our sleeping dogs
    order_probability = classifier.probability(('control', '60602', 'male'))
    assert order_probability == 0.50, "Males should have a base probability of ordering."
    order_probability = classifier.probability(('variant', '60602', 'male'))
    assert order_probability == 0.45, "Males should be more likely to order with the new campaign"

def given_a_never_before_seen_observation_test():
    classifier = SimplisticClasses.VariantImprovesAndFemaleMoreSoClassifier()
    probability = classifier.probability(('boo', 'bibbit'))
    assert probability == None, "Should return None"

def given_any_input_test():
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    results = regression_model.predict(input=(42,'hai'))
    assert results == 12.25, "Should be a constant amount regardless of the input."

def given_a_sleeping_dog_test():
    classification_model = SimplisticClasses.VariantImprovesAndFemaleMoreSoClassifier()
    regression_model = SimplisticClasses.AllCasesHaveSameProfitRegressionModel()
    customer = ('60602', 'male')
    ad_name = SimplisticClasses.assign_ad_for(customer, classification_model, regression_model)
    assert ad_name == 'control', "Should let sleeping dogs lie."

def given_a_variant_that_improves_on_probability_of_ordering_over_control_test():
    classification_model = SimplisticClasses.VariantImprovesAndFemaleMoreSoClassifier()
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
