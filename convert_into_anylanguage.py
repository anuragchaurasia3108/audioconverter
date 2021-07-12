import googletrans
import speech_recognition as sr
import gtts
import playsound
r=sr.Recognizer()
# print(googletrans.LANGUAGES)
translator=googletrans.Translator()
input_lang='en-IN'
output_lang='es'
try:
	print("let's started...\n")
	with sr.Microphone() as source2:

		r.adjust_for_ambient_noise(source2, duration=0.2) 
		audio2 = r.listen(source2)  
		MyText = r.recognize_google(audio2) 
		MyText = MyText.lower() 


		print("Did you say "+MyText) 
		translated=translator.translate(Text, dest=output_lang)
		print(translated.text)
		converted=gtts.gTTS(translated.Text,output_lang=lanng)
		converted.save('check.mp3')
		playsound.playsound('check.mp3') 
except:
	pass	
