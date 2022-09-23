from tkinter.filedialog import asksaveasfile
#from functions import *
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import sys, os



class App(ThemedTk):
    def __init__(self):
        super().__init__()
        self.wm_minsize(1100, 600)
        self.resizable(False, False)
        self.title("Star-Light")
        #self.set_theme("arc")
        positionRight = int(self.winfo_screenwidth()/10)
        positionDown = int(self.winfo_screenheight()/10)
        self.geometry("+{}+{}".format(positionRight, positionDown))
        self.iconphoto(False, PhotoImage(file='star.png'))
        #self.iconbitmap(r'/home/islam/Documents/Star_Light-tk/star.ico')
        #self.tk.call('wm', 'iconphoto', self._w, PhotoImage(file='star.png'))
        self.tk.call("source", "sun-valley/sv.tcl")
        self.tk.call("set_theme", "dark")
        self.ui()
        Atmosphere.atmosphere_tab(self, ThemedTk)
        Irradiance.irradiance_tab(self, ThemedTk)
        Drag.drag_tab(self, ThemedTk)
        CMEActivity.cmeactivity_tab(self, ThemedTk)
        Debris.debris_tab(self, ThemedTk)
        Orbit.orbit_tab(self, ThemedTk)
        self.resizable(True, True)
        self.style = ttk.Style(self)
        bc = "#FC6C85"
        fc = "#7FFFD4"
        self.style.configure('.', foreground=fc)
        self.style.configure('TCombobox', background=bc, fieldbackground=bc, foreground=fc, darkcolor=bc, selectbackground="grey", lightcolor="lime")
        self.style.configure('TButton', background=bc, foreground=fc)
        self.style.configure('TEntry', background=bc, foreground=fc)
        self.style.configure('TText', background=bc, foreground=fc)

    def ui(self):
        menu_bar = Menu(self, background='black', foreground='white', activebackground='orange',
                        activeforeground='black', relief='flat')
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Restart", compound='left', command=self.new, background='black',foreground='white', activebackground='orange',
                              activeforeground='black')
        file_menu.add_command(label="Save", compound='left', command=self.pro_save_as, background='black',foreground='white',
                              activebackground='orange', activeforeground='black')
        file_menu.add_command(label="Save as...", compound='left', command=self.pro_save_as, background='black',foreground='white',
                              activebackground='orange', activeforeground='black')
        file_menu.add_command(label="Dark-Light", compound='left', command=self.change_theme, background='black',foreground='white',
                              activebackground='orange', activeforeground='black')
        file_menu.add_command(label="Close", compound='left', command=sys.exit, background='black',foreground='white', activebackground='orange',
                              activeforeground='black')
        file_menu.bind("<Control-Q>", sys.exit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Help Index", compound='left', command=self.help_index, background='black',foreground='white',
                              activebackground='orange', activeforeground='black')
        help_menu.add_command(label="About...", compound='left', command=self.about, background='black',foreground='white', activebackground='orange',
                              activeforeground='black')
        menu_bar.add_cascade(label="Help", menu=help_menu)
        self.config(menu=menu_bar)
        # tabs
        self.tab_control = ttk.Notebook(self)
        self.tab1, self.tab2, self.tab3 = ttk.Frame(self.tab_control), ttk.Frame(self.tab_control), ttk.Frame(self.tab_control) #relief="solid"
        self.tab4, self.tab5, self.tab6 = ttk.Frame(self.tab_control), ttk.Frame(self.tab_control), ttk.Frame(self.tab_control) #relief="solid"
        self.tab_control.add(self.tab1, text='Atmosphere')
        self.tab_control.add(self.tab2, text='Irradiance')
        self.tab_control.add(self.tab3, text='Orbital Lifetime')
        self.tab_control.add(self.tab4, text='Solar Activity')
        self.tab_control.add(self.tab5, text='LEO Debris')
        self.tab_control.add(self.tab6, text='Visualization')
        self.tab_control.pack(expand=True, fill='both')

    def pro_save_as(self):
        try:
            file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                            ('Text Document', '*.txt'),
                                            ('Excel File', '*.xls'),
                                            ('CSV File', '*.csv')], initialfile="result.txt",
                                title="Save the Informations", defaultextension='.txt')
            text_save = str(f'{self.result_box.get(0.0, END)} \n {self.irr_result_box.get(0.0, END)} \n {self.orbitdrag.get(0.0, END)}'
                            f'{self.deb_visi_resu.get(0.0, END)} \n {self.orb_visi_resu.get(0.0, END)}')
            file.write(text_save)
            file.close()
        except AttributeError:
            x = 1

    def new(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def help_index(self):
        os.system('information.pdf')

    def about(self):
        about_win = Toplevel(height=200, width=567)
        about_win.minsize(height=200, width=567)
        about_win.resizable(False, False)
        columns1 = ('#1', '#2', '#3')
        tree = ttk.Treeview(about_win, columns=columns1, show='headings')
        tree.heading('#1', text='Developer')
        tree.heading('#2', text='Specialization')
        tree.heading('#3', text='Email')
        contacts = [('Islam Reda Ahmed', 'Astronomy', 'Islamtrabeih.me@gmail.com'), ('Rahma Ashraf Khalil', 'Physics', 'RahmaAshraf64@gmail.com')]
        for contact in contacts:
            tree.insert('', END, values=contact)
        tree.pack(side=BOTTOM, fill='x')
        label_Dir = Message(about_win, text="Low Earth Orbit Program \nBy: Star_Light Team 2021", width=1000)
        label_Dir.config(font=('Times New Roman', 13))
        label_Dir.pack(side=BOTTOM, fill='both')

    def change_theme(self):
        if self.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
            self.tk.call("set_theme", "light")
            bc = "#FC6C85"
            fc = "#FC6C85"
            self.style.configure('.', foreground=fc)
            self.style.configure('TCombobox', background=bc, foreground=fc, darkcolor=bc, selectbackground="grey", lightcolor="lime")
            self.style.configure('TButton', background=bc, foreground=fc)
            self.style.configure('TEntry', background=bc, foreground=fc)
            self.style.configure('TText', background=bc, foreground=fc)
        elif self.tk.call("ttk::style", "theme", "use") == "sun-valley-light":
            self.tk.call("set_theme", "dark")
            bc = "#FC6C85"
            fc = "#7FFFD4"
            self.style.configure('.', foreground=fc)
            self.style.configure('TCombobox', background=bc,  foreground=fc, darkcolor=bc, selectbackground="grey", lightcolor="lime")
            self.style.configure('TButton', background=bc, foreground=fc)
            self.style.configure('TEntry', background=bc, foreground=fc)
            self.style.configure('TText', background=bc, foreground=fc)


class Atmosphere():
    def __init__(self, parent=App):
        App.__init__(self)

    def atmosphere_tab(self, ThemedTk):
        # Atmosphere
        self.tab1.grid_columnconfigure(0, weight=1)
        self.tab1.grid_rowconfigure(0, weight=1)
        atm_inputs = ttk.LabelFrame(self.tab1, text="inputs")
        atm_inputs.grid(column=0, row=0, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        atm_outputs = ttk.LabelFrame(self.tab1, text="result")
        atm_outputs.grid(column=0, row=1, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        # date label
        labelDir = ttk.Label(atm_inputs, text="Date :                 ")
        labelDir.grid(column=0, row=1)
        # month Combobox
        self.month_list = IntVar(None)
        self.month_list.set("month")
        month = ttk.Combobox(atm_inputs, width=14, textvariable=self.month_list)
        month['values'] = [i for i in range(1, 13)]
        month.grid(column=1, row=1)
        # years Combobox
        self.year_list = IntVar(None)
        self.year_list.set("year")
        year = ttk.Combobox(atm_inputs, width=14, textvariable=self.year_list)
        year['values'] = [i for i in range(1996, 2031)]
        year.grid(column=2, row=1)
        # height label
        height_lbl = ttk.Label(atm_inputs, text="Height :             ")
        height_lbl.grid(column=0, row=2)
        # height options
        self.height_list = IntVar(None)
        self.height_list.set("height in Km")
        height = ttk.Combobox(atm_inputs, width=14, textvariable=self.height_list)
        height['values'] = [i for i in range(100, 1050, 50)]
        height.grid(column=1, row=2)
        # Check buttons
        self.density = IntVar()
        ttk.Checkbutton(atm_inputs, text="Density", variable=self.density, style="Switch.TCheckbutton").grid(column=1, row=4, sticky=NW)
        self.Ar_atoms = IntVar()
        ttk.Checkbutton(atm_inputs, text="Argon", variable=self.Ar_atoms, style="Switch.TCheckbutton").grid(column=1, row=5, sticky=NW)
        self.He_atoms = IntVar()
        ttk.Checkbutton(atm_inputs, text="Helium", variable=self.He_atoms, style="Switch.TCheckbutton").grid(column=1, row=6, sticky=NW)
        self.temperature = IntVar()
        ttk.Checkbutton(atm_inputs, text="Temperature", variable=self.temperature, style="Switch.TCheckbutton").grid(column=2, row=4, sticky=NW)
        self.N2_molecules = IntVar()
        ttk.Checkbutton(atm_inputs, text="N Molecules", variable=self.N2_molecules, style="Switch.TCheckbutton").grid(column=2, row=5, sticky=NW)
        self.O2_molecules = IntVar()
        ttk.Checkbutton(atm_inputs, text="O Molecules", variable=self.O2_molecules, style="Switch.TCheckbutton").grid(column=2, row=6, sticky=NW)
        self.O_atoms = IntVar()
        ttk.Checkbutton(atm_inputs, text="O Atoms", variable=self.O_atoms, style="Switch.TCheckbutton").grid(column=3, row=4, sticky=NW)
        self.N_atoms = IntVar()
        ttk.Checkbutton(atm_inputs, text="N Atoms", variable=self.N_atoms, style="Switch.TCheckbutton").grid(column=3, row=5, sticky=NW)
        self.H_atoms = IntVar()
        ttk.Checkbutton(atm_inputs, text="Hydrogen", variable=self.H_atoms, style="Switch.TCheckbutton").grid(column=3, row=6, sticky=NW)
        # output
        result = ttk.Button(atm_outputs, text='Result', width=10, command=show_result)
        result.grid(row=7, column=0, sticky=N, padx=0, pady=0)
        # flat, groove, raised, ridge, solid, or sunken
        atmo_frame = ttk.Frame(atm_outputs, style='new.TFrame')
        atmo_frame.grid(row=7, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=1, columnspan=3)
        self.result_text = Text(atmo_frame, wrap="none", width=82, height=4, font=("Times New Roman", 10), relief="solid")
        vsb = ttk.Scrollbar(atmo_frame, command=self.result_text.yview, orient="vertical")
        self.result_text.configure(yscrollcommand=vsb.set)
        atmo_frame.grid_rowconfigure(0, weight=1)
        atmo_frame.grid_columnconfigure(0, weight=1)
        vsb.grid(row=0, column=1, sticky="ns")
        self.result_text.grid(row=0, column=0, sticky="nsew")
        # buttons

        def atmo_save():
            try:
                file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                                ('Text Document', '*.txt')], initialfile="result.txt",
                                    title="Save the Informations", defaultextension='.txt')
                text_save = str(self.result_box.get(0.0, END))
                file.write(text_save)
                file.close()
            except AttributeError:
                x = 1

        plot = ttk.Button(atm_outputs, text='Plot', width=10, command=data_plot1)
        plot.grid(row=10, column=0, sticky=N, padx=0, pady=0)
        save = ttk.Button(atm_outputs, text='Save', width=10, command=atmo_save)
        save.grid(row=11, column=0, sticky=N, padx=0, pady=0)
        atmo_frame_2 = ttk.Frame(atm_outputs)
        atmo_frame_2.grid(row=10, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
        self.result_box = Text(atmo_frame_2, wrap="none", width=82, height=16, font=("Times New Roman", 10), relief="solid")
        vsb_atm2 = ttk.Scrollbar(atmo_frame_2, command=self.result_box.yview, orient="vertical")
        self.result_box.configure(yscrollcommand=vsb_atm2.set)
        atmo_frame_2.grid_rowconfigure(0, weight=1)
        atmo_frame_2.grid_columnconfigure(0, weight=1)
        vsb_atm2.grid(row=0, column=1, sticky="ns")
        self.result_box.grid(row=0, column=0, sticky="nsew")
        for col in range(4):
            atm_inputs.columnconfigure(col, weight=1)
        for col in range(4):
            atm_outputs.columnconfigure(col, weight=1)
        for row in range(4):
            atm_inputs.rowconfigure(row, weight=1)
        for row in range(6):
            atm_outputs.rowconfigure(row, weight=1)



class Irradiance():
    def __init__(self, parent=App):
        App.__init__(self)

    def irradiance_tab(self, ThemedTk):
        self.tab2.grid_columnconfigure(0, weight=1)
        self.tab2.grid_rowconfigure(0, weight=1)
        irr_inputs = ttk.LabelFrame(self.tab2, text="inputs")
        irr_inputs.grid(column=0, row=0, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        irr_outputs = ttk.LabelFrame(self.tab2, text="result")
        irr_outputs.grid(column=0, row=1, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        # months
        self.irr_month_list = StringVar(None)
        self.irr_month_list.set('month')
        month = ttk.Combobox(irr_inputs, width=14, textvariable=self.irr_month_list)
        month['values'] = [i for i in range(1, 13)]
        month.grid(column=1, row=1)
        # years
        self.irr_year_list = StringVar(None)
        self.irr_year_list.set('year')
        year = ttk.Combobox(irr_inputs, width=14, textvariable=self.irr_year_list)
        year['values'] = [i for i in range(1996, 2031)]
        year.grid(column=2, row=1)
        # Labels
        date_irr = ttk.Label(irr_inputs, text='Date :         ')
        date_irr.grid(column=0, row=1)
        lat = ttk.Label(irr_inputs, text='Inclination :')
        lat.grid(column=0, row=2)
        # Inclination Entry
        self.lat_enter = IntVar(None)
        lat_box = ttk.Spinbox(irr_inputs, from_= 0, to_= 360, width = 10, textvariable = self.lat_enter)
        lat_box.grid(column=1, row=2, padx=0, pady=10)
        # Buttons

        def irr_save():
            try:
                file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                                ('Text Document', '*.txt')], initialfile="result.txt",
                                    title="Save the Informations", defaultextension='.txt')
                text_save = str(self.irr_result_box.get(0.0, END))
                file.write(text_save)
                file.close()
            except AttributeError:
                x = 1

        def irr_result():
            try:
                self.irr_result_text.delete(0, 1000)
                ph, yy, mm = self.lat_enter.get(), self.irr_month_list.get(), self.irr_year_list.get()
                data1= irradiance(yy, mm, ph)
                self.irr_result_text.insert('end', f'maximum = {data[0]} W/m^2' + '    ' + f'minimum = {data[1]} W/m^2')
            except ValueError:
                self.irr_result_text.delete(0, 1000)
                self.irr_result_text.insert('end', "Invalid date or Inclination")

        def irr_plot2():
            try:
                self.irr_result_box.delete('0.0', END)
                phi, yy, mm = self.lat_enter.get(), self.irr_month_list.get(), self.irr_year_list.get()
                y = irr_plot(yy, mm)
                x = irr_plot1(yy, mm, phi)
                self.irr_result_box.insert('end', f'{cell_irr_info(yy, mm, phi)}')
            except ValueError:
                self.irr_result_box.delete('0.0', END)
                self.irr_result_box.insert('end', "Invalid date or Inclination")

        result = ttk.Button(irr_outputs, text='Result', width=10, command=irr_result)
        result.grid(row=5, column=0, sticky=N, padx=0, pady=0)
        self.irr_result_text = ttk.Entry(irr_outputs, justify=LEFT)
        self.irr_result_text.grid(row=5, column=1, ipadx=0, ipady=0, columnspan=3, sticky="NSEW")
        Plot = ttk.Button(irr_outputs, text='Plot', width=10, command=irr_plot2)
        Plot.grid(row=6, column=0, sticky=N, padx=0, pady=0)
        save = ttk.Button(irr_outputs, text='Save', width=10, command=irr_save)
        save.grid(row=7, column=0, sticky=N, padx=0, pady=0)
        irr_frame = ttk.Frame(irr_outputs)
        irr_frame.grid(row=6, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=2, columnspan=3)
        self.irr_result_box = Text(irr_frame, wrap="none", width=82, height=22, font=("Times New Roman", 10), relief="solid")
        vsb_irr = ttk.Scrollbar(irr_frame, command=self.irr_result_box.yview, orient="vertical")
        self.irr_result_box.configure(yscrollcommand=vsb_irr.set)
        irr_frame.grid_rowconfigure(0, weight=1)
        irr_frame.grid_columnconfigure(0, weight=1)
        vsb_irr.grid(row=0, column=1, sticky="ns")
        self.irr_result_box.grid(row=0, column=0, sticky="nsew")
        for col in range(4):
            irr_inputs.columnconfigure(col, weight=1)
        for col in range(4):
            irr_outputs.columnconfigure(col, weight=1)
        for row in range(4):
            irr_inputs.rowconfigure(row, weight=1)
        for row in range(4):
            irr_outputs.rowconfigure(row, weight=1)



class Drag():
    def __init__(self, parent=App):
        App.__init__(self)

    def drag_tab(self, ThemedTk):
        self.tab3.grid_columnconfigure(0, weight=1)
        self.tab3.grid_rowconfigure(0, weight=1)
        drag_inputs = ttk.LabelFrame(self.tab3, text="inputs")
        drag_inputs.grid(column=0, row=0, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        drag_outputs = ttk.LabelFrame(self.tab3, text="result")
        drag_outputs.grid(column=0, row=1, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        # date
        life_date = ttk.Label(drag_inputs, text="Date :                 ")
        life_date.grid(column=0, row=1, padx=10, sticky="NSEW")
        # months options button
        self.drg_month_list = IntVar(None)
        self.drg_month_list.set("month")
        month = ttk.Combobox(drag_inputs, width=14, textvariable=self.drg_month_list)
        month['values'] = [i for i in range(1, 13)]
        month.grid(column=1, row=1)
        # years options button
        self.drg_year_list = IntVar(None)
        self.drg_year_list.set("year")
        year = ttk.Combobox(drag_inputs, width=14, textvariable=self.drg_year_list)
        year['values'] = [i for i in range(1996, 2031)]
        year.grid(column=3, row=1)
        # labels
        life_sem_lbl = ttk.Label(drag_inputs, text='Semi-major axis :').grid(column=0, row=2, padx=10, sticky=W)
        self.life_sem_enter = ttk.Entry(drag_inputs, justify='center', width=17)
        self.life_sem_enter.grid(column=1, row=2)
        life_ecc_lbl = ttk.Label(drag_inputs, text='Eccentricity :').grid(column=2, row=2, padx=10, sticky=W)
        self.life_ecc_enter = ttk.Entry(drag_inputs, justify='center', width=17)
        self.life_ecc_enter.grid(column=3, row=2)
        life_inc_lbl = ttk.Label(drag_inputs, text='Inclination :').grid(column=0, row=3, padx=10, sticky=W)
        self.life_inc_enter = ttk.Entry(drag_inputs, justify='center', width=17, state='disabled')
        self.life_inc_enter.grid(column=1, row=3)
        life_mass_lbl = ttk.Label(drag_inputs, text='Mass kg :').grid(column=2, row=3, padx=10, sticky=W)
        self.life_mass_enter = ttk.Entry(drag_inputs, justify='center', width=17)
        self.life_mass_enter.grid(column=3, row=3)
        life_arp_lbl = ttk.Label(drag_inputs, text='Argument Perigee :').grid(column=0, row=4, padx=10, sticky=W)
        self.life_arp_enter = ttk.Entry(drag_inputs, justify='center', width=17, state='disabled')
        self.life_arp_enter.grid(column=1, row=4)
        life_area_lbl = ttk.Label(drag_inputs, text='Area m^2 :').grid(column=2, row=4, padx=10, sticky=W)
        self.life_area_enter = ttk.Entry(drag_inputs, justify='center', width=17)
        self.life_area_enter.grid(column=3, row=4)
        life_true_lbl = ttk.Label(drag_inputs, text='Treu Anomaly :').grid(column=0, row=5, padx=10, sticky=W)
        self.life_true_enter = ttk.Entry(drag_inputs, justify='center', width=17)
        self.life_true_enter.grid(column=1, row=5)
        # check
        self.semi_major_axis = IntVar()
        ttk.Checkbutton(drag_inputs, text="Semi-major Axis", variable=self.semi_major_axis,
                        style="Switch.TCheckbutton").grid(column=1, row=6, sticky=NW)
        self.eccentricity_life = IntVar()
        ttk.Checkbutton(drag_inputs, text="Eccentricity", variable=self.eccentricity_life,
                        style="Switch.TCheckbutton").grid(column=1, row=7, sticky=NW, pady=5)
        self.atmo_drag = IntVar()
        ttk.Checkbutton(drag_inputs, text="Drag", variable=self.atmo_drag,
                        style="Switch.TCheckbutton").grid(column=3, row=6, sticky=NW)
        self.earth_oblate = IntVar()
        ttk.Checkbutton(drag_inputs, text="Under Oblateness", state=DISABLED, variable=self.earth_oblate,
                        style="Switch.TCheckbutton").grid(column=3, row=7, sticky=NW, pady=5)
        # output

        def drag_save():
            try:
                file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                                ('Text Document', '*.txt')], initialfile="result.txt",
                                    title="Save the Informations", defaultextension='.txt')
                text_save = str(self.orbitdrag.get(0.0, END))
                file.write(text_save)
                file.close()
            except AttributeError:
                x = 1

        def lifetime():
            try:
                self.orbitdrag.delete('0.0', END)
                yy, mm = self.drg_month_list.get(), self.drg_month_list.get()
                s_a, ecc = float(self.life_sem_enter.get()), float(self.life_ecc_enter.get())
                mass, true, area = float(self.life_mass_enter.get()), float(self.life_true_enter.get()), float(self.life_area_enter.get())
                s_a_check, oblateness, drag = self.semi_major_axis.get(), self.earth_oblate.get(), self.atmo_drag.get()
                ecc_check = self.eccentricity_life.get()
                if s_a_check:
                    if drag:
                        x = a_drag(s_a, ecc, true, area, mass, yy, mm)
                        self.orbitdrag.insert(END, f' \nvariation of a = {x[0]} km \n'
                                            f'it would take {x[1]} second to be 100 km orbit')
                if ecc_check:
                    if drag:
                        x = e_drag(s_a, ecc, true, area0, mass, yy, mm)
                        self.orbitdrag.insert(END, f' \nvariation of e = {x[0]} \n'
                                            f'it would take {x[1]} second to be circular orbit')
            except ValueError:
                self.orbitdrag.insert(END, 'Insert valid numbers')
            except TclError:
                self.orbitdrag.insert(END, 'Insert valid numbers')

        life_result = ttk.Button(drag_outputs, text='Result', width=10, command=lifetime)
        life_result.grid(row=9, column=0, sticky=N, padx=0, pady=0)
        life_save = ttk.Button(drag_outputs, text='Save', width=10, command=drag_save)
        life_save.grid(row=10, column=0, sticky=N, padx=0, pady=0)
        life_frame = ttk.Frame(drag_outputs)
        life_frame.grid(row=9, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
        self.orbitdrag = Text(life_frame, wrap="none", width=82, height=16, font=("Times New Roman", 10), relief="solid")
        vsb_life = ttk.Scrollbar(life_frame, command=self.orbitdrag.yview, orient="vertical")
        self.orbitdrag.configure(yscrollcommand=vsb_life.set)
        life_frame.grid_rowconfigure(0, weight=1)
        life_frame.grid_columnconfigure(0, weight=1)
        vsb_life.grid(row=0, column=1, sticky="ns")
        self.orbitdrag.grid(row=0, column=0, sticky="nsew")
        for col in range(4):
            drag_inputs.columnconfigure(col, weight=1)
        for col in range(4):
            drag_outputs.columnconfigure(col, weight=1)
        for row in range(6):
            drag_inputs.rowconfigure(row, weight=1)
        for row in range(4):
            drag_outputs.rowconfigure(row, weight=1)



class CMEActivity():
    def __init__(self, parent=App):
        App.__init__(self)

    def cmeactivity_tab(self, ThemedTk):
        self.tab4.grid_columnconfigure(0, weight=1)
        self.tab4.grid_rowconfigure(0, weight=1)
        cme_inputs = ttk.LabelFrame(self.tab4, text="inputs")
        cme_inputs.grid(column=0, row=0, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        cme_outputs = ttk.LabelFrame(self.tab4, text="result")
        cme_outputs.grid(column=0, row=1, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        # date label
        cme_date = ttk.Label(cme_inputs, text="Date :                 ")
        cme_date.grid(column=0, row=1)
        # days
        self.cme_day_list = IntVar(None)
        self.cme_day_list.set("day")
        day = ttk.Combobox(cme_inputs, width=14, textvariable=self.cme_day_list)
        day['values'] = [i for i in range(1, 32)]
        day.grid(column=1, row=1)
        # months options button
        self.cme_month_list = IntVar(None)
        self.cme_month_list.set("month")
        month = ttk.Combobox(cme_inputs, width=14, textvariable=self.cme_month_list)
        month['values'] = [i for i in range(1, 13)]
        month.grid(column=2, row=1)
        # years options button
        self.cme_year_list = IntVar(None)
        self.cme_year_list.set("year")
        year = ttk.Combobox(cme_inputs, width=14, textvariable=self.cme_year_list)
        year['values'] = [i for i in range(1996, 2031)]
        year.grid(column=3, row=1)
        # check box
        self.Central_PA = IntVar()
        ttk.Checkbutton(cme_inputs, text="Central PA", variable=self.Central_PA, style="Switch.TCheckbutton").grid(column=2, row=3)
        self.Linear_Speed = IntVar()
        ttk.Checkbutton(cme_inputs, text="Linear_Speed", variable=self.Linear_Speed, style="Switch.TCheckbutton").grid(column=1, row=3)
        self.MPA = IntVar()
        ttk.Checkbutton(cme_inputs, text="Mass         ", variable=self.MPA, style="Switch.TCheckbutton").grid(column=2, row=4, pady=5)
        self.Width = IntVar()
        ttk.Checkbutton(cme_inputs, text="Width         ", variable=self.Width, style="Switch.TCheckbutton").grid(column=3, row=3)
        # output

        def cme_save():
            try:
                file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                                ('Text Document', '*.txt')], initialfile="result.txt",
                                    title="Save the Informations", defaultextension='.txt')
                text_save = str(self.cme_result_box.get(0.0, END))
                file.write(text_save)
                file.close()
            except AttributeError:
                x = 1

        result = ttk.Button(cme_outputs, text='Result', width=10, command=cme_result)
        result.grid(row=5, column=0, sticky=N, padx=0, pady=0)
        self.cme_result_text = ttk.Entry(cme_outputs, justify=LEFT)
        self.cme_result_text.grid(row=5, column=1, ipadx=0, ipady=0, columnspan=3, sticky="NSEW")
        Plot = ttk.Button(cme_outputs, text='Plot', width=10, command=cme_plot1)
        Plot.grid(row=6, column=0, sticky=N, padx=0, pady=0)
        save = ttk.Button(cme_outputs, text='Save', width=10, command=cme_save)
        save.grid(row=7, column=0, sticky=N, padx=0, pady=0)
        cme_frame = ttk.Frame(cme_outputs)
        cme_frame.grid(row=6, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
        self.cme_result_box = Text(cme_frame, wrap="none", width=82, height=21, font=("Times New Roman", 10), relief="solid")
        vsb_cme = ttk.Scrollbar(cme_frame, command=self.cme_result_box.yview, orient="vertical")
        self.cme_result_box.configure(yscrollcommand=vsb_cme.set)
        cme_frame.grid_rowconfigure(0, weight=1)
        cme_frame.grid_columnconfigure(0, weight=1)
        vsb_cme.grid(row=0, column=1, sticky="ns")
        self.cme_result_box.grid(row=0, column=0, sticky="nsew")
        for col in range(4):
            cme_inputs.columnconfigure(col, weight=1)
        for col in range(4):
            cme_outputs.columnconfigure(col, weight=1)
        for row in range(4):
            cme_inputs.rowconfigure(row, weight=1)
        for row in range(4):
            cme_outputs.rowconfigure(row, weight=1)



class Debris():
    def __init__(self, parent=App):
        App.__init__(self)

    def debris_tab(self, ThemedTk):
        self.tab5.grid_columnconfigure(0, weight=1)
        self.tab5.grid_rowconfigure(0, weight=1)
        deb_inputs = ttk.LabelFrame(self.tab5, text="inputs")
        deb_inputs.grid(column=0, row=0, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        deb_outputs = ttk.LabelFrame(self.tab5, text="result")
        deb_outputs.grid(column=0, row=1, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        # a, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss
        # date
        deb_date = ttk.Label(deb_inputs, text="Date :                 ")
        deb_date.grid(column=0, row=1, padx=10, sticky=W)
        # day
        self.deb_day_list = IntVar(None)
        self.deb_day_list.set("day")
        day = ttk.Combobox(deb_inputs, width=14, textvariable=self.deb_day_list)
        day['values'] = [i for i in range(1, 32)]
        day.grid(column=1, row=1)
        # months options button
        self.deb_month_list = IntVar(None)
        self.deb_month_list.set("month")
        month = ttk.Combobox(deb_inputs, width=14, textvariable=self.deb_month_list)
        month['values'] = [i for i in range(1, 13)]
        month.grid(column=2, row=1)
        # years options button
        self.deb_year_list = IntVar(None)
        self.deb_year_list.set("year")
        year = ttk.Combobox(deb_inputs, width=14, textvariable=self.deb_year_list)
        year['values'] = [i for i in range(1996, 2031)]
        year.grid(column=3, row=1)
        # hours options button
        self.deb_hours_list = IntVar(None)
        self.deb_hours_list.set("hours")
        hours = ttk.Combobox(deb_inputs, width=14, textvariable=self.deb_hours_list)
        hours['values'] = [i for i in range(1, 24)]
        hours.grid(column=1, row=2)
        # minuts options button
        self.deb_minuts_list = IntVar(None)
        self.deb_minuts_list.set("minutes")
        minuts = ttk.Combobox(deb_inputs, width=14, textvariable=self.deb_minuts_list)
        minuts['values'] = [i for i in range(1, 60)]
        minuts.grid(column=2, row=2)
        # seconds options button
        self.deb_seconds_list = IntVar(None)
        self.deb_seconds_list.set("seconds")
        seconds = ttk.Combobox(deb_inputs, width=14, textvariable=self.deb_seconds_list)
        seconds['values'] = [i for i in range(1, 60)]
        seconds.grid(column=3, row=2)
        # sa, ecc, inc, raan, argp, nu, yy, mm, dd, p, aa, m
        # labels
        deb_sem_lbl = ttk.Label(deb_inputs, text='Semi-major axis :    ').grid(column=0, row=3, padx=10, sticky=W)
        self.deb_sem_enter = ttk.Entry(deb_inputs, justify='center', width=17)
        self.deb_sem_enter.grid(column=1, row=3)
        deb_ecc_lbl = ttk.Label(deb_inputs, text='Eccentricity :       ').grid(column=2, row=3, padx=10, sticky=W)
        self.deb_ecc_enter = ttk.Entry(deb_inputs, justify='center', width=17)
        self.deb_ecc_enter.grid(column=3, row=3)
        deb_inc_lbl = ttk.Label(deb_inputs, text='Inclination :        ').grid(column=0, row=4, padx=10, sticky=W)
        self.deb_inc_enter = ttk.Entry(deb_inputs, justify='center', width=17)
        self.deb_inc_enter.grid(column=1, row=4)
        deb_raa_lbl = ttk.Label(deb_inputs, text='Right Ascension :    ').grid(column=2, row=4, padx=10, sticky=W)
        self.deb_raa_enter = ttk.Entry(deb_inputs, justify='center', width=17)
        self.deb_raa_enter.grid(column=3, row=4)
        deb_arp_lbl = ttk.Label(deb_inputs, text='Argument Perigee :').grid(column=0, row=5, padx=10, sticky=W)
        self.deb_arp_enter = ttk.Entry(deb_inputs, justify='center', width=17)
        self.deb_arp_enter.grid(column=1, row=5)
        deb_tru_lbl = ttk.Label(deb_inputs, text='True Anomaly :       ').grid(column=2, row=5, padx=10, sticky=W)
        self.deb_tru_enter = ttk.Entry(deb_inputs, justify='center', width=17)
        self.deb_tru_enter.grid(column=3, row=5)
        # result

        def deb_save():
            try:
                file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                                ('Text Document', '*.txt')], initialfile="result.txt",
                                    title="Save the Informations", defaultextension='.txt')
                text_save = str(self.deb_visi_resu.get(0.0, END))
                file.write(text_save)
                file.close()
            except AttributeError:
                x = 1


        def deb_plotter():
            try:
                self.deb_visi_resu.delete('0.0', END)
                sa, ecc, inc = float(self.deb_sem_enter.get()), float(self.deb_ecc_enter.get()), float(self.deb_inc_enter.get())
                raan, argp, nu = float(self.deb_raa_enter.get()), float(self.deb_arp_enter.get()), float(self.deb_tru_enter.get())
                yy, mm, dd = self.deb_year_list.get(), self.deb_month_list.get(), self.deb_day_list.get()
                hh, mn, ss = self.deb_hours_list.get(), self.deb_minuts_list.get(), self.deb_seconds_list.get()
                x = deb_plot(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss)
                self.deb_visi_resu.insert(END, deb_info(sa))
            except ValueError:
                self.deb_visi_resu.delete('0.0', END)
                self.deb_visi_resu.insert(END, "Invalid Input Number, please make sure that all inputs are valid or numbers")

        deb_visi_plot = ttk.Button(deb_outputs, text='Plot', width=10, command=deb_plotter)
        deb_visi_plot.grid(row=7, column=0, sticky=N, padx=0, pady=0)
        deb_visi_save = ttk.Button(deb_outputs, text='Save', width=10, command=deb_save)
        deb_visi_save.grid(row=8, column=0, sticky=N, padx=0, pady=0)
        dep_frame = ttk.Frame(deb_outputs)
        dep_frame.grid(row=7, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
        self.deb_visi_resu = Text(dep_frame, wrap="none", width=82, height=19, font=("Times New Roman", 10), relief="solid")
        vsb_dep = ttk.Scrollbar(dep_frame, command=self.deb_visi_resu.yview, orient="vertical")
        self.deb_visi_resu.configure(yscrollcommand=vsb_dep.set)
        dep_frame.grid_rowconfigure(0, weight=1)
        dep_frame.grid_columnconfigure(0, weight=1)
        vsb_dep.grid(row=0, column=1, sticky="ns")
        self.deb_visi_resu.grid(row=0, column=0, sticky="nsew")
        for col in range(4):
            deb_inputs.columnconfigure(col, weight=1)
        for col in range(4):
            deb_outputs.columnconfigure(col, weight=1)
        for row in range(5):
            deb_inputs.rowconfigure(row, weight=1)
        for row in range(4):
            deb_outputs.rowconfigure(row, weight=1)



class Orbit():
    def __init__(self, parent=App):
        App.__init__(self)

    def orbit_tab(self, ThemedTk):
        self.tab6.grid_columnconfigure(0, weight=1)
        self.tab6.grid_rowconfigure(0, weight=1)
        vis_inputs = ttk.LabelFrame(self.tab6, text="inputs")
        vis_inputs.grid(column=0, row=0, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        vis_outputs = ttk.LabelFrame(self.tab6, text="result")
        vis_outputs.grid(column=0, row=1, columnspan=2, sticky="WE", padx=5, pady=0, ipadx=0, ipady=0)
        # date
        visi_date = ttk.Label(vis_inputs, text="Date :                 ")
        visi_date.grid(column=0, row=1, padx=10, sticky=W)
        # day
        self.orb_day_list = IntVar()
        self.orb_day_list.set("day")
        day = ttk.Combobox(vis_inputs, width=14, textvariable=self.orb_day_list)
        day['values'] = [i for i in range(1, 32)]
        day.grid(column=1, row=1)
        # months options button
        self.orb_month_list = IntVar(None)
        self.orb_month_list.set("month")
        month = ttk.Combobox(vis_inputs, width=14, textvariable=self.orb_month_list)
        month['values'] = [i for i in range(1, 13)]
        month.grid(column=2, row=1)
        # years options button
        self.orb_year = IntVar(None)
        self.orb_year.set("year")
        year = ttk.Combobox(vis_inputs, width=14, textvariable=self.orb_year)
        year['values'] = [i for i in range(1996, 2031)]
        year.grid(column=3, row=1)
        # hours options button
        self.orb_hours = IntVar(None)
        self.orb_hours.set("hours")
        hours = ttk.Combobox(vis_inputs, width=14, textvariable=self.orb_hours)
        hours['values'] = [i for i in range(1, 24)]
        hours.grid(column=1, row=2)
        # hours options button
        self.orb_minuts = IntVar(None)
        self.orb_minuts.set("minutes")
        minuts = ttk.Combobox(vis_inputs, width=14, textvariable=self.orb_minuts)
        minuts['values'] = [i for i in range(1, 60)]
        minuts.grid(column=2, row=2)
        # hours options button
        self.orb_seconds = IntVar(None)
        self.orb_seconds.set("seconds")
        seconds = ttk.Combobox(vis_inputs, width=14, textvariable=self.orb_seconds)
        seconds['values'] = [i for i in range(1, 60)]
        seconds.grid(column=3, row=2)
        # sa, ecc, inc, raan, argp, nu, yy, mm, dd, p, aa, m
        # labels
        sem_lbl = ttk.Label(vis_inputs, text='Semi-major axis :    ').grid(column=0, row=3, padx=10, sticky=W)
        self.orb_sem_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_sem_enter.grid(column=1, row=3)
        ecc_lbl = ttk.Label(vis_inputs, text='Eccentricity :       ').grid(column=2, row=3, padx=10, sticky=W)
        self.orb_ecc_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_ecc_enter.grid(column=3, row=3)
        inc_lbl = ttk.Label(vis_inputs, text='Inclination :        ').grid(column=0, row=4, padx=10, sticky=W)
        self.orb_inc_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_inc_enter.grid(column=1, row=4)
        raa_lbl = ttk.Label(vis_inputs, text='Right Ascension :    ').grid(column=2, row=4, padx=10, sticky=W)
        self.orb_raa_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_raa_enter.grid(column=3, row=4)
        arp_lbl = ttk.Label(vis_inputs, text='Argument Perigee :').grid(column=0, row=5, padx=10, sticky=W)
        self.orb_arp_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_arp_enter.grid(column=1, row=5)
        tru_lbl = ttk.Label(vis_inputs, text='True Anomaly :       ').grid(column=2, row=5, padx=10, sticky=W)
        self.orb_tru_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_tru_enter.grid(column=3, row=5)
        prd_lbl = ttk.Label(vis_inputs, text='Number of Tours :    ').grid(column=0, row=6, padx=10, sticky=W)
        self.orb_prd_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_prd_enter.grid(column=1, row=6)
        mas_lbl = ttk.Label(vis_inputs, text='Mass Kg :            ').grid(column=2, row=6, padx=10, sticky=W)
        self.orb_mas_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_mas_enter.grid(column=3, row=6)
        are_lbl = ttk.Label(vis_inputs, text='Area m^2 :           ').grid(column=0, row=7, padx=10, sticky=W)
        self.orb_are_enter = ttk.Entry(vis_inputs, justify='center', width=17)
        self.orb_are_enter.grid(column=1, row=7)
        # result

        def visi_save():
            try:
                file = asksaveasfile(filetypes=[('All Files', '*.*'),
                                                ('Text Document', '*.txt')], initialfile="result.txt",
                                    title="Save the Informations", defaultextension='.txt')
                text_save = str(self.orb_visi_resu.get(0.0, END))
                file.write(text_save)
                file.close()
            except AttributeError:
                x = 1

        def orb_plotter():
            try:
                self.orb_visi_resu.delete('0.0', END)
                sa, ecc, inc = float(self.orb_sem_enter.get()), float(self.orb_ecc_enter.get()), float(self.orb_inc_enter.get())
                raan, argp, nu = float(self.orb_raa_enter.get()), float(self.orb_arp_enter.get()), float(self.orb_tru_enter.get())
                p, aa, m = float(self.orb_prd_enter.get()), float(self.orb_are_enter.get()), float(self.orb_mas_enter.get())
                yy, mm, dd = self.orb_year.get(), self.orb_month_list.get(), self.orb_day_list.get()
                hh, mn, ss = self.orb_hours.get(), self.orb_month.get(), self.orb_seconds.get()
                x = orb_calc(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss, p, aa, m)
                self.orb_visi_resu.insert(END, orb_info_ri(sa, ecc, inc, raan, argp, nu, yy, mm, dd, hh, mn, ss))
            except ValueError:
                self.orb_visi_resu.delete('0.0', END)
                self.orb_visi_resu.insert(END, "Invalid Input Number, please make sure that all inputs are valid or numbers")

        visi_plot = ttk.Button(vis_outputs, text='Plot', width=10, command=orb_plotter)
        visi_plot.grid(row=9, column=0, sticky=N, padx=0, pady=0)
        visi_save = ttk.Button(vis_outputs, text='Save', width=10, command=visi_save)
        visi_save.grid(row=10, column=0, sticky=N, padx=0, pady=0)
        visio_frame = ttk.Frame(vis_outputs)
        visio_frame.grid(row=9, column=1, ipadx=10, ipady=0, sticky="NSEW", rowspan=3, columnspan=3)
        self.orb_visi_resu = Text(visio_frame, wrap="none", width=82, height=16, font=("Times New Roman", 10), relief="solid")
        vsb_visio = ttk.Scrollbar(visio_frame, command=self.orb_visi_resu.yview, orient="vertical")
        self.orb_visi_resu.configure(yscrollcommand=vsb_visio.set)
        visio_frame.grid_rowconfigure(0, weight=1)
        visio_frame.grid_columnconfigure(0, weight=1)
        vsb_visio.grid(row=0, column=1, sticky="ns")
        self.orb_visi_resu.grid(row=0, column=0, sticky="nsew")
        for col in range(4):
            vis_inputs.columnconfigure(col, weight=1)
        for col in range(4):
            vis_outputs.columnconfigure(col, weight=1)
        for row in range(7):
            vis_inputs.rowconfigure(row, weight=1)
        for row in range(4):
            vis_outputs.rowconfigure(row, weight=1)



'''
bc = "gray"
fc = "black"
s = ttk.Style()
s.configure('TFrame', background=bc, foreground=fc)
s.configure('TCombobox', background=bc, fieldbackground=bc, foreground=fc, darkcolor=bc, selectbackground="grey", lightcolor="lime")
s.configure('TCheckbutton', background=bc, foreground=fc)
s.configure('TButton', background=bc, foreground=fc)
s.configure('TLabel', background=bc, foreground=fc)
s.configure('TEntry', background=bc, foreground=fc)
s.configure('TNotebook', background=bc, foreground=fc)
s.configure('TLabelFrame', background=bc, foreground=fc)
s.configure('Vertical.TScrollbar', background=bc, foreground=fc)
'''

# atmosphere
# ---------------------------------------------------------------------------------------------------------------------

def show_result():
    '''
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
    '''
    pass


def data_plot1():
    '''
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
    '''
    pass


# cme activity
# ---------------------------------------------------------------------------------------------------------------------


def cme_result():
    '''
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
    '''
    pass


def cme_plot1():
    '''
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
    '''
    pass


# window pack
# ---------------------------------------------------------------------------------------------------------------------


app = App()
app.mainloop()
