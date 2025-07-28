export function loadPage(container, next) {
  container.innerHTML = `
    <div style="padding: 40px; color: black; background: white; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
      <p style="font-size: 18px;">Geburtsdatum</p>
      <input type="date" id="dobInput" style="font-size: 16px; padding: 10px; margin: 20px 0;">
      <button id="nextBtn" disabled style="padding: 10px 20px; font-size: 16px; background: #007BFF; color: white; border: none; border-radius: 6px;">Next</button>
    </div>
  `;

  const btn = document.getElementById('nextBtn');
  const dob = document.getElementById('dobInput');
  const start = Date.now();

  dob.addEventListener('change', () => {
    btn.disabled = !dob.value;
  });

  btn.addEventListener('click', () => {
    const birthDate = new Date(dob.value);
    const today = new Date();
    let age = today.getFullYear() - birthDate.getFullYear();
    const m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }

    const duration = Date.now() - start;

    const data = {
      participant_age: age,
      dob_response_time: duration
    };

    jatos.appendResultData(data);
    window.jatosData = { ...(window.jatosData || {}), ...data };

    next();
  });
}