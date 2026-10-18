const PALETTES = [
  "linear-gradient(135deg,#00ffcc 0%,#00d9ff 100%)",
  "linear-gradient(135deg,#ff006e 0%,#ff80b0 100%)",
  "linear-gradient(135deg,#ffd60a 0%,#ff9500 100%)",
  "linear-gradient(135deg,#8338ec 0%,#3a0ca3 100%)",
  "linear-gradient(135deg,#06ffa5 0%,#0096c7 100%)",
  "linear-gradient(135deg,#ff1744 0%,#ff6e6e 100%)",
  "linear-gradient(135deg,#00d9ff 0%,#b3cc00 100%)",
  "linear-gradient(135deg,#00d9ff 0%,#006b84 100%)"
];

function openTeam(card) {
  const takimId = card.dataset.takim;
  const takimAd = card.dataset.takimAd;

  fetch(`/api/takim/${takimId}/oyuncular/`)
    .then((r) => r.json())
    .then((data) => renderLightbox({
      ad: takimAd,
      oyuncular: data.oyuncular
    }))
    .catch((err) => {
      console.error("Oyuncular yuklenirken hata:", err);
      renderLightbox({
        ad: takimAd,
        oyuncular: []
      });
    });
}

function renderLightbox(takim) {
  document.getElementById("lbTeamName").textContent = takim.ad;
  document.getElementById("lbTeamCategory").textContent = "Oyuncular";

  const icon = document.getElementById("lbIcon");
  icon.textContent = "⚽";
  icon.style.background = "linear-gradient(135deg,#00ffcc 0%,#00d9ff 100%)";

  const grid = document.getElementById("lbPlayersGrid");
  grid.innerHTML = "";

  if (!takim.oyuncular || takim.oyuncular.length === 0) {
    grid.innerHTML = `
      <div class="lb-empty" style="grid-column:1/-1">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/>
        </svg>
        <p>Bu takimda henuz oyuncu bulunmuyor.</p>
      </div>`;
  } else {
    takim.oyuncular.forEach((oyuncu, i) => {
      const bg = PALETTES[i % PALETTES.length];
      const delay = `${i * 35}ms`;
      grid.innerHTML += `
        <div class="lb-player-card" style="animation-delay:${delay}">
          <div class="lb-player-avatar" style="background:${bg}">
            <span class="lb-player-number">${oyuncu.numara || "—"}</span>
          </div>
          <div class="lb-player-info">
            <h3>${oyuncu.ad}</h3>
            <div class="lb-player-pos">${oyuncu.pozisyon}</div>
            <span class="lb-player-badge">#${oyuncu.numara || "—"}</span>
          </div>
        </div>`;
    });
  }

  document.getElementById("lightboxOverlay").classList.add("active");
  document.body.style.overflow = "hidden";
  document.getElementById("lightboxPanel").scrollTop = 0;
}

function closeLightbox() {
  document.getElementById("lightboxOverlay").classList.remove("active");
  document.body.style.overflow = "";
}

function closeLightboxOutside(e) {
  if (e.target === document.getElementById("lightboxOverlay")) closeLightbox();
}

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeLightbox();
});
