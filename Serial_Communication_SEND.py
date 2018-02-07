# -*- coding: utf-8 -*

"""GUI模块"""
import tkinter
import tkinter.ttk as ttk
"""串口操作模块"""
import serial
import serial.tools.list_ports
"""程序休眠"""
import time

serial_control = 0

def sned_data(send_srt, comname, baud, databits, oebits, stopbits):
    global serial_control
    if serial_control:
        parity_ch = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD, serial.PARITY_MARK, serial.PARITY_SPACE]
        parity_chi = ('NONE', 'EVEN', 'ODD', 'MARK', 'SPACE')
        k = 0
        while True:
            if oebits == parity_chi[k]:
                break
            else:
                k += 1
        ser = serial.Serial(comname, int(baud), timeout=0.5)
        ser.bytesize = int(databits)
        ser.stopbits = float(stopbits)
        ser.parity = parity_ch[k]
        time.sleep(0.5)
        for s in send_srt:
            print(type(s),s)
            print(ser.write(bytes.fromhex(hex(ord(s))[2:])))
        ser.close()
    else:
        print('Serial is OFF')
        
    
    
def open_serial(index):
    global serial_control
    if index:
        serial_control = 0
    else:
        plist = serial.tools.list_ports.comports()
        if len(plist) != 0:
            serial_control = 1
            plist = list(plist[0])[0]
            print(plist, 'is available.')
            boxchoice['value'] = plist
            boxchoice.current(0)
        else:
            print('No serial to open.')
            serial_control = 0


root = tkinter.Tk()
root.title("Serial Communication")
#root.geometry('500x300')

label_com_name = tkinter.Label(root, text='Available COM name:')
label_com_name.grid(row=0, column=0)

label_baud = tkinter.Label(root, text='Baud:')
label_baud.grid(row=1, column=0)

label_data = tkinter.Label(root, text='Data bits:')
label_data.grid(row=2, column=0)

label_oddeven = tkinter.Label(root, text='Odd/Even:')
label_oddeven.grid(row=3, column=0)

label_stop = tkinter.Label(root, text='Stop bit:')
label_stop.grid(row=4, column=0)

send_data = tkinter.StringVar()
entry_senddata = tkinter.Entry(root, textvariable=send_data)
send_data.set('')
entry_senddata.grid(row=5, column=0, rowspan=2, columnspan=2, sticky='W'+'E'+'N'+'S', padx=5, pady=10)

box_choice_value = tkinter.StringVar()
boxchoice = ttk.Combobox(root, textvariable=box_choice_value, state='readonly')
boxchoice['value'] = ('COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6')
boxchoice.current(0)
boxchoice.bind('<<ComboboxSelected>>')
boxchoice.grid(row=0, column=1, sticky='W')

box_choice_baud_value = tkinter.StringVar()
box_baud = ttk.Combobox(root, textvariable=box_choice_baud_value, state='readonly')
box_baud['value'] = (100, 300, 600,1200,2400,4800,9600,14400,19200,38400,56000,57600,15200,128000,256000)
box_baud.current(6)
box_baud.bind('<<ComboboxSelected>>')
box_baud.grid(row=1, column=1, sticky='w')

box_choice_data_value = tkinter.StringVar()
box_data = ttk.Combobox(root, textvariable=box_choice_data_value)
box_data['value'] = (5, 6, 7, 8)
box_data.current(3)
box_data.bind('<<ComcoboxSelected>>')
box_data.grid(row=2, column=1, sticky='w')

box_choice_oddeven_value = tkinter.StringVar()
box_oddeven = ttk.Combobox(root, textvariable=box_choice_oddeven_value)
box_oddeven['value'] = ('NONE', 'EVEN', 'ODD', 'MARK','SPACE')
box_oddeven.current(0)
box_oddeven.bind('<<ComcoboxSelected>>')
box_oddeven.grid(row=3, column=1, sticky='w')

box_choice_stop_value = tkinter.StringVar()
box_stop = ttk.Combobox(root, textvariable=box_choice_stop_value)
box_stop['value'] = (1, 1.5, 2)
box_stop.current(0)
box_stop.bind('<<ComcoboxSelected>>')
box_stop.grid(row=4, column=1, sticky='w')

button_open_serial = tkinter.Button(root, text='Open Serial', command=lambda: open_serial(0))
button_open_serial.grid(row=7, column=0, sticky='w')

button_stop_serial = tkinter.Button(root, text='Close Serial', command=lambda: open_serial(1))
button_stop_serial.grid(row=7, column=1, sticky='w')

button_send = tkinter.Button(root, text='Send', command=lambda:sned_data(send_data.get(), box_choice_value.get(), box_choice_baud_value.get(), box_choice_data_value.get(), box_choice_oddeven_value.get(), box_choice_stop_value.get()))
button_send.grid(row=7, column=2, sticky='w')

root.mainloop()



