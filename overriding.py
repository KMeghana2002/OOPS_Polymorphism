class mock():
    def saturday(self):
        print('nxt week')
    
class remock(mock):
    def saturday(self):
        print('this week')
obj=remock()
obj.saturday()
