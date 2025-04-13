fout = open('SURNAME.txt', 'w')
print (fout)

line1= "Welcome. This is my analyzation.\n"
fout.write(line1)

line2= "This program seems to allow me to write sentences,\n"
fout.write(line2)

line3= "provided i have quotes in my assigned variable so it can be read as a string by Pyhton.\n"
fout.write(line3)

line4= "Now,the read function,as the word suggests,allows the program to read my analysis,line by line,\n"
fout.write(line4)

line5= "in which whatever i typed here with the slash n function,would have an output in line by line,\n"
fout.write(line5)

line6= "enabling organization in my sentences. I hope you enjoyed reading my analysis on the code.\n"
fout.write(line6)

line7= "These are essential in reading text files with comprehension and efficiency,saving time and energy."
fout.write(line7)


fout.close()

fhand = open('SURNAME.txt','r')
analysis = fhand.read()
print(analysis)
fhand.close()
