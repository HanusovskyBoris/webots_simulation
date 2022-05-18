from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import sounddevice as sd
from scipy.io.wavfile import write




def answer():
    api_key = "K3TxBAsAiwucOS33A9ZWwSOMhn78rHBN3ZrBGylQef9N"
    url = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/50ae105f-52bb-49ab-a2f3-f525d69e6581"
    
    authenticator = IAMAuthenticator(api_key)
    stt = SpeechToTextV1(authenticator =authenticator)
    stt.set_service_url(url)
    
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print("before")
    sd.wait()  # Wait until recording is finished
    print("after")
    write('..\\..\\jokes\\kids\\output.wav', fs, myrecording)  # Save as WAV file 
    with open('..\\..\\jokes\\kids\\output.wav', 'rb') as f:
        res = stt.recognize(audio = f, content_type = 'audio/wav', model = 'en-US_NarrowbandModel').get_result()

    print(res) 
   
if __name__ == "__main__":
    pass   