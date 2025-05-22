from pydub import AudioSegment
import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

# Memuat file audio MP3
audio = AudioSegment.from_mp3("back.mp3")

# Mengubah audio menjadi data numpy
samples = np.array(audio.get_array_of_samples())

# Menampilkan data audio asli
plt.figure(figsize=(10, 6))
plt.plot(samples[:1000])  # Menampilkan sampel pertama untuk visualisasi
plt.title("Waveform of Audio")
plt.show()

# Melakukan transformasi Fourier (FFT) untuk melihat frekuensi dalam audio
frequencies = fft(samples)

# Menampilkan spektrum frekuensi
plt.figure(figsize=(10, 6))
plt.plot(np.abs(frequencies[:1000]))  # Menampilkan frekuensi pertama
plt.title("Frequency Spectrum")
plt.show()

# (Optional) Manipulasi spektrum untuk menghilangkan watermark (jika diketahui frekuensinya)

# Melakukan inverse FFT untuk mengembalikan audio
reconstructed_audio = ifft(frequencies)
reconstructed_audio = np.real(reconstructed_audio).astype(np.int16)

# Menyimpan audio yang telah dimodifikasi
modified_audio = AudioSegment(
    reconstructed_audio.tobytes(), 
    frame_rate=audio.frame_rate,
    sample_width=reconstructed_audio.dtype.itemsize, 
    channels=audio.channels
)

modified_audio.export("backfix.mp3", format="mp3")
