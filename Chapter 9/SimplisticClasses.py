class VariantImprovesAndFemaleMoreSoClassifier():
    def probability(self, input):
        return {
            ('control', '60626', 'female'): 0.60,
            ('variant', '60626', 'female'): 0.65,
        }[input]
