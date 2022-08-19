#reading the file
log_file = open(r"/Users/dominicaamanfo/Downloads/exam.log", 'r')

#reading the lines
lines = log_file.readlines()

count = 0
#conting the lines
for line in lines:

 #conting the lines with ERROR, 23 = start of word, 28 = end of word      
  if line[23:28] == "ERROR":
       count += 1

#print the lines counted
print(count)






