from tkinter.filedialog import asksaveasfile
from functions import *
# from tkinter import *
# from tkinter import ttk
from ttkthemes import ThemedTk
import sys


window = ThemedTk(theme = "arc")
window.title("Star-Light")
positionRight = int(window.winfo_screenwidth()/4)
positionDown = int(window.winfo_screenheight()/10)
window.geometry("+{}+{}".format(positionRight, positionDown))
# window.iconphoto(False, PhotoImage(file='data/icons/ursa-major.ico'))
# window.tk.call("source", "forest/forest-light.tcl")
# ttk.Style().theme_use('forest-light')
# window.tk.call("set_theme", "dark")


# window
# ---------------------------------------------------------------------------------------------------------------------


def pro_save_as():
    try:
        file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                        ('Text Document', '*.txt'),
                                        ('Excel File', '*.xls'),
                                        ('CSV File', '*.csv')], initialfile="result.txt",
                             title="Save the Informations", defaultextension='.txt')
        text_save = str(f'{result2.get(0.0, END)} \n {result5.get(0.0, END)} \n {result11.get(0.0, END)}'
                        f'{deb_visi_resu.get(0.0, END)} \n {visi_resu.get(0.0, END)}')
        file.write(text_save)
        file.close()
    except AttributeError:
        x = 1


def about():
    about_win = Toplevel(height=550, width=900)
    about_win.minsize(height=550, width=900)
    about_win.resizable(False, False)

    columns1 = ('#1', '#2', '#3')
    tree1 = ttk.Treeview(about_win, columns=columns1, show='headings')
    tree1.heading('#1', text='Students')
    tree1.heading('#2', text='Sections')
    tree1.heading('#3', text='Email')
    contacts1 = [('Islam Reda Ahmed', 'Tab[Theoretical(1,2,3,6), Pro(1,2,3,4,5,6)]',
                 'islamtrabeih.me@gmail.com'), ('Mohamed Abd_Elaleem Mohamed',
                 'Orbit Lifetime[Theoretical, Pro]', 'mohamed3lam22@gmail.com'), ('Mahmoud Adel mohamed',
                 'Theoretical: CME', 'mahmoud.adel2810@gmail.com'),
                 ('Mustafa Saied ElSayed', 'Theoretical: Debris, IPM', 'mustafasaied454@gmail.com'),
                 ('Islam Mohamed Ibrahim', 'Theoretical: Geomagnitic storm,  AO and Ozone',
                 'wwwislamemaracom1@gmail.com'), ('Ahmed Mamdouh Ghanem', 'Theoretical: Flair, Solar f10.7',
                 'ahmedmamdouh2248@gmail.com'), ('Mahmoud Mohamed Ali', 'Theoretical: Solar Wind',
                 'mahmoud01022006138@gmail.com'), ('Ahmed ElHanoney Mohamed', 'Boundary layer Analysis',
                 'ahmedhanoney7@gmail.com'), ('Read Essa Mahmoud ', 'Boundary layer Analysis',
                 'redaesaa1797@gmail.com'), ('Taha Fekry Ahmed', 'Boundary layer Analysis', 'fekrytaha46@gmail.com')]
    for contact in contacts1:
        tree1.insert('', END, values=contact)
    tree1.pack(side=BOTTOM, fill='x')

    columns = ('#1', '#2', '#3')
    tree = ttk.Treeview(about_win, columns=columns, show='headings')
    tree.heading('#1', text='Supervisor')
    tree.heading('#2', text='Orgnization')
    tree.heading('#3', text='Email')
    contacts = [('Kamel Abdelatif Khalil Gadallah', 'Al-Azhar, Faculity of science', 'k.gadallah@azhar.edu.eg'),
                ('Wael Mohamed Mahmoud', 'EgSA', 'wael.mohamed@egsa.gov.eg'),
                ('Abdelrazek kasem shaltout', 'Al-Azhar, Faculity of science', 'shaltout123@gmail.com'),
                ('Ahmed Mohamed Abdelbar', 'Al-Azhar, Faculity of science', 'ahmed_bar86@azhar.edu.eg'),
                ('Ahmed Hafez Mohammed', 'Al-Azhar, Faculity of science', 'ahmed_hafez@azhar.edu.eg'),
                ('Abdelrahman Mouner Ahmed', 'Al-Azhar, Faculity of science', 'abdelra123@gmail.com'),
                ('Ramy Mawad', 'Al-Azhar, Faculity of science', 'ramy@azhar.edu.eg'),
                ('Ali Gamal awis', 'Al-Azhar, Faculity of science', 'ali.astro@azhar.edu.eg'),
                ('Inal Adham Hassan', 'Al-Azhar, Faculity of science', 'inalds_hassan@yahoo.com'),
                ('Mostafa Mohamed Abdel Aziz', 'Al-Azhar, Faculity of science', 'mostafa_morsy@azhar.edu.eg')]
    for contact in contacts:
        tree.insert('', END, values=contact)
    tree.pack(side=BOTTOM, fill='both')

    data1 = StringVar()
    data1.set("Low Earth Orbit Program \nBy: Al_Azhar University students 2021")
    label_Dir = Message(about_win, textvariable=data1, width=1000)
    lst2 = ('Times New Roman', 13)
    label_Dir.config(font=lst2)
    label_Dir.pack(side=BOTTOM, fill='both')


def new():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def help_index():
    os.system('information.pdf')


menu_bar = Menu(window, background='black', foreground='white', activebackground='orange',
                activeforeground='black', relief='flat')
file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Restart", compound='left', command=new, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
file_menu.add_command(label="Save", compound='left', command=pro_save_as, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
file_menu.add_command(label="Save as...", compound='left', command=pro_save_as, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
file_menu.add_command(label="Close", compound='left', command=sys.exit, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
file_menu.bind("<Control-Q>", sys.exit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help Index", compound='left', command=help_index, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
help_menu.add_command(label="About...", compound='left', command=about, background='black',
                      foreground='white', activebackground='orange', activeforeground='black')
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

# styles
#bc = "gray"
#fc = "black"
#s = ttk.Style()
#s.configure('TFrame', background=bc, foreground=fc)
#s.configure('TCombobox', background=bc,
                         #fieldbackground=bc,
                         #foreground=fc,
                         #darkcolor=bc,
                         #selectbackground="grey",
                         #lightcolor="lime")
#s.configure('TCheckbutton', background=bc, foreground=fc)
#s.configure('TButton', background=bc, foreground=fc)
#s.configure('TLabel', background=bc, foreground=fc)
#s.configure('TEntry', background=bc, foreground=fc)
#s.configure('TNotebook', background=bc, foreground=fc)
#s.configure('TLabelFrame', background=bc, foreground=fc)
#s.configure('Vertical.TScrollbar', background=bc, foreground=fc)

# tabs
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control) #relief="solid"
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Atmosphere')
tab_control.add(tab2, text='Irradiance')
tab_control.add(tab3, text='Orbital Lifetime')
tab_control.add(tab4, text='Solar Activity')
tab_control.add(tab5, text='LEO Debris')
tab_control.add(tab6, text='Visualization')
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_rowconfigure(0, weight=1)


# atmosphere
# ---------------------------------------------------------------------------------------------------------------------


def atmo_save():
    try:
        file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                        ('Text Document', '*.txt')], initialfile="result.txt",
                             title="Save the Informations", defaultextension='.txt')
        text_save = str(result2.get(0.0, END))
        file.write(text_save)
        file.close()
    except AttributeError:
        x = 1


def show_result():
    try:
        result1.delete('0.0', END)
        zz1 = height_list.get()
        yy1 = year.get()
        mm1 = month.get()

        dd1 = density1.get()
        if dd1:
            data1 = data_sheets(zz1, dd1, yy1, mm1, 'density')[0]
            result1.insert('end', f'Density = {data1} g/cm^3')
        tt1 = temperature1.get()
        if tt1:
            data1 = data_sheets(zz1, tt1, yy1, mm1, 'temperature')[0]
            result1.insert('end', f'\nTemperature = {data1} K')
        O1 = O_atoms1.get()
        if O1:
            data1 = data_sheets(zz1, O1, yy1, mm1, 'O_atoms')[0]
            result1.insert('end', f'\nAtomic Oxygen = {data1} (O)Atom/cm^3')
        N2 = N2_molecules1.get()
        if N2:
            data1 = data_sheets(zz1, N2, yy1, mm1, 'N2_molecules')[0]
            result1.insert('end', f'\nNitrogen = {data1} (N)Molecule/cm^3')
        Ar1 = Ar_atoms1.get()
        if Ar1:
            data1 = data_sheets(zz1, Ar1, yy1, mm1, 'Ar_atoms')[0]
            result1.insert('end', f'\nArgon = {data1} (Ar)Atom/cm^3')
        N1 = N_atoms1.get()
        if N1:
            data1 = data_sheets(zz1, N1, yy1, mm1, 'N_atoms')[0]
            result1.insert('end', f'\nAtomic Nitrogen = {data1} (N)Atom/cm^3')
        He1 = He_atoms1.get()
        if He1:
            data1 = data_sheets(zz1, He1, yy1, mm1, 'He_atoms')[0]
            result1.insert('end', f'\nHelium = {data1} (He)Atom/cm^3')
        O2 = O2_molecules1.get()
        if O2:
            data1 = data_sheets(zz1, O2, yy1, mm1, 'O2_molecules')[0]
            result1.insert('end', f'\nOxygen = {data1} (O)Molecule/cm^3')
        H1 = H_atoms1.get()
        if H1:
            data1 = data_sheets(zz1, H1, yy1, mm1, 'H_atoms')[0]
            result1.insert('end', f'\nHydrogen = {data1} (H)Atom/cm^3')
    except TclError:
        result1.delete('0.0', END)
        result1.insert('0.0', "Invalid Height")
    except KeyError:
        result1.delete('0.0', END)
        result1.insert('0.0', "Invalid Height")
    except ValueError:
        result1.delete('0.0', END)
        result1.insert('0.0', "Invalid Date")
    except UnboundLocalError:
        result1.delete('0.0', END)
        result1.insert('0.0', "Invalid Height or select the Argument")


def data_plot1():
    try:
        result2.delete('0.0', END)
        zz1 = height_list.get()
        yy1 = year.get()
        mm1 = month.get()
        dd1 = density1.get()
        if dd1:
            data1 = data_plot(zz1, 1, yy1, mm1, 'density')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'density'))
        tt1 = temperature1.get()
        if tt1:
            data1 = data_plot(zz1, 1, yy1, mm1, 'temperature')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'temperature'))
        O1 = O_atoms1.get()
        if O1:
            data1 = data_plot(zz1, 1, yy1, mm1, 'O_atoms')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'O_atoms'))
        N1 = N_atoms1.get()
        if N1:
            data1 = data_plot(zz1, 1, yy1, mm1, 'N_atoms')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'N_atoms'))
        N2 = N2_molecules1.get()
        if N2:
            data1 = data_plot(zz1, 1, yy1, mm1, 'N2_molecules')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'N2_molecules'))
        O2 = O2_molecules1.get()
        if O2:
            data1 = data_plot(zz1, 1, yy1, mm1, 'O2_molecules')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'O2_molecules'))
        Ar1 = Ar_atoms1.get()
        if Ar1:
            data1 = data_plot(zz1, 1, yy1, mm1, 'Ar_atoms')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'Ar_atoms'))
        He1 = He_atoms1.get()
        if He1:
            data1 = data_plot(zz1, 1, yy1, mm1, 'He_atoms')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'He_atoms'))
        H1 = H_atoms1.get()
        if H1:
            data1 = data_plot(zz1, 1, yy1, mm1, 'H_atoms')
            result2.insert(END, cell_atmo_info(zz1, 1, yy1, mm1, 'H_atoms'))
    except TclError:
        result2.delete('0.0', END)
        result2.insert('0.0', "Invalid Height")
    except KeyError:
        result2.delete('0.0', END)
        result2.insert('0.0', "Invalid Height")
    except ValueError:
        result2.delete('0.0', END)
        result2.insert('0.0', "Invalid Date")
    except UnboundLocalError:
        result2.delete('0.0', END)
        result2.insert('0.0', "Invalid Height or select the Argument")


atmo_lbl = ttk.Label(tab1, text='-- Regression for Atmosphere Properties --', foreground="black", anchor=CENTER,
                 font=("Times New Roman", 15))
atmo_lbl.grid(column=0, row=0, columnspan=5, sticky="NSEW")

# date label
date = StringVar()
date.set("Date :                 ")
labelDir = ttk.Label(tab1, textvariable=date)
labelDir.grid(column=0, row=1)

# months options button
# months = ["month",1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12]
month_list = IntVar(None)
month_list.set("Month")
month = ttk.Combobox(tab1, width=15, textvariable=month_list)
month['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# month = ttk.OptionMenu(tab1, month_list, *months)
month.grid(column=1, row=1)

# years options button
# years = ["years",1996 , 1997 , 1998 , 1999 , 2000 , 2001 , 2002 , 2003 , 2004 , 2005 , 2006 , 2007 ,
#          2008 , 2009 , 2010 , 2011 , 2012 , 2013 , 2014 , 2015 , 2016 , 2017 , 2018 , 2019 , 2020,
#          2021 , 2022 , 2023 , 2024 , 2025 , 2026 , 2027 , 2028 , 2029 , 2030]
year_list = IntVar(None)
year_list.set("Year")
# year = ttk.OptionMenu(tab1, year_list, *years)
year = ttk.Combobox(tab1, width=15, textvariable=year_list)
year['values'] = (1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                  2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
                  2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030)
year.grid(column=2, row=1)

# height label
height = StringVar(None)
height.set("Height :             ")
height_lbl = ttk.Label(tab1, textvariable=height)
height_lbl.grid(column=0, row=2)

# height options
height_list = IntVar(None)
height_list.set("Height in Km")
height1 = ttk.Combobox(tab1, width=15, textvariable=height_list)
height1['values'] = (100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650,
                     700, 750, 800, 850, 900, 950, 1000)
height1.grid(column=1, row=2)

# label
atmo_prop = ttk.Label(tab1, text='-- Choose the Property --', foreground="black", anchor=CENTER,
                  font=("Times New Roman", 11))
atmo_prop.grid(column=0, row=3, columnspan=5, sticky="NSEW")

# Check buttons
density1 = IntVar()
ttk.Checkbutton(tab1, text="Density", variable=density1).grid(column=1, row=4, sticky=NW)
Ar_atoms1 = IntVar()
ttk.Checkbutton(tab1, text="Argon", variable=Ar_atoms1).grid(column=1, row=5, sticky=NW)
He_atoms1 = IntVar()
ttk.Checkbutton(tab1, text="Helium", variable=He_atoms1).grid(column=1, row=6, sticky=NW)
temperature1 = IntVar()
ttk.Checkbutton(tab1, text="Temperature", variable=temperature1).grid(column=2, row=4, sticky=NW)
N2_molecules1 = IntVar()
ttk.Checkbutton(tab1, text="N Molecules", variable=N2_molecules1).grid(column=2, row=5, sticky=NW)
O2_molecules1 = IntVar()
ttk.Checkbutton(tab1, text="O Molecules", variable=O2_molecules1).grid(column=2, row=6, sticky=NW)
O_atoms1 = IntVar()
ttk.Checkbutton(tab1, text="O Atoms", variable=O_atoms1).grid(column=3, row=4, sticky=NW)
N_atoms1 = IntVar()
ttk.Checkbutton(tab1, text="N Atoms", variable=N_atoms1).grid(column=3, row=5, sticky=NW)
H_atoms1 = IntVar()
ttk.Checkbutton(tab1, text="Hydrogen", variable=H_atoms1).grid(column=3, row=6, sticky=NW)

# output
result0 = ttk.Button(tab1, text='Result', width=10, command=show_result)
result0.grid(row=7, column=0, sticky=N, padx=0, pady=0)
# result1 = Entry(tab1, justify=LEFT, relief="flat")
# flat, groove, raised, ridge, solid, or sunken
#result1 = scrolledtext.ScrolledText(tab1, width=82, height=4, font=("Times New Roman", 10), relief="solid")
atmo_frame = ttk.Frame(tab1, style='new.TFrame')
atmo_frame.grid(row=7, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=1, columnspan=3)
result1 = Text(atmo_frame, wrap="none", width=82, height=4, font=("Times New Roman", 10), relief="solid")
vsb = ttk.Scrollbar(atmo_frame, command=result1.yview, orient="vertical")
result1.configure(yscrollcommand=vsb.set)
atmo_frame.grid_rowconfigure(0, weight=1)
atmo_frame.grid_columnconfigure(0, weight=1)
vsb.grid(row=0, column=1, sticky="ns")
result1.grid(row=0, column=0, sticky="nsew")

Plot1 = ttk.Button(tab1, text='Plot', width=10, command=data_plot1)
Plot1.grid(row=10, column=0, sticky=N, padx=0, pady=0)
save1 = ttk.Button(tab1, text='save', width=10, command=atmo_save)
save1.grid(row=11, column=0, sticky=N, padx=0, pady=0)

atmo_frame_2 = ttk.Frame(tab1)
atmo_frame_2.grid(row=10, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
result2 = Text(atmo_frame_2, wrap="none", width=82, height=19, font=("Times New Roman", 10), relief="solid")
vsb_atm2 = ttk.Scrollbar(atmo_frame_2, command=result2.yview, orient="vertical")
result2.configure(yscrollcommand=vsb_atm2.set)
atmo_frame_2.grid_rowconfigure(0, weight=1)
atmo_frame_2.grid_columnconfigure(0, weight=1)
vsb_atm2.grid(row=0, column=1, sticky="ns")
result2.grid(row=0, column=0, sticky="nsew")

#result2 = scrolledtext.ScrolledText(tab1, width=82, height=19, font=("Times New Roman", 10), relief="solid")
#result2.grid(row=10, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)

tab1.rowconfigure(0, weight=1)
for col in range(5):
    tab1.columnconfigure(col, weight=1)
tab1.rowconfigure(10, weight=1)


# ---------------------------------------------------------------------------------------------------------------------
# irradiance
# ---------------------------------------------------------------------------------------------------------------------


def irr_result():
    try:
        result4.delete(0, 1000)
        ph1 = lat_enter.get()
        yy1 = year.get()
        mm1 = month.get()
        data1 = irradiance(yy1, mm1, ph1)
        result4.insert('end', f'maximum = {data1[0]} W/m^2' + '    ' + f'minimum = {data1[1]} W/m^2')
    except ValueError:
        result4.delete(0, 1000)
        result4.insert('end', "Invalid date or Inclination")


def irr_plot2():
    try:
        result5.delete('0.0', END)
        yy = year.get()
        mm = month.get()
        phi = int(lat_enter.get())
        y = irr_plot(yy, mm)
        x = irr_plot1(yy, mm, phi)
        result5.insert('end', f'{cell_irr_info(yy, mm, phi)}')
    except ValueError:
        result5.delete('0.0', END)
        result5.insert('end', "Invalid date or Inclination")


def irr_save():
    try:
        file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                        ('Text Document', '*.txt')], initialfile="result.txt",
                             title="Save the Informations", defaultextension='.txt')
        text_save = str(result5.get(0.0, END))
        file.write(text_save)
        file.close()
    except AttributeError:
        x = 1


irr_lbl = ttk.Label(tab2, text='-- Regression for Solar Irradiance --', foreground="black", anchor=CENTER,
                font=("Times New Roman", 15))
irr_lbl.grid(column=0, row=0, columnspan=5)

# date label
#irr_date = ttk.Label(tab2, textvariable=date)
#irr_date.grid(column=0, row=1)

# months options button
month = ttk.Combobox(tab2, width=15, textvariable=month_list)
month['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
month.grid(column=1, row=1)

# years options button
year = ttk.Combobox(tab2, width=15, textvariable=year_list)
year['values'] = (1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                  2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
                  2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030)
year.grid(column=2, row=1)

# label
lat = ttk.Label(tab2, text='Inclination :     ')
lat.grid(column=0, row=2)

# Inclination Entry
lat_enter = ttk.Entry(tab2, justify='center', width=17)
lat_enter.insert(0, 'Irradiance')
lat_enter.grid(column=1, row=2)
# relief = (flat, groove, raised, ridge, solid, or sunken) shape in tk

irr_lbl = ttk.Label(tab2, text='-- Irradiance --', foreground="black", anchor=CENTER,
                font=("Times New Roman", 11))
irr_lbl.grid(column=0, row=3, columnspan=5, rowspan=2)

result3 = ttk.Button(tab2, text='Result', width=10, command=irr_result)
result3.grid(row=5, column=0, sticky=N, padx=0, pady=0)
result4 = ttk.Entry(tab2, justify=LEFT)
result4.grid(row=5, column=1, ipadx=0, ipady=0, columnspan=3, sticky="NSEW")
Plot2 = ttk.Button(tab2, text='Plot', width=10, command=irr_plot2)
Plot2.grid(row=6, column=0, sticky=N, padx=0, pady=0)
save2 = ttk.Button(tab2, text='save', width=10, command=irr_save)
save2.grid(row=7, column=0, sticky=N, padx=0, pady=0)

irr_frame = ttk.Frame(tab2)
irr_frame.grid(row=6, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=2, columnspan=3)
result5 = Text(irr_frame, wrap="none", width=82, height=19, font=("Times New Roman", 10), relief="solid")
vsb_irr = ttk.Scrollbar(irr_frame, command=result5.yview, orient="vertical")
result5.configure(yscrollcommand=vsb_irr.set)
irr_frame.grid_rowconfigure(0, weight=1)
irr_frame.grid_columnconfigure(0, weight=1)
vsb_irr.grid(row=0, column=1, sticky="ns")
result5.grid(row=0, column=0, sticky="nsew")

#result5 = scrolledtext.ScrolledText(tab2, width=82, height=19, font=("Times New Roman", 10), relief="solid")
#result5.grid(row=6, column=1, ipadx=9, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)

tab2.rowconfigure(0, weight=1)
for col in range(5):
    tab2.columnconfigure(col, weight=1)
tab2.rowconfigure(6, weight=1)


# ---------------------------------------------------------------------------------------------------------------------
# orbital drag
# ---------------------------------------------------------------------------------------------------------------------


def lifetime():
    try:
        orbitdrag.delete('0.0', END)
        yy = year3.get()
        mm = month3.get()
        s_a = float(life_sem_enter.get())
        ecc = float(life_ecc_enter.get())
        # inc = float(life_inc_enter.get())
        mass = float(life_mass_enter.get())
        true = float(life_true_enter.get())
        area0 = float(life_area_enter.get())
        # argp = float(life_arp_enter.get())

        s_a_check = semi_major_axis.get()
        oblateness = earth_oblate.get()
        drag = atmo_drag.get()
        if s_a_check:
            if drag:
                x = a_drag(s_a, ecc, true, area0, mass, yy, mm)
                orbitdrag.insert(END, f' \nvariation of a = {x[0]} km \n'
                                      f'it would take {x[1]} second to be 100 km orbit')
        ecc_check = eccentricity_life.get()
        if ecc_check:
            if drag:
                x = e_drag(s_a, ecc, true, area0, mass, yy, mm)
                orbitdrag.insert(END, f' \nvariation of e = {x[0]} \n'
                                      f'it would take {x[1]} second to be circular orbit')
    except ValueError:
        orbitdrag.insert(END, 'Insert valid numbers')


def drag_save():
    try:
        file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                        ('Text Document', '*.txt')], initialfile="result.txt",
                             title="Save the Informations", defaultextension='.txt')
        text_save = str(orbitdrag.get(0.0, END))
        file.write(text_save)
        file.close()
    except AttributeError:
        x = 1


life_lbl = ttk.Label(tab3, text='-- Drag and Lifetime --', foreground="black", anchor=CENTER,
                 font=("Times New Roman", 15))
life_lbl.grid(column=0, row=0, columnspan=5, sticky="NSEW")

# date
life_date = ttk.Label(tab3, textvariable=date)
life_date.grid(column=0, row=1, padx=10, sticky="NSEW")

# months options button
month_list3 = IntVar(None)
month_list3.set("Month")
month3 = ttk.Combobox(tab3, width=15, textvariable=month_list3)
month3['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
month3.grid(column=1, row=1)

# years options button
year3 = ttk.Combobox(tab3, width=15, textvariable=year_list)
year3['values'] = (1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                   2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
                   2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030)
year3.grid(column=3, row=1)

# labels
life_sem_lbl = ttk.Label(tab3, text='Semi-major axis :').grid(column=0, row=2, padx=10, sticky=W)
life_sem_enter = ttk.Entry(tab3, justify='center', width=17)
life_sem_enter.grid(column=1, row=2)
life_ecc_lbl = ttk.Label(tab3, text='Eccentricity :').grid(column=2, row=2, padx=10, sticky=W)
life_ecc_enter = ttk.Entry(tab3, justify='center', width=17)
life_ecc_enter.grid(column=3, row=2)
life_inc_lbl = ttk.Label(tab3, text='Inclination :').grid(column=0, row=3, padx=10, sticky=W)
life_inc_enter = ttk.Entry(tab3, justify='center', width=17, state='disabled')
life_inc_enter.grid(column=1, row=3)
life_mass_lbl = ttk.Label(tab3, text='Mass kg :').grid(column=2, row=3, padx=10, sticky=W)
life_mass_enter = ttk.Entry(tab3, justify='center', width=17)
life_mass_enter.grid(column=3, row=3)
life_arp_lbl = ttk.Label(tab3, text='Argument Perigee :').grid(column=0, row=4, padx=10, sticky=W)
life_arp_enter = ttk.Entry(tab3, justify='center', width=17, state='disabled')
life_arp_enter.grid(column=1, row=4)
life_area_lbl = ttk.Label(tab3, text='Area m^2 :').grid(column=2, row=4, padx=10, sticky=W)
life_area_enter = ttk.Entry(tab3, justify='center', width=17)
life_area_enter.grid(column=3, row=4)
life_true_lbl = ttk.Label(tab3, text='Treu Anomaly :').grid(column=0, row=5, padx=10, sticky=W)
life_true_enter = ttk.Entry(tab3, justify='center', width=17)
life_true_enter.grid(column=1, row=5)

# check
semi_major_axis = IntVar()
ttk.Checkbutton(tab3, text="Semi-major Axis km", variable=semi_major_axis).grid(column=1, row=7, sticky=NW)
eccentricity_life = IntVar()
ttk.Checkbutton(tab3, text="Eccentricity", variable=eccentricity_life).grid(column=1, row=8, sticky=NW)
atmo_drag = IntVar()
ttk.Checkbutton(tab3, text="Drag", variable=atmo_drag).grid(column=3, row=7, sticky=NW)
earth_oblate = IntVar()
ttk.Checkbutton(tab3, text="Under Oblateness", state=DISABLED, variable=earth_oblate).grid(column=3, row=8, sticky=NW)

drag_lbl = ttk.Label(tab3, text='note that the operation would take minutes or may be hours', foreground="gray", anchor=CENTER,)
drag_lbl.grid(column=0, row=6, columnspan=6, sticky="NSEW")

# output
life_result = ttk.Button(tab3, text='Result', width=10, command=lifetime)
life_result.grid(row=9, column=0, sticky=N, padx=0, pady=0)
life_save = ttk.Button(tab3, text='save', width=10, command=drag_save)
life_save.grid(row=10, column=0, sticky=N, padx=0, pady=0)

life_frame = ttk.Frame(tab3)
life_frame.grid(row=9, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
orbitdrag = Text(life_frame, wrap="none", width=82, height=19, font=("Times New Roman", 10), relief="solid")
vsb_life = ttk.Scrollbar(life_frame, command=orbitdrag.yview, orient="vertical")
orbitdrag.configure(yscrollcommand=vsb_life.set)
life_frame.grid_rowconfigure(0, weight=1)
life_frame.grid_columnconfigure(0, weight=1)
vsb_life.grid(row=0, column=1, sticky="ns")
orbitdrag.grid(row=0, column=0, sticky="nsew")

#orbitdrag = scrolledtext.ScrolledText(tab3, width=82, height=19, font=("Times New Roman", 10), relief="solid")
#orbitdrag.grid(row=9, column=1, ipadx=9, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)


tab3.rowconfigure(0, weight=1)
for col in range(5):
    tab3.columnconfigure(col, weight=1)
tab3.rowconfigure(9, weight=1)


# ---------------------------------------------------------------------------------------------------------------------
# cme activity
# ---------------------------------------------------------------------------------------------------------------------


def cme_result():
    try:
        result10.delete(0, END)
        yy1 = year4.get()
        mm1 = month4.get()
        dd1 = day.get()
        cpa = Central_PA.get()
        if cpa:
            data1 = cme_sheets(1, yy1, mm1, dd1, 'central PA')[0]
            result10.insert('end', f'        Central PA = {data1} degree')
        ls = Linear_Speed.get()
        if ls:
            data1 = cme_sheets(1, yy1, mm1, dd1, 'Linear speed')[0]
            result10.insert('end', f'        Linear speed = {data1} Km/s')
        mpa = MPA.get()
        if mpa:
            data1 = cme_sheets(1, yy1, mm1, dd1, 'Mass')[0]
            result10.insert('end', f'        Mass = {data1} gram')
        wdth = Width.get()
        if wdth:
            data1 = cme_sheets(1, yy1, mm1, dd1, 'width')[0]
            result10.insert('end', f'        Width = {data1} degree')
    except ValueError:
        result10.delete(0, END)
        result10.insert(0, "Invalid Date or Date is not available")


def cme_plot1():
    try:
        result11.delete('0.0', END)
        yy1 = year4.get()
        mm1 = month4.get()
        dd1 = day.get()
        cpa = Central_PA.get()
        if cpa:
            data1 = cme_plot(yy1, mm1, dd1, 1)
            result11.insert(END, cell_cme_info(1, yy1, mm1, dd1, 'central PA'))
        ls = Linear_Speed.get()
        if ls:
            data1 = cme_plot(yy1, mm1, dd1, 2)
            result11.insert(END, cell_cme_info(1, yy1, mm1, dd1, 'Linear speed'))
        mpa = MPA.get()
        if mpa:
            data1 = cme_plot(yy1, mm1, dd1, 4)
            result11.insert(END, cell_cme_info(1, yy1, mm1, dd1, 'Mass'))
        wdth = Width.get()
        if wdth:
            data1 = cme_plot(yy1, mm1, dd1, 6)
            result11.insert(END, cell_cme_info(1, yy1, mm1, dd1, 'width'))
    except ValueError:
        result10.delete(0, END)
        result10.insert(0, "Invalid Date or Date is not available")


def cme_save():
    try:
        file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                        ('Text Document', '*.txt')], initialfile="result.txt",
                             title="Save the Informations", defaultextension='.txt')
        text_save = str(result11.get(0.0, END))
        file.write(text_save)
        file.close()
    except AttributeError:
        x = 1


cme_lbl = ttk.Label(tab4, text='-- Regression for Solar Activity (CME) --', foreground="black", anchor=CENTER,
                font=("Times New Roman", 15))
cme_lbl.grid(column=0, row=0, columnspan=5, sticky="NSEW")

# date label
cme_date = ttk.Label(tab4, textvariable=date)
cme_date.grid(column=0, row=1)


day_list = IntVar()
day_list.set("days")
day = ttk.Combobox(tab4, width=15, textvariable=day_list)
day['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
day.grid(column=1, row=1)

# months options button
month_list4 = IntVar(None)
month_list4.set("Month")
month4 = ttk.Combobox(tab4, width=15, textvariable=month_list4)
month4['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
month4.grid(column=2, row=1)

# years options button
year4 = ttk.Combobox(tab4, width=15, textvariable=year_list)
year4['values'] = (1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                   2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
                   2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030)
year4.grid(column=3, row=1)


cme_prop = ttk.Label(tab4, text='-- CME property --', foreground="black", anchor=CENTER,
                 font=("Times New Roman", 11))
cme_prop.grid(column=0, row=2, columnspan=5)

# check box
Central_PA = IntVar()
ttk.Checkbutton(tab4, text="Central PA", variable=Central_PA).grid(column=2, row=3, sticky=N)
Linear_Speed = IntVar()
ttk.Checkbutton(tab4, text="Linear_Speed", variable=Linear_Speed).grid(column=1, row=3, sticky=NW)
MPA = IntVar()
ttk.Checkbutton(tab4, text="Mass          ", variable=MPA).grid(column=2, row=4, sticky=N)
Width = IntVar()
ttk.Checkbutton(tab4, text="Width         ", variable=Width).grid(column=3, row=3, sticky=NE)

# output
result9 = ttk.Button(tab4, text='Result', width=10, command=cme_result)
result9.grid(row=5, column=0, sticky=N, padx=0, pady=0)
result10 = ttk.Entry(tab4, justify=LEFT)
result10.grid(row=5, column=1, ipadx=0, ipady=0, columnspan=3, sticky="NSEW")
Plot4 = ttk.Button(tab4, text='Plot', width=10, command=cme_plot1)
Plot4.grid(row=6, column=0, sticky=N, padx=0, pady=0)
save4 = ttk.Button(tab4, text='save', width=10, command=cme_save)
save4.grid(row=7, column=0, sticky=N, padx=0, pady=0)

cme_frame = ttk.Frame(tab4)
cme_frame.grid(row=6, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
result11 = Text(cme_frame, wrap="none", width=82, height=19, font=("Times New Roman", 10), relief="solid")
vsb_cme = ttk.Scrollbar(cme_frame, command=result11.yview, orient="vertical")
result11.configure(yscrollcommand=vsb_cme.set)
cme_frame.grid_rowconfigure(0, weight=1)
cme_frame.grid_columnconfigure(0, weight=1)
vsb_cme.grid(row=0, column=1, sticky="ns")
result11.grid(row=0, column=0, sticky="nsew")

#result11 = scrolledtext.ScrolledText(tab4, width=82, height=19, font=("Times New Roman", 10), relief="solid")
#result11.grid(row=6, column=1, ipadx=9, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)

tab4.rowconfigure(0, weight=1)
for col in range(5):
    tab4.columnconfigure(col, weight=1)
tab4.rowconfigure(6, weight=1)


# ---------------------------------------------------------------------------------------------------------------------
# debris
# ---------------------------------------------------------------------------------------------------------------------


def deb_plotter():
    try:
        visi_resu.delete('0.0', END)
        sa = float(deb_sem_enter.get())
        ecc = float(deb_ecc_enter.get())
        inc = float(deb_inc_enter.get())
        raan = float(deb_raa_enter.get())
        argp = float(deb_arp_enter.get())
        nu = float(deb_tru_enter.get())
        yy = year5.get()
        mm = month5.get()
        dd = day5.get()
        hh = hours0.get()
        mn = minuts0.get()
        ss = seconds0.get()
        x = deb_plot(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss)
        deb_visi_resu.insert(END, deb_info(sa))
    except ValueError:
        deb_visi_resu.delete('0.0', END)
        deb_visi_resu.insert(END, "Invalid Input Number, please make sure that all inputs are valid or numbers")


def deb_save():
    try:
        file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                        ('Text Document', '*.txt')], initialfile="result.txt",
                             title="Save the Informations", defaultextension='.txt')
        text_save = str(deb_visi_resu.get(0.0, END))
        file.write(text_save)
        file.close()
    except AttributeError:
        x = 1


debris_lbl = ttk.Label(tab5, text='-- Debris Hazards --', foreground="black", anchor=CENTER,
                   font=("Times New Roman", 15))
debris_lbl.grid(column=0, row=0, columnspan=5, sticky="NSEW")
# a, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss
# date
deb_date = ttk.Label(tab5, textvariable=date)
deb_date.grid(column=0, row=1, padx=10, sticky=W)

# day
day_list0 = IntVar()
day_list0.set("days")
day5 = ttk.Combobox(tab5, width=15, textvariable=day_list0)
day5['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                  16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
day5.grid(column=1, row=1)

# months options button
month_list5 = IntVar(None)
month_list5.set("Month")
month5 = ttk.Combobox(tab5, width=15, textvariable=month_list5)
month5['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
month5.grid(column=2, row=1)

# years options button
year5 = ttk.Entry(tab5, justify='center', width=17)
year5.insert(0, 'years')
year5.grid(column=3, row=1)
# hours options button
hours_0 = IntVar(None)
hours_0.set("hours")
hours0 = ttk.Combobox(tab5, width=15, textvariable=hours_0)
hours0['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
hours0.grid(column=1, row=2)
# hours options button
minuts_0 = IntVar(None)
minuts_0.set("minutes")
minuts0 = ttk.Combobox(tab5, width=15, textvariable=minuts_0)
minuts0['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                     27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                     51, 52, 53, 54, 55, 56, 57, 58, 59)
minuts0.grid(column=2, row=2)
# hours options button
seconds_0 = IntVar(None)
seconds_0.set("seconds")
seconds0 = ttk.Combobox(tab5, width=15, textvariable=seconds_0)
seconds0['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                      51, 52, 53, 54, 55, 56, 57, 58, 59)
seconds0.grid(column=3, row=2)
# sa, ecc, inc, raan, argp, nu, yy, mm, dd, p, aa, m
# labels
deb_sem_lbl = ttk.Label(tab5, text='Semi-major axis :    ').grid(column=0, row=3, padx=10, sticky=W)
deb_sem_enter = ttk.Entry(tab5, justify='center', width=17)
deb_sem_enter.grid(column=1, row=3)
deb_ecc_lbl = ttk.Label(tab5, text='Eccentricity :       ').grid(column=2, row=3, padx=10, sticky=W)
deb_ecc_enter = ttk.Entry(tab5, justify='center', width=17)
deb_ecc_enter.grid(column=3, row=3)
deb_inc_lbl = ttk.Label(tab5, text='Inclination :        ').grid(column=0, row=4, padx=10, sticky=W)
deb_inc_enter = ttk.Entry(tab5, justify='center', width=17)
deb_inc_enter.grid(column=1, row=4)
deb_raa_lbl = ttk.Label(tab5, text='Right Ascension :    ').grid(column=2, row=4, padx=10, sticky=W)
deb_raa_enter = ttk.Entry(tab5, justify='center', width=17)
deb_raa_enter.grid(column=3, row=4)
deb_arp_lbl = ttk.Label(tab5, text='Argument Perigee :').grid(column=0, row=5, padx=10, sticky=W)
deb_arp_enter = ttk.Entry(tab5, justify='center', width=17)
deb_arp_enter.grid(column=1, row=5)
deb_tru_lbl = ttk.Label(tab5, text='True Anomaly :       ').grid(column=2, row=5, padx=10, sticky=W)
deb_tru_enter = ttk.Entry(tab5, justify='center', width=17)
deb_tru_enter.grid(column=3, row=5)
#
deb_lbl = ttk.Label(tab5, text='  ', foreground="black")
deb_lbl.grid(column=0, row=6, columnspan=5, sticky="NSEW")
# result
deb_visi_plot = ttk.Button(tab5, text='Plot', width=10, command=deb_plotter)
deb_visi_plot.grid(row=7, column=0, sticky=N, padx=0, pady=0)
deb_visi_save = ttk.Button(tab5, text='save', width=10, command=deb_save)
deb_visi_save.grid(row=8, column=0, sticky=N, padx=0, pady=0)

dep_frame = ttk.Frame(tab5)
dep_frame.grid(row=7, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
deb_visi_resu = Text(dep_frame, wrap="none", width=82, height=19, font=("Times New Roman", 10), relief="solid")
vsb_dep = ttk.Scrollbar(dep_frame, command=deb_visi_resu.yview, orient="vertical")
deb_visi_resu.configure(yscrollcommand=vsb_dep.set)
dep_frame.grid_rowconfigure(0, weight=1)
dep_frame.grid_columnconfigure(0, weight=1)
vsb_dep.grid(row=0, column=1, sticky="ns")
deb_visi_resu.grid(row=0, column=0, sticky="nsew")

#deb_visi_resu = scrolledtext.ScrolledText(tab5, width=82, height=19, font=("Times New Roman", 10), relief="solid")
#deb_visi_resu.grid(row=7, column=1, ipadx=9, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)


tab5.rowconfigure(0, weight=1)
for col in range(5):
    tab5.columnconfigure(col, weight=1)
tab5.rowconfigure(7, weight=1)


# ---------------------------------------------------------------------------------------------------------------------
# orbital visiualization
# ---------------------------------------------------------------------------------------------------------------------


def orb_plotter():
    try:
        visi_resu.delete('0.0', END)
        sa = float(sem_enter.get())
        ecc = float(ecc_enter.get())
        inc = float(inc_enter.get())
        raan = float(raa_enter.get())
        argp = float(arp_enter.get())
        nu = float(tru_enter.get())
        p = float(prd_enter.get())
        aa = float(are_enter.get())
        m = float(mas_enter.get())
        yy = year6.get()
        mm = month6.get()
        dd = day6.get()
        hh = hours1.get()
        mn = minuts1.get()
        ss = seconds1.get()
        x = orb_calc(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss, p, aa, m)
        visi_resu.insert(END, orb_info_ri(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss))
    except ValueError:
        visi_resu.delete('0.0', END)
        visi_resu.insert(END, "Invalid Input Number, please make sure that all inputs are valid or numbers")


def visi_save():
    try:
        file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                        ('Text Document', '*.txt')], initialfile="result.txt",
                             title="Save the Informations", defaultextension='.txt')
        text_save = str(visi_resu.get(0.0, END))
        file.write(text_save)
        file.close()
    except AttributeError:
        x = 1


visi_lbl = ttk.Label(tab6, text='-- Orbital Visiualization --', foreground="black", anchor=CENTER,
                 font=("Times New Roman", 15))
visi_lbl.grid(column=0, row=0, columnspan=5, sticky="NSEW")

# date
visi_date = ttk.Label(tab6, textvariable=date)
visi_date.grid(column=0, row=1, padx=10, sticky=W)

# day
day_list1 = IntVar()
day_list1.set("days")
day6 = ttk.Combobox(tab6, width=15, textvariable=day_list1)
day6['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                  16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
day6.grid(column=1, row=1)

# months options button
month_list6 = IntVar(None)
month_list6.set("Month")
month6 = ttk.Combobox(tab6, width=15, textvariable=month_list6)
month6['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
month6.grid(column=2, row=1)

# years options button
year6 = ttk.Entry(tab6, justify='center', width=17)
year6.insert(0, 'years')
year6.grid(column=3, row=1)
# hours options button
hours = IntVar(None)
hours.set("hours")
hours1 = ttk.Combobox(tab6, width=15, textvariable=hours)
hours1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
hours1.grid(column=1, row=2)
# hours options button
minuts = IntVar(None)
minuts.set("minutes")
minuts1 = ttk.Combobox(tab6, width=15, textvariable=minuts)
minuts1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                     27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                     51, 52, 53, 54, 55, 56, 57, 58, 59)
minuts1.grid(column=2, row=2)
# hours options button
seconds = IntVar(None)
seconds.set("seconds")
seconds1 = ttk.Combobox(tab6, width=15, textvariable=seconds)
seconds1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                      51, 52, 53, 54, 55, 56, 57, 58, 59)
seconds1.grid(column=3, row=2)
# sa, ecc, inc, raan, argp, nu, yy, mm, dd, p, aa, m
# labels
sem_lbl = ttk.Label(tab6, text='Semi-major axis :    ').grid(column=0, row=3, padx=10, sticky=W)
sem_enter = ttk.Entry(tab6, justify='center', width=17)
sem_enter.grid(column=1, row=3)
ecc_lbl = ttk.Label(tab6, text='Eccentricity :       ').grid(column=2, row=3, padx=10, sticky=W)
ecc_enter = ttk.Entry(tab6, justify='center', width=17)
ecc_enter.grid(column=3, row=3)
inc_lbl = ttk.Label(tab6, text='Inclination :        ').grid(column=0, row=4, padx=10, sticky=W)
inc_enter = ttk.Entry(tab6, justify='center', width=17)
inc_enter.grid(column=1, row=4)
raa_lbl = ttk.Label(tab6, text='Right Ascension :    ').grid(column=2, row=4, padx=10, sticky=W)
raa_enter = ttk.Entry(tab6, justify='center', width=17)
raa_enter.grid(column=3, row=4)
arp_lbl = ttk.Label(tab6, text='Argument Perigee :').grid(column=0, row=5, padx=10, sticky=W)
arp_enter = ttk.Entry(tab6, justify='center', width=17)
arp_enter.grid(column=1, row=5)
tru_lbl = ttk.Label(tab6, text='True Anomaly :       ').grid(column=2, row=5, padx=10, sticky=W)
tru_enter = ttk.Entry(tab6, justify='center', width=17)
tru_enter.grid(column=3, row=5)
prd_lbl = ttk.Label(tab6, text='Number of Tours :    ').grid(column=0, row=6, padx=10, sticky=W)
prd_enter = ttk.Entry(tab6, justify='center', width=17)
prd_enter.grid(column=1, row=6)
mas_lbl = ttk.Label(tab6, text='Mass :               ').grid(column=2, row=6, padx=10, sticky=W)
mas_enter = ttk.Entry(tab6, justify='center', width=17)
mas_enter.grid(column=3, row=6)
are_lbl = ttk.Label(tab6, text='Area :               ').grid(column=0, row=7, padx=10, sticky=W)
are_enter = ttk.Entry(tab6, justify='center', width=17)
are_enter.grid(column=1, row=7)
#
visi_lbl = ttk.Label(tab6, text='         ', foreground="black", font=("Times New Roman", 15))
visi_lbl.grid(column=0, row=8, columnspan=5, sticky="NSEW")
# result
visi_plot = ttk.Button(tab6, text='Plot', width=10, command=orb_plotter)
visi_plot.grid(row=9, column=0, sticky=N, padx=0, pady=0)
visi_save = ttk.Button(tab6, text='save', width=10, command=visi_save)
visi_save.grid(row=10, column=0, sticky=N, padx=0, pady=0)

visio_frame = ttk.Frame(tab6)
visio_frame.grid(row=9, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
visi_resu = Text(visio_frame, wrap="none", width=82, height=19, font=("Times New Roman", 10), relief="solid")
vsb_visio = ttk.Scrollbar(visio_frame, command=visi_resu.yview, orient="vertical")
visi_resu.configure(yscrollcommand=vsb_visio.set)
visio_frame.grid_rowconfigure(0, weight=1)
visio_frame.grid_columnconfigure(0, weight=1)
vsb_visio.grid(row=0, column=1, sticky="ns")
visi_resu.grid(row=0, column=0, sticky="nsew")

#visi_resu = scrolledtext.ScrolledText(tab6, width=82, height=19, font=("Times New Roman", 10), relief="solid")
#visi_resu.grid(row=9, column=1, ipadx=9, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)


tab6.rowconfigure(0, weight=1)
for col in range(5):
    tab6.columnconfigure(col, weight=1)
tab6.rowconfigure(9, weight=1)


# ---------------------------------------------------------------------------------------------------------------------
# window pack
# ---------------------------------------------------------------------------------------------------------------------

while True:
    window.wm_minsize(625, 567)
    window.resizable(True, True)
    tab_control.pack(expand=True, fill='both')
    # window.state('zoomed')
    # window.wm_attributes("-transparentcolor", 'white')

    window.mainloop()
