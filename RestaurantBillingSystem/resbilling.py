import random
import time
import datetime
import tkinter.messagebox
from tkinter import *

root=Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background= 'Cadet Blue')

Tops= Frame(root, bg='Cadet Blue', bd=20, pady =5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle =Label(Tops, font=('arial',58,'bold'),text='Restaurant Management System',bd=21,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_F= Frame(root, bg='Powder Blue', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame= Frame(root, bg='Cadet Blue', bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='Powder Blue', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Cadet Blue', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Chickdish_F=Frame(MenuFrame, bg='Powder Blue', bd=10, relief=RIDGE)
Chickdish_F.pack(side=RIGHT)

#===========================================Variables==============================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder= StringVar()
Receipt_Ref= StringVar()
PaidTax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()
CostofDishes= StringVar()
CostofDrinks= StringVar()
ServiceCharge= StringVar()

text_Input= StringVar()
operator=""

E_Thumbsup=StringVar()
E_Redbull=StringVar()
E_Sevenup=StringVar()
E_Bira=StringVar()
E_Corona=StringVar()
E_Budweiser=StringVar()
E_Hoegaarden=StringVar()
E_Heineken=StringVar()

E_Roganjosh=StringVar()
E_Butterchicken=StringVar()
E_Tikkamasala=StringVar()
E_Bhuna=StringVar()
E_Hybiryani=StringVar()
E_Dumbiryani=StringVar()
E_Kadhai=StringVar()
E_Chefspecial=StringVar()

E_Thumbsup.set("0")
E_Redbull.set("0")
E_Sevenup.set("0")
E_Bira.set("0")
E_Corona.set("0")
E_Budweiser.set("0")
E_Hoegaarden.set("0")
E_Heineken.set("0")

E_Roganjosh.set("0")
E_Butterchicken.set("0")
E_Tikkamasala.set("0")
E_Bhuna.set("0")
E_Hybiryani.set("0")
E_Dumbiryani.set("0")
E_Kadhai.set("0")
E_Chefspecial.set("0")

DateofOrder.set(time.strftime("%d/%m/%Y"))

#===========================================Function Declaration======================================
class funcdeclare:
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Exit", "Are you sure?")
        if iExit>0:
            root.destroy()
            return

    def Reset(self):
        E_Thumbsup.set("0")
        E_Redbull.set("0")
        E_Sevenup.set("0")
        E_Bira.set("0")
        E_Corona.set("0")
        E_Budweiser.set("0")
        E_Hoegaarden.set("0")
        E_Heineken.set("0")

        E_Roganjosh.set("0")
        E_Butterchicken.set("0")
        E_Tikkamasala.set("0")
        E_Bhuna.set("0")
        E_Hybiryani.set("0")
        E_Dumbiryani.set("0")
        E_Kadhai.set("0")
        E_Chefspecial.set("0")

        CostofDishes.set("0")
        CostofDrinks.set("0")
        ServiceCharge.set("0")
        SubTotal.set("0")
        PaidTax.set("0")
        TotalCost.set("0")

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

        txtThumbsup.configure(state =DISABLED)
        txtRedbull.configure(state=DISABLED)
        txtSevenup.configure(state=DISABLED)
        txtBira.configure(state=DISABLED)
        txtCorona.configure(state=DISABLED)
        txtBudweiser.configure(state=DISABLED)
        txtHoegaarden.configure(state=DISABLED)
        txtHeineken.configure(state=DISABLED)
        txtRoganjosh.configure(state=DISABLED)
        txtButterChicken.configure(state=DISABLED)
        txtTikkamasala.configure(state=DISABLED)
        txtBhuna.configure(state=DISABLED)
        txtHybiryani.configure(state=DISABLED)
        txtDumbiryani.configure(state=DISABLED)
        txtKadhai.configure(state=DISABLED)
        txtChefspecial.configure(state=DISABLED)

    def CostofItem(self):
        Item1=float(E_Thumbsup.get())
        Item2=float(E_Redbull.get())
        Item3=float(E_Sevenup.get())
        Item4=float(E_Bira.get())
        Item5=float(E_Corona.get())
        Item6=float(E_Budweiser.get())
        Item7=float(E_Hoegaarden.get())
        Item8=float(E_Heineken.get())

        Item9=float(E_Roganjosh.get())
        Item10=float(E_Butterchicken.get())
        Item11=float(E_Tikkamasala.get())
        Item12=float(E_Bhuna.get())
        Item13=float(E_Hybiryani.get())
        Item14=float(E_Dumbiryani.get())
        Item15=float(E_Kadhai.get())
        Item16=float(E_Chefspecial.get())

        PriceofDrinks=((Item1 * 40 ) + (Item2 * 200) + (Item3 * 40) + (Item4 * 300)
                       + (Item5 * 150) + (Item6 * 200) + (Item7 * 200) + (Item8 * 300))
        PriceofDishes=((Item9 * 200) + (Item10 * 250) + (Item11 * 230) + (Item12 * 200)
                       + (Item13 * 300) + (Item14 * 280) + (Item15 * 200) + (Item16 * 400))

        DrinksPrice="Rs", str('%.2f'%(PriceofDrinks))
        DishesPrice="Rs", str('%.2f'%(PriceofDishes))
        CostofDishes.set(DishesPrice)
        CostofDrinks.set(DrinksPrice)
        SC="Rs", str('%.2f'%(2.5))
        ServiceCharge.set(SC)

        SubTotalofITEMS="Rs", str('%.2f'%(PriceofDrinks + PriceofDishes + 2.5))
        SubTotal.set(SubTotalofITEMS)

        Tax="Rs", str('%.2f'%((PriceofDrinks + PriceofDishes + 2.5)*0.5))
        PaidTax.set(Tax)
        TT=((PriceofDrinks + PriceofDishes + 2.5) * 0.5)
        TC="Rs", str('%.2f'%(PriceofDishes + PriceofDrinks + 2.5 + TT))
        TotalCost.set(TC)


    def chkThumbsup(self):
        if(var1.get()==1):
            txtThumbsup.configure(state= NORMAL)
            txtThumbsup.focus()
            txtThumbsup.delete('0', END)
            E_Thumbsup.set("")
        elif(var1.get()==0):
            txtThumbsup.configure(state= DISABLED)
            E_Thumbsup.set("0")
    def chkRedbull(self):
        if(var2.get()==1):
            txtRedbull.configure(state= NORMAL)
            txtRedbull.focus()
            txtRedbull.delete('0', END)
            E_Redbull.set("")
        elif(var2.get()==0):
            txtRedbull.configure(state= DISABLED)
            E_Redbull.set("0")
    def chkSevenup(self):
        if(var3.get()==1):
            txtSevenup.configure(state= NORMAL)
            txtSevenup.focus()
            txtSevenup.delete('0', END)
            E_Sevenup.set("")
        elif(var3.get()==0):
            txtSevenup.configure(state= DISABLED)
            E_Sevenup.set("0")
    def chkBira(self):
        if(var4.get()==1):
            txtBira.configure(state= NORMAL)
            txtBira.focus()
            txtBira.delete('0', END)
            E_Bira.set("")
        elif(var4.get()==0):
            txtBira.configure(state= DISABLED)
            E_Bira.set("0")
    def chkCorona(self):
        if(var5.get()==1):
            txtCorona.configure(state= NORMAL)
            txtCorona.focus()
            txtCorona.delete('0', END)
            E_Corona.set("")
        elif(var5.get()==0):
            txtCorona.configure(state= DISABLED)
            E_Corona.set("0")
    def chkBudweiser(self):
        if(var6.get()==1):
            txtBudweiser.configure(state= NORMAL)
            txtBudweiser.focus()
            txtBudweiser.delete('0', END)
            E_Budweiser.set("")
        elif(var6.get()==0):
            txtBudweiser.configure(state= DISABLED)
            E_Budweiser.set("0")
    def chkHoegaarden(self):
        if(var7.get()==1):
            txtHoegaarden.configure(state= NORMAL)
            txtHoegaarden.focus()
            txtHoegaarden.delete('0', END)
            E_Hoegaarden.set("")
        elif(var7.get()==0):
            txtHoegaarden.configure(state= DISABLED)
            E_Hoegaarden.set("0")
    def chkHeineken(self):
        if(var8.get()==1):
            txtHeineken.configure(state= NORMAL)
            txtHeineken.focus()
            txtHeineken.delete('0', END)
            E_Heineken.set("")
        elif(var8.get()==0):
            txtHeineken.configure(state= DISABLED)
            E_Heineken.set("0")
    def chkRoganjosh(self):
        if(var9.get()==1):
            txtRoganjosh.configure(state= NORMAL)
            txtRoganjosh.focus()
            txtRoganjosh.delete('0', END)
            E_Roganjosh.set("")
        elif(var9.get()==0):
            txtRoganjosh.configure(state= DISABLED)
            E_Roganjosh.set("0")
    def chkButterchicken(self):
        if(var10.get()==1):
            txtButterChicken.configure(state= NORMAL)
            txtButterChicken.focus()
            txtButterChicken.delete('0', END)
            E_Butterchicken.set("")
        elif(var10.get()==0):
            txtButterChicken.configure(state= DISABLED)
            E_Butterchicken.set("0")
    def chkTikkamasala(self):
        if(var11.get()==1):
            txtTikkamasala.configure(state= NORMAL)
            txtTikkamasala.focus()
            txtTikkamasala.delete('0', END)
            E_Tikkamasala.set("")
        elif(var11.get()==0):
            txtTikkamasala.configure(state= DISABLED)
            E_Tikkamasala.set("0")
    def chkBhuna(self):
        if(var12.get()==1):
            txtBhuna.configure(state= NORMAL)
            txtBhuna.focus()
            txtBhuna.delete('0', END)
            E_Bhuna.set("")
        elif(var12.get()==0):
            txtBhuna.configure(state= DISABLED)
            E_Bhuna.set("0")
    def chkHybiryani(self):
        if(var13.get()==1):
            txtHybiryani.configure(state= NORMAL)
            txtHybiryani.focus()
            txtHybiryani.delete('0', END)
            E_Hybiryani.set("")
        elif(var13.get()==0):
            txtHybiryani.configure(state= DISABLED)
            E_Hybiryani.set("0")
    def chkDumbiryani(self):
        if(var14.get()==1):
            txtDumbiryani.configure(state= NORMAL)
            txtDumbiryani.focus()
            txtDumbiryani.delete('0', END)
            E_Dumbiryani.set("")
        elif(var14.get()==0):
            txtDumbiryani.configure(state= DISABLED)
            E_Dumbiryani.set("0")
    def chkKadhai(self):
        if(var15.get()==1):
            txtKadhai.configure(state= NORMAL)
            txtKadhai.focus()
            txtKadhai.delete('0', END)
            E_Kadhai.set("")
        elif(var15.get()==0):
            txtKadhai.configure(state= DISABLED)
            E_Kadhai.set("0")
    def chkChefspecial(self):
        if(var16.get()==1):
            txtChefspecial.configure(state= NORMAL)
            txtChefspecial.focus()
            txtChefspecial.delete('0', END)
            E_Chefspecial.set("")
        elif(var16.get()==0):
            txtChefspecial.configure(state= DISABLED)
            E_Chefspecial.set("0")
    def Receipt(self):
        txtReceipt.delete("1.0",END)
        x= random.randint(10903, 609235)
        randomRef= str(x)
        Receipt_Ref.set("BILL" + randomRef)

        txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + "\t" + DateofOrder.get() + "\n")
        txtReceipt.insert(END, 'Item:\t\t\t' + "No of Items\n")
        txtReceipt.insert(END, 'Thumbsup: \t\t\t\t' + E_Thumbsup.get() + "\n")
        txtReceipt.insert(END, 'Red Bull: \t\t\t\t' + E_Redbull.get() + "\n")
        txtReceipt.insert(END, '7Up: \t\t\t\t' + E_Sevenup.get() + "\n")
        txtReceipt.insert(END, 'Bira: \t\t\t\t' + E_Bira.get() + "\n")
        txtReceipt.insert(END, 'Corona: \t\t\t\t' + E_Corona.get() + "\n")
        txtReceipt.insert(END, 'Budweiser: \t\t\t\t' + E_Budweiser.get() + "\n")
        txtReceipt.insert(END, 'Hoegaarden: \t\t\t\t' + E_Hoegaarden.get() + "\n")
        txtReceipt.insert(END, 'Heineken: \t\t\t\t' + E_Heineken.get() + "\n")
        txtReceipt.insert(END, 'Chicken Rogan Josh Biryani: \t\t\t\t' + E_Roganjosh.get() + "\n")
        txtReceipt.insert(END, 'Butter Chicken Biryani: \t\t\t\t' + E_Butterchicken.get() + "\n")
        txtReceipt.insert(END, 'Chicken Tikka Masala Biryani: \t\t\t\t' + E_Tikkamasala.get() + "\n")
        txtReceipt.insert(END, 'Chicken Bhuna Biryani: \t\t\t\t' + E_Bhuna.get() + "\n")
        txtReceipt.insert(END, 'Chicken Hyderabadi Biryani: \t\t\t\t' + E_Hybiryani.get() + "\n")
        txtReceipt.insert(END, 'Chicken Dum Biryani: \t\t\t\t' + E_Dumbiryani.get() + "\n")
        txtReceipt.insert(END, 'Chicken Kadhai Biryani: \t\t\t\t' + E_Kadhai.get() + "\n")
        txtReceipt.insert(END, 'Chef\'s special Biryani: \t\t\t\t' + E_Chefspecial.get() + "\n")

obj=funcdeclare()

#===========================================Drinks===================================================

Thumbsup=Checkbutton(Drinks_F, text='Thumbs Up', variable=var1, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkThumbsup).grid(row=0,sticky=W)
Redbull=Checkbutton(Drinks_F, text='Red Bull', variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkRedbull).grid(row=1,sticky=W)
Sevenup=Checkbutton(Drinks_F, text='7 Up', variable=var3, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkSevenup).grid(row=2,sticky=W)
Bira=Checkbutton(Drinks_F, text='Bear', variable=var4, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkBira).grid(row=3,sticky=W)
Corona=Checkbutton(Drinks_F, text='Sprite', variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkCorona).grid(row=4,sticky=W)
Budweiser=Checkbutton(Drinks_F, text='Mango_Juise', variable=var6, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkBudweiser).grid(row=5,sticky=W)
Hoegaarden=Checkbutton(Drinks_F, text='Corona', variable=var7, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkHoegaarden).grid(row=6,sticky=W)
Heineken=Checkbutton(Drinks_F, text='Water', variable=var8, onvalue=1, offvalue=0, font=('arial',18,'bold')
                  ,bg= "Powder Blue", command=obj.chkHeineken).grid(row=7,sticky=W)


#===========================================Entry Box for Drinks===========================================================

txtThumbsup= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Thumbsup)
txtThumbsup.grid(row=0,column=1)

txtRedbull= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Redbull)
txtRedbull.grid(row=1,column=1)

txtSevenup= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Sevenup)
txtSevenup.grid(row=2,column=1)

txtBira= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Bira)
txtBira.grid(row=3,column=1)

txtCorona= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Corona)
txtCorona.grid(row=4,column=1)

txtBudweiser= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Budweiser)
txtBudweiser.grid(row=5,column=1)

txtHoegaarden= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Hoegaarden)
txtHoegaarden.grid(row=6,column=1)

txtHeineken= Entry(Drinks_F,font=('arial',16,'bold'),bd=8, width=6, justify=LEFT, state= DISABLED, textvariable=E_Heineken)
txtHeineken.grid(row=7,column=1)


#===========================================Foods=================================================================

Roganjosh=Checkbutton(Chickdish_F, text='Chicken Biryani', variable=var9, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkRoganjosh).grid(row=0,sticky=W)
ButterChicken=Checkbutton(Chickdish_F, text='Butter Chicken Biryani', variable=var10, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkButterchicken).grid(row=1,sticky=W)
Tikkamasala=Checkbutton(Chickdish_F, text='Chicken Tikka Masala Biryani', variable=var11, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue",command=obj.chkTikkamasala).grid(row=2,sticky=W)
Bhuna=Checkbutton(Chickdish_F, text='Egg Biryani', variable=var12, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkBhuna).grid(row=3,sticky=W)
Hybiryani=Checkbutton(Chickdish_F, text='Matar Panner', variable=var13, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkHybiryani).grid(row=4,sticky=W)
Dumbiryani=Checkbutton(Chickdish_F, text='Chola Bhatura', variable=var14, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkDumbiryani).grid(row=5,sticky=W)
Kadhai=Checkbutton(Chickdish_F, text='Panner Mashala', variable=var15, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkKadhai).grid(row=6,sticky=W)
Chefspecial=Checkbutton(Chickdish_F, text='Chef\'s special Chicken Biryani', variable=var16, onvalue=1, offvalue=0, font=('arial',16,'bold')
                  ,bg= "Powder Blue", command=obj.chkChefspecial).grid(row=7,sticky=W)


#===========================================Entry Box for Foods===================================================

txtRoganjosh= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Roganjosh)
txtRoganjosh.grid(row=0,column=1)
txtButterChicken= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Butterchicken)
txtButterChicken.grid(row=1,column=1)
txtTikkamasala= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Tikkamasala)
txtTikkamasala.grid(row=2,column=1)
txtBhuna= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Bhuna)
txtBhuna.grid(row=3,column=1)
txtHybiryani= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Hybiryani)
txtHybiryani.grid(row=4,column=1)
txtDumbiryani= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Dumbiryani)
txtDumbiryani.grid(row=5,column=1)
txtKadhai= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Kadhai)
txtKadhai.grid(row=6,column=1)
txtChefspecial= Entry(Chickdish_F,font=('arial',16,'bold'),bd=8, width=10, justify=LEFT, state= DISABLED, textvariable=E_Chefspecial)
txtChefspecial.grid(row=7,column=1)

#=======================================================Total Cost=========================================================
lblCostofDrinks =Label(Cost_F, font=('arial',14,'bold'),text='Cost of Drinks\t',bg='Powder Blue',fg='black')
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1)

lblCostofDishes =Label(Cost_F, font=('arial',14,'bold'),text='Cost of Dishes\t',bg='Powder Blue',fg='black')
lblCostofDishes.grid(row=1,column=0, sticky=W)
txtCostofDishes= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=CostofDishes)
txtCostofDishes.grid(row=1, column=1)

lblServiceCharge =Label(Cost_F, font=('arial',14,'bold'),text='Service Charge\t',bg='Powder Blue',fg='black')
lblServiceCharge.grid(row=2,column=0, sticky=W)
lblServiceCharge= Entry(Cost_F, bg='white',width=40, bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=ServiceCharge)
lblServiceCharge.grid(row=2, column=1)

#=======================================================Payment Information================================================
lblPaidTax =Label(Cost_F, font=('arial',14,'bold'),text='\tPaid Tax',bg='Powder Blue',fg='black')
lblPaidTax.grid(row=0,column=2, sticky=W)
txtPaidTax= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=0, column=3)

lblSubTotal =Label(Cost_F, font=('arial',14,'bold'),text='\tSub Total',bg='Powder Blue',fg='black')
lblSubTotal.grid(row=1,column=2, sticky=W)
txtSubTotal= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=1, column=3)

lblTotalCost =Label(Cost_F, font=('arial',14,'bold'),text='\tTotal Cost',bg='Powder Blue',fg='black')
lblTotalCost.grid(row=2,column=2, sticky=W)
txtTotalCost= Entry(Cost_F, width=40, bg='white', bd=7, font=('arial',7,'bold'), justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=2, column=3)


#=======================================================Receipt============================================================

txtReceipt= Text(Receipt_F, width=46, height=12, bg='white', bd=4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)

#=======================================================Buttons============================================================

btnTotal=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Total", bg="Powder Blue", command=obj.CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Receipt", bg="Powder Blue", command=obj.Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Reset", bg="Powder Blue", command=obj.Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="Exit", bg="Powder Blue", command=obj.iExit).grid(row=0,column=3)

#=======================================================Calculator Display=================================================

class calcfunc:
    def btnClick(self,numbers):
        global operator
        operator= operator + str(numbers)
        text_Input.set(operator)

    def btnClear(self):
        global operator
        operator = ""
        text_Input.set("")

    def btnEquals(self):
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator = ""

    txtDisplay= Entry(Cal_F, width=45, bg='white', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable= text_Input)
    txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
    txtDisplay.insert(0,"0")

obj1=calcfunc()

#=======================================================Calculator Buttons=================================================

btn7=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="7", bg="Powder Blue", command=lambda:obj1.btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="8", bg="Powder Blue", command=lambda:obj1.btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="9", bg="Powder Blue", command=lambda:obj1.btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="+", bg="Powder Blue", command=lambda:obj1.btnClick("+")).grid(row=2,column=3)

#=======================================================Calculator Buttons=================================================

btn4=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="4", bg="Powder Blue", command=lambda:obj1.btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="5", bg="Powder Blue", command=lambda:obj1.btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="6", bg="Powder Blue", command=lambda:obj1.btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="-", bg="Powder Blue", command=lambda:obj1.btnClick("-")).grid(row=3,column=3)

#=======================================================Calculator Buttons=================================================

btn1=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="1", bg="Powder Blue", command=lambda:obj1.btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="2", bg="Powder Blue", command=lambda:obj1.btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="3", bg="Powder Blue", command=lambda:obj1.btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="*", bg="Powder Blue", command=lambda:obj1.btnClick("*")).grid(row=4,column=3)

#=======================================================Calculator Buttons=================================================

btn0=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="0", bg="Powder Blue", command=lambda:obj1.btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="C", bg="Powder Blue", command=obj1.btnClear).grid(row=5,column=1)
btnEquals=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="=", bg="Powder Blue", command=obj1.btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F, padx=16, pady=1, bd=7, fg='black', font=('arial',16,'bold'),
                width=4, text="/", bg="Powder Blue", command=lambda:obj1.btnClick("/")).grid(row=5,column=3)


root.mainloop()
