import os

ffmpeg_path = r"C:\@Storage\Documents\Data\00. itenas\06. smst VI\05. Pengenalan Ucapan - Pa Jasman\code\converter\ffmpeg\bin\ffmpeg.exe"
ffprobe_path = r"C:\@Storage\Documents\Data\00. itenas\06. smst VI\05. Pengenalan Ucapan - Pa Jasman\code\converter\ffmpeg\bin\ffprobe.exe"
input_file = r"c:\@Storage\Documents\Data\00. itenas\06. smst VI\05. Pengenalan Ucapan - Pa Jasman\code\converter\input\1_152022182_L_01.m4a"

print("Cek FFmpeg:", os.path.exists(ffmpeg_path))
print("Cek FFprobe:", os.path.exists(ffprobe_path))
print("Cek File Audio:", os.path.exists(input_file))
