from sklearn.ensemble import RandomForestClassifier
class Classifier:
  def __init__(self):
    self._forest = RandomForestClassifier(n_estimators = 100)
    self._model = None
  def batch_train(self, observations):
    class_labels = map(lambda x: x[0], observations)
    class_inputs = map(lambda x: x[1], observations)
    self._model = self._forest.fit(class_inputs, class_labels)
  def classify(self, observation):
    return self._model.predict(observation)
