

import flask
from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)

# Database simulasi antrean restoran
antrean_db = {
    "A01": {"nama": "Keluarga Budi", "jumlah_orang": 4, "status": "Menunggu"},
    "A02": {"nama": "Ani dan Cici", "jumlah_orang": 2, "status": "Sudah Dipanggil"},
    "A03": {"nama": "Rombongan Dedi", "jumlah_orang": 6, "status": "Menunggu"},
    "A04": {"nama": "Eka Sendiri", "jumlah_orang": 1, "status": "Menunggu"},
}
db_lock = threading.Lock()

def log_server_activity(message):
    """Fungsi sederhana untuk logging di sisi server (ke konsol)."""
    print(f"[SERVER-MAKANENAK] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

@app.route('/antrean/<nomor_antrean>/status', methods=['GET'])
def get_status_antrean(nomor_antrean):
    """Endpoint untuk mendapatkan status antrean berdasarkan nomor."""
    log_server_activity(f"Permintaan status untuk antrean: {nomor_antrean}")
    
    time.sleep(random.uniform(0.1, 0.3)) 
    
    with db_lock:
        antrean = antrean_db.get(nomor_antrean.upper())
    
    if antrean:
        response_data = antrean.copy()
        response_data["nomor_antrean"] = nomor_antrean.upper()
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Nomor antrean tidak valid atau sudah selesai"}), 404

if __name__ == '__main__':
    log_server_activity("API Sistem Antrean Restoran MakanEnak dimulai.")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False, use_reloader=False)