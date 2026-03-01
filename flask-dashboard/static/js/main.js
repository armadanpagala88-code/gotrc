// CCTV Dashboard - Flask Version
let players = {};
let onlineCount = 0;
let currentLayout = '3x3';

// Update clock
function updateClock() {
    const now = new Date();
    document.getElementById('clock').textContent = now.toLocaleTimeString('id-ID');
    const dateEl = document.getElementById('date');
    if (dateEl) {
        dateEl.textContent = now.toLocaleDateString('id-ID', {
            weekday: 'short', day: 'numeric', month: 'short', year: 'numeric'
        });
    }
}
setInterval(updateClock, 1000);
updateClock();

// Set grid layout
function setLayout(layout) {
    currentLayout = layout;
    const grid = document.getElementById('grid');
    grid.className = `grid grid-${layout}`;

    // Update active button
    document.querySelectorAll('.layout-btns .btn').forEach((btn, i) => {
        const layouts = ['2x2', '3x3', '4x4'];
        btn.classList.toggle('active', layouts[i] === layout);
    });
}

// Initialize HLS players
function initPlayers() {
    cameras.forEach((cam, index) => {
        setTimeout(() => initHLS(cam.id), index * 200);
    });
}

function initHLS(camId) {
    const video = document.getElementById(`video-${camId}`);
    const status = document.getElementById(`status-${camId}`);

    if (!video || !Hls.isSupported()) return;

    const hls = new Hls({
        enableWorker: true,
        lowLatencyMode: true
    });

    hls.loadSource(`${GO2RTC_URL}/api/stream.m3u8?src=${camId}`);
    hls.attachMedia(video);

    hls.on(Hls.Events.MANIFEST_PARSED, () => {
        video.play();
        status.textContent = 'LIVE';
        status.className = 'badge';
        onlineCount++;
        document.getElementById('online').textContent = onlineCount;
    });

    hls.on(Hls.Events.ERROR, (event, data) => {
        if (data.fatal) {
            status.textContent = 'Offline';
            status.className = 'badge error';
        }
    });

    players[camId] = hls;
}

// Screenshot
function screenshot(camId) {
    const video = document.getElementById(`video-${camId}`);
    if (!video) return;

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);

    const link = document.createElement('a');
    link.download = `${camId}_${Date.now()}.png`;
    link.href = canvas.toDataURL();
    link.click();
}

// Fullscreen
function fullscreen(camId) {
    const box = document.getElementById(`box-${camId}`);
    if (box) {
        if (document.fullscreenElement) {
            document.exitFullscreen();
        } else {
            box.requestFullscreen();
        }
    }
}

// Initialize on load
document.addEventListener('DOMContentLoaded', initPlayers);
