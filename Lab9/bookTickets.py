from tkinter import *
from tkinter import ttk

class Application(Frame):
	
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()
		self.click()
		self.click1()
		self.display()
		
		
	def create_widgets(self):
		Label(self,text="Movie Application").grid()
		self.r=StringVar()

		self.r1=Radiobutton(self,value="English",variable=self.r,text="English",command=self.click)
		self.r1.grid(row=1,column=0,sticky=W)

		self.r2=Radiobutton(self,value="Kannada",variable=self.r,text="Hindi",command=self.click1)
		self.r2.grid(row=2,column=0,sticky=W)

		Button(self,text="Submit",command=self.display).grid(row=5,column=0,sticky=W)
		self.g=Text(self,width=30,height=20)	
		self.g.grid(row=6,column=0,sticky=W)	
	
		

	def click(self):
		self.c1=BooleanVar()
		Checkbutton(self,variable=self.c1,text="peter parker").grid(row=3,column=0,sticky=W)
		self.op= [1,2,3,4,5]
		self.cb=ttk.Combobox(self,values=self.op,width=10).grid(row=3,column=1,sticky=W)


		self.c2=BooleanVar()
		Checkbutton(self,variable=self.c2,text="spidy").grid(row=4,column=0,sticky=W)
		self.op= [1,2,3,4,5]

		self.cb1=ttk.Combobox(self,values=self.op,width=10).grid(row=4,column=1,sticky=W)

	def click1(self):
		self.c1=BooleanVar()
		Checkbutton(self,variable=self.c1,text="some1").grid(row=3,column=0,sticky=W)
		self.op= [1,2,3,4,5]
		self.cb=ttk.Combobox(self,values=self.op,width=10).grid(row=3,column=1,sticky=W)

		self.c2=BooleanVar()
		Checkbutton(self,variable=self.c2,text="some2").grid(row=4,column=0,sticky=W)
		self.op= [1,2,3,4,5]
		self.cb1=ttk.Combobox(self,values=self.op,width=10).grid(row=4,column=1,sticky=W)	
	def display(self):
		p=""
		if(self.r.get()=="English"):
			if(self.c1.get()):
				p+="spidy\n"
			if(self.c2.get()):
				p+="spidy\n"

		elif(self.r.get()=="Hindi"):
			if(self.c1.get()):
				p+="kirik\n"
			if(self.c2.get()):
				p+="chichore\n"
		if(p==""):
			self.g.delete(0.0,END)
			self.g.insert(0.0,"Error")

		else:
			self.g.delete(0.0,END)
			self.g.insert(0.0,p)	
			print(self.cb.get())
			print(self.cb1.get())
			
			
		
root=Tk()
root.title("movies")
root.geometry("200x200")
app=Application(root)
root.mainloop()
