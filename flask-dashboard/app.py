from flask import Flask, render_template, jsonify, redirect, url_for
import requests

app = Flask(__name__)

# Configuration
# URL go2rtc yang bisa diakses dari browser user (bukan localhost!)
GO2RTC_URL = "http://36.93.71.27:1984"

# Camera data
CAMERAS = [
    {"id": "labkesda1", "name": "Labkesda 1", "group": "Labkesda"},
    {"id": "labkesda2", "name": "Labkesda 2", "group": "Labkesda"},
    {"id": "sosial1", "name": "Sosial 1", "group": "Dinsos"},
    {"id": "sosial2", "name": "Sosial 2", "group": "Dinsos"},
    {"id": "asambu1", "name": "Asambu 1", "group": "Asambu"},
    {"id": "asambu2", "name": "Asambu 2", "group": "Asambu"},
    {"id": "unaaha1", "name": "Kel. Unaaha 1", "group": "Kel. Unaaha"},
    {"id": "unaaha2", "name": "Kel. Unaaha 2", "group": "Kel. Unaaha"},
    {"id": "pasar_asinua1", "name": "Pasar Asinua 1", "group": "Pasar Asinua"},
    {"id": "pasar_asinua2", "name": "Pasar Asinua 2", "group": "Pasar Asinua"},
    {"id": "asinua1", "name": "Asinua 1", "group": "Asinua"},
    {"id": "asinua2", "name": "Asinua 2", "group": "Asinua"},
    {"id": "inalahi1", "name": "Inalahi 1", "group": "Inalahi"},
    {"id": "inalahi2", "name": "Inalahi 2", "group": "Inalahi"},
    {"id": "uepai1", "name": "Uepai 1", "group": "Uepai"},
    {"id": "uepai2", "name": "Uepai 2", "group": "Uepai"},
    {"id": "unilaki1", "name": "Unilaki 1", "group": "Unilaki"},
    {"id": "unilaki2", "name": "Unilaki 2", "group": "Unilaki"},
]


@app.route("/")
def index():
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", 
                         cameras=CAMERAS, 
                         go2rtc_url=GO2RTC_URL,
                         title="CCTV Dashboard Admin",
                         is_public=False)


@app.route("/public")
def public():
    return render_template("public.html", 
                         cameras=CAMERAS, 
                         go2rtc_url=GO2RTC_URL,
                         title="CCTV Publik",
                         is_public=True)


@app.route("/api/cameras")
def api_cameras():
    return jsonify(CAMERAS)


@app.route("/api/streams")
def api_streams():
    try:
        resp = requests.get(f"{GO2RTC_URL}/api/streams", timeout=5)
        return jsonify(resp.json())
    except:
        return jsonify({"error": "Failed to fetch streams"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
