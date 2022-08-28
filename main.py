from pydub import AudioSegment
from pydub.utils import mediainfo
from pathlib import Path
import argparse

def Wav2Flac(inInput:str):
    input = Path(inInput)
    if not input.exists():
        return

    export = Path(".") / "export"
    export.mkdir(parents=True, exist_ok=True)

    wavs = input.glob("*.wav")
    for wav in wavs:
        print(f"Conv... {wav.name} => {wav.stem + '.flac'}")
        song = AudioSegment.from_wav(wav)
        meta = mediainfo(wav)
        song.export(Path("./") / "export" / (wav.stem  + ".flac"), tags=meta["TAG"], format = "flac")
    print("Success")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()

    Wav2Flac(args.input)