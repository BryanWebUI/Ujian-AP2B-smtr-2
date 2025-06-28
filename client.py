

import requests
import threading
import time

# --- Konfigurasi Klien ---
BASE_API_URL = "http://127.0.0.1:5000"

# Data untuk diuji oleh klien: Daftar nomor antrean yang akan dicek
ANTREAN_UNTUK_DICEK = ["A01", "A03", "A99", "A04"] # Satu nomor antrean (A99) tidak ada

# ==============================================================================
# SOAL: Implementasi Fungsi untuk Cek Status Antrean via API
# ==============================================================================
def client_cek_antrean_via_api(nomor_antrean, thread_name):
    """
    TUGAS ANDA:
    Lengkapi fungsi ini untuk mengambil informasi status antrean dari API
    dan mencetak hasilnya ke konsol.

    Langkah-langkah:
    1. Bentuk URL target: f"{BASE_API_URL}/antrean/{nomor_antrean}/status"
    2. Cetak pesan ke konsol bahwa thread ini ('thread_name') memulai pengecekan untuk 'nomor_antrean'.
       Contoh: print(f"[{thread_name}] Mengecek antrean: {nomor_antrean}")
    3. Gunakan blok 'try-except' untuk menangani potensi error saat melakukan permintaan HTTP.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke URL target menggunakan 'requests.get()'. Sertakan timeout.
          ii. Periksa 'response.status_code':
              - Jika 200 (sukses):
                  - Dapatkan data JSON dari 'response.json()'.
                  - Cetak nama dan status antrean ke konsol.
                    Contoh: print(f"[{thread_name}] Antrean {nomor_antrean} atas nama '{data.get('nama')}': Status {data.get('status')}")
              - Jika 404 (antrean tidak ditemukan):
                  - Cetak pesan bahwa nomor antrean tidak valid.
                    Contoh: print(f"[{thread_name}] Nomor antrean {nomor_antrean} tidak valid.")
              - Untuk status code lain:
                  - Cetak pesan error umum ke konsol.
       b. Di blok 'except requests.exceptions.Timeout':
          - Cetak pesan bahwa permintaan timeout ke konsol.
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Cetak pesan error permintaan umum ke konsol.
    4. Setelah blok try-except, cetak pesan ke konsol bahwa thread ini ('thread_name') selesai memproses 'nomor_antrean'.
    """
    target_url = f"{BASE_API_URL}/antrean/{nomor_antrean}/status"
    print(f"[{thread_name}] Mengecek antrean: {nomor_antrean}")
    try:
        response = requests.get(target_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"[{thread_name}] Antrean {nomor_antrean} atas nama '{data.get('nama')}': Status {data.get('status')}")
        elif response.status_code == 404:
            print(f"[{thread_name}] Nomor antrean {nomor_antrean} tidak valid.")
        else:
             print(f"[{thread_name}] Error untuk nomor antrian {nomor_antrean}: Status {response.status_code}")

    except requests.exceptions.Timeout:
        print(f"[{thread_name}] permintaan timeout untuk nomor rekening: {nomor_antrean}")
    except requests.exceptions.RequestException as e:
        print(f"[{thread_name}] pesan error untuk nomor rekening: {nomor_antrean}. Error: {str(e)}")
    print(f"[{thread_name}] selesai memproses Nomor antrean {nomor_antrean} tidak valid.")





    # ===== TULIS KODE ANDA DI SINI =====
    #
    # Hapus 'pass' ini setelah Anda mengisi kode
    #
    # ====================================

# --- Bagian Utama Skrip (Tidak Perlu Diubah Peserta) ---
if __name__ == "__main__":
    print(f"Memulai Klien Pengecek untuk {len(ANTREAN_UNTUK_DICEK)} Antrean Secara Concurrent.")
    
    threads = []
    start_time = time.time()

    for i, antrean_cek in enumerate(ANTREAN_UNTUK_DICEK):
        thread_name_for_task = f"Layar-{i+1}" 
        thread = threading.Thread(target=client_cek_antrean_via_api, args=(antrean_cek, thread_name_for_task))
        threads.append(thread)
        thread.start()

    for thread_instance in threads:
        thread_instance.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nSemua pengecekan antrean telah selesai diproses dalam {total_time:.2f} detik.")