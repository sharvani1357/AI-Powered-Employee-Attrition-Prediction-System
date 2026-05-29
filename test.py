import pickle
import numpy as np

model = pickle.load(
    open(
        "employee_attrition_model.pkl",
        "rb"
    )
)

sample = np.random.rand(
    1,
    34
)

prediction = model.predict(
    sample
)

print(prediction)