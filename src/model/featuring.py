import os
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from src.utils import CONFIG, get_today_date, find_pickle_file



class FeatureEngineering:
    def __init__(self):
        self.scaler = None
        self.feature_names = None
        self.scaler_path = find_pickle_file(get_today_date(), "scaler") 

    def set_feature_names(self, feature_names):
        self.feature_names = feature_names

    def scale_data(self, data):
        if isinstance(data, pd.Series):
            if self.feature_names is None:
                raise ValueError("Please set the feature names using set_feature_names method.")
            data = pd.DataFrame(data).T

        if isinstance(data, pd.DataFrame):
            if self.scaler is None:
                if os.path.exists(self.scaler_path):
                    with open(self.scaler_path, "rb") as f:
                        self.scaler = pickle.load(f)
                else:
                    if self.feature_names is None:
                        raise ValueError("Please set the feature names using set_feature_names method.")
                    self.scaler = MinMaxScaler()
                    scaled_data = self.scaler.fit_transform(data)
                    with open(self.scaler_path, "wb") as f:
                        pickle.dump(self.scaler, f)
                    return pd.DataFrame(scaled_data, columns=self.feature_names)
            
            return pd.DataFrame(self.scaler.transform(data), columns=self.feature_names)
        else:
            raise ValueError("Data must be a pandas DataFrame or Series.")

   