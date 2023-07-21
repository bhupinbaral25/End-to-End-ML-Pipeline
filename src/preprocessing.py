import pandas as pd
from pandas_profiling import ProfileReport
from sklearn.model_selection import train_test_split

from src.utils import CONFIG
from src.decorator import data_error_handler

def generate_data_visualization(df, output_html_path):
 
    profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)

    profile.to_file(output_file=output_html_path)

def save_data(df, save_path:str):

    df.to_csv(save_path)

    return True

class DataPipeline:

    def __init__(self, data: pd.DataFrame):
        self.raw_data = data
        self.processed_data = None
    
    @data_error_handler
    def preprocess_data(self):

        new_df = self.raw_data.dropna(ignore_index = True)
        self.processed_data = new_df.drop(['x'], axis = 1)

        return self.processed_data
    
    def split_data(self):

        train_data, test_data = train_test_split(
            self.processed_data, 
            test_size=CONFIG['test_size'], 
            random_state=42
            )
        
        return train_data, test_data

        
    







