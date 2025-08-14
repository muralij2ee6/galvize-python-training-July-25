import random
from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


class FraudScenarioGenerator:
    def __init__(self):
        self.faker = Faker()
        self.fraud_patterns = [
            self._card_testing_scenario,
            self._money_mule_activity,
            self._merchant_collusion,
            # ... 12 more patterns
        ]

    def _card_testing_scenario(self):
        """Series of small transactions followed by large purchase"""
        base_amount = random.uniform(0.5, 5)
        return [{
            'amount': base_amount * (i + 1),
            'time_gap': 60,  # seconds
            'merchant': 'TEST_' + self.faker.word(),
            'is_fraud': 1 if i > 3 else 0
        } for i in range(8)]

    def _money_mule_activity(self):
        """Rapid transfers between accounts"""
        return [{
            'amount': random.uniform(300, 5000),
            'time_gap': random.randint(10, 120),
            'merchant': 'TRANSFER_' + str(random.randint(1000, 9999)),
            'is_fraud': 1
        } for _ in range(random.randint(3, 7))]

    def generate_dataset(self, n=100000):
        records = []
        for _ in range(n):
            # 5% chance to trigger a fraud pattern
            if random.random() < 0.05:
                pattern = random.choice(self.fraud_patterns)
                records.extend(pattern())
            else:
                records.append({
                    'amount': abs(np.random.normal(50, 30)),
                    'time_gap': random.randint(300, 3600),
                    'merchant': self.faker.company(),
                    'is_fraud': 0
                })
        return pd.DataFrame(records)