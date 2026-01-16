# 🎥 CCTV Server - go2rtc

Server streaming CCTV menggunakan go2rtc dengan dashboard web custom.

## 📋 Fitur

- ✅ **Multi-Camera Support** - 5 kamera CCTV
- ✅ **Browser Compatible** - Transcoding H.264 untuk playback di browser
- ✅ **HLS Streaming** - Support multi-viewer dengan low latency
- ✅ **Dashboard Web** - Interface modern dengan drag & drop
- ✅ **Bandwidth Monitor** - Real-time bandwidth per kamera
- ✅ **Camera Groups** - Kelompokkan kamera berdasarkan lokasi
- ✅ **Snapshot** - Capture dan download screenshot
- ✅ **Mobile Responsive** - Tampilan optimal di HP/tablet
- ✅ **Nginx Reverse Proxy** - Dengan Basic Authentication

## 🚀 Quick Start

### 1. Jalankan go2rtc
```bash
cd /Volumes/Untitled/PROJECT/gotrc
./go2rtc
```

### 2. Akses Dashboard
| URL | Keterangan |
|-----|------------|
| http://localhost:8080/dashboard.html | Dashboard CCTV |
| http://localhost:8081 | go2rtc Web UI (dengan login) |
| http://localhost:1984 | go2rtc API (direct) |

### 3. Login
- **Username:** admin
- **Password:** 2025-CCTVknw

## 📹 Daftar Kamera

| Nama | Stream | Port | Status |
|------|--------|------|--------|
| Camera 2 | camera2_web | 4554 | ✅ |
| Camera 3 | camera3_web | 6554 | ✅ |
| Pintu Masuk 1B | pintu_masuk_1b_web | 8554 | ⚠️ |
| Pintu Keluar 2B | pintu_keluar_2b_web | 7554 | ✅ |
| Pintu Keluar 2A | pintu_keluar_2a_web | 5554 | ✅ |

## 🔗 URL Stream

### Browser (HLS)
```
http://localhost:1984/api/stream.m3u8?src=camera2_web
http://localhost:1984/api/stream.m3u8?src=camera3_web
```

### RTSP (VLC)
```
rtsp://localhost:8554/camera2_web
rtsp://localhost:8554/camera3_web
```

### WebRTC
```
http://localhost:1984/stream.html?src=camera2_web
```

## 📁 Struktur File

```
gotrc/
├── go2rtc           # Binary executable
├── go2rtc.yaml      # Konfigurasi streams
├── dashboard.html   # Dashboard web custom
└── README.md        # Dokumentasi
```

## ⚙️ Konfigurasi

### go2rtc.yaml
- **streams** - Definisi kamera RTSP
- **ffmpeg** - Hardware acceleration (VideoToolbox)
- **api** - Web UI port 1984
- **rtsp** - RTSP server port 8554
- **webrtc** - WebRTC port 8555

### Nginx
- **Port 8081** - Reverse proxy dengan Basic Auth
- **Config:** `/opt/homebrew/etc/nginx/servers/go2rtc.conf`
- **Password:** `/opt/homebrew/etc/nginx/.htpasswd`

## 🛠️ Troubleshooting

### Stream tidak muncul
1. Cek go2rtc berjalan: `pgrep go2rtc`
2. Cek log: http://localhost:1984/log.html
3. Restart: `pkill go2rtc && ./go2rtc`

### 401 Unauthorized
- Password kamera salah, cek `go2rtc.yaml`

### Transcoding lambat
- FFmpeg menggunakan hardware acceleration (VideoToolbox)
- Pastikan stream menggunakan `_web` suffix

## 📱 Mobile Access

Dashboard responsive, bisa diakses dari HP:
1. Pastikan HP terhubung ke jaringan yang sama
2. Ganti `localhost` dengan IP komputer server
3. Contoh: `http://192.168.1.100:8080/dashboard.html`

## 🔒 Security

- Gunakan port 8081 untuk akses dengan login
- Jangan expose port 1984 ke internet tanpa authentication
- Untuk akses dari luar, setup VPN atau port forwarding dengan HTTPS

---
**go2rtc version:** 1.9.13  
**Platform:** macOS ARM64
