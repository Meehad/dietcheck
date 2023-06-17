import customtkinter
from tkinter import messagebox
from tkinter import *

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
        def __init__(self):
                super().__init__()
                
                self.title("Diet Check")
                self.iconbitmap("C:/Users/Safiya/Desktop/meehad17/dietcheck/favicon.ico")
                self.geometry(f"{400}x{380}")
                self.grid_columnconfigure(1, weight=1)
                self.grid_columnconfigure((2, 3), weight=0)
                self.grid_rowconfigure((0, 1, 2), weight=1)
                
                self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
                self.sidebar_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
                self.sidebar_frame.grid_columnconfigure(2, weight=1)
                
                sugarlevel = StringVar()
                sugarlevel.set('')

                customtkinter.CTkLabel(self.sidebar_frame, text="Welcome to Diet Check", font=customtkinter.CTkFont(size=23, weight="bold")).grid(row=0,column=0,columnspan=2)
                customtkinter.CTkLabel(self, text="\nWhat is your sugar level: ",font=customtkinter.CTkFont(size=13, weight="normal")).grid(row=1,column=0)
                
                self.sugarlevel = customtkinter.CTkEntry(self,textvariable=sugarlevel,placeholder_text="For eg:123,etc")
                self.sugarlevel.grid(row=1, column=1)
                
                customtkinter.CTkButton(self, text='SUBMIT', command=self.Submit).grid(row=2,column=0,columnspan=2,ipadx=135)
                customtkinter.CTkLabel(self, text='\nYou should have Foods that is high in:',font=customtkinter.CTkFont(size=13, weight="normal")).grid(row=3,column=0)
                
                self.diet = customtkinter.CTkEntry(self)
                self.diet.grid(row=3,column=1)
                
                customtkinter.CTkButton(self, text='VIEW MORE',command=self.more).grid(row=4,column=0,columnspan=2,ipadx=135)
                customtkinter.CTkLabel(self, text='\nFor example  :\n',font=customtkinter.CTkFont(size=13, weight="normal")).grid(row=5,column=0)
                self.d = customtkinter.CTkEntry(self)
                
                self.d.grid(row=5,column=1)
                
                customtkinter.CTkButton(self, text='RESET',command=self.Reset).grid(row=6,column=1)
                customtkinter.CTkButton(self, text='HISTORY',command=self.Reset).grid(row=7,column=1)
                customtkinter.CTkButton(self, text='HELP', command=self.Help).grid(row=8,column=1)
                customtkinter.CTkButton(self, text='EXIT', command=self.Exit,fg_color='red',hover_color='dark red').grid(row=9,column=1)
                
                self.appearance_mode_label = customtkinter.CTkLabel(self, text="Appearance Mode:", anchor="w")
                self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
                self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=[ "Dark","Light", "System"],command=self.change_appearance_mode_event)
                self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
                self.scaling_label = customtkinter.CTkLabel(self, text="UI Scaling:", anchor="w")
                self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
                self.scaling_optionemenu = customtkinter.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
                self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))
        
        def Submit(self):
                try:
                        global x
                        x=self.sugarlevel.get()
                        int(x)
                        if float(x) < 69:
                                messagebox.showwarning('Diet Check','You should consult a nearest doctor you are in critical condition')
                                self.diet.insert(0,'carbohydrates and foods high in protein')
                        elif float(x) < 79:
                                self.diet.insert(0,'carbohydrates and foods high in protein')
                        elif float(x) > 240:
                                messagebox.showwarning('Diet Check','You should consult a nearest doctor you are in critical condition')
                                self.diet.insert(0,'Magneisum,fiber and Protein')
                        elif float(x) > 110:
                                self.diet.insert(0,'Magneisum,fiber and Protein')
                        else:
                                messagebox.showinfo('Diet Check','You have normal sugarlevel maintain this sugar level')
                                return True
                except:
                        messagebox.showwarning('Diet Check','Type in number')
                        self.sugarlevel.delete(0 , END)
                        self.diet.delete(0 , END)
                        return False
                        raise

        def more(self):
                if float(x) < 79:
                        self.d.insert(0,'Rice,Bread,Fruits and Sugar, and Meats,Fish,Eggs,Milk and Diary products, and Oily foods')
                elif float(x) > 110:
                        self.d.insert(0,'Raw, Cooked, or Roasted Vegetables, Melon or Berries')
                else:
                        self.d.insert(0,'')
                        return

        def Exit(self):
                self.qExit = messagebox.askyesno('Diet Check','do you want to exit the program')
                if self.qExit > 0:
                        app.destroy()
                        return

        def Reset(self):
                self.sugarlevel.delete(0 , END)
                self.diet.delete(0 , END)
                self.d.delete(0, END)
                return

        # def Help(self):
        #         root2=customtkinter.CTkToplevel()
        #         root2.title("Diet Check")
        #         root2.iconbitmap('C:/Users/Safiya/Desktop/meehad17/dietcheck/favicon.ico')
        #         def Exit2():
        #                 root2.destroy()
        #                 return
        #         customtkinter.CTkLabel(root2, text='HELP').pack()#,customtkinter.CTkFont(size=12, weight="normal")).pack()
        #         customtkinter.CTkLabel(root2, text='''Type your sugarlevel in the textbox near where it asks what is your sugarlevel then click submit and
        #         it will show what nutrients you are rpyeqired but if you dont know what food ypu should consume to get these nutrients
        #         click view more it will show food items with these nutrients.
        #         If you enter wrong sugarlevel by mistake dont worry just click reset and it will reset your entry.
        #         If you want to exit program click exit and click yes then the program will close.
        #         (NOTE:You should consult a nearest doctor in critical condition as this program only advices diet in uncritical condition)
        #         Have a nice day''').pack()#,customtkinter.CTkFont(size=8, weight="normal")).pack()
        #         customtkinter.CTkButton(root2, text='OK', command=Exit2()).pack()

        def Help(self):
                root2=customtkinter.CTkToplevel()
                root2.title("Diet Check")
                root2.configure(background="white")
                root2.iconbitmap('C:/Users/Safiya/Desktop/meehad17/dietcheck/favicon.ico')
                def Exit2():
                        root2.destroy()
                        return
                customtkinter.CTkLabel(root2, text='HELP').pack()
                customtkinter.CTkLabel(root2, text='''Type your sugarlevel in the textbox near where it asks what is your sugarlevel then click submit and
                        it will show what nutrients you are rpyeqired but if you dont know what food ypu should consume to get these nutrients
                        click view more it will show food items with these nutrients.
                        If you enter wrong sugarlevel by mistake dont worry just click reset and it will reset your entry.
                        If you want to exit program click exit and click yes then the program will close.
                        (NOTE:You should consult a nearest doctor in critical condition as this program only advices diet in uncritical condition)
                                Have a nice day''').pack()
                customtkinter.CTkButton(root2, text='OK',command=Exit2).pack()

        def change_appearance_mode_event(self, new_appearance_mode: str):
                customtkinter.set_appearance_mode(new_appearance_mode)

        def change_scaling_event(self, new_scaling: str):
                new_scaling_float = int(new_scaling.replace("%", "")) / 100
                customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
        app = App()
        app.mainloop()