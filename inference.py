import pickle
import pandas as pd

def model_fn(model_dir):
    model = pickle.load(open(f"{model_dir}/employee_attrition_model.pkl", "rb"))
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        return pd.DataFrame([request_body])
    raise ValueError("Unsupported content type")

def predict_fn(input_data, model):
    prediction = model.predict(input_data)
    return prediction

def output_fn(prediction, accept):
    return str(int(prediction[0]))