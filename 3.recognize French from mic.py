import speech_recognition as sr
import pyaudio


def recognize_speech_from_mic(recognizer, microphone):
    '''
    Transcribe speech from recorded from `microphone`.
    :param recognizer: 
    :param microphone: 
    :return: `None` if speech could not be transcribed, otherwise a string containing the transcribed text
    '''
    print('Please read the French sentence')
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # try recognizing the speech in the recording in french
    '''
    - SpeechRecognition package (need to install by `pip install SpeechRecognition`) it support these speech recognitions: 
    - `recognize_bing()`: [Microsoft Bing Speech](https://azure.microsoft.com/en-us/services/cognitive-services/speech/)
    - `recognize_google()`: [Google Web Speech API](https://w3c.github.io/speech-api/speechapi.html)
    - `recognize_google_cloud()`: [Google Cloud Speech](https://cloud.google.com/speech/) - requires installation of the google-cloud-speech package
    - `recognize_houndify()`: [Houndify](https://www.houndify.com/) by SoundHound
    - `recognize_ibm()`: [IBM Speech to Text](https://www.ibm.com/watson/services/speech-to-text/)
    - `recognize_sphinx()`: [CMU Sphinx](https://cmusphinx.github.io/) - requires installing PocketSphinx
    - `recognize_wit()`: [Wit.ai](https://wit.ai/)
    - pyaudio package (need to install by `pip install pyaudio`)
    '''
    try:
        text = recognizer.recognize_google(audio, language='fr-FR')
        
    except Exception as e:
        print(e)
        text = None

    return text


if __name__ == '__main__':
    # input a French word or sentence
    text = input('Please input a French word or sentence: ').strip()

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # get your speech text
    speech_text = recognize_speech_from_mic(recognizer, microphone)

    while speech_text != None and text.lower() != speech_text.lower():
        print(speech_text)
        # get your speech text
        speech_text = recognize_speech_from_mic(recognizer, microphone)

    if speech_text:
        print('{} {}'.format(speech_text, '>_<'))
    else:
        print('Please try the speech recognization service later or change another one.')