
const circularProgressElements = document.querySelectorAll('.circular-progress-1, .circular-progress-2, .circular-progress-3');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      if (entry.target.classList.contains('circular-progress-1')) {
        runProgress1();
      } else if (entry.target.classList.contains('circular-progress-2')) {
        runProgress2();
      } else if (entry.target.classList.contains('circular-progress-3')) {
        runProgress3();
      }
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 1 });

circularProgressElements.forEach(element => observer.observe(element));

// Progress functions
function runProgress1() {
  let circularProgress_1 = document.querySelector(".circular-progress-1"),
    progressValue_1 = document.querySelector(".progress-value-1");
  let progressStartValue_1 = 0,
    progressEndValue_1 = Number(patientCount),
    speed_1 = 100;
    console.log(patientCount);

  let progress_1 = setInterval(() => {
    progressStartValue_1++;
    progressValue_1.textContent = `${progressStartValue_1}`
    circularProgress_1.style.background = `conic-gradient(black ${progressStartValue_1 * 360 / progressEndValue_1}deg, #ededed 0deg)`
    if (progressStartValue_1 === progressEndValue_1) {
      clearInterval(progress_1);
    }
  }, speed_1);
}

function runProgress2() {
  let circularProgress_2 = document.querySelector(".circular-progress-2"),
    progressValue_2 = document.querySelector(".progress-value-2");
  let progressStartValue_2 = 0,
    progressEndValue_2 = Number(medicalCount),
    speed_2 = 100;

  let progress_2 = setInterval(() => {
    progressStartValue_2++;
    progressValue_2.textContent = `${progressStartValue_2}`
    circularProgress_2.style.background = `conic-gradient(black ${progressStartValue_2 * 360 / progressEndValue_2}deg, #ededed 0deg)`
    if (progressStartValue_2 === progressEndValue_2) {
      clearInterval(progress_2);
    }
  }, speed_2);
}

function runProgress3() {
  let circularProgress_3 = document.querySelector(".circular-progress-3"),
    progressValue_3 = document.querySelector(".progress-value-3");
  let progressStartValue_3 = 0,
    progressEndValue_3 = Number(hospitalCount),
    speed_3 = 100;

  let progress_3 = setInterval(() => {
    progressStartValue_3++;
    progressValue_3.textContent = `${progressStartValue_3}`
    circularProgress_3.style.background = `conic-gradient(black ${progressStartValue_3 * 360 / progressEndValue_3}deg, #ededed 0deg)`
    if (progressStartValue_3 === progressEndValue_3) {
      clearInterval(progress_3);
    }
  }, speed_3);
}

const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

document.querySelector(".section#company-name").onmouseover = function (event) {
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
