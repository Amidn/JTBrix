export function loadPage(container, next) {
  container.innerHTML = `
    <div class="screen text-input-screen" style="height: 100vh; background: white; color: black; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px;">
      <p style="font-size: 20px; margin-bottom: 20px;">Geben Sie bitte einen Codenamen für sich ein:</p>
      <input type="text" id="user-input" placeholder="Your full name"
             style="width: 60%; padding: 15px; font-size: 18px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 6px;" />
      <button id="next-button" disabled
              style="padding: 12px 24px; font-size: 18px; background: #007BFF; color: white; border: none; border-radius: 6px;">
        Weiter
      </button>
    </div>
  `;

  const input = document.getElementById("user-input");
  const nextBtn = document.getElementById("next-button");
  const startTime = performance.now();

  input.addEventListener("input", () => {
    nextBtn.disabled = input.value.trim() === "";
  });

  nextBtn.addEventListener("click", () => {
    const trimmedResponse = input.value.trim();
    const duration = Math.round(performance.now() - startTime);

    const data = {
      participant_first_name: trimmedResponse,
      participant_first_name_time: duration
    };

    jatos.appendResultData(data);
    window.jatosData = { ...(window.jatosData || {}), ...data };

    next();
  });
}