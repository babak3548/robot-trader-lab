from sklearn.linear_model import LogisticRegression, SGDClassifier
import torch
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.preprocessing import PolynomialFeatures, SplineTransformer, PowerTransformer, FunctionTransformer, QuantileTransformer, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error

class LogiRegrPolynomialFeaturesModel:
    def __init__(self, data):
        self.data = data

    def PreparingData(self):
        X = self.data[:, :-1].copy()
        y = self.data[:, -1].copy().astype(np.int64)

        normz = StandardScaler()
        X = normz.fit_transform(X)

        self.x_train, self.x_valid, self.y_train, self.y_valid = train_test_split(X, y, train_size=0.8, random_state=42, shuffle=False)

    def TrainModel(self):
        model = make_pipeline(PolynomialFeatures(degree=3, interaction_only=True),
                              LogisticRegression(max_iter=1500, random_state=9))
        self.PreparingData()
        model.fit(self.x_train, self.y_train)
        accuracyTrain=model.score(self.x_train, self.y_train)
        accuracyValidtion = model.score(self.x_valid, self.y_valid)

        print("accuracy LogisticRegression Train:", accuracyTrain, "\naccuracy LogisticRegression validtion:", accuracyValidtion)
        return model