export function loadPage(container, next) {
  container.innerHTML = `
    <div style="padding: 40px; color: black; background: white; height: 100%;">
      <p style="font-size: 18px;"> Liebe Teilnehmenden, Vielen Dank für dein Interesse! In dieser Studie geht es um die Beurteilungen von wahren und falschen Aussagen. Die Studie dauert ungefähr 5 Minuten. Mit Ihrer Teilnahme erklären Sie sich einverstanden, dass Ihre Daten pseudonymisiert und anonym verarbeitet werden. Ihre Daten werden gemäß DSGVO vertraulich behandelt und geschützt. Sie können Ihre Zustimmung jederzeit ohne Angabe von Gründen widerrufen. Verantwortlich für diese Studie sind Prof. Dr. Hannes Rakoczy, Dr. Marina Proft und Saba Amirhaftehran (Universität Göttingen)..</p>

      
        <label>
          <input type="checkbox" class="consent-checkbox"> Hiermit bestätige ich, dass ich mindestens 18 Jahre alt bin und mit der Teilnahme an dieser Studie einverstanden bin.
        </label><br>
      
        <label>
          <input type="checkbox" class="consent-checkbox"> Hiermit stimme ich der Datenerhebung und -verarbeitung zu gemäß Artikel 6 DSGVO.
        </label><br>
      

      <br>
      <button id="startBtn" disabled
              style="padding: 10px 20px; font-size: 16px; background: #28a745; color: white; border: none; border-radius: 6px;">
        Start
      </button>
    </div>
  `;

  const btn = document.getElementById("startBtn");
  const boxes = document.querySelectorAll(".consent-checkbox");

  function toggleButton() {
    btn.disabled = ![...boxes].every(b => b.checked);
  }

  boxes.forEach(cb => cb.addEventListener("change", toggleButton));
  toggleButton();

  btn.addEventListener("click", () => {
    next(); // Load next page
  });

  history.replaceState(null, "", window.location.href);
  window.addEventListener("popstate", () => {
    location.replace(window.location.href);
  });
}