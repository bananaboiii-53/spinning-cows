import os
filehandle = open('dropdownoptions_out', 'w')
for file in os.listdir("./spokenword"):
    statement = '<option value="'+file+'">'+file+'</option>'
    #print(file)
    #print(statement)
    filehandle.write(statement)
    filehandle.write('\n')
