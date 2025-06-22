import asyncio
from lmnt.api import Speech
from playsound import playsound
from io import BytesIO
import base64

async def text_to_audio(text: str, voice: str = 'leah') -> bytes:
    async with Speech() as speech:
        synthesis = await speech.synthesize(text, voice)
        print("t1", type(synthesis))
        print("t2", type(synthesis['audio']))
        return synthesis['audio']

def text_to_audio_sync(text: str, voice: str = 'leah') -> bytes:
    return asyncio.run(text_to_audio(text, voice))

def play_tts(text):
    with open("./temp/audio.mp3", "wb") as audio_file:
        audio_file.write(text_to_audio_sync(text))

    playsound("./temp/audio.mp3")

if __name__ == "__main__":
    play_tts("Hello there, how are you? This is an AI voice that is created using an AI voice creating thing that creates AI voices.")