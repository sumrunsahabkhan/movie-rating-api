from sklearn.preprocessing import StandardScaler
import numpy as np

# Dummy scaler example if you saved one
def preprocess(data):
    # In real case, use saved StandardScaler
    return np.array(data).reshape(1, -1)
