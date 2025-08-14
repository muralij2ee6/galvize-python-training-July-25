import React from 'react';
import ConverterForm from './components/ConverterForm';
import './styles.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Currency Converter</h1>
      </header>
      <main>
        <ConverterForm />
      </main>
    </div>
  );
}

export default App;

// function App() {
//   return (
//     <div style={{ padding: '20px' }}>
//       <h1>Currency Converter</h1>
//       <p>If you see this, React is working!</p>
//     </div>
//   );
// }
// export default App;