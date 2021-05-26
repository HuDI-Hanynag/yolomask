import getpass
class UserData(object):
    def getUserData(self):
        self.username = input('Enter mciotextension username (user@domain.com) ')
        self.password = getpass.getpass('Enter password:')
        return self.username + ':' + self.password
    
if __name__ == "__main__":
    userData = UserData()
    print(userData.getUserData())
