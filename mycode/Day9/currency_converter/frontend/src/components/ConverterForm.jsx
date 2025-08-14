import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ConverterForm = () => {
  // const [currencies, setCurrencies] = useState([]);
  const [currencies, setCurrencies] = useState(['USD', 'EUR', 'GBP', 'JPY', 'AUD']);
  const [formData, setFormData] = useState({
    amount: '',
    fromCurrency: 'USD',
    toCurrency: 'EUR'
  });
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchCurrencies = async () => {
      try {
        const response = await axios.get('http://localhost:8000/currencies');
        setCurrencies(response.data.common_currencies);
      } catch (err) {
        console.error("Full error details:", error.response || error.message);
        setError('Failed to fetch currencies');
      }
    };
    fetchCurrencies();
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const response = await axios.post('http://localhost:8000/convert', {
        amount: formData.amount,
        from_currency: formData.fromCurrency,
        to_currency: formData.toCurrency
      });
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Conversion failed');
    }
  };

  return (
    <div className="converter-container">
      <h2>Currency Converter</h2>
      {error && <div className="error">{error}</div>}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Amount:</label>
          <input
            type="text"
            name="amount"
            value={formData.amount}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>From:</label>
          <select
            name="fromCurrency"
            value={formData.fromCurrency}
            onChange={handleChange}
          >
            {currencies.map(currency => (
              <option key={`from-${currency}`} value={currency}>
                {currency}
              </option>
            ))}
          </select>
        </div>
        <div className="form-group">
          <label>To:</label>
          <select
            name="toCurrency"
            value={formData.toCurrency}
            onChange={handleChange}
          >
            {currencies.map(currency => (
              <option key={`to-${currency}`} value={currency}>
                {currency}
              </option>
            ))}
          </select>
        </div>
        <button type="submit">Convert</button>
      </form>
      {result && (
        <div className="result">
          <h3>Result:</h3>
          <p>
            {result.original_amount} {result.from_currency} =
            <strong> {result.converted_amount} {result.to_currency}</strong>
          </p>
          <p>Exchange Rate: 1 {result.from_currency} = {result.rate} {result.to_currency}</p>
        </div>
      )}
    </div>
  );
};

export default ConverterForm;

// const ConverterForm = () => {
//   return <div>TEST: Form Component Loaded!</div>;
// };
//
// useEffect(() => {
//   axios.get('http://localhost:8000/currencies')
//     .then(res => console.log("API Success:", res.data))
//     .catch(err => console.error("API Error:", err));
// }, []);