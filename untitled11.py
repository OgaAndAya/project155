from tkinter import*

root= Tk()
root.title("Random Colours Dictionary")
root.geometry("500x500")
root.configure(background= "green")




dictionary=  {'Key': '"maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"',
              }

def bg_color_change():
    random_color= random.randint(0,7)
    print(dictionary["Color"][random_color])
    root.configure(background= dictionary["Color"]["random_color"])
    
    btn= Button(root,text= "Click me to change the color", command= bg_color_change)
    btn.place(relx= 0.5, rely= 0.5, anchor= CENTER)


root.mainloop()
