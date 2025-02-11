
import os 
import tkinter as tk 
import PyPDF2 
import pyttsx3
from tkinter import messagebox,filedialog,PhotoImage
from tkinter import *
import speech_recognition as sr  
from Foundation import NSAppleScript #maclibrary
from AppKit import NSWorkspace,NSSpeechSynthesizer#maclibrary
import keyboard
os.environ['TK_SILENCE_DEPRECATION'] = '1'
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
speaker = NSSpeechSynthesizer.alloc().init()

root = tk.Tk()
root.state("zoomed")
root.wm_title('Voice to Text and VisaVersa By MUSTAFA BHARMAL')
bg = PhotoImage(file='/Users/mrperfect/Work/Project/Speak-Write/bc.png')
img_label = tk.Label( root, image = bg)
img_label.place(x = 0, y = 0)


def frame_STT():
	root.attributes('-topmost',False)
	FST = tk.Toplevel(root)
	FST.geometry("500x600")
	FST.title("Speech to Text")
	FST.attributes('-topmost',True)
	FST.resizable(0,0)
	FST['bg']='#7d7d7d'

	def Audio_Recognizer():
		try:
			with mic as source:
				Audio = r.listen(source,phrase_time_limit=5)
				msg = r.recognize_google(Audio)
				text_Box.insert(END , msg+'\n')
		except sr.UnknownValueError:
			print("GOOGLE could not understand audio")
			text_Box.insert(END,"GOOGLE could not understand audio"+'\n')
		except sr.RequestError as e:
			print("GOOGLE error; {0}".format(e))
			text_Box.insert(END,"GOOGLE error; {0}".format(e)+'\n')
		except:
			print("Check Your Connection")
			text_Box.insert(END,"Check Your Connection"+'\n')

	def Save_File():
		try:
			path = filedialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
		
		except:
			return   
		
		with open(path, 'w') as f:
			f.write(text_Box.get('1.0', tk.END))

	def Clear_TextBook():
		text_Box.delete(1.0, tk.END)

	Listen_Button = tk.Button(FST, bg='#32CD32', fg='black',font=("Times new roman", 18, 'bold'),command=Audio_Recognizer)
	Listen_Button['text'] = 'Listen'
	Listen_Button.place(x=30,y=20)

	save_file = tk.Button(FST, bg='#8B8B00', fg='white',font=("Times new roman", 18, 'bold'),command=Save_File)
	save_file['text'] = 'Save file'
	save_file.place(x=150,y=20)

	Back_Button = tk.Button(FST, bg='red', fg='black',font=("Times new roman", 18, 'bold'),command=FST.destroy)
	Back_Button['text'] = ' <-- '
	Back_Button.place(x=390, y=20)

	clear_button = tk.Button(FST, bg='blue', fg='white',font=("Times new roman", 18, 'bold'),command=Clear_TextBook)
	clear_button['text'] = 'Clear'
	clear_button.place(x=280, y=20)

	text_Box = tk.Text(FST)
	scroll_Bar = tk.Scrollbar(text_Box, orient = tk.VERTICAL)
 
	text_Box.configure(font=("Verdana", 12), yscrollcommand = scroll_Bar.set)
	text_Box.place(x=20, y=100, width=460, height=480)
 
	scroll_Bar.config(command = text_Box.yview)

	scroll_Bar.pack(side=RIGHT, fill='y')



def frame_TTS():
	root.attributes('-topmost',False)
	FTS = tk.Toplevel(root)
	FTS.geometry("500x600")
	FTS.title("Text to Speech")
	FTS.resizable(0,0)
	FTS['bg']='#7d7d7d'


	text_Box = tk.Text(FTS)
	scroll_Bar = tk.Scrollbar(text_Box, orient = tk.VERTICAL)
 
	text_Box.configure(font=("Verdana", 12), yscrollcommand = scroll_Bar.set)
	text_Box.place(x=20, y=20, width=460, height=480)
 
	scroll_Bar.config(command = text_Box.yview)

	scroll_Bar.pack(side=RIGHT, fill='y')

	FTS.attributes('-topmost',True)

	def Read_File():
		filename = filedialog.askopenfilename(initialdir=Working_Dir)
		if (filename == '') :
			messagebox.showerror('Can not load file', 'Choose a text file to read')

		elif filename.endswith('.txt'):
			with open(filename) as f:
				text1 = f.read()
				Clear_TextBook()
				text_Box.insert('1.0', text1)

		elif filename.endswith('.pdf'):
			pdfReader = PyPDF2.PdfFileReader(filename)
			number_of_pages = pdfReader.getNumPages()
			Clear_TextBook()
			for page_number in range(number_of_pages):
				from_page = pdfReader.getPage(page_number)
				text1 = from_page.extractText()
				text_Box.insert(END, text1)
				print(text1)

	def Clear_TextBook():
		text_Box.delete(1.0, tk.END)

	def Convert_TextToSpeech():
		msg = text_Box.get(tk.SEL_FIRST, tk.SEL_LAST)
		speak = pyttsx3.init()
		speak.setProperty("rate",178)
		voice = speak.getProperty('voices')
		speak.setProperty('voice', voice[1].id)
		speak.say(msg)
		speak.runAndWait()

	GET_Audio = tk.Button(FTS, bg='#32CD32', fg='black',font=("Times new roman", 18, 'bold'),command=Convert_TextToSpeech)
	GET_Audio['text'] = 'Get Audio'
	GET_Audio.place(x=20,y=530)

	read_file = tk.Button(FTS, bg='#8B8B00', fg='white',font=("Times new roman", 18, 'bold'),command=Read_File)
	read_file['text'] = 'Read file'
	read_file.place(x=170,y=530)

	Clear_Frame = tk.Button(FTS, bg='blue', fg='white',font=("Times new roman", 18, 'bold'),command=Clear_TextBook)
	Clear_Frame['text'] = 'Clear'
	Clear_Frame.place(x=300, y=530)

	Back_Button = tk.Button(FTS, bg='red', fg='black',font=("Times new roman", 18, 'bold'),command=FTS.destroy)
	Back_Button['text'] = ' <-- '
	Back_Button.place(x=400, y=530)


Title_Label = tk.Label(root,font=("Comic Sans MS", 25, 'bold'))
Title_Label['text'] = 'Convert PDF File Text to Audio Speech and vice versa using Python'
Title_Label.place(x=220,y=50)

STT_Buttton = tk.Button(root, bg='#1A1A1A', fg='white',font=("Times new roman", 20, 'bold'),command= frame_STT)
STT_Buttton['text'] = 'Voice to Text'
STT_Buttton.place(x=700,y=550,width=200)

TTS_Button = tk.Button(root, bg='#1A1A1A', fg='white',font=("Times new roman", 20, 'bold'),command=frame_TTS)
TTS_Button['text'] = 'Text to Voice'
TTS_Button.place(x=700,y=230,width=200)

credit_Label = tk.Label(root,font=("Comic Sans MS", 25, 'bold'))
credit_Label['text'] = 'Project By: Mustafa Bharmal\n Guided By: Mitesh Sir'
credit_Label.place(x=550,y=700)

root.mainloop()
