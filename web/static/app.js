document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const btn = document.getElementById('predict-btn');
    const btnText = btn.querySelector('.btn-text');
    const loading = btn.querySelector('.loading');
    const resultSection = document.getElementById('result-section');
    const resultClass = document.getElementById('result-class');
    const confidenceBar = document.getElementById('confidence-bar');
    const confidenceValue = document.getElementById('confidence-value');
  
    const probBars = {
      normal: document.getElementById('prob-normal'),
      hernia: document.getElementById('prob-hernia'),
      spondy: document.getElementById('prob-spondy')
    };
    const probVals = {
      normal: document.getElementById('prob-normal-val'),
      hernia: document.getElementById('prob-hernia-val'),
      spondy: document.getElementById('prob-spondy-val')
    };
  
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
  
      // Show loading
      btn.disabled = true;
      btnText.classList.add('hidden');
      loading.classList.remove('hidden');
  
      // Collect values
      const data = {
        pelvic_incidence: parseFloat(document.getElementById('pelvic_incidence').value),
        pelvic_tilt: parseFloat(document.getElementById('pelvic_tilt').value),
        lumbar_lordosis_angle: parseFloat(document.getElementById('lumbar_lordosis_angle').value),
        sacral_slope: parseFloat(document.getElementById('sacral_slope').value),
        pelvic_radius: parseFloat(document.getElementById('pelvic_radius').value),
        degree_spondylolisthesis: parseFloat(document.getElementById('degree_spondylolisthesis').value)
      };
  
      try {
        const response = await fetch('http://127.0.0.1:8000/predict', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });
      
        if (!response.ok) throw new Error('Server error: ' + response.status);
      
        const result = await response.json();
      
        // Show result section
        resultSection.classList.remove('hidden');
        
        // Main class
        resultClass.textContent = result.class_name;
        
        let color = '#22c55e'; // green default
        if (result.class_name === 'Hernia') color = '#f59e0b';
        if (result.class_name === 'Spondylolisthesis') color = '#ef4444';
        
        resultClass.style.color = color;
        
        // Confidence (max prob)
        const confPercent = (result.confidence * 100).toFixed(1);
        confidenceBar.style.width = `${confPercent}%`;
        confidenceBar.style.background = `linear-gradient(90deg, ${color}, #a5b4fc)`;
        confidenceValue.textContent = `${confPercent}% confidence`;
      
        // All probabilities
        const probs = result.probabilities;
        probBars.normal.style.width = `${probs[0] * 100}%`;
        probBars.hernia.style.width = `${probs[1] * 100}%`;
        probBars.spondy.style.width = `${probs[2] * 100}%`;
      
        probVals.normal.textContent = `${(probs[0] * 100).toFixed(1)}%`;
        probVals.hernia.textContent = `${(probs[1] * 100).toFixed(1)}%`;
        probVals.spondy.textContent = `${(probs[2] * 100).toFixed(1)}%`;
      
      } catch (err) {
        alert('Error: Could not get prediction.\n' + err.message);
      } finally {
        btn.disabled = false;
        btnText.classList.remove('hidden');
        loading.classList.add('hidden');
      }
    });
  });