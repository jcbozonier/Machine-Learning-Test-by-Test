class VariantImprovesAndFemaleMoreSoClassifier():
    def probability(self, input):
        data = {
            ('control', '60626', 'female'): 0.60,
            ('variant', '60626', 'female'): 0.65,
        }
        if input in data:
            return data[input]
        else:
            return None
