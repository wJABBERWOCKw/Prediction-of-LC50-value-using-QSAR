 document.querySelector('form').onsubmit = function(event) {
            event.preventDefault(); // Prevent page from reloading on form submission
            const form = event.target;
            const formData = new FormData(form);

            fetch('/predict', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('prediction_result').innerText = 'LC50 Prediction: ' + data.LC50_prediction;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        };