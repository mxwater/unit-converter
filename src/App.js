import React, { useState } from "react";
import "./App.css";

function App() {
  // State variables for managing input, conversion type, and result
  const [conversionType, setConversionType] = useState("Temperature");
  const [value, setValue] = useState("");
  const [result, setResult] = useState("");

  // Function to handle conversions
  const handleConvert = () => {
    const numericValue = parseFloat(value); // Convert input to a number

    if (isNaN(numericValue)) {
      setResult("Please enter a valid number.");
      return;
    }

    let conversionResult = "";
    if (conversionType === "Temperature") {
      conversionResult = `${numericValue}°C = ${(numericValue * 9/5 + 32).toFixed(2)}°F`;
    } else if (conversionType === "Weight") {
      conversionResult = `${numericValue} kg = ${(numericValue * 2.20462).toFixed(2)} lbs`;
    } else if (conversionType === "Measurement") {
      conversionResult = `${numericValue} meters = ${(numericValue * 3.28084).toFixed(2)} feet`;
    } else {
      conversionResult = "Invalid conversion type.";
    }

    setResult(conversionResult); // Update the result
  };

  return (
    <div className="App">
      <h1>A Lifesaver App for a Brazilian Living in the US</h1>

      {/* Dropdown to select conversion type */}
      <label htmlFor="conversionType">Choose a type of conversion:</label>
      <select
        id="conversionType"
        value={conversionType}
        onChange={(e) => setConversionType(e.target.value)}
      >
        <option value="Temperature">Temperature</option>
        <option value="Weight">Weight</option>
        <option value="Measurement">Measurement</option>
      </select>

      {/* Input field for the value */}
      <label htmlFor="valueToConvert">Enter a value:</label>
      <input
        type="number"
        id="valueToConvert"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder="Enter value here"
      />

      {/* Convert button */}
      <button onClick={handleConvert}>Convert</button>

      {/* Display the result */}
      <div className="result">
        <h3>Result:</h3>
        <p>{result}</p>
      </div>
    </div>
  );
}

export default App;
