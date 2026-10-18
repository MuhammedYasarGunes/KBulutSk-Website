(function () {
    "use strict";

    // ---------------- SLIDER ----------------
    var slides = document.querySelectorAll(".slide");
    var dotsContainer = document.getElementById("dotsContainer");
    var prevBtn = document.getElementById("sliderPrev");
    var nextBtn = document.getElementById("sliderNext");

    if (!dotsContainer || slides.length === 0) return;

    var total = slides.length;
    var current = 0;
    var timer;
    var INTERVAL = 5000;

    var dots = [];

    // 🔥 FIX: tekrar çalışmada dot birikmesini engelle
    dotsContainer.innerHTML = "";

    function goTo(n) {
        current = ((n % total) + total) % total;

        for (var i = 0; i < total; i++) {
            slides[i].classList.toggle("active", i === current);
            dots[i].classList.toggle("active", i === current);
        }
    }

    function resetTimer() {
        if (timer) clearInterval(timer);
        timer = setInterval(function () {
            goTo(current + 1);
        }, INTERVAL);
    }

    // dots oluştur
    for (var i = 0; i < total; i++) {
        (function (index) {
            var dot = document.createElement("span");
            dot.className = "dot";

            dot.addEventListener("click", function () {
                goTo(index);
                resetTimer();
            });

            dotsContainer.appendChild(dot);
            dots.push(dot);
        })(i);
    }

    if (prevBtn) {
        prevBtn.addEventListener("click", function () {
            goTo(current - 1);
            resetTimer();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener("click", function () {
            goTo(current + 1);
            resetTimer();
        });
    }

    document.addEventListener("keydown", function (e) {
        if (e.key === "ArrowLeft") {
            goTo(current - 1);
            resetTimer();
        }
        if (e.key === "ArrowRight") {
            goTo(current + 1);
            resetTimer();
        }
    });

    goTo(0);
    resetTimer();

    // ---------------- NEWS DETAIL ----------------
    var haberler = window.haberlerData || [];
    var overlay = document.getElementById("newsDetailPanel");
    var ndClose = document.getElementById("ndCloseBtn");
    var cardRow = document.getElementById("newsCardsRow");

    function openDetail(id) {
        var haber = null;

        for (var i = 0; i < haberler.length; i++) {
            if (Number(haberler[i].id) === Number(id)) {
                haber = haberler[i];
                break;
            }
        }

        if (!haber || !overlay) return;

        var cover = document.getElementById("detailCover");
        if (cover) {
            cover.style.background = haber.kapak
                ? "url('" + haber.kapak + "') center/cover no-repeat"
                : "linear-gradient(135deg,#00ffcc 0%,#00d9ff 100%)";
        }

        var dateEl = document.getElementById("detailDate");
        var titleEl = document.getElementById("detailTitle");
        var tagsEl = document.getElementById("detailTags");
        var bodyEl = document.getElementById("detailBody");

        if (dateEl) dateEl.textContent = haber.tarih || "";
        if (titleEl) titleEl.textContent = haber.baslik || "";

        if (tagsEl) {
            var tags = haber.etiketler || [];
            var html = "";

            for (var t = 0; t < tags.length; t++) {
                html += "<span class='nd-tag'>" + tags[t] + "</span>";
            }

            tagsEl.innerHTML = html;
        }

        if (bodyEl) {
            var raw = (haber.icerik || "").replace(/\\n/g, "\n");
            var parts = raw.split(/\n\n+/);

            var html = "";
            for (var p = 0; p < parts.length; p++) {
                if (parts[p].trim()) {
                    html += "<p>" + parts[p].trim() + "</p>";
                }
            }

            bodyEl.innerHTML = html || "<p>" + (haber.icerik || "") + "</p>";
        }

        overlay.classList.add("open");
        document.body.style.overflow = "hidden";
    }

    function closeDetail() {
        if (!overlay) return;
        overlay.classList.remove("open");
        document.body.style.overflow = "";
    }

    if (cardRow) {
        cardRow.addEventListener("click", function (e) {
            var btn = e.target.closest(".read-more-btn");
            if (btn) openDetail(btn.dataset.newsId);
        });
    }

    if (ndClose) {
        ndClose.addEventListener("click", closeDetail);
    }

    if (overlay) {
        overlay.addEventListener("click", function (e) {
            if (e.target === overlay) closeDetail();
        });
    }

    document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") closeDetail();
    });
})();