import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# 1. Load Sinyal Ucapan
# file_path = 'output_salam.wav'
file_path_a = 'file_audio/output_a.wav'
# file_path_b = 'file_audio/output_b.wav'
# file_path_c = 'file_audio/output_c.wav'
# file_path_d = 'file_audio/output_d.wav'

# file_path_i = 'file_audio/output_i.wav'
# file_path_u = 'file_audio/output_u.wav'
# file_path_e = 'file_audio/output_e.wav'
# file_path_o = 'file_audio/output_o.wav'
# sr sample rate: jumlah sample per detik dari file audio
# y : panjang array, menunjukkan jumlah sample dalam file audio
# Jika sr=None, maka librosa akan memuat audio dengan sample rate asli dari file tersebut.
# Misalnya, file audio direkam pada 44.1 kHz, maka sr akan bernilai 4410
# y → Array amplitudo suara dalam domain waktu
# sr → Sample rate (jumlah sampel per detik).

y_a, sr = librosa.load(file_path_a, sr=None)
# y_b, sr = librosa.load(file_path_b, sr=None)
# y_c, sr = librosa.load(file_path_c, sr=None)
# y_d, sr = librosa.load(file_path_d, sr=None)

# y_i, sr = librosa.load(file_path_i, sr=None)
# y_u, sr = librosa.load(file_path_u, sr=None)
# y_e, sr = librosa.load(file_path_e, sr=None)
# y_o, sr = librosa.load(file_path_o, sr=None)
print(y_a[:10])
print(f"Sample Rate: {sr}, Panjang l = {len(y_a)} Duration: {len(y_a)/sr:.2f} seconds")

# Plot Hasil Pre-processing
plt.figure(figsize=(15, 10))

plt.subplot(5, 1, 1)
librosa.display.waveshow(y_a, sr=sr)