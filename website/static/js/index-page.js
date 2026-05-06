(function () {
    "use strict";

    var slides = document.querySelectorAll(".slide");
    var dotsContainer = document.getElementById("dotsContainer");
    var prevBtn = document.getElementById("sliderPrev");
    var nextBtn = document.getElementById("sliderNext");
    var total = slides.length;
    var current = 0;
    var timer = null;
    var INTERVAL = 5000;

    if (total === 0) return;

    var dots = [];
    slides.forEach(function (_, i) {
        var dot = document.createElement("span");
        dot.className = "dot";
        dot.addEventListener("click", function () { goTo(i); resetTimer(); });
        dotsContainer.appendChild(dot);
        dots.push(dot);
    });

    function goTo(n) {
        current = ((n % total) + total) % total;
        slides.forEach(function (s, i) { s.classList.toggle("active", i === current); });
        dots.forEach(function (d, i) { d.classList.toggle("active", i === current); });
    }

    function resetTimer() {
        clearInterval(timer);
        timer = setInterval(function () { goTo(current + 1); }, INTERVAL);
    }

    if (prevBtn) prevBtn.addEventListener("click", function () { goTo(current - 1); resetTimer(); });
    if (nextBtn) nextBtn.addEventListener("click", function () { goTo(current + 1); resetTimer(); });

    document.addEventListener("keydown", function (e) {
        if (e.key === "ArrowLeft") { goTo(current - 1); resetTimer(); }
        if (e.key === "ArrowRight") { goTo(current + 1); resetTimer(); }
    });

    goTo(0);
    resetTimer();

    var haberler = window.haberlerData || [];
    var overlay = document.getElementById("newsDetailPanel");
    var ndClose = document.getElementById("ndCloseBtn");
    var cardRow = document.getElementById("newsCardsRow");

    function openDetail(id) {
        var haber = haberler.find(function (h) { return h.id === id; });
        if (!haber) return;

        var cover = document.getElementById("detailCover");
        cover.style.background = haber.kapak
            ? "url('" + haber.kapak + "') center/cover no-repeat"
            : "linear-gradient(135deg,#00ffcc 0%,#00d9ff 100%)";

        document.getElementById("detailDate").textContent = haber.tarih;
        document.getElementById("detailTitle").textContent = haber.baslik;
        document.getElementById("detailTags").innerHTML = (haber.etiketler || [])
            .map(function (t) { return "<span class='nd-tag'>" + t + "</span>"; })
            .join("");

        var raw = (haber.icerik || "").replace(/\\n/g, "\n");
        var paragraflar = raw.split(/\n\n+/).filter(function (p) { return p.trim(); });
        document.getElementById("detailBody").innerHTML = paragraflar.length
            ? paragraflar.map(function (p) { return "<p>" + p.trim() + "</p>"; }).join("")
            : "<p>" + (haber.icerik || "") + "</p>";

        overlay.classList.add("open");
        document.body.style.overflow = "hidden";
    }

    function closeDetail() {
        overlay.classList.remove("open");
        document.body.style.overflow = "";
    }

    if (cardRow) {
        cardRow.addEventListener("click", function (e) {
            var btn = e.target.closest(".read-more-btn");
            if (btn) openDetail(Number(btn.dataset.newsId));
        });
    }
    if (ndClose) ndClose.addEventListener("click", closeDetail);
    if (overlay) {
        overlay.addEventListener("click", function (e) {
            if (e.target === overlay) closeDetail();
        });
    }
    document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && overlay.classList.contains("open")) closeDetail();
    });
})();
