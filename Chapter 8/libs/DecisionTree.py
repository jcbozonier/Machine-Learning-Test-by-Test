from sklearn.tree import DecisionTreeRegressor

class Classifier:
    def __init__(self):
      self._decision_tree = DecisionTreeRegressor()
      self._model = None
    def batch_train(self, observations):
        class_labels = map(lambda x: x[0], observations)
        class_inputs = map(lambda x: x[1], observations)
        observations = self._decision_tree.fit(class_inputs, class_labels)
        pass
    def classify(self, observation):
        return self._decision_tree.predict(observation)
