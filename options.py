from tkinter import *
from chat_client import Client

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
        client.send('DELETE ACCOUNT REQUEST'.encode('utf-8'))
        done = client.recv(1024).decode('utf-8')
        print(done)
        exit(0)

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
        font=('Times', 20, 'bold')
    )

    items = ['Password', 'Age', 'Contact']
    item = StringVar(settings_wind)
    item.set(items[0])

    options = OptionMenu(
        settings_wind,
        item,
        items[0],
        *items
    )
    
    adj_lbl = Label(
        settings_wind,
        text='What would you like to change?',
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white'
    )

    adjustment = Entry(
        settings_wind,
        textvariable=adj_lbl,
        width=30
    )

    adj_button = Button(
        settings_wind,
        text='Change',
        font=('Courier', 12, 'bold'),
        bg='white',
        fg='green'
    )

    def send_info():
        pass

    settings_lbl.pack()
    options.pack()
    adjustment.pack()
    adj_button.pack()
    settings_wind.mainloop()
