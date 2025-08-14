import xgboost as xgb
from sklearn.preprocessing import KBinsDiscretizer
import pandas as pd
import numpy as np


class XGBoostFraudModel:
    def __init__(self):
        self.model = xgb.XGBClassifier(
            objective='binary:logistic',
            n_estimators=500,
            max_depth=9,
            learning_rate=0.01,
            subsample=0.8,
            colsample_bytree=0.8,
            gamma=0.5,
            scale_pos_weight=15  # Adjust for class imbalance
        )
        self.binner = KBinsDiscretizer(n_bins=10, encode='ordinal')

    def feature_engineering(self, df):
        """Create advanced features"""
        # Temporal features
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['day_of_week'] = pd.to_datetime(df['timestamp']).dt.dayofweek

        # Behavioral features
        df['amt_per_sec'] = df['amount'] / df['seconds_since_last_txn']
        df['velocity_ratio'] = df['txn_count_1h'] / (df['txn_count_24h'] + 1)

        # Binned features
        df['amount_bin'] = self.binner.fit_transform(df[['amount']])
        return df

    def predict(self, transaction):
        """Predict with feature engineering"""
        feats = self.feature_engineering(pd.DataFrame([transaction]))
        return self.model.predict_proba(feats)[0][1]