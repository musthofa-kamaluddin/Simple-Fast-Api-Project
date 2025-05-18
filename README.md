# Todo List API & Web App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Todo List** adalah aplikasi manajemen tugas sederhana dengan backend API berbasis [FastAPI](https://fastapi.tiangolo.com/) dan frontend berbasis HTML, JavaScript, dan Tailwind CSS. Aplikasi ini memungkinkan pengguna untuk mengelola tugas, mencari, dan memfilter tugas berdasarkan status selesai.

## Fitur
- **Manajemen Tugas**: Buat, edit, hapus, dan tandai tugas sebagai selesai.
- **Pencarian**: Cari tugas berdasarkan judul atau deskripsi.
- **Filter**: Tampilkan tugas berdasarkan status selesai atau belum selesai.
- **Validasi Data**: Validasi ketat di backend menggunakan Pydantic.
- **UI Responsif**: Antarmuka ramah untuk desktop dan mobile.
- **Logging**: Pelacakan operasi dan error di backend.
- **Dokumentasi API**: Akses dokumentasi interaktif di `/docs`.

## Teknologi
- **Backend**: FastAPI, Pydantic, Uvicorn
- **Frontend**: HTML, JavaScript, Tailwind CSS (via CDN)
- **Lainnya**: Python 3.8+, Logging

## Struktur Proyek
```
todo-list/
├── main.py          # Backend API FastAPI
├── index.html       # Frontend Todo List
├── requirements.txt # Dependensi Python
├── .gitignore       # File yang diabaikan Git
├── LICENSE          # Lisensi MIT
├── README.md        # Dokumentasi proyek
```

## Prasyarat
- Python 3.8+
- Browser modern (Chrome, Firefox, dll.)
- Koneksi internet (untuk Tailwind CSS CDN)

## Instalasi
1. **Kloning Repositori**:
   ```bash
   git clone https://github.com/<username>/todo-list.git
   cd todo-list
   ```

2. **Buat Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instal Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi
1. **Jalankan Server API**:
   ```bash
   python main.py
   ```
   - API berjalan di `http://localhost:8000`.
   - Dokumentasi API: `http://localhost:8000/docs`.

2. **Jalankan Frontend**:
   ```bash
   python -m http.server 8080
   ```
   - Buka `http://localhost:8080` di browser.

## Penggunaan
- **Tambah Tugas**: Isi judul dan (opsional) deskripsi, lalu klik "Add Task".
- **Cari Tugas**: Gunakan kolom pencarian untuk mencari berdasarkan judul/deskripsi.
- **Filter Tugas**: Pilih "Completed" atau "Not Completed" dari dropdown.
- **Edit/Hapus**: Klik "Edit" untuk memperbarui atau "Delete" untuk menghapus tugas.
- **Tandai Selesai**: Centang checkbox untuk mengubah status tugas.

## Endpoint API
| Metode | Endpoint               | Deskripsi                       | Query Parameter       |
|--------|------------------------|---------------------------------|-----------------------|
| GET    | `/tasks`              | Dapatkan semua tugas            | `completed`, `search` |
| GET    | `/tasks/{task_id}`    | Dapatkan tugas berdasarkan ID   | -                     |
| POST   | `/tasks`              | Buat tugas baru                 | -                     |
| PUT    | `/tasks/{task_id}`    | Perbarui tugas                  | -                     |
| DELETE | `/tasks/{task_id}`    | Hapus tugas                     | -                     |

**Contoh POST**:
```json
{
    "id": 1,
    "title": "Belajar FastAPI",
    "description": "Membuat Todo List",
    "completed": false
}
```

## Pemecahan Masalah
- **CORS Error**: Pastikan API berjalan di `http://localhost:8000` sebelum frontend.
- **Tugas Tidak Muncul**: Periksa konsol browser (F12) untuk error fetch atau kosongkan `tasks_db` dengan menambahkan tugas baru.
- **Dependensi Gagal**: Jalankan `pip install -r requirements.txt` kembali.

## Kontribusi
1. Fork repositori.
2. Buat branch baru: `git checkout -b feature/nama-fitur`.
3. Commit perubahan: `git commit -m 'Menambahkan fitur X'`.
4. Push ke branch: `git push origin feature/nama-fitur`.
5. Buat Pull Request di GitHub.

## Pengembangan Lanjutan
- Tambahkan database (SQLite/PostgreSQL) untuk penyimpanan permanen.
- Implementasikan autentikasi JWT.
- Gunakan React/Vue.js untuk frontend yang lebih dinamis.
- Tambahkan notifikasi toast untuk aksi pengguna.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

## Kontak
Pertanyaan atau saran? Buat [issue](https://github.com/musthofa-kamaluddin/Simple-Fast-Api-Project/issues) di GitHub.

---
Dibuat dengan ☕ menggunakan FastAPI dan Tailwind CSS.
