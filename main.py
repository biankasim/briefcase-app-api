from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from model import predict_class
from model import __version__ as model_version
from color_extraction import *


app = FastAPI()


class PredictionOut(BaseModel):
    clothing_type: str
    color: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}



@app.post("/predict", response_model=PredictionOut)
def predict(file: UploadFile = File(...)):
    #check if the uploaded file is an image
    if file.content_type.startswith("image/"):
        #classify image
        clothing_type = predict_class(file.file)
        #get color
        color = get_color_name(get_mode_color(file.file))
        return {"clothing_type" : clothing_type, "color" : color}
    else:
        return JSONResponse(status_code=400, content={"error": "Invalid file format. Please upload an image."})
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
