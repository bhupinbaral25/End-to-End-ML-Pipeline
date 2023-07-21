import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from src.helper import read_pickle_file, save_to_pickle
from src.utils import CONFIG, get_today_date, find_pickle_file
from src.model.inference import get_model_inference
from src.decorator import loger

today_date = get_today_date()
model_path = find_pickle_file(today_date, selection = "lrmodel")
global_dict_path = f"{CONFIG['result']}{today_date}_{CONFIG['process_dict_flag']}"
global_dict = read_pickle_file(global_dict_path)
save_to_pickle(global_dict_path, global_dict)

MODEL = read_pickle_file(model_path)
global_dict['api'] = True
app = FastAPI()

class InputData(BaseModel):
    x: float

@loger
@app.post("/predict/")
async def process_data(input_data: InputData):

    result = get_model_inference(MODEL, {CONFIG['Features'][0]: input_data.x})
    return {"result": result[0][0]}

if __name__ == "__main__":
    uvicorn.run(app)