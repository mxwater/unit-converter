
document.addEventListener('DOMContentLoaded', () => {
 
    const convertButton = document.getElementById('convertButton'); 
    const conversionType = document.getElementById('conversionType'); 
    const valueToConvert = document.getElementById('valueToConvert'); 
    const resultText = document.getElementById('resultText'); 
  
   
    convertButton.addEventListener('click', () => {
      const type = conversionType.value; 
      const value = parseFloat(valueToConvert.value); 


      if (isNaN(value)) {
        resultText.textContent = 'Please enter a valid number.';
        return;
      }
  
      
      let result;
      if (type === 'Temperature') {
        result = `${value}°C = ${(value * 9/5 + 32).toFixed(2)}°F`; 
      } else if (type === 'Weight') {
        result = `${value} kg = ${(value * 2.20462).toFixed(2)} lbs`; 
      } else if (type === 'Measurement') {
        result = `${value} meters = ${(value * 3.28084).toFixed(2)} feet`; 
      } else {
        result = 'Invalid conversion type.';
      }
  

      resultText.textContent = result;
    });
  });
  