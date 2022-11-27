from tkinter import *

root = Tk()
root.title("Mutual Funds SIP Goal Calculator")
root.geometry("700x300")
root.config(bg = "light blue")

def Calculate():
    P = int(month_invest_entry.get())
    CAGR = int(return_rate_entry.get())
    time = int(time_period_entry.get())  # in months
    i = CAGR/(time*100)
    Amount_Received_on_maturity = int(P * (((1 + i)**(time)-1) / i) * (1 + i))
    Label(text = f"{Amount_Received_on_maturity}",font = "arial 25 bold").place(x = 400, y = 235)
    
#In the above formula –
# Amount_Rececived_on_maturity : is the amount you receive upon maturity.(calculated considering integer (absolute))
# P is the fixed monthly investment amount ie the amount you invest at regular intervals(monthly).
# time is the number of payments you have made(total no of months).
# i is the periodic rate of interest (i = rate of interest/time)

month_invest = Label(root,text = "Monthly Investment",font = "arial 15")
return_rate = Label(root,text = "Expected Return Rate", font = "arial 15")
time_period = Label(root,text = "Time Period (months)", font = "arial 15")

month_invest.place(x = 30,y = 20)
return_rate.place(x = 30,y = 90)
time_period.place(x = 30,y = 160)

Amount_Recieved_on_maturity = Label(root, text = "Matured Amount ~ ", font = "arial 30").place(x = 50, y = 230)

month_invest_value = StringVar()
return_rate_value = StringVar()
time_period_value = StringVar()

month_invest_entry = Entry(root, textvariable = month_invest_value, font = "arial 20", width = 10)
return_rate_entry = Entry(root, textvariable = return_rate_value, font = "arial 20", width = 8)
time_period_entry = Entry(root, textvariable = time_period_value, font = "arial 20", width = 6)

month_invest_entry.place(x = 300,y=20)
return_rate_entry.place(x = 300,y=90)
time_period_entry.place(x = 300,y=160)

Button(root, text = "Calculate",font = "arial 15", command = Calculate).place(x = 550,y = 20)
Button(root, text = "Exit", command = lambda:exit(),font = "arial 15", width = 8).place(x = 550, y = 90)
root.mainloop()