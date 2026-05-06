(function () {
    function loadYoutubeThumbs() {
        document.querySelectorAll("[data-bg-image]").forEach((el) => {
            const url = el.dataset.bgImage;
            if (!url) return;
            const img = new Image();
            img.onload = () => {
                el.style.backgroundImage = `url('${url}')`;
                el.style.backgroundSize = "cover";
                el.style.backgroundPosition = "center";
                el.classList.remove("loading");
                el.classList.add("loaded");
                el.removeAttribute("data-bg-image");
            };
            img.onerror = () => {
                const fallback = url.replace("hqdefault", "mqdefault");
                el.style.backgroundImage = `url('${fallback}')`;
                el.classList.add("loaded");
            };
            img.src = url;
        });
    }

    function loadImages() {
        document.querySelectorAll("img[data-src]").forEach((img) => {
            const src = img.dataset.src;
            if (!src) return;
            const tmp = new Image();
            tmp.onload = () => {
                img.src = src;
                img.removeAttribute("data-src");
                img.classList.remove("loading");
                img.classList.add("loaded");
            };
            tmp.onerror = () => {
                img.classList.remove("loading");
                img.classList.add("error");
            };
            tmp.src = src;
        });
    }

    function captureFrame(video) {
        return new Promise((resolve) => {
            const seekTo = Math.min(1, (video.duration || 10) * 0.1);
            const doCapture = () => {
                try {
                    const canvas = document.createElement("canvas");
                    canvas.width = video.videoWidth || 320;
                    canvas.height = video.videoHeight || 240;
                    canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
                    const dataUrl = canvas.toDataURL("image/jpeg", 0.8);
                    resolve(dataUrl.length < 1500 ? null : dataUrl);
                } catch {
                    resolve(null);
                }
            };

            if (video.readyState >= 2) {
                video.addEventListener("seeked", doCapture, { once: true });
                video.currentTime = seekTo;
            } else {
                video.addEventListener("loadedmetadata", () => {
                    video.addEventListener("seeked", doCapture, { once: true });
                    video.currentTime = seekTo;
                }, { once: true });
            }
        });
    }

    async function loadVideoThumbs() {
        const videos = document.querySelectorAll(".video-thumbnail video");
        const promises = Array.from(videos).map(async (video) => {
            const container = video.closest(".video-thumbnail");
            if (!container) return;

            if (
                container.dataset.bgImage ||
                (container.style.backgroundImage && !container.style.backgroundImage.includes("gradient"))
            ) return;

            const source = video.querySelector("source[data-src]");
            if (source) {
                source.src = source.dataset.src;
                source.removeAttribute("data-src");
            }

            video.preload = "metadata";
            video.muted = true;
            video.load();

            let dataUrl = await captureFrame(video);
            if (!dataUrl) {
                await new Promise((r) => setTimeout(r, 800));
                dataUrl = await captureFrame(video);
            }

            if (dataUrl) {
                container.style.backgroundImage = `url('${dataUrl}')`;
                container.style.backgroundSize = "cover";
                container.style.backgroundPosition = "center";
            }
            container.classList.remove("loading");
            container.classList.add("loaded");
        });

        await Promise.allSettled(promises);
    }

    function initFilters() {
        const filterBtns = document.querySelectorAll(".filter-btn");
        const allItems = document.querySelectorAll(".gallery-item");

        filterBtns.forEach((btn) => {
            btn.addEventListener("click", () => {
                filterBtns.forEach((b) => b.classList.remove("active"));
                btn.classList.add("active");
                const filter = btn.dataset.filter;

                allItems.forEach((item) => {
                    const category = item.dataset.category;
                    const show = filter === "all" || category === filter;
                    if (show) {
                        item.removeAttribute("hidden");
                        item.style.display = "";
                    } else {
                        item.style.display = "none";
                    }
                });
            });
        });
    }

    function initGalleryAssets() {
        loadYoutubeThumbs();
        loadImages();
        loadVideoThumbs();
        initFilters();
    }

    const lightboxModal = document.getElementById("lightboxModal");
    const lightboxImage = document.getElementById("lightboxImage");
    const lightboxYouTube = document.getElementById("lightboxYouTube");
    const lightboxLocalVideo = document.getElementById("lightboxLocalVideo");
    const lightboxVideoSource = document.getElementById("lightboxVideoSource");
    const lightboxClose = document.getElementById("lightboxClose");
    const lightboxPrev = document.getElementById("lightboxPrev");
    const lightboxNext = document.getElementById("lightboxNext");

    let currentIndex = 0;
    let visibleItems = [];

    function updateVisibleItems() {
        visibleItems = Array.from(document.querySelectorAll(".gallery-item"))
            .filter((item) => item.style.display !== "none");
    }

    function openLightbox() {
        lightboxModal.classList.add("active");
        document.body.style.overflow = "hidden";
        document.documentElement.style.overflow = "hidden";
        lightboxClose.focus();
    }

    function closeLightbox() {
        lightboxModal.classList.remove("active");
        lightboxImage.style.display = "none";
        lightboxYouTube.style.display = "none";
        lightboxLocalVideo.style.display = "none";
        lightboxImage.src = "";
        lightboxYouTube.src = "";
        lightboxLocalVideo.pause();
        lightboxVideoSource.src = "";
        document.body.style.overflow = "";
        document.documentElement.style.overflow = "";
    }

    function getYoutubeId(url) {
        if (!url) return null;
        url = url.trim();
        if (/^[a-zA-Z0-9_-]{11}$/.test(url)) return url;

        try {
            const u = new URL(url);
            const embedMatch = u.pathname.match(/\/embed\/([a-zA-Z0-9_-]{11})/);
            if (embedMatch) return embedMatch[1];

            const v = u.searchParams.get("v");
            if (v && /^[a-zA-Z0-9_-]{11}$/.test(v)) return v;

            if (u.hostname.includes("youtu.be")) {
                const id = u.pathname.slice(1).split("?")[0];
                if (/^[a-zA-Z0-9_-]{11}$/.test(id)) return id;
            }

            const shortsMatch = u.pathname.match(/\/shorts\/([a-zA-Z0-9_-]{11})/);
            if (shortsMatch) return shortsMatch[1];

            const liveMatch = u.pathname.match(/\/live\/([a-zA-Z0-9_-]{11})/);
            if (liveMatch) return liveMatch[1];
        } catch {}

        const fallback = url.match(/(?:v=|\/embed\/|youtu\.be\/|\/shorts\/|\/live\/)([a-zA-Z0-9_-]{11})/);
        return fallback ? fallback[1] : null;
    }

    function showLightbox(index) {
        currentIndex = index;
        const item = visibleItems[index];
        if (!item) return;

        const data = item.querySelector(".gallery-data");
        if (!data) return;

        const type = data.dataset.type;
        lightboxImage.style.display = "none";
        lightboxYouTube.style.display = "none";
        lightboxLocalVideo.style.display = "none";
        lightboxYouTube.src = "";
        lightboxLocalVideo.pause();
        lightboxVideoSource.src = "";

        if (type === "video") {
            const videoType = data.dataset.videoType;
            const videoUrl = data.dataset.videoUrl;

            if (videoType === "youtube") {
                const youtubeId = getYoutubeId(videoUrl);
                if (!youtubeId) return;
                lightboxYouTube.src = `https://www.youtube.com/embed/${youtubeId}?rel=0&autoplay=1`;
                lightboxYouTube.style.display = "block";
                openLightbox();
            } else if (videoType === "local") {
                lightboxVideoSource.src = videoUrl;
                lightboxLocalVideo.load();
                lightboxLocalVideo.style.display = "block";
                lightboxLocalVideo.play().catch(() => {});
                openLightbox();
            }
        } else {
            lightboxImage.src = data.dataset.imageUrl;
            lightboxImage.style.display = "block";
            openLightbox();
        }
    }

    function navigate(direction) {
        if (!visibleItems.length) return;
        currentIndex = (currentIndex + direction + visibleItems.length) % visibleItems.length;
        showLightbox(currentIndex);
    }

    document.querySelectorAll(".gallery-item").forEach((item) => {
        item.addEventListener("click", () => {
            updateVisibleItems();
            const idx = visibleItems.indexOf(item);
            if (idx === -1) return;
            showLightbox(idx);
        });

        item.addEventListener("keydown", (e) => {
            if (e.key === "Enter" || e.key === " ") {
                e.preventDefault();
                updateVisibleItems();
                const idx = visibleItems.indexOf(item);
                if (idx === -1) return;
                showLightbox(idx);
            }
        });
    });

    lightboxClose.addEventListener("click", closeLightbox);
    lightboxPrev.addEventListener("click", () => navigate(-1));
    lightboxNext.addEventListener("click", () => navigate(1));

    lightboxModal.addEventListener("click", (e) => {
        if (e.target === lightboxModal) closeLightbox();
    });

    document.addEventListener("keydown", (e) => {
        if (!lightboxModal.classList.contains("active")) return;
        if (e.key === "ArrowLeft") navigate(-1);
        if (e.key === "ArrowRight") navigate(1);
        if (e.key === "Escape") closeLightbox();
    });

    let touchStartX = 0;
    lightboxModal.addEventListener("touchstart", (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });
    lightboxModal.addEventListener("touchend", (e) => {
        const diff = touchStartX - e.changedTouches[0].screenX;
        if (Math.abs(diff) > 50) navigate(diff > 0 ? 1 : -1);
    }, { passive: true });

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initGalleryAssets);
    } else {
        initGalleryAssets();
    }

    window.addEventListener("pageshow", (e) => {
        if (e.persisted) initGalleryAssets();
    });
})();
