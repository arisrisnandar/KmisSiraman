import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data sampel referensi (pastikan path-nya benar)
reference_data = pd.read_excel(r'HDPE (1).xlsx')

# Data sampel baru (pastikan path-nya benar)
new_data = pd.read_excel(r'BKT (1).xlsx')

# Konversi kolom 'X' dan 'Y' ke tipe data numerik dengan penanganan kesalahan
reference_data['X'] = pd.to_numeric(reference_data['X'], errors='coerce')
reference_data['Y'] = pd.to_numeric(reference_data['Y'], errors='coerce')

# Ekstrak kolom 'X' dan 'Y' dari data referensi
x_reference = reference_data['X']
y_reference = reference_data['Y']

# Konversi kolom 'X' dan 'Y' dari data baru ke tipe data numerik dengan penanganan kesalahan
new_data['X'] = pd.to_numeric(new_data['X'], errors='coerce')
new_data['Y'] = pd.to_numeric(new_data['Y'], errors='coerce')

# Ekstrak kolom 'X' dan 'Y' dari data baru
x_new = new_data['X']
y_new = new_data['Y']

# Membuat dua subplot, satu untuk sampel referensi Polypropelene dan satu untuk sampel baru
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot sampel referensi pada subplot pertama

# Membuat kurva interpolasi untuk sampel referensi
x_interp_reference = np.linspace(x_reference.min(), x_reference.max(), 500)  # Membuat titik-titik baru untuk sumbu X
spl_reference = make_interp_spline(x_reference, y_reference, k=3)  # Membuat spline interpolasi kubik
y_interp_reference = spl_reference(x_interp_reference)  # Menghasilkan data kurva yang mulus

# Plot kurva referensi dengan warna biru
ax1.plot(x_interp_reference, y_interp_reference, color='blue', label='Fingerprint Referensi ')
ax1.set_xlabel('Kolom X')
ax1.set_ylabel('Kolom Y')
ax1.set_title('Fingerprint Referensi ')

# Hitung persentase kesamaan nilai X dan Y antara sampel baru dan referensi
percentage_similarity_x = (1 - np.abs(x_new - x_reference) / x_reference).mean() * 100
percentage_similarity_y = (1 - np.abs(y_new - y_reference) / y_reference).mean() * 100

# Menghitung selisih antara kedua persentase similarity
difference_x_y = abs(percentage_similarity_x - percentage_similarity_y)

# Menentukan keterangan berdasarkan selisih
if 0 <= percentage_similarity_x <= 100 and 0 <= percentage_similarity_y <= 100:
    if percentage_similarity_x >= 91 and percentage_similarity_y >= 91:
        keterangan_similarity = 'Sampel Cocok'
    elif 71 <= percentage_similarity_x <= 90 and 71 <= percentage_similarity_y <= 90:
        keterangan_similarity = 'Kemiripan Tinggi'
    elif 51 <= percentage_similarity_x <= 70 and 51 <= percentage_similarity_y <= 70:
        keterangan_similarity = 'Mirip'
    elif 31 <= percentage_similarity_x <= 50 and 31 <= percentage_similarity_y <= 50:
        keterangan_similarity = 'Hampir Mirip'
    elif difference_x_y < 20:
        keterangan_similarity = 'Sedikit Berbeda'
    else:
        keterangan_similarity = 'Cukup Berbeda'
else:
    keterangan_similarity = 'Gambar Tidak Cocok'

ax1.legend()
ax1.grid(False)

# Plot sampel yang dimiliki pada subplot kedua

# Membuat kurva interpolasi untuk sampel baru
x_interp_new = np.linspace(x_new.min(), x_new.max(), 500)  # Membuat titik-titik baru untuk sumbu X
spl_new = make_interp_spline(x_new, y_new, k=3)  # Membuat spline interpolasi kubik
y_interp_new = spl_new(x_interp_new)  # Menghasilkan data kurva yang mulus

# Plot kurva sampel baru dengan warna biru
ax2.plot(x_interp_new, y_interp_new, color='blue', label='Fingerprint Sampel Data')
ax2.set_xlabel('Kolom X')
ax2.set_ylabel('Kolom Y')
ax2.set_title('Fingerprint Sampel Data')

# Tambahkan teks dengan persentase similarity dan keterangan
ax2.text(0.015, 0.85, f'Persentase Similarity X: {percentage_similarity_x:.2f}%', transform=ax2.transAxes, fontsize=10, color='black')
ax2.text(0.015, 0.80, f'Persentase Similarity Y: {percentage_similarity_y:.2f}%', transform=ax2.transAxes, fontsize=10, color='black')
ax2.text(0.015, 0.75, f'Keterangan: {keterangan_similarity}', transform=ax2.transAxes, fontsize=10, color='blue')

ax2.legend()
ax2.grid(False)

# Mengatur jarak antara kedua subplot
plt.tight_layout()

# Tampilkan plot
plt.show()