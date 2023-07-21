
import pickle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

from src.decorator import loger
from src.utils import CONFIG, get_today_date
from src.model.featuring import FeatureEngineering

today_date = get_today_date()
plot_file_path = f"{CONFIG['result']}{today_date}_actual_vs_predicted.png"

class ModelTraining:
    def __init__(self):
        self.model = LinearRegression()

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        return self.model

    def evaluate_model(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        self.y_pred = y_pred
        self.y_test = y_test

        return rmse, mae

    def prepare_plot(self):

        plt.scatter(self.y_test, self.y_pred, c='r', label='Predicted')  # Red for predicted values
        plt.scatter(self.y_test, self.y_test, c='b', label='Actual')  # Blue for actual values
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.title('Actual vs. Predicted')
        plt.legend(loc='upper left')

        plt.savefig(plot_file_path)
        plt.close()
       
    def save_model(self, model_path):
        with open(model_path, 'wb') as f:
            pickle.dump(self.model, f)

@loger
def get_model_training(train_data_path: str, test_data_path:str):

    train_data = pd.read_csv(train_data_path)
    test_data = pd.read_csv(test_data_path)

    fe = FeatureEngineering()
    fe.set_feature_names(train_data.columns.tolist())
    train_data = fe.scale_data(train_data)
    test_data = fe.scale_data(test_data)

    mt = ModelTraining()
    mt.train_model(train_data[CONFIG['Features']], train_data[CONFIG['Lable']])
    print("...Model Training Sucessful....")
    rmse, mae = mt.evaluate_model(test_data[CONFIG['Features']], test_data[CONFIG['Lable']])
    print("rmse is ", rmse)
    mt.prepare_plot()

    if rmse <= CONFIG['threshold_rmse']:
        mt.save_model(f"{CONFIG['model_path']}/{today_date}_lrmodel.pkl")
        return True
    else:
        return False

random_dict = {"Unnamed: 0":0,"x2":5, "y": 0}