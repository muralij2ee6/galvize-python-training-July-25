# **Fraud Detection System Explained for Junior Developers**  

Hey there! 👋 Let me break down this **Fraud Detection System** in simple terms. Imagine you're building a security guard for online transactions—it checks every payment and flags suspicious ones. Here's how it works:

---

## **🌐 1. The Big Picture**
We built a system with **3 main parts**:
1. **Server (MCP Server)** - The "brain" that detects fraud  
2. **Client (MCP Client)** - Sends transactions to the server  
3. **Monitoring** - Watches for fraud in real-time  

Like a **security camera system**:
- **Camera (Client)** → **Security Software (Server)** → **Monitor Screen (Dashboard)**  

---

## **🔍 2. How Fraud Detection Works**
### **A) The Machine Learning Models**
We use **3 smart algorithms** to catch fraudsters:

#### **1. Hugging Face Transformer (AI for Text)**
- **What it does**: Reads transaction descriptions (e.g., "iPhone purchase") and flags weird wordings.  
- **Example**: If someone writes "urgent payment!!!" + asks for $5,000 → **fraud risk!**  

#### **2. XGBoost (Traditional ML)**
- **What it does**: Checks numbers (amount, time, location) for patterns.  
- **Example**:  
  - Normal: You buy coffee for $5 at 9 AM near home ✅  
  - Fraud: $2,000 purchase at 3 AM from another country ❌  

#### **3. Graph Analysis (Network Detective)**
- **What it does**: Maps connections between users/merchants.  
- **Example**:  
  - If 10 new accounts send money to the same store → **possible scam!**  

---

### **B) The Data**
We generate **fake-but-realistic transactions** (for testing):
```python
# Example generated fraud transaction
{
  "amount": 1500,       # High amount
  "time": "3:00 AM",    # Unusual hour
  "location": "Russia", # Different country
  "is_fraud": 1         # Marked as fraud
}
```

---

## **💻 3. The Code Structure**
### **A) Server (FastAPI) - `/server`**
- **`main.py`** - Handles HTTP requests (like a web server)  
- **`models.py`** - Contains the fraud-detection AI  
- **`schemas.py`** - Defines data shapes (like a contract)  

#### **Example API Endpoint**
```python
@app.post("/detect")
def check_fraud(transaction: Transaction):
    score = model.predict(transaction)  # Get fraud score (0-1)
    return {"fraud_score": score}
```
- **Input**: Transaction details (amount, user, time, etc.)  
- **Output**: Fraud probability (`0.9` = 90% risky)  

---

### **B) Client - `/client`**
- **`api_client.py`** - Sends data to the server  
- **`cli.py`** - Command-line tool for testing  

#### **Example CLI Command**
```bash
python cli.py --amount 5000 --user-id 123 --location "Nigeria"
```
**Output:**  
```json
{
  "fraud_score": 0.87,
  "verdict": "HIGH_RISK",
  "reason": "Unusual large amount + high-risk country"
}
```

---

### **C) Monitoring - `/monitoring**
- **`live_dashboard.py`** - Real-time fraud alerts  
- **`analysis.ipynb`** - Jupyter Notebook for investigations  

#### **Dashboard Example**
![Fraud Dashboard](https://i.imgur.com/JQ8zF1l.png)  
- **Red dots** = Fraud  
- **Green dots** = Safe  

---

## **🚀 4. How to Run It**
1. **Start the server**  
   ```bash
   cd server
   docker build -t fraud-server .
   docker run -p 8000:8000 fraud-server
   ```

2. **Test with the client**  
   ```bash
   python client/cli.py --amount 2000 --user-id 456
   ```

3. **Open the dashboard**  
   ```bash
   python monitoring/live_dashboard.py
   ```

---

## **🔧 5. Key Things to Remember**
✅ **Fraud detection = AI + Rules** (We combine both)  
✅ **Real-time monitoring** helps catch fraud fast  
✅ **Explainability** (SHAP/LIME) tells **why** a transaction is risky  

---

## **❓ What’s Next?**
- Try adding **new fraud patterns** in `synthetic_data_generator.py`  
- Improve the **XGBoost model** with new features  
- Connect to a **real payment gateway** (Stripe/PayPal)  

Want me to explain any part in more detail? 😊