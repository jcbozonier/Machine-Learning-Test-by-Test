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
