from tkinter import *
    

def DeziToDual():
    ip = ""
    dual = ["", "", "", ""]
    dezi = [int(edtDezi1.get()), int(edtDezi2.get()),
             int(edtDezi3.get()), int(edtDezi4.get())]
    step = 128
    while(step != 0):
        for i in range(4):
            dual[i] += str(int(dezi[i] / step))
            if(int(dezi[i] / step) != 0):
                dezi[i] -= step
        step = int(step / 2)
    ip += dual[0] + "." + dual[1] + "." + dual[2] + "." + dual[3]
    lblGetDual.config(text = ip)

root = Tk()
root.title("Dezi2Dual")
root.geometry("325x100")

lblDezi = Label(root, text = "Dezimal: ")
lblDezi.place(x = 25, y = 25)

edtDezi = []

edtDezi1 = Entry(root, width = 3)
edtDezi1.place(x = 100, y = 25)
edtDezi2 = Entry(root, width = 3)
edtDezi2.place(x = 135, y = 25)
edtDezi3 = Entry(root, width = 3)
edtDezi3.place(x = 169, y = 25)
edtDezi4 = Entry(root, width = 3)
edtDezi4.place(x = 202, y = 25)

lblDual = Label(root, text = "Dual: ")
lblDual.place(x = 25, y = 50)

lblGetDual = Label(root, text = "00000000.00000000.00000000.00000000")
lblGetDual.place(x = 100, y = 50)

btnDezi = Button(root, text = "Dual", command = DeziToDual,
                 width = 7, relief = GROOVE)
btnDezi.place(x = 250, y = 20)

root.mainloop()
