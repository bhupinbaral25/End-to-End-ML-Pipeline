import pickle
from src.utils import CONFIG, get_today_date

today_date = get_today_date()
global_dict= {
    "data_pipeline": False,
    "model_process": False,
    "api":False
}

save_path = f"{CONFIG['result']}{today_date}_{CONFIG['process_dict_flag']}"

with open(save_path, 'wb') as file:
    pickle.dump(global_dict, file)

