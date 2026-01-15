# CCTV Server

Server streaming CCTV menggunakan [go2rtc](https://github.com/AlexxIT/go2rtc).

## Instalasi

```bash
# Download go2rtc (macOS ARM64)
curl -L -o go2rtc.zip https://github.com/AlexxIT/go2rtc/releases/latest/download/go2rtc_mac_arm64.zip
unzip go2rtc.zip && rm go2rtc.zip && chmod +x go2rtc
```

## Jalankan

```bash
./go2rtc
```

## Akses

- Web UI: http://localhost:1984
- HLS: http://localhost:1984/api/stream.m3u8?src=camera_name
- RTSP: rtsp://localhost:8554/camera_name

## Konfigurasi

Edit `go2rtc.yaml` untuk menambah stream RTSP.
