import numpy as np

def calculate(list):
    calculations = {}
    if len(list) == 9:
        matrix_list = np.array(list).reshape(3,3)
        calculations["mean"] = [np.mean(matrix_list, axis=0).tolist(), np.mean(matrix_list, axis=1).tolist(), np.mean(list)]
        calculations["variance"] = [np.var(matrix_list, axis=0).tolist(), np.var(matrix_list, axis=1).tolist(), np.var(list)]
        calculations["standard deviation"] = [np.std(matrix_list, axis=0).tolist(), np.std(matrix_list, axis=1).tolist(), np.std(list)]
        calculations["max"] = [np.max(matrix_list, axis=0).tolist(), np.max(matrix_list, axis=1).tolist(), np.max(list)]
        calculations["min"] = [np.min(matrix_list, axis=0).tolist(), np.min(matrix_list, axis=1).tolist(), np.min(list)]
        calculations["sum"] = [np.sum(matrix_list, axis=0).tolist(), np.sum(matrix_list, axis=1).tolist(), np.sum(list)]
    else:
        raise ValueError("List must contain nine numbers.")

    return calculations
