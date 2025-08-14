import shap
import matplotlib.pyplot as plt
from server.ml_models.xgboost_ensemble import XGBoostFraudModel

model = XGBoostFraudModel()
explainer = shap.TreeExplainer(model.model)

def explain_transaction(transaction):
    shap_values = explainer.shap_values(transaction)
    shap.summary_plot(shap_values, transaction, plot_type="bar")
    plt.savefig("shap_explanation.png")
    return {"shap_values": shap_values.tolist()}