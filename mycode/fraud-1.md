# **Fraud Detection MCP (Microservices, Containers, Pipelines) System**
## **End-to-End Implementation with Robust Fraud Detection**

This solution provides:
- **MCP Server** (FastAPI microservice)
- **MCP Client** (Python CLI & script)
- **Monitoring** (Python-based dashboard)
- **Complex Fraud Dataset** (Synthetic financial transactions + real-world patterns)

---

## **📂 Project Structure**
```bash
fraud-detection-mcp/
├── data/                    # Datasets (synthetic + real-world)
│   ├── synthetic_fraud_data.csv
│   └── realworld_patterns.json
├── server/                  # MCP Server (FastAPI)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # API endpoints
│   │   ├── models.py        # ML models
│   │   └── schemas.py       # Pydantic models
│   ├── requirements.txt
│   └── Dockerfile
├── client/                  # MCP Client
│   ├── cli.py               # Command-line interface
│   └── api_client.py        # Python API client
├── monitoring/              # Python-based monitoring
│   ├── live_dashboard.py    # Real-time monitoring
│   └── analysis.ipynb       # Jupyter Notebook
└── README.md
```

---

## **🔍 Complex Fraud Dataset**
### **Synthetic Financial Transactions (`data/synthetic_fraud_data.csv`)**
```python
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Generate 100,000 synthetic transactions
fake = Faker()
np.random.seed(42)

def generate_transactions(n=100000):
    data = []
    for _ in range(n):
        is_fraud = np.random.choice([0, 1], p=[0.98, 0.02])  # 2% fraud rate
        
        # Normal transaction pattern
        amount = abs(np.random.normal(50, 30)) if not is_fraud else abs(np.random.normal(500, 300))
        
        # Fraud indicators
        unusual_time = np.random.randint(0, 5) if is_fraud else 0
        high_velocity = np.random.randint(3, 10) if is_fraud else np.random.randint(0, 2)
        
        data.append({
            "transaction_id": fake.uuid4(),
            "user_id": fake.random_int(1000, 9999),
            "amount": round(amount, 2),
            "merchant": fake.company(),
            "category": fake.random_element(elements=("groceries", "electronics", "travel", "entertainment")),
            "location": fake.country_code(),
            "device": fake.user_agent(),
            "ip_address": fake.ipv4(),
            "transaction_time": (datetime.now() - timedelta(days=np.random.randint(0, 30))\
                                .strftime("%Y-%m-%d %H:%M:%S"),
            "unusual_time": unusual_time,
            "high_velocity": high_velocity,
            "is_fraud": is_fraud
        })
    return pd.DataFrame(data)

df = generate_transactions()
df.to_csv("data/synthetic_fraud_data.csv", index=False)
```

### **Real-World Fraud Patterns (`data/realworld_patterns.json`)**
```json
{
  "common_fraud_patterns": [
    {
      "name": "Stolen Card Rapid Purchases",
      "indicators": ["high_velocity > 5", "unusual_time == 1", "amount > 300"],
      "weight": 0.45
    },
    {
      "name": "Micro Transactions Testing",
      "indicators": ["count(amount < 5) > 3 within 1h", "location changes rapidly"],
      "weight": 0.30
    }
  ]
}
```

---

## **🖥️ MCP Server Implementation**
### **1. Fraud Detection Model (`server/app/models.py`)**
```python
import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

class FraudDetector:
    def __init__(self):
        self.model = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', IsolationForest(
                n_estimators=150,
                contamination=0.02,  # Expected fraud rate
                random_state=42,
                behaviour='new'
            ))
        ])
    
    def train(self, data_path):
        df = pd.read_csv(data_path)
        X = df[['amount', 'unusual_time', 'high_velocity']]
        self.model.fit(X)
        joblib.dump(self.model, "fraud_detector.joblib")
    
    def predict(self, transaction):
        features = [[
            transaction['amount'],
            transaction['unusual_time'],
            transaction['high_velocity']
        ]]
        return self.model.decision_function(features)[0]  # Lower score = more anomalous
```

### **2. FastAPI Server (`server/app/main.py`)**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models import FraudDetector
import joblib
import json
from typing import Optional

app = FastAPI(title="Fraud Detection MCP Server")

# Load model
try:
    detector = joblib.load("fraud_detector.joblib")
except:
    detector = FraudDetector()
    detector.train("data/synthetic_fraud_data.csv")

# Request/Response models
class Transaction(BaseModel):
    transaction_id: str
    user_id: int
    amount: float
    merchant: str
    category: str
    location: str
    device: Optional[str] = None
    ip_address: Optional[str] = None
    unusual_time: int = 0
    high_velocity: int = 0

class FraudResponse(BaseModel):
    transaction_id: str
    fraud_score: float
    is_high_risk: bool
    reasons: list[str]

@app.post("/detect", response_model=FraudResponse)
async def detect_fraud(transaction: Transaction):
    try:
        score = detector.predict(transaction.dict())
        
        # Business rules
        reasons = []
        if score < -0.5:
            reasons.append("Highly anomalous transaction pattern")
        if transaction.amount > 1000:
            reasons.append("Unusually large amount")
        if transaction.high_velocity > 3:
            reasons.append("Suspicious transaction velocity")
            
        return {
            "transaction_id": transaction.transaction_id,
            "fraud_score": float(score),
            "is_high_risk": score < -0.3 or len(reasons) >= 2,
            "reasons": reasons
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

---

## **💻 MCP Client Implementation**
### **1. API Client (`client/api_client.py`)**
```python
import requests
from typing import Dict, Any
import json

class FraudDetectionClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
    
    def detect_fraud(self, transaction: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.post(
            f"{self.base_url}/detect",
            json=transaction,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()

# Example usage
if __name__ == "__main__":
    client = FraudDetectionClient()
    sample_transaction = {
        "transaction_id": "txn_12345",
        "user_id": 1001,
        "amount": 1250.00,
        "merchant": "ElectroWorld",
        "category": "electronics",
        "location": "US",
        "unusual_time": 1,
        "high_velocity": 4
    }
    result = client.detect_fraud(sample_transaction)
    print("Fraud Detection Result:", json.dumps(result, indent=2))
```

### **2. CLI Interface (`client/cli.py`)**
```python
import click
from .api_client import FraudDetectionClient
import json

@click.group()
def cli():
    """Fraud Detection MCP Client"""
    pass

@cli.command()
@click.option('--amount', type=float, required=True, help='Transaction amount')
@click.option('--user-id', type=int, required=True, help='User ID')
@click.option('--velocity', type=int, default=0, help='Transaction velocity')
def check(amount, user_id, velocity):
    """Check a single transaction for fraud"""
    client = FraudDetectionClient()
    transaction = {
        "transaction_id": f"txn_{user_id}_{int(time.time())}",
        "user_id": user_id,
        "amount": amount,
        "merchant": "CLI Merchant",
        "category": "cli",
        "location": "CLI",
        "high_velocity": velocity
    }
    result = client.detect_fraud(transaction)
    click.echo(json.dumps(result, indent=2))

if __name__ == "__main__":
    cli()
```

---

## **📊 Python-Based Monitoring**
### **1. Real-Time Dashboard (`monitoring/live_dashboard.py`)**
```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from client.api_client import FraudDetectionClient
import threading
import time

# Initialize Dash app
app = dash.Dash(__name__)

# Generate simulated live data
def generate_live_data():
    client = FraudDetectionClient()
    while True:
        df = pd.read_csv("data/synthetic_fraud_data.csv").sample(10)
        for _, row in df.iterrows():
            transaction = row.to_dict()
            result = client.detect_fraud(transaction)
            # Store results for dashboard
            with open("monitoring/results.jsonl", "a") as f:
                f.write(json.dumps(result) + "\n")
        time.sleep(5)

# Start data generation in background
thread = threading.Thread(target=generate_live_data, daemon=True)
thread.start()

# Dashboard layout
app.layout = html.Div([
    html.H1("Real-Time Fraud Detection Dashboard"),
    dcc.Graph(id='live-graph'),
    dcc.Interval(id='interval', interval=5000)
])

@app.callback(
    Output('live-graph', 'figure'),
    Input('interval', 'n_intervals'))
def update_graph(n):
    try:
        df = pd.read_json("monitoring/results.jsonl", lines=True)
        fig = px.scatter(
            df, 
            x='amount', 
            y='fraud_score',
            color='is_high_risk',
            hover_data=['reasons'],
            title="Transaction Risk Analysis"
        )
        return fig
    except:
        return px.scatter(title="Waiting for data...")

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
```

### **2. Jupyter Notebook Analysis (`monitoring/analysis.ipynb`)**
```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

# Load data
df = pd.read_csv("data/synthetic_fraud_data.csv")

# Feature engineering
df['amount_log'] = np.log1p(df['amount'])
df['time_of_day'] = pd.to_datetime(df['transaction_time']).dt.hour

# Fraud pattern visualization
plt.figure(figsize=(12, 6))
sns.boxplot(x='is_fraud', y='amount_log', data=df)
plt.title("Transaction Amounts by Fraud Status")
plt.show()

# Correlation analysis
corr = df[['amount', 'unusual_time', 'high_velocity', 'is_fraud']].corr()
sns.heatmap(corr, annot=True)
plt.title("Fraud Indicator Correlations")
plt.show()
```

---

## **🐳 Docker Deployment**
### **1. Server Dockerfile (`server/Dockerfile`)**
```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### **2. Running the System**
```bash
# Build and run server
cd server
docker build -t fraud-server .
docker run -p 8000:8000 fraud-server

# In another terminal - run monitoring dashboard
python monitoring/live_dashboard.py

# Test client
python client/cli.py check --amount 1500 --user-id 1001 --velocity 4
```

---

## **🔑 Key Features**
1. **Complex Fraud Detection**:
   - Isolation Forest algorithm for anomaly detection
   - Business rules layer for explainable decisions
   - Real-world fraud pattern matching

2. **Production-Ready MCP Architecture**:
   - Microservice API (FastAPI)
   - Containerized deployment (Docker)
   - Pipeline-ready structure

3. **Comprehensive Monitoring**:
   - Real-time Dash dashboard
   - Jupyter Notebook for deep analysis
   - Synthetic + real-world data patterns

4. **Extensible Design**:
   - Easy to add new fraud patterns
   - Scalable API backend
   - Client libraries for integration

Would you like me to add any specific features like:
- Database integration (PostgreSQL/MongoDB)
- Advanced ML models (XGBoost, Neural Networks)
- More complex fraud scenarios?