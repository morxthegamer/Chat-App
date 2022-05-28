class StartUp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.config(bg='black')
        self.window.title('Cord Chat App')
        
        self.chat_label = Label(
            self.window,
            text="Cord Chat",
            font=("Courier", 20, 'bold'),
            bg='black',
            fg='white'
        )

        self.sign_up_button = Button(
            self.window,
            text="Sign Up",
            font=("Courier", 14, "bold"),
            bg='yellow',
            fg='black',
            command=
        )

        self.login_button = Button(
            self.window,
            text="Log In",
            font=("Courier", 14, "bold"),
            bg='green',
            fg='white',
            command=
        )

    def check(self, name, pw):
        i = self.data.getDataJson(f"user[{name}].json")

        if (i["Username"] != name):
            print("Login failed. Wrong Username. Please try again.")
            exit(1)
    
        if (i["Password"] != pw):
            print("Login failed. Wrong Password. Please try again.")
            exit(1)
    
        if (i["Username"] == name and i["Password"] == pw):
            print("Successfully logged in!")
    
    def login(self):
        def keypress(event):
          print('Logging In...\n')
          self.check()

        login_wind = Tk()
        login_wind.geometry('400x400')
        login_wind.config(bg='black')
        login_wind.title('Log In')
        login_wind.bind('<Return>', self.keypress)
    
        login_label = Label(
            login_wind,
            text='Please Login',
            font=('Courier', 20,'bold'),
            bg='black',
            fg='white'
        )
    
        name_label = Label(
            login_wind,
            text='Username:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )
    
        pass_label = Label(
            login_wind,
            text='Password:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )
    
        username = Entry(
            login_wind,
            textvariable=name_label,
            width=30,
        )
    
        password = Entry(
            login_wind,
            textvariable=pass_label,
            width=30,
        )
        
        login_label.place(x=100, y=60)
        name_label.place(x=65, y=140)
        pass_label.place(x=65, y=160)
        username.place(x=145, y=140)
        password.place(x=145, y=160)
        confirm_button.place(x=165, y=200)
    
        i = self.data.getDataJson(f"user[{name}].json")
    
    def sign_up(self):
        sign_up_wind = Tk()
        sign_up_wind.geometry('400x400')
        sign_up_wind.config(bg='black')
        sign_up_wind.title('Sign Up')
    
        # Labels
    
        sign_up_lbl = Label(
            sign_up_wind,
            text='Sign Up',
            font=('Courier', 20, 'bold'),
            bg='black',
            fg='white'
        )
    
        name_label = Label(
            sign_up_wind,
            text='Username:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )
    
        mail_label = Label(
            sign_up_wind,
            text='Email:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )
    
        pass_label = Label(
            sign_up_wind,
            text='Password:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )
    
        age_label = Label(
            sign_up_wind,
            text='Age:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )
    
        phone_number_label = Label(
            sign_up_wind,
            text='Phone Number:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )
    
        # Text Area
    
        username = Entry(
            sign_up_wind,
            textvariable=name_label,
            width=30,
        )
    
        email = Entry(
            sign_up_wind,
            textvariable=mail_label,
            width=30,
        )
    
        password = Entry(
            sign_up_wind,
            textvariable=pass_label,
            width=30,
        )
    
        age = Entry(
            sign_up_wind,
            textvariable=age_label,
            width=30,
        )
    
        phone_number = Entry(
            sign_up_wind,
            textvariable=phone_number_label,
            width=30,
        )
    
        def set_data():
            name, mail, pw, age, number = username.get(), email.get(), password.get(), age.get(), phone_number.get()
            for file in os.listdir('DataBase'):
                filename = file[5:-6]
    
                if name == filename:
                    print('This username is already taken. Please try again.')
                    exit(1)
    
                mail = self.data.getDataJson(file)['Email']
    
                if (email == mail):
                    print('This email is already taken. Please try again.')
                    exit(1)
    
            user = {
                'Username': name,
                'Email': mail,
                'Password': pw,
                'Age': age,
                'Contact': number,
                'Extras': {
                    'Theme': 'white',
                    'Badge': '💬',
                    'Text': 'Type A Message: ',
                    'Boost Subscription': False
                }
            }
    
            print('Signing you up...')
            time.sleep(2)
    
            self.data.setDataJson(f'user[{name}].json', user)
            print(f"Sign up was successful! Welcome {name}.")
    
        confirm_button = Button(
            sign_up_wind,
            text='Sign Up',
            font=('Courier', 12, 'bold'),
            bg='black',
            fg='white',
            command=set_data
        )
    
        sign_up_lbl.place(x=143, y=60)
        name_label.place(x=65, y=140)
        mail_label.place(x=89, y=160)
        pass_label.place(x=65, y=180)
        age_label.place(x=105, y=200)
        phone_number_label.place(x=33, y=220)
    
        username.place(x=145, y=140)
        email.place(x=145, y=160)
        password.place(x=145, y=180)
        age.place(x=145, y=200)
        phone_number.place(x=145, y=220)
        confirm_button.place(x=165, y=280)
    
        sign_up_wind.mainloop()