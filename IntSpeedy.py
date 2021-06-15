'''
    Program: GAS : Internet Speed Tester
    Author: Shashi Kumar
    GitHub: sbkshashi
'''
import tkinter
import speedtest

root=tkinter.Tk()
st=speedtest.Speedtest()
root.title("GAS: Internet Speed Tester")

# Definition for Download Speed
def get_download_speed():
    dw_sp=st.download()
    print(dw_sp)
    red_slider.set(dw_sp)

output_frame=tkinter.Frame(root)
input_frame=tkinter.Frame(root)
output_frame.pack()
input_frame.pack()

red_slider = tkinter.Scale(input_frame, from_=255, to=0)
red_slider.pack()
bton=tkinter.Button(input_frame,text="check",command=get_download_speed)
bton.pack()
root.mainloop()

'''
st = speedtest.Speedtest()
option=int(input("choose 123"))
if option==1:
    print(st.download())
elif option==2:
    print(st.upload())
elif option==3:
    servernames=[]
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print("incorect chice")
def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]
def main():
    for i in range(3):
        print("making test #{}".format(i+1))
        d, u, p = test()
        print(f"Test {i+1}")
        print(f"Download {d}")
        print(f"Upload {u}")
        print(f"Ping {p}")
if __name__ == "__main__":
    main()'''

    
'''
	Read Me Before running
		1. All module should come with Python basic installation except speedtest.
		2. To install speedtest run 
			a. pip install speedtest_cli
		3. I have used Python3.9.2 64-bit

'''
readme_label = Label(window, test='1. All module should come with Python basic installation except speedtest.\n 2. To install speedtest run.\n\t a. pip install speedtest_cli \n 3. I have used Python3.9.2 64-bit', justify=RIGHT, anchor=NW).grid()
