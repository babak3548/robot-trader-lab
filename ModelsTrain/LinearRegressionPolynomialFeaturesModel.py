from sklearn.linear_model import LogisticRegression, SGDClassifier
import torch
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.preprocessing import PolynomialFeatures, SplineTransformer, PowerTransformer, FunctionTransformer, QuantileTransformer, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression, SGDRegressor

class LinearRegressionPolynomialFeaturesModel:
    def __init__(self, data):
        self.data = data
        print('-'*10, "class LinearRegressionPolynomialFeaturesModel")
        #print("data.head(10):", data[:1,:])

    def PreparingData(self):
        # x = torch.tensor(self.data[:, :-1], dtype=torch.float32)
        # y = torch.tensor(self.data[:, -1], dtype=torch.long)
        #
        # data_reg_max_min = self.data[:, 1:14]
        #
        # x = torch.tensor(data_reg_max_min[:, :-1], dtype=torch.float32)
        # y = torch.tensor(data_reg_max_min[:, -1], dtype=torch.long)
        # y = y.reshape(-1, 1)
        X = self.data[:, :-1].copy()
        y = self.data[:, -1].copy().astype(np.int64)

        normz = StandardScaler()
        X = normz.fit_transform(X)

        ##1-2: Train_Test_Split
        self.x_train, self.x_valid, self.y_train, self.y_valid = train_test_split(X, y, train_size=0.8, random_state=42, shuffle=False)

    def TrainModel(self):
        # model_pipline = make_pipeline(PolynomialFeatures(),   LinearRegression())
        alpha = 3
        model_pipline = make_pipeline(
             SplineTransformer(n_knots=3, degree=2),  # .927
             #PowerTransformer(),
            # FunctionTransformer(lambda x: np.exp(-alpha*x)),
            # todo: 1/(x+0.5)^2.3
            # QuantileTransformer(n_quantiles=5, output_distribution='normal'),
            LinearRegression())
        self.PreparingData()

        model_pipline.fit(self.x_train, self.y_train)
        accuracyTrain=model_pipline.score(self.x_train, self.y_train)
        accuracyValidtion =model_pipline.score(self.x_valid, self.y_valid)

        print("accuracy LogisticRegression Train:", accuracyTrain, "\naccuracy LogisticRegression validtion:", accuracyValidtion)
        return model_pipline