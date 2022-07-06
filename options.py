from tkinter import *
from tkinter import ttk
from chat_client import Client
import time
from gui import *

def start(client):
    client.send('INFO REQUEST'.encode('utf-8'))
    host, port = '127.0.0.1', 9000
    info = eval(client.recv(1024).decode('utf-8'))

    chatClient = Client(host, port, info["Username"], info['Extras']['Theme'], info['Extras']['Badge'], info['Extras']['Text'])
    chatClient.start()

def status(client):
    client.send('INFO REQUEST'.encode('utf-8'))
    i = eval(client.recv(1024).decode('utf-8'))

    status_wind = Tk()
    status_wind.geometry('400x400')
    status_wind.config(bg='black')
    status_wind.title('Status')

    status_lbl = Label(
        status_wind,
        text='Status',
        font=('Times', 20, 'bold'),
        bg='black',
        fg='white'
    )

    status_text = Label(
        status_wind,
        text=f"""
    Username: {i['Username']}
    Email: {i['Email']}
    Password: {i['Password']}
    Age: {i['Age']}
    Phone: {i['Contact']}

    Current Badge: {i['Extras']['Badge']}
    Current Theme: {i['Extras']['Theme']}
    Frontline Text: {i['Extras']['Text']}
    Boost Subscription: {i['Extras']['Boost']}
    """,
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white'
    )

    status_lbl.place(x=169, y=60)
    status_text.place(x=0, y=100)

    status_wind.mainloop()

def delete_account(client):
    del_acc_wind = Tk()
    del_acc_wind.geometry('400x400')
    del_acc_wind.config(bg='black')
    del_acc_wind.title('Delete Your Account')

    confirmation = Label(
        del_acc_wind,
        text='''
         Are you sure you want 
        to delete your account?
        ''',
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white'
    )

    def send_info():
        try:
          client.send('DELETE ACCOUNT REQUEST'.encode('utf-8'))
          done = client.recv(1024).decode('utf-8')
          print(done)
          exit(0)
        except Exception as e:
          print(e)
          exit(1)

    yes_button = Button(
        del_acc_wind,
        text='Yes',
        font=('Courier', 12, 'bold'),
        bg='green',
        fg='black',
        width=8,
        command=send_info
    )

    no_button = Button(
        del_acc_wind,
        text='No',
        font=('Courier', 12, 'bold'),
        bg='red',
        fg='black',
        width=8,
        command=del_acc_wind.destroy
    )

    confirmation.place(x=0, y=100)
    yes_button.place(x=110, y=180)
    no_button.place(x=200, y=180)
    del_acc_wind.mainloop()

def settings(client):
    settings_wind = Tk()
    settings_wind.geometry('400x400')
    settings_wind.config(bg='black')
    settings_wind.title('Settings')

    settings_lbl = Label(
        settings_wind,
        text='Settings',
        font=('Times', 20, 'bold'),
        bg='black',
        fg='white'
    )

    items = ['Password', 'Age        ', 'Contact  ']
    item = StringVar(settings_wind)
    item.set(items[0])

    options = ttk.OptionMenu(
        settings_wind,
        item,
        items[0],
        *items,
    )
    
    adj_lbl1 = Label(
        settings_wind,
        text='''
        What would you like
        to change?
        ''',
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white'
    )

    adj_lbl2 = Label(
        settings_wind,
        text='''
        Please Enter
        Your Adjustment
        ''',
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white'
    )

    adjustment = Text(
        settings_wind,
        font=("Courier", 16, 'bold'),
        width=14,
        height=1,
        bg='black',
        fg='white'
    )

    def send_info():
        try:
            client.send('SETTINGS REQUEST'.encode('utf-8'))
    
            if 'Age' in item.get():
                client.send('Age'.encode('utf-8'))
            elif 'Contact' in item.get():
                client.send('Contact'.encode('utf-8'))
            else:
                client.send(item.get().encode('utf-8'))
    
            time.sleep(1)
            client.send(adjustment.get('1.0', 'end').encode('utf-8'))
            done = client.recv(1024).decode('utf-8')
            
            if 'Success' in done:
                s = SuccessWindow()
                exit(1)
        except Exception as e:
            print(e)
            exit(1)

    adj_button = Button(
        settings_wind,
        text='Change',
        width=12,
        font=('Courier', 12, 'bold'),
        bg='blue',
        fg='white',
        command=send_info
    )

    settings_lbl.place(x=160, y=50)
    adj_lbl1.place(x=30, y=90)
    options.place(x=165, y=170)
    adj_lbl2.place(x=45, y=200)
    adjustment.place(x=111, y=264.5)
    adj_button.place(x=140, y=303)
    settings_wind.mainloop()