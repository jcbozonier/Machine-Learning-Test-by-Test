class VariantImprovesAndFemaleMoreSoClassifier():
    def probability(self, input):
        data = {
            ('control', '60626', 'female'): 0.60,
            ('variant', '60626', 'female'): 0.65,
            ('control', '60626', 'male'): 0.45,
            ('variant', '60626', 'male'): 0.45,
            ('control', '60602', 'female'): 0.70,
            ('variant', '60602', 'female'): 0.70,
            ('control', '60602', 'male'): 0.50,
            ('variant', '60602', 'male'): 0.45,
        }
        if input in data:
            return data[input]
        else:
            return None

class AllCasesHaveSameProfitRegressionModel():
    def predict(self, input):
        return 12.25

def assign_ad_for(customer, classifier, regression_model):
    control_input = ('control',) + customer
    variant_input = ('variant',) + customer
    control_probability_of_order = classifier.probability(control_input)
    variant_probability_of_order = classifier.probability(variant_input)
    if control_probability_of_order >= variant_probability_of_order:
        return 'control'
    else:
        return 'variant'
