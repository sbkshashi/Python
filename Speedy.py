'''
    Program: GAS : Internet Speed Tester
    Author: Shashi Kumar
    GitHub: sbkshashi

	Read Me Before running
		1. All module should come with Python basic installation except speedtest.
		2. To install speedtest run 
			a. pip install speedtest_cli
		3. I have used Python3.9.2 64-bit

'''
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from importlib import reload
import speedtest


st = speedtest.Speedtest()

'''
	Declearing all required variables
'''
dowload_speed = st.download() / 1000.0 / 1000.0
dnld_mpbs = "{:.2f}".format(dowload_speed)
upload_speed = st.upload() / 1000.0 / 1000.0
upld_mpbs = "{:.2f}".format(upload_speed)
ping = st.results.ping
isp = st.results.client['isp']
country = st.results.client['country']
ip = st.results.client['ip']
server = st.results.server['sponsor']
sever_location = st.results.server['name']

'''
	Initializing Python Empty Window
'''
window = Tk()
window.title("GAS: Internet Speed Checker")
window.geometry('400x450')

'''
	Defining style for the empty window
'''
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green', justify='center')
style.configure("BW.TLabel", foreground="black", background="white")

'''
	Labeling
		Heading for Python Window
		Data gathered on each veribles.
'''
label = Label(window, text="    Python Based Internet Speed Checker \n ", justify=CENTER, anchor=NW).grid()

Network_det_label = Label(window, text='Network : '+isp+'          Test server : '+server+
	              '  \n \ncountry : '+country+'             Region : '+sever_location+
	              ' \n \nip address : '+ip+' \n \nPing Time : '+str(round(ping, 0))+
	              ' ms  \n ', justify=CENTER, anchor=NW
	              ).grid()

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar', mode="determinate")
bar['value'] = dnld_mpbs
bar.grid()
dnld_label = Label(window, text='Download speed : '+str(dnld_mpbs)+' Mbps \n  ', justify=CENTER, anchor=NW).grid()

bar1 = Progressbar(window, length=200, style='black.Horizontal.TProgressbar', mode="determinate")
bar1['value'] = upld_mpbs
bar1.grid()
upld_label = Label(window, text='Upload speed : '+str(upld_mpbs)+' Mbps', justify=CENTER, anchor=NW).grid()

label = Label(window, text=" \n\nREAD ME \n ", justify=CENTER, anchor=NW).grid()
readme_label = Label(window, text='1. All module should come with Python basic installation except speedtest. \n' + 
'2. To install speedtest run.\n\t a. pip install speedtest_cli \n'+
'3. I have used Python3.9.2 64-bit', justify=LEFT, anchor=NW).grid()

window.mainloop()
