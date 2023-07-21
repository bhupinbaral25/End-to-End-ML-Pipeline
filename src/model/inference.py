
import pandas as pd
import numpy as np

from src.decorator import loger
from src.utils import CONFIG
from src.model.featuring import FeatureEngineering
from src.model.modeling import random_dict

@loger
def get_model_inference(Model, data:dict):

    fe = FeatureEngineering()
    input_data = random_dict
    input_data[CONFIG['Features'][0]] = data[CONFIG['Features'][0]]
    fe.set_feature_names([key for key in input_data.keys()])
    data = pd.Series(input_data)
    scale_data = fe.scale_data(data)
    user_input = np.array(list(scale_data[CONFIG['Features'][0]])).reshape(-1, 1)

    return Model.predict(user_input)
    




