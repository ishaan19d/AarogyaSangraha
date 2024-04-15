const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

document.querySelector(".name").onmouseover = function (event) {
    let i = 0;
    const interval = setInterval(() => {
        event.target.innerText = event.target.innerText.split("")
            .map((letter, index) => {
                if (index < i) {
                    return event.target.dataset.value[index];
                }
                return letters[Math.floor(Math.random() * letters.length)];
            })
            .join("");

        if (i >= event.target.dataset.value.length) clearInterval(interval);
        i += 1 / 3;
    }, 30);
};

async function enterTreatmentId() {
  const treatmentId = prompt("Please enter the treatment ID:");
  if (treatmentId) {
      try {
          const response = await fetch('http://127.0.0.1:8000/treatment/verifyTreatment', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': '{{ csrf_token }}'
              },
              body: JSON.stringify({ 'treatmentId': treatmentId })
          });

          const data = await response.json();

          if (data.message === 'Treatment verified!') {
              Swal.fire({
                  title: 'Treatment verified!',
                  html: `Date: ${data.date}<br>Patient Name: ${data.patient_name}<br>Hospital Visited: ${data.hospital_name}<br>Department Concerned: ${data.department}<br>Treated By: ${data.doc_name}`,
                  icon: 'success'
              });
          } else {
              Swal.fire({
                  title: 'Forged!',
                  text: data.message,
                  icon: 'error'
              });
          }
      } catch (error) {
          console.error('Error:', error);
          Swal.fire({
              title: 'Forged!',
              text: data.message,
              icon: 'error'
          });
      }
  }
}