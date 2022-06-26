import eel
from main import TimeTable

# Set web files folder
eel.init('web')

t = TimeTable()
@eel.expose
def gui(filename):
    jsondata = t.start(filename)
    print(jsondata)
    return jsondata

@eel.expose                         
def add(x,y):
    print('sum')
    output = int(x) + int(y)
    return output


eel.start('start.html', size=(1280,720))  # Start