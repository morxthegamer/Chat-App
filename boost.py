from data import Data
import datetime

class Boost:
    def __init__(self, username, subscription):
        print(f'Welcome {username}, to your Boost Subscription!')
        self.username = username
        self.subscription = subscription
        self.badges = ['green', 'red', 'blue']
        self.badges = ['😀', '😎', '🥱', '✅', '🤖', '🎁', '👀', '✨']
        self.dataset = Data('DataBase')

    def change_features(self):
        adjustment = input('What would you like to change? (Theme, Badge, Text)')

        if (adjustment == 'Theme'):
            data = self.dataset.getDataJson(f'user[{self.username}].json')
            while (True):
                new_theme = input(f'Ok, Enter a new theme: [{self.themes}]')
                if new_theme not in self.themes:
                    print('Not avaliable option.')
                    continue

                data['Theme'] = new_theme
                self.dataset.setDataJson(f'user[{self.username}].json', data)
                break
        
        if (adjustment == 'Badge'):
            data = self.dataset.getDataJson(f'user[{self.username}].json')
            while (True):
                new_badge = input(f'Ok, Enter a new badge: [{self.badges}]')
                if new_badge not in self.badges:
                    print('Not avaliable option.')
                    continue

                data['Badge'] = new_badge
                self.dataset.setDataJson(f'user[{self.username}].json', data)
                break

        if (adjustment == 'Text'):
            data = self.dataset.getDataJson(f'user[{self.username}].json')
            while (True):
                new_text = input(f'Ok, Enter a new frontline text: [{self.badges}]')
                data['Text'] = new_text

                self.dataset.setDataJson(f'user[{self.username}].json', data)
                break

    def set_time(self):
        self.subscription['Months']
        the_time = datetime.datetime.today()