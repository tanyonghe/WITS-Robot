import cv2
import datetime as dt
import numpy as np
import os
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
			frame = cv2.flip(frame,0)

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

    
def initialize_webcam_gui():


	def destroy_root():
		destroy = tkinter.messagebox.askquestion('Exit', 'Do you wish to exit?')
		if destroy == 'yes':
			root.destroy()


	root = tk.Tk()
	root.title('Webcam GUI')
	root.geometry('300x300+0+0')

	tk.Label(root, text = 'Press to start recording your activity session.', fg = "white", bg = '#85929e').pack()
	record_btn = tk.Button(root, text = 'Start Activity', fg = "white", bg = '#85929e', command = record_webcam).pack()
	tk.Label(root, text = 'Press to end your activity session.', fg = "white", bg = '#85929e').pack()
	stop_btn = tk.Button(root, text = 'End Activity', fg = "white", bg = '#85929e', command = destroy_root).pack()

	root.config(bg = '#85929e')

	root.mainloop()

	
if __name__ == "__main__":
	initialize_webcam_gui()

