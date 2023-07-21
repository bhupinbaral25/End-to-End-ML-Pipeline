import pickle 
from src.decorator import pickle_error

@pickle_error
def read_pickle_file(path):

    with open(path, 'rb') as file:
        return pickle.load(file)
  
def save_to_pickle(path, result):
    with open(path, 'wb') as file:
        pickle.dump(result, file)
    return True


def render_html(viz_html_file_path):
    with open(viz_html_file_path, "r") as file:
        html_content = file.read()
    return html_content

def read_log_file(log_file_path):
    with open(log_file_path, "r") as file:
        lines = file.readlines()
        last_20_lines = lines[-30:]
    return "".join(last_20_lines)
