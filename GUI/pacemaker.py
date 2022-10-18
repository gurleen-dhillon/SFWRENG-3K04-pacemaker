from tkinter import *
from tkinter import messagebox
import ast

def launchApp():
    app = Tk()
    app.title("App")
    app.geometry('950x500+300+150')
    app.configure(bg='white')
    app.resizable(False, False)

    heading1 = Label(app, text='Choose Pacemaker Mode', fg='#737CA1', bg='white',
                     font=('Microsoft YaHei UI Light', 16, 'bold'))
    heading1.place(x=35, y=20)
    ## MODE SELECTION
    modes = [
        "AOO",
        "VOO",
        "AAI",
        "VVI",
    ]
    menuFrame = Frame(app, width=150, height=25, bg='white')
    menuFrame.place(x=310, y=0)
    displayFrame = Frame(app, width=900, height=425, bg='white')
    displayFrame.place(x=20, y=50)


    def clear_frame():
        for widgets in displayFrame.winfo_children():
            widgets.destroy()

    def selected(x):
        clear_frame()
        setButton()
        if x=='AOO' or x=='VOO':
            LRL_slider()
            URL_slider()
            AA_slider()
            APW_slider()
        elif x=='AAI':
            LRL_slider()
            URL_slider()
            AA_slider()
            APW_slider()
            ARP_slider()
            A_sens()
            PVARP()
            hyst()
            rateSm()
        elif x=='VVI':
            LRL_slider()
            URL_slider()
            AA_slider()
            APW_slider()
            VRP_slider()
            V_sens()
            hyst()
            rateSm()
        global modeSet
        print(x)
        modeSet=x
        return modeSet


    clicked = StringVar()
    clicked.set(modes[0])
    dropdown = OptionMenu(menuFrame, clicked, *modes, command=selected)
    dropdown.config(bg='white', width=10, fg='black', activebackground='white', activeforeground='#737CA1')
    dropdown["menu"].config(bg="white", fg="black", activebackground="white", activeforeground="#737CA1")
    dropdown.pack(side='left')
    dropdown.pack(pady=20)


    ## SLIDER

    # def selectedLRL(x):
    #     global LRL_value
    #     LRL_value=IntVar()
    #     LRL_value=x
    def LRL_slider():
        LRL_modes = [
        "30","35","40","45","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70",
        "70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89",
        "90","95","105","110","115","120","125","130","135","140","145","150","155","160","165","170","175",
        ]
        global clickedLRL
        clickedLRL = StringVar()
        clickedLRL.set(LRL_modes[14])
        dropdownLRL = OptionMenu(displayFrame, clickedLRL, *LRL_modes)
        dropdownLRL.config(bg='white', width=10, fg='black', activebackground='white', activeforeground='#737CA1')
        dropdownLRL["menu"].config(bg="white", fg="black", activebackground="white", activeforeground="#737CA1")
        dropdownLRL.place(x=200,y=50)

        # s1 = Scale(displayFrame, from_=30, to=175, orient=HORIZONTAL, length=250, resolution=5, background='white',troughcolor='#737CA1',activebackground='white')
        # s1.place(x=200, y=50)
        # s1.set(60)
        Label(displayFrame, text='Lower Rate Limit (ppm):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=0, y=50)
    def URL_slider():
        global URL_value
        URL_value=IntVar()
        s2 = Scale(displayFrame, from_=50, to=175, orient=HORIZONTAL, length=250, resolution=5, background='white',troughcolor='#737CA1',activebackground='white',variable=URL_value)
        s2.place(x=200, y=120)
        s2.set(120)
        Label(displayFrame, text='Upper Rate Limit (ppm):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=0, y=120)

    def AA_slider():
        # var0=IntVar()
        # c0 = Checkbutton(displayFrame, text="Set Amplitude OFF", bg='white',variable=var0)
        # c0.place(x=465,y=200)
        # s3 = Scale(displayFrame, from_=0.5, to=3.2, orient=HORIZONTAL, length=250, resolution=0.1, background='white',troughcolor='#737CA1',activebackground='white')
        # s3.place(x=200, y=190)
        AA_modes = [
            "0", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6",
            "1.7", "1.8", "1.9", "2.0","2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
            "3.0", "3.1", "3.2", "3.5", "4.0", "4.5", "5.0", "5.5", "6.0", "6.5", "7.0", "7.5",
        ]
        global clickedAA
        clickedAA = StringVar()
        clickedAA.set(AA_modes[-9])
        dropdownAA = OptionMenu(displayFrame, clickedAA, *AA_modes)
        dropdownAA.config(bg='white', width=10, fg='black', activebackground='white', activeforeground='#737CA1')
        dropdownAA["menu"].config(bg="white", fg="black", activebackground="white", activeforeground="#737CA1")
        dropdownAA.place(x=200,y=190)
        Label(displayFrame, text='Amplitude (Volts):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=0, y=190)

    def APW_slider():
        global PW_value
        PW_value=IntVar()
        s4 = Scale(displayFrame, from_=0.1, to=1.9, orient=HORIZONTAL, length=250, resolution=0.1, background='white',troughcolor='#737CA1',activebackground='white',variable=PW_value)
        s4.place(x=200, y=260)
        Label(displayFrame, text='Pulse Width (ms):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=0, y=260)
    def ARP_slider():
        global ARP_value
        ARP_value=IntVar()
        s5 = Scale(displayFrame, from_=150, to=500, orient=HORIZONTAL, length=250, resolution=10, background='white',troughcolor='#737CA1',activebackground='white',variable=ARP_value)
        s5.place(x=620, y=200)
        s5.set(250)
        Label(displayFrame, text='Atrial Refactory \n Period (ms):', padx=6,bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=460, y=200)
    def VRP_slider():
        global VRP_value
        VRP_value=IntVar()
        s6 = Scale(displayFrame, from_=150, to=500, orient=HORIZONTAL, length=250, resolution=10, background='white',troughcolor='#737CA1',activebackground='white',variable=VRP_value)
        s6.place(x=620, y=200)
        s6.set(320)
        Label(displayFrame, text='Ventricular Refactory \nPeriod (ms):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=460, y=200)
    def hyst():
        global hyst_value
        hyst_value=IntVar()
        c1=Checkbutton(displayFrame,text="Hysteresis Rate Limit (Same as LRL)",bg='white',variable=hyst_value)
        c1.place(x=0,y=330)
    def rateSm():
        global smoothingRate
        smoothingRate=IntVar()
        s6 = Scale(displayFrame, from_=0, to=25, orient=HORIZONTAL, length=250, resolution=3.07, background='white',troughcolor='#737CA1',activebackground='white',variable=smoothingRate)
        s6.place(x=620, y=260)
        Label(displayFrame, text='Rate Smoothing (%):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=460, y=260)
    def V_sens():
        # s7 = Scale(displayFrame, from_=1, to=10, orient=HORIZONTAL, length=250, resolution=0.5, background='white',troughcolor='#737CA1', activebackground='white')
        # s7.place(x=620, y=50)
        # s7.set(2.5)
        V_sens_modes = [
            "0.25", "0.5", "0.75", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5", "5.0", "5.5",
            "6.0", "6.5", "7.0", "7.5", "8.0", "8.5", "9.0", "9.5", "10.0",
        ]
        global V_clicked_sens
        V_clicked_sens = StringVar()
        V_clicked_sens.set(V_sens_modes[6])
        V_dropdown_sens = OptionMenu(displayFrame, V_clicked_sens, *V_sens_modes)
        V_dropdown_sens.config(bg='white', width=10, fg='black', activebackground='white', activeforeground='#737CA1')
        V_dropdown_sens["menu"].config(bg="white", fg="black", activebackground="white", activeforeground="#737CA1")
        V_dropdown_sens.place(x=620, y=50)
        Label(displayFrame, text='Sensitivity (mV):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=480, y=50)
    def A_sens():
        # s8 = Scale(displayFrame, from_=0.25, to=0.75,digits=2, orient=HORIZONTAL, length=250, resolution=0.25, background='white',troughcolor='#737CA1', activebackground='white')
        # s8.place(x=620, y=50)
        # s8.set(0.75)
        A_sens_modes = [
            "0.25", "0.5", "0.75", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5", "5.0", "5.5",
            "6.0", "6.5", "7.0", "7.5", "8.0", "8.5", "9.0", "9.5", "10.0",
        ]
        global A_clicked_sens
        A_clicked_sens = StringVar()
        A_clicked_sens.set(A_sens_modes[2])
        A_dropdown_sens = OptionMenu(displayFrame, A_clicked_sens, *A_sens_modes)
        A_dropdown_sens.config(bg='white', width=10, fg='black', activebackground='white', activeforeground='#737CA1')
        A_dropdown_sens["menu"].config(bg="white", fg="black", activebackground="white", activeforeground="#737CA1")
        A_dropdown_sens.place(x=620, y=50)
        Label(displayFrame, text='Sensitivity (mV):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=480, y=50)
    def PVARP():
        global PVARP1
        PVARP1=IntVar()
        s9 = Scale(displayFrame, from_=150, to=500, orient=HORIZONTAL, length=250, resolution=10, background='white',troughcolor='#737CA1', activebackground='white', variable=PVARP1)
        s9.place(x=620, y=130)
        s9.set(250)
        Label(displayFrame, text='PVARP (ms):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(x=480, y=130)
        Label(displayFrame, text='(Post Ventricular Atrial Refractory Period)', bg='white', fg='#737CA1', font=('Helvetica bold', 9)).place(x=635, y=175)

    def outputVal():
        print('------------------------------')
        print(modeSet)
        if modeSet=='AOO' or modeSet=='VOO':
            print('Lower Rate Limit',clickedLRL.get()+'ppm')
            print('Upper Rate Limit',str(URL_value.get())+'ppm')
            print('Amplitude: ',clickedAA.get(),'V')
            print('Pulse Width: ',PW_value.get(),'V')
        elif modeSet=='AAI':
            print('Lower Rate Limit',clickedLRL.get()+'ppm')
            print('Upper Rate Limit',str(URL_value.get())+'ppm')
            print('Amplitude: ',clickedAA.get(),'V')
            print('Pulse Width: ',PW_value.get(),'V')
            print('Refractory Period: ',str(ARP_value.get())+'ms')
            print('A Sensitivity: ',A_clicked_sens.get(),'mV')
            print('PVARP: '+str(PVARP1.get())+'ms')
            if int(hyst_value.get())==1:
                print('Hysterisis Rate Limit, same as LRL=',clickedLRL.get(),'ppm')
            else:
                print('Hysteresis is OFF')
            print('Smoothing Rate: ',str(smoothingRate.get())+'%')
        elif modeSet=='VVI':
            print('Lower Rate Limit',clickedLRL.get()+'ppm')
            print('Upper Rate Limit',str(URL_value.get())+'ppm')
            print('Amplitude: ',clickedAA.get(),'V')
            print('Pulse Width: ',PW_value.get(),'V')
            print('Refractory Period: ',str(VRP_value.get())+'ms')
            print('V Sensitivity: ',V_clicked_sens.get(),'mV')
            print('Hysteresis',hyst_value.get())
            print('Smoothing Rate: ',str(smoothingRate.get())+'%')
    def setButton():
        Button(displayFrame, width=30, pady=8, text="Set Values", bg='#737CA1', fg='white', border=0, command=outputVal).place(x=375, y=375)

    app.mainloop()
