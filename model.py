import pickle
import re
from pathlib import Path
import numpy as np
import pandas as pd

from PIL import Image
from io import BytesIO

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


classes = ["tshirt",
           "longsleeve",
           "pants",
           "dress",
           "outwear",
           "shorts",
           "skirt",]




def predict_class(file: Image.Image):
    img = Image.open(file)
    img = np.asarray(img.resize((120,160))).flatten()
    pixels = img.reshape(-1, len(img))
    columns = range(120*160*3)
    df = pd.DataFrame(pixels, columns=columns)
    pred = model.predict(df)
    return classes[pred[0]]
