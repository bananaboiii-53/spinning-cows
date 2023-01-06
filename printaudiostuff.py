import os
filehandle = open('audiostuff_out', 'w')
for file in os.listdir("./spokenword"):
    path = 'spokenword/' + file
    statement = '<audio controls><source src=' + "\"" + path + "\"" + ' type="audio/mpeg">Please download the latest MP3 codec from a reliable source in order to play this file, if you choose.</audio><br /><br />'
    #print(file)
    #print(statement)
    filehandle.write(file)
    filehandle.write('\n')
    filehandle.write(statement)
    filehandle.write('\n')
