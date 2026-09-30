from tkinter import *
window=Tk()#creates window
window.geometry("500x500")#the measureemnts of the window
window.title("restaurant")
window.config(background="red")


def calculateprice():
    foods=spinboxone.get()
    amounto=int(spinboxtwo.get())
    drinks=spinboxthree.get()
    amountt=int(spinboxfour.get())
    deserts=spinboxfive.get()
    amounth=int(spinboxsix.get())
    desp=0
    drinkp=0
    foodp=0


    if foods=="pizza":
        foodp=5*amounto
        
    elif foods=="burger":
        foodp=6*amounto
        
    elif foods=="none":
        foodp=0*amounto
        
    elif drinks=="cola":
        drinkp=6*amountt
        
    elif drinks=="sprite":
        drinkp=1*amountt
        
    elif drinks=="none":
        drinkp=0*amountt

    elif deserts=="cake":
        desp=8*amounth

    elif deserts=="icecream":
        desp=5*amounth

    elif deserts=="none":
        desp=0*amounth
    
    prices=desp+drinkp+foodp    
    price.config(text="The total price is "+str(prices))

name=Label(window,text="NAME:",font=("Arial",17),background="red",foreground="white")
email=Label(window,text="EMAIL:",font=("Arial",17),background="red",foreground="white")
nameentry=Entry(window,foreground="dark blue")
emailentry=Entry(window,foreground="dark blue")
nameentry.place(x=190,y=105)
emailentry.place(x=190,y=75)
name.place(x=100,y=95)
email.place(x=100,y=70)

food=Label(window,text="what food would you like?:pizza ,burger or none",font=("Arial",14),background="red",foreground="white")
food.place(x=50,y=150)
spinboxone=Spinbox(window,values=("pizza","burger","none"))
spinboxtwo=Spinbox(window,from_=0,to=50)
spinboxone.place(x=100,y=185)
spinboxtwo.place(x=240,y=185)

beverage=Label(window,text="what drink would you like ? cola, sprite, water, or none",font=("Arial",14),background="red",foreground="white")
beverage.place(x=45,y=210)
spinboxthree=Spinbox(window,values=("cola","sprite","none"))
spinboxfour=Spinbox(window,from_=0,to=50)
spinboxthree.place(x=100,y=245)
spinboxfour.place(x=240,y=245)

desert=Label(window,text="what desert would you like?:cake, icecream, or none",font=("Arial",14),background="red",foreground="white")
desert.place(x=45,y=270)
spinboxfive=Spinbox(window,values=("cake","icecream","none"))
spinboxsix=Spinbox(window,from_=0,to=50)
spinboxfive.place(x=100,y=305)
spinboxsix.place(x=240,y=305)



submit_button=Button(window,text="calculate total price",command=calculateprice)
submit_button.place(x=170,y=365)

price=Label(window,text=" total price:",font=("Arial",17),background="red",foreground="white")
price.place(x=170,y=410)






window.mainloop()
