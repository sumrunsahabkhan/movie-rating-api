import joblib

def load_model(path="C:\\Users\\ok\\OneDrive - Higher Education Commission\\6th sem\\Big Data\\Theory project\\movie-rating-api\\best_model (1).pkl"):
    model = joblib.load(path)
    return model
