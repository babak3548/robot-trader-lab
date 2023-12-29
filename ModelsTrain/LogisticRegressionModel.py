from sklearn.linear_model import LogisticRegression, SGDClassifier
import torch
import numpy as np
from sklearn.model_selection import train_test_split

class LogisticRegressionModel:
    def __init__(self, data):
        self.data=data

    def PreparingData(self):
        x = torch.tensor(self.data[:, :-1], dtype=torch.float32)
        y = torch.tensor(self.data[:, -1], dtype=torch.long)
        y = y.reshape(-1, 1)
        print("x.shape, y.shape:", x.shape, y.shape)
        ## Split data to train and test
        self.x_train, self.x_valid, self.y_train, self.y_valid = train_test_split(x, y, train_size=0.8, random_state=42, shuffle=False)
        self.y_train = self.y_train.ravel()
        # self.y_valid = self.y_valid.ravel()

        y_t_count_T = np.unique(self.y_train, return_counts=1)
        y_t_count_F = np.unique(self.y_train, return_counts=0)
        print('-' * 10)
        y_t_count_T, y_t_count_F


    def TrainModel(self):
        model = LogisticRegression(solver='sag', max_iter=6000, random_state=9)
        self.PreparingData()
        model.fit(self.x_train, self.y_train)
        accuracyTrain = model.score(self.x_train, self.y_train)
        accuracyValidtion= model.score(self.x_valid, self.y_valid)
        print("accuracy LogisticRegression Train:", accuracyTrain, "accuracy LogisticRegression validtion:" , accuracyValidtion)
        return model

