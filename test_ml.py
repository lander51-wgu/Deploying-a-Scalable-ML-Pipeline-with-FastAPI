import pytest
# TODO: add necessary import
import pandas as pd
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference
from train_model import data, cat_features

# TODO: implement the first test. Change the function name and input as needed
def test_size_of_data_vs_processed():
    """
    Test that the size of the data remains the same after processing.
    """
    # Your code here
    X, y, encoder, lb = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )
    assert X.shape[0] == data.shape[0]
    assert y.shape[0] == data.shape[0]


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics_values_function():
    """
    Test that compute_model_metrics returns the correct precision, recall,
    and F1 values for a known input.
    """

    # Your code here
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert precision == pytest.approx(1.0)
    assert recall == pytest.approx(2 / 3)
    assert fbeta == pytest.approx(0.8)


# TODO: implement the third test. Change the function name and input as needed
def test_prediction_function():
    """
    Tests that prediction function returns 0 or 1.
    """
    # Your code here
    preds = inference(model, X_test)
    assert all(pred in [0, 1] for pred in preds)
