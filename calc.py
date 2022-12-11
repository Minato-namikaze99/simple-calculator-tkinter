import tkinter as tk
import tkinter.messagebox


# couldn't make it a grid because it doesn't allow us to make the buttons resizeable
fr=tk.Tk()
fr.title("Calculator")
fr.geometry("250x230")
fr.config(bg="black")
displaybox=tk.Entry(master=fr, width=80, borderwidth=3)
displaybox.grid(row=0, column=0, columnspan=4, pady=5, padx=5, ipady=5, ipadx=5)

tk.Grid.rowconfigure(fr,0,weight=1) #makes the buttons resizeable
tk.Grid.rowconfigure(fr,1,weight=1)
tk.Grid.rowconfigure(fr,2,weight=1)
tk.Grid.rowconfigure(fr,3,weight=1)
tk.Grid.rowconfigure(fr,4,weight=1)
tk.Grid.rowconfigure(fr,5,weight=1)

tk.Grid.columnconfigure(fr,0,weight=1)
tk.Grid.columnconfigure(fr,1,weight=1)
tk.Grid.columnconfigure(fr,2,weight=1)
tk.Grid.columnconfigure(fr,3,weight=1)


def clicked(num): #displayes the value that we provided as input
    displaybox.insert(tk.END, num)

def equal():
    try:
        x=str(eval(displaybox.get()))
        displaybox.delete(0, tk.END)
        displaybox.insert(0, x)
    except:
        tkinter.messagebox.showerror("ERROR", "The syntax you entered is wrong")

def clear():
    displaybox.delete(0, tk.END)

but_ac=tk.Button(master=fr, text="AC", padx=5, pady=5, width=15, command=lambda: clear())
but_ac.grid(row=1, column=0, pady=2, padx=2)

but_div=tk.Button(master=fr, text="/", padx=5, pady=5, width=15, command=lambda: clicked("/"))
but_div.grid(row=1, column=1, pady=2, padx=2)

but_mult=tk.Button(master=fr, text="*", padx=5, pady=5, width=15, command=lambda: clicked("*"))
but_mult.grid(row=1, column=2, pady=2, padx=2)

but_minus=tk.Button(master=fr, text="-", padx=5, pady=5, width=15, command=lambda: clicked("-"))
but_minus.grid(row=1, column=3, pady=2, padx=2)

but_7=tk.Button(master=fr, text="7", padx=5, pady=5, width=15, command=lambda: clicked(7))
but_7.grid(row=2, column=0, pady=2, padx=2)

but_8=tk.Button(master=fr, text="8", padx=5, pady=5, width=15, command=lambda: clicked(8))
but_8.grid(row=2, column=1, pady=2, padx=2)

but_9=tk.Button(master=fr, text="9", padx=5, pady=5, width=15, command=lambda: clicked(9))
but_9.grid(row=2, column=2, pady=2, padx=2)

but_4=tk.Button(master=fr, text="4", padx=5, pady=5, width=15, command=lambda: clicked(4))
but_4.grid(row=3, column=0, pady=2, padx=2)

but_5=tk.Button(master=fr, text="5", padx=5, pady=5, width=15, command=lambda: clicked(5))
but_5.grid(row=3, column=1, pady=2, padx=2)

but_6=tk.Button(master=fr, text="6", padx=5, pady=5, width=15, command=lambda: clicked(6))
but_6.grid(row=3, column=2, pady=2, padx=2)

but_1=tk.Button(master=fr, text="1", padx=5, pady=5, width=15, command=lambda: clicked(1))
but_1.grid(row=4, column=0, pady=2, padx=2)

but_2=tk.Button(master=fr, text="2", padx=5, pady=5, width=15, command=lambda: clicked(2))
but_2.grid(row=4, column=1, pady=2, padx=2)

but_3=tk.Button(master=fr, text="3", padx=5, pady=5, width=15, command=lambda: clicked(3))
but_3.grid(row=4, column=2, pady=2, padx=2)

but_0=tk.Button(master=fr, text="0", padx=5, pady=5, width=15, command=lambda: clicked(0))
but_0.grid(row=5, column=0, pady=2, padx=2)

but_00=tk.Button(master=fr, text="00", padx=5, pady=5, width=15, command=lambda: clicked("00"))
but_00.grid(row=5, column=1, pady=2, padx=2)

but_dot=tk.Button(master=fr, text=".", padx=5, pady=5, width=15, command=lambda: clicked("."))
but_dot.grid(row=5, column=2, pady=2, padx=2)

but_plus=tk.Button(master=fr, text="+", padx=5, pady=5, width=15, command=lambda: clicked("+"))
but_plus.grid(row=2, column=3, pady=2, padx=2, rowspan=2, sticky="nswe")

but_equals=tk.Button(master=fr, text="=", padx=5, pady=5, width=15, command=lambda: equal())
but_equals.grid(row=4, column=3, pady=2, padx=2, rowspan=2, sticky="nswe")




fr.mainloop()