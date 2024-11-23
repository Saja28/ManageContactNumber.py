import json

class ContactNumber:
    def __init__ (self, name, number, hobby):
        self.name= name
        self.number= number
        self.hobby = hobby
    def print_info (self) :
         print(f" {self.name}  {self.number} {self.hobby}")
    
    def save_to_json(self , filename):
        my_contact = { 'name' : self.name, 'number':self.number, 'hobby': self.hobby}
        with open(filename,'w' ) as f :
            f.write(json.dumps(my_contact, indent=2))
    def load_from_json(self, filename): 
        with open(filename,'r') as f:
            data= json.loads(f.read())

        self.name = data['name']
        self.number = data['number']
        self.hobby = data['hobby']


p1 = ContactNumber("mike" , 919990 ,"dancing" )
p1.print_info()
p1.save_to_json("mike.json")

p2 = ContactNumber("Ali" , 91908656 , "none")
p2.print_info()
p2.save_to_json("Ali.json")
        


        


             

#def obj_creator(d):

  #  return ContactNumber(d['name'], d['number'], d['age'])

   # with open('Contact.json', 'r') as fp:
     #   obj = json.load(fp, object_hook = obj_creator)
       # print ("obj")
# prints

##########################3https://www.youtube.com/watch?v=uBiQEL43AQU&ab_channel=LukePeters
        # https://www.youtube.com/watch?v=jABj-SEhtBc&ab_channel=NeuralNine
#from pprint import pprint
#json_data=open('bookmarks.json')
#jdata = json.load(json_data)
#pprint (jdata)
#json_data.close()
# https://stackoverflow.com/questions/8383136/parsing-json-and-searching-through-it



         