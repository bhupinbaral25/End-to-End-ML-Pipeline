
from src.utils import CONFIG, get_today_date
from src.model.modeling import get_model_training
from src.helper import read_pickle_file, save_to_pickle


today_date = get_today_date()
global_dict_path = f"{CONFIG['result']}{today_date}_{CONFIG['process_dict_flag']}"
global_dict = read_pickle_file(global_dict_path)

if __name__ == "__main__":

    train_path = f"{CONFIG['base_data_path']}{today_date}_{CONFIG['preprocess_data_path']}"
    test_path = f"{CONFIG['base_data_path']}{today_date}_{CONFIG['preprocess_test_data_path']}"

    result = get_model_training(train_path, test_path)
    global_dict['model_process'] = result
    save_to_pickle(global_dict_path, global_dict)

    


