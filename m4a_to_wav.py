import os
from pydub import AudioSegment

f_m4a = "m4as/"
f_mp3 = "mp3s/"
f_wav = "wavs/"

def main():
    os.makedirs("mp3s", exist_ok=True)
    os.makedirs("wavs", exist_ok=True)
    files = [f[:-4] for f in os.listdir(f_m4a) if '.m4a' in f]

    for file in files:
        m4a = f_m4a + file + ".m4a"
        mp3 = f_mp3 + file + ".mp3"
        wav = f_wav + file + ".wav"
        if os.path.isfile(wav):
            continue
        os.system(f"ffmpeg -i {m4a} -ab 256k {mp3} -y")
        # convert wav to mp3                                                            
        audSeg = AudioSegment.from_mp3(mp3)
        audSeg.export(wav, format="wav")

if __name__ == "__main__":
    main()