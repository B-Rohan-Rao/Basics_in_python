'''TO USE STRINGS THE WORDS SHOULD BE WRITTEN IN SINGLE, DOUBLE OR TRIPPLE QUOTE. IT MUST BE WRITTEN IN SUCH A MANNER THAT THE SYSTEM SHOLD NOT GET CONFUSED BETWEEN WHERE THE QOTATION ENDS.'''

'''CONTATINATING TWO STRINGS'''
#Greeting=''Good morning, ''
#name='' ROHAN''
#print(Greeting+name)

'''or another method can be used by creting another string'''
#Greeting=''Good morning, ''
#name='' ROHAN''
#c=Greeting+name
#print (type (name))
#print=(c)

name = 'ROHAN'
print(name[0])

#STRING SLICING
print(name[0:3])

#NEGETIVE INDICES
c= name [-4:-1] #works same as name[1:4]
print(c)


#FUCTIONS OF STRING 
story="once upon a time there lived a king in a village."
print(len(story))
print(story.endswith("village"))
print(story.count("t"))
print(story.capitalize())
print(story.find("village"))
print(story.replace("king","prince"))