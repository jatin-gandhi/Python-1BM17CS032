class CallDetails(object) :
	def __init__(self,number,sender,receiver,duration,typ):
		self.number=number
		self.sender=sender
		self.receiver=receiver
		self.duration=duration
		self.type=typ

class Util:
	def __init__(self):
		self.list_of_call_objects =[]
		
	def parse_customer(self,list_of_call_st):
		i=0		
		for call in list_of_call_st:
			i+=1
			details = call.split(',')
			self.list_of_call_objects.append(CallDetails(i,details[0],details[1],details[2],details[3]))
	def show(self):
		for obj in self.list_of_call_objects:
			print("\nCustomer:",obj.number,"\nSender: ",obj.sender,"\nReceiver: " ,obj.receiver,"\nDuration :",obj.duration,"\nCall Type: ",obj.type)




call='9990000001,9330000001,23,STD'

call2='9990000001,9330000002,54,Local'

call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]

uobject=Util()
uobject.parse_customer(list_of_call_string)
uobject.show()


"""OUTPUT


Customer: 1 
Sender:  9990000001 
Receiver:  9330000001 
Duration : 23 
Call Type:  STD

Customer: 2 
Sender:  9990000001 
Receiver:  9330000002 
Duration : 54 
Call Type:  Local

Customer: 3 
Sender:  9990000001 
Receiver:  9330000003 
Duration : 6 
Call Type:  ISD
"""
