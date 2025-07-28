export function loadPage(container, next) {
  container.innerHTML = `
    <div style="padding: 40px; color: black; background: white; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
      <p style="font-size: 18px;">Ist Deutsch deine Muttersprache??</p>
      <select id="dropdown" style="font-size: 16px; padding: 10px; margin: 20px 0;">
        <option value="" disabled selected>Select...</option>
        
          <option value="Ja">Ja</option>
        
          <option value="Nein">Nein</option>
        
      </select>
      <button id="nextBtn" disabled style="padding: 10px 20px; font-size: 16px; background: #007BFF; color: white; border: none; border-radius: 6px;">
        Next
      </button>
    </div>
  `;

  const dropdown = document.getElementById("dropdown");
  const btn = document.getElementById("nextBtn");
  const start = Date.now();

  dropdown.addEventListener("change", () => {
    btn.disabled = !dropdown.value;
  });

  btn.addEventListener("click", () => {
    const selected = dropdown.value;
    const duration = Date.now() - start;

    const data = {
      : selected,
      _time: duration
    };

    jatos.appendResultData(data);
    window.jatosData = { ...(window.jatosData || {}), ...data };

    next();
  });
}