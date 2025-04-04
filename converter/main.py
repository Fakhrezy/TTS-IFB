from pydub import AudioSegment
import os

def convert_m4a_to_wav(input_folder, output_folder):
    # Pastikan folder output ada
    os.makedirs(output_folder, exist_ok=True)
    
    for file in os.listdir(input_folder):
        if file.endswith(".m4a"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file.replace(".m4a", ".wav"))
            
            # Load dan konversi file
            audio = AudioSegment.from_file(input_path, format="m4a")
            audio.export(output_path, format="wav")
            print(f"Konversi selesai: {output_path}")

# Contoh penggunaan
input_folder = "input"  # Ganti dengan path folder input
output_folder = "output"  # Ganti dengan path folder output
convert_m4a_to_wav(input_folder, output_folder)
