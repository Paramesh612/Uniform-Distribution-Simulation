import tkinter as tk
from tkinter import ttk
import math
from PIL import Image, ImageTk
from statsmodels.stats.proportion import proportions_ztest
import scipy.stats as stats

class HypothesisTestingApp:
    def __init__(self, root):
        self.root1 = root
        self.root1.title("Hypothesis Testing App")

        
        self.background_image = Image.open("stat.jpg") 
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root1, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1) 
        self.root = ttk.Frame(self.root1, padding=(10, 10, 10, 10), relief="raised") 
        self.root.grid(row=1, column=0)

       
        self.root1.columnconfigure(0, weight=1)
        self.root1.rowconfigure(1, weight=1)

       
        self.root1.update_idletasks() 
        window_width = self.root1.winfo_width()
        window_height = self.root1.winfo_height()
        frame_width = self.root.winfo_reqwidth()
        frame_height = self.root.winfo_reqheight()

        x = (window_width - frame_width) // 2
        y = (window_height - frame_height) // 2

        self.root1.geometry(f"+{x}+{y}")

        
        common_font = ('Times New Roman', 12)
        self.root.option_add('*TButton*Font', common_font)
        self.root.option_add('*TLabel*Font', common_font)
        self.root.option_add('*TCombobox*Font', common_font)
        

        self.create_widgets()

    def create_widgets(self):
        
        self.hypothesis_type = tk.StringVar()
        self.hypothesis_type.set("select the type")  
        
        self.var_population_prop = tk.DoubleVar()
        self.var_sample_size = tk.DoubleVar()
        self.var_no_success = tk.DoubleVar()
        self.var_sample_mean = tk.DoubleVar()
        self.var_sample_std = tk.DoubleVar()
        self.var_population_mean = tk.DoubleVar()
        self.var_population_SD = tk.DoubleVar()

        self.var_sample_mean_1 = tk.DoubleVar()
        self.var_sample_std_1 = tk.DoubleVar()
        self.var_sample_size_1 = tk.DoubleVar()

        self.var_sample_mean_2 = tk.DoubleVar()
        self.var_sample_std_2 = tk.DoubleVar()
        self.var_sample_size_2 = tk.DoubleVar()
        self.var_sample_prop_1 = tk.DoubleVar()
        self.var_sample_prop_2 = tk.DoubleVar()
        self.var_los=tk.DoubleVar()
        self.var_tail=tk.StringVar()
        self.calc_z=tk.DoubleVar()

        
        ttk.Label(self.root, text="Select Hypothesis Type:").grid(row=0, column=0, padx=10, pady=5)
        hypothesis_type_combobox = ttk.Combobox(self.root, textvariable=self.hypothesis_type,
                                                values=["proposition", "proposition_diff", "mean", "std_dev", "mean_diff", "std_dev_diff"])
        hypothesis_type_combobox.grid(row=0, column=1, padx=10, pady=5)

        
        hypothesis_type_combobox.bind("<<ComboboxSelected>>", lambda event: self.show_input_fields())

        
        self.output_label = ttk.Label(self.root, text="")
        self.output_label.grid(row=11, column=0, columnspan=2)

        
        ttk.Button(self.root, text="Perform Hypothesis Test", command=self.perform_test).grid(row=12, column=0, columnspan=2, pady=10)
    def clear_input_fields(self):
        
        self.var_population_prop.set(0.0)
        self.var_sample_prop.set(0.0)
        self.var_sample_mean_1.set(0.0)
        self.var_sample_std_1.set(0.0)
        self.var_sample_size_1.set(0.0)
        self.var_sample_mean_2.set(0.0)
        self.var_sample_std_2.set(0.0)
        self.var_sample_size_2.set(0.0)

    def show_input_fields(self):
        hypothesis_type = self.hypothesis_type.get()

        
        for widget in self.root.winfo_children():
            if isinstance(widget, (ttk.Entry, ttk.Label)):
                widget.grid_forget()

        ttk.Label(self.root, text="Select Hypothesis Type:").grid(row=0, column=0, padx=10, pady=5)
        hypothesis_type_combobox = ttk.Combobox(self.root, textvariable=self.hypothesis_type,
                                                values=["proposition", "proposition_diff", "mean", "std_dev", "mean_diff", "std_dev_diff"])
        hypothesis_type_combobox.grid(row=0, column=1, padx=10, pady=5)
        hypothesis_type_combobox.bind("<<ComboboxSelected>>", lambda event: self.show_input_fields())

        
        if hypothesis_type == "proposition":
            ttk.Label(self.root, text="Population Proportion(P):").grid(row=1, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_population_prop).grid(row=1, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Size(n):").grid(row=2, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size).grid(row=2, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="No. of success(X):").grid(row=3, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_no_success).grid(row=3, column=1, padx=10, pady=5)
        elif hypothesis_type == "proposition_diff":
            ttk.Label(self.root, text="Sample size 1(n1):").grid(row=1, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size_1).grid(row=1, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Proportion 1(p1):").grid(row=2, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_prop_1).grid(row=2, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample size 2(n2):").grid(row=3, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size_2).grid(row=3, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Proportion 2(p2):").grid(row=4, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_prop_2).grid(row=4, column=1, padx=10, pady=5)
        elif hypothesis_type == "mean":
            ttk.Label(self.root, text="Population Mean:(μ)").grid(row=1, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_population_mean).grid(row=1, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Mean(x):").grid(row=2, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_mean).grid(row=2, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample size(n):").grid(row=3, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size).grid(row=3, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Population SD(σ):").grid(row=4, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_population_SD).grid(row=4, column=1, padx=10, pady=5)
        elif hypothesis_type == "std_dev":
            ttk.Label(self.root, text="Population Standard Deviation(σ):").grid(row=1, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_population_SD).grid(row=1, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Standard Deviation:(s)").grid(row=2, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_std).grid(row=2, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample size:(n)").grid(row=3, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size).grid(row=3, column=1, padx=10, pady=5)
        elif hypothesis_type == "mean_diff":
            ttk.Label(self.root, text="Sample Mean 1(x1):").grid(row=1, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_mean_1).grid(row=1, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Standard Deviation 1(s1):").grid(row=2, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_std_1).grid(row=2, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Size 1(n1):").grid(row=3, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size_1).grid(row=3, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Mean 2(x2):").grid(row=4, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_mean_2).grid(row=4, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Standard Deviation 2(s2):").grid(row=5, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_std_2).grid(row=5, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Size 2(n2):").grid(row=6, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size_2).grid(row=6, column=1, padx=10, pady=5)
        elif hypothesis_type == "std_dev_diff":
            ttk.Label(self.root, text="Sample Standard Deviation 1(s1):").grid(row=1, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_std_1).grid(row=1, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Size 1(n1):").grid(row=2, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size_1).grid(row=2, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Standard Deviation 2(s2):").grid(row=3, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_std_2).grid(row=3, column=1, padx=10, pady=5)

            ttk.Label(self.root, text="Sample Size 2(n2):").grid(row=4, column=0, padx=10, pady=5)
            ttk.Entry(self.root, textvariable=self.var_sample_size_2).grid(row=4, column=1, padx=10, pady=5)
        else:
            ttk.Label(self.root, text="Invalid hypothesis type selected.").grid(row=1, column=0, padx=10, pady=5)

        
        ttk.Label(self.root, text="Select LOS(%):").grid(row=7, column=0, padx=10, pady=5)
        hypothesis_type_combobox = ttk.Combobox(self.root, textvariable=self.var_los,
                                                values=[1,2,5,10])
        hypothesis_type_combobox.grid(row=7, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Select Type of test(tail):").grid(row=8, column=0, padx=10, pady=5)
        hypothesis_type_combobox = ttk.Combobox(self.root, textvariable=self.var_tail,
                                                values=["two-tail","left-tail","right-tail"])
        hypothesis_type_combobox.grid(row=8, column=1, padx=10, pady=5)


    def table_z(self):
        los = self.var_los.get()
        tail = self.var_tail.get()

        los=los/100

        if(tail=="two-tail"):
            los = los/2
            
        return stats.norm.ppf(los)


    def perform_test(self):
        
        hypothesis_type = self.hypothesis_type.get()
        calc_z = 0

        if hypothesis_type == "proposition":
            print("Testing of hypothesis about population proportion")
            pop_prop = self.var_population_prop.get()
            sample_size = self.var_sample_size.get()
            no_success = self.var_no_success.get()

            print(f"Hypothesis Testing Function {pop_prop}, {sample_size}, {no_success}")
            calc_z, p_value = proportions_ztest(no_success, sample_size, pop_prop, prop_var=pop_prop)
            
        elif hypothesis_type == "proposition_diff":
            print("Testing of hypothesis about difference between two proportions")
            sample_size_1 = self.var_sample_size_1.get()
            sample_prop_1 = self.var_sample_prop_1.get()

            sample_size_2 = self.var_sample_size_2.get()
            sample_prop_2 = self.var_sample_prop_2.get()

            print("Hypothesis Testing Function")
            P = ((sample_size_1 * sample_prop_1) + (sample_size_2 * sample_prop_2)) / (sample_size_1 + sample_size_2)
            calc_z, p_value_diff = proportions_ztest([sample_prop_1, sample_prop_2], [sample_size_1, sample_size_2],
                                                     value=sample_prop_1 - sample_prop_2, prop_var=P)
            
        elif hypothesis_type == "mean":
            print("Testing of hypothesis about population mean")
            pop_mean = self.var_population_mean.get()
            sample_mean = self.var_sample_mean.get()
            SD = self.var_population_SD.get()
            n = self.var_sample_size.get()

            print("Hypothesis Testing Function")
            calc_z = (sample_mean - pop_mean) / (SD / math.sqrt(n))
            
        elif hypothesis_type == "std_dev":
            print("Testing of hypothesis about population standard deviation")
            pop_std = self.var_population_SD.get()
            sample_std = self.var_sample_std.get()
            n = self.var_sample_size.get()

            print("Hypothesis Testing Function")
            calc_z = ((sample_std - pop_std) / ((pop_std) / (math.sqrt(2 * n))))
            
        elif hypothesis_type == "mean_diff":
            print("Testing of hypothesis about difference between two means")
            sample_mean_1 = self.var_sample_mean_1.get()
            sample_std_1 = self.var_sample_std_1.get()
            sample_size_1 = self.var_sample_size_1.get()

            sample_mean_2 = self.var_sample_mean_2.get()
            sample_std_2 = self.var_sample_std_2.get()
            sample_size_2 = self.var_sample_size_2.get()

            print("Hypothesis Testing Function")
            calc_z = (sample_mean_1 - sample_mean_2) / (math.sqrt(((sample_std_1) ** 2 / sample_size_1) + (
                        (sample_std_2) ** 2 / sample_size_2)))
            
        elif hypothesis_type == "std_dev_diff":
            print("Testing of hypothesis about difference between two standard deviations")
            SD_1 = self.var_sample_std_1.get()
            SD_2 = self.var_sample_std_2.get()
            sample_1 = self.var_sample_size_1.get()
            sample_2 = self.var_sample_size_2.get()

            print("Hypothesis Testing Function")
            calc_z = (SD_1 - SD_2) / (math.sqrt(((SD_1 ** 2) / (2 * sample_1)) + ((SD_2 ** 2) / (2 * sample_2))))
            
        else:
            output_text = "Invalid hypothesis type selected."

        tab_z = self.table_z()
        if abs(tab_z) >= abs(calc_z):
            output_text = f"Hypothesis Test Result : \ncalc_z = {calc_z}\ntable_z = {tab_z}\nAccept H0"

        else:
            output_text = f"Hypothesis Test Result : \ncalc_z = {calc_z}\ntable_z = {tab_z}\nReject H0"

        
        print(" Display the results : ", output_text)
        self.output_label.config(text=output_text)
        self.output_label.grid(row=11, column=0, columnspan=2)




if __name__ == "__main__":
    root = tk.Tk()
    app = HypothesisTestingApp(root)
    root.mainloop()
