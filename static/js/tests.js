// test.js — countdown timer + answer tracking
document.addEventListener('DOMContentLoaded', function () {
  const timerEl = document.getElementById('testTimer');
  const form = document.getElementById('testForm');
  const answeredEl = document.getElementById('answeredCount');
  const totalEl = document.getElementById('totalCount');

  // Timer
  if (timerEl) {
    const minutes = parseInt(timerEl.dataset.minutes || '15');
    let seconds = minutes * 60;

    const tick = setInterval(function () {
      seconds--;
      const m = Math.floor(seconds / 60);
      const s = seconds % 60;
      timerEl.textContent = `${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;

      if (seconds <= 60) timerEl.classList.add('warning');

      if (seconds <= 0) {
        clearInterval(tick);
        if (form) form.submit();
      }
    }, 1000);
  }

  // Track answered questions
  if (form && answeredEl && totalEl) {
    const radios = form.querySelectorAll('input[type="radio"]');
    const groups = new Set([...radios].map(r => r.name));
    totalEl.textContent = groups.size;

    radios.forEach(function (radio) {
      radio.addEventListener('change', function () {
        const answered = new Set(
          [...form.querySelectorAll('input[type="radio"]:checked')].map(r => r.name)
        ).size;
        answeredEl.textContent = answered;
      });
    });
  }
});