

#WK2 ex1
text = "X-DSPAM-Confidence:    0.8475";
st=text.find(' ')
num=text[st+1:]
num=float(num)
print(num)

#WK3 ex1
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()
    print(line.upper())

#WK3 ex2
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    count=count+1
    stpos=line.find(':')
    num=float(line[stpos+2:])
    total=total+num
print("Average spam confidence:", total/count)


#WK4 ex1
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.split()  
    for i in range(len(words)):
        if words[i] not in lst:
            lst.append(words[i])
lst.sort()
print(lst)


#WK4 ex2
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    line=line.rstrip()
    if not line.startswith('From '): 
        continue
    words=line.split()
    print(words[1])
	
    count=count+1
print('There were', count, 'lines in the file with '
      'From as the first word') 
#text too long, use ' '   ' ' to break the long



#WK5, exercise 1 (assigment 9.4)
#find the email with the highest number of mail sent
#output: email and its count
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts=dict()
emails=list()

for line in handle:
    #line=line.rstrip()
    if not line.startswith('From '):
        continue
    words=line.split()
    emails.append(words[1]) 
    #need to use .append() to add elements to list
        
for email in emails:
        counts[email]=counts.get(email,0)+1

bigemail=None
bigcount=None

for email,count in counts.items():
    if bigcount is None or count>bigcount:
        bigemail=email
        bigcount=count
print(bigemail, bigcount)        
#output is cwen@iupui.edu 5


#WK6. Exercise#1
#Write a program to read through the mbox-short.txt 
#and figure out the distribution by hour of the day 
#for each of the messages. You can pull the hour out 
#from the 'From ' line by finding the time and then 
#splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, 
#print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

times=list()
for line in handle:
    if not line.startswith('From '):
        continue
    words=line.split()
    times.append(words[5])

counts=dict()

for line in times:
    line=line.split(':')
    hour=line[0]
    counts[hour]=counts.get(hour,0)+1
    
for k,v in sorted(counts.items()):
    print(k,v)

