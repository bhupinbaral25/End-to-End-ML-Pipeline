
import pandas as pd 

from src.utils import CONFIG, get_today_date
from src.helper import read_pickle_file, save_to_pickle
from src.preprocessing import DataPipeline, save_data, generate_data_visualization
from src.decorator import data_error_handler, loger

today_date = get_today_date()
global_dict_path = f"{CONFIG['result']}{today_date}_{CONFIG['process_dict_flag']}"
viz_html_file = f"{CONFIG['result']}{today_date}_{CONFIG['viz_html_file']}"
global_dict = read_pickle_file(global_dict_path)

@loger
@data_error_handler
def prepare_data(raw_data_path):
    today_date = get_today_date()
    raw_data = pd.read_csv(raw_data_path, delimiter=CONFIG['delimeter'])
    generate_data_visualization(raw_data, viz_html_file)
    print("Html file generated for vizualization")
    pipeline = DataPipeline(raw_data)
    pipeline.preprocess_data()
    train_data, test_data = pipeline.split_data()
    save_data(
        train_data,
        f"{CONFIG['base_data_path']}{today_date}_{CONFIG['preprocess_data_path']}"
    )
    save_data(
        test_data,
        f"{CONFIG['base_data_path']}{today_date}_{CONFIG['preprocess_test_data_path']}"
    )
    print("Data Preprocessing Completed....\n")

    return True

if __name__ == "__main__":
    result = prepare_data(CONFIG['raw_data_path'])
    global_dict['data_pipeline'] = result
    save_to_pickle(global_dict_path, global_dict)


    






    
