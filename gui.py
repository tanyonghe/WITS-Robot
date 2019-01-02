import cv2
import datetime as dt
import flappy
import mediaAPI as mAPI
import numpy as np
import os
import shakeit
import tkinter as tk
import tkinter.messagebox

path = './videos'
access_rights = 0o755

try:  
    os.mkdir(path, access_rights)
except OSError:  
    pass


def record_webcam():
	cap = cv2.VideoCapture(0)

	# Define the codec and create VideoWriter object
	current_datetime = dt.datetime.now().strftime("%Y-%m-%d_%H-%M")
	current_datetime = '2019-01-07_09-35'
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('./videos/' + current_datetime + '.avi', fourcc, 20.0, (640,480))

	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == True:
			#frame = cv2.flip(frame,0)

			# write the flipped frame
			out.write(frame)

			cv2.imshow('frame',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			if cv2.getWindowProperty('frame',cv2.WND_PROP_AUTOSIZE) < 1:
				break
		else:
			break

	# Release everything if job is finished
	cap.release()
	out.release()
	cv2.destroyAllWindows()

    
def initialize_gui(activity):

	
	def destroy_window(window):
		def des_win():
			if window == root:
				destroy = tkinter.messagebox.askquestion('Exit', 'Do you wish to exit?')
				if destroy == 'yes':
					window.destroy()
			else:
				window.destroy()
		return des_win
			
			
	def play_games():
		games = tk.Tk()
		games.title('Games')
		games.geometry('500x300+0+0')
		tk.Label(games, text = 'Games', fg = "white", bg = '#85929e', font=("Helvetica", 14, "bold")).pack()
		tk.Label(games, text = '', fg = "white", bg = '#85929e').pack()
		tk.Button(games, text = 'Play Power Shake!', fg = "white", bg = '#85929e', font=("Helvetica", 12), command = shakeit.main).pack()
		tk.Label(games, text = '', fg = "white", bg = '#85929e').pack()
		tk.Button(games, text = 'Play Flappy Bird!', fg = "white", bg = '#85929e', font=("Helvetica", 12), command = flappy.main).pack()
		tk.Label(games, text = '', fg = "white", bg = '#85929e').pack()
		tk.Button(games, text = 'Exit Games', fg = "white", bg = '#85929e', font=("Helvetica", 12), command = destroy_window(games)).pack()
		games.config(bg = '#85929e')
		games.mainloop()
			
	
	def play_audio(file_path):
		def play():
			mAPI.play_audio(file_path)
			root.after(300000, play_audio('./sounds/angry.wav'))
		return play


	root = tk.Tk()
	root.title('WITS Robot')
	root.geometry('500x300+0+0')
	#root.iconbitmap('./docs/images/dog.ico')

	tk.Label(root, text = 'Current Activity', fg = "white", bg = '#85929e', font=("Helvetica", 14, "bold")).pack()
	tk.Label(root, text = activity, fg = "white", bg = '#85929e', font=("Helvetica", 14)).pack()
	tk.Label(root, text = '', fg = "white", bg = '#85929e').pack()
	tk.Label(root, text = 'Press to start recording your activity session.', fg = "white", bg = '#85929e', font=("Helvetica", 12)).pack()
	record_btn = tk.Button(root, text = 'Start Activity', fg = "white", bg = '#85929e', font=("Helvetica", 12), command = record_webcam).pack()
	tk.Label(root, text = '', fg = "white", bg = '#85929e').pack()
	tk.Label(root, text = 'Press to end your activity session.', fg = "white", bg = '#85929e', font=("Helvetica", 12)).pack()
	stop_btn = tk.Button(root, text = 'End Activity', fg = "white", bg = '#85929e', font=("Helvetica", 12), command = destroy_window(root)).pack()
	tk.Label(root, text = '', fg = "white", bg = '#85929e').pack()
	tk.Label(root, text = '', fg = "white", bg = '#85929e').pack()
	games_btn = tk.Button(root, text = 'Play Games!', fg = "white", bg = '#85929e', font=("Helvetica", 12), command = play_games).pack()

	root.config(bg = '#85929e')
	
	root.after(300000, play_audio('./sounds/angry.wav'))  # plays audio every 5 min or 300000 ms
	root.mainloop()

	
if __name__ == "__main__":
	initialize_gui("<Insert Activity Here>")

