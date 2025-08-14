const ResultDisplay = ({ result }) => {
  if (!result) return null;

  return (
    <div className="result-display">
      <h3>Conversion Result</h3>
      <p>
        {result.original_amount} {result.from_currency} =
        <strong> {result.converted_amount} {result.to_currency}</strong>
      </p>
      <p>Exchange Rate: 1 {result.from_currency} = {result.rate} {result.to_currency}</p>
    </div>
  );
};

export default ResultDisplay;