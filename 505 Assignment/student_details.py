import tkinter as tk

class FruitGUI:
    def __init__(self, master):
        self.master = master
        self.fruit_list =['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grapefruit', 'honeydew', 'imbe', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla bean', 'watermelon', 'xigua (Chinese watermelon)', 'yellow passionfruit', 'zucchini', 'apricot', 'blueberry', 'cranberry', 'dragonfruit', 'elderflower', 'feijoa', 'grape', 'huckleberry', 'indian gooseberry', 'jujube']
        self.selected_fruit = tk.StringVar()
        self.selected_fruit.set(self.fruit_list[0])

        # Create the left frame for scrolling through the fruit list
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create the scrollbar and attach it to the left frame
        self.scrollbar = tk.Scrollbar(self.left_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the listbox and attach it to the left frame and scrollbar
        self.listbox = tk.Listbox(self.left_frame, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.config(command=self.listbox.yview)

        # Fill the listbox with fruits from the fruit list
        for fruit in self.fruit_list:
            self.listbox.insert(tk.END, fruit)

        # Bind a function to execute when a new selection is made in the listbox
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # Create the right frame for displaying the selected fruit
        self.right_frame = tk.Frame(self.master)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a label to display the selected fruit and attach it to the right frame
        self.selected_fruit_label = tk.Label(self.right_frame, textvariable=self.selected_fruit, font=("Arial", 20))
        self.selected_fruit_label.pack(padx=50, pady=50)

    def on_select(self, event):
        # Get the selected fruit from the listbox and update the label
        self.selected_fruit.set(self.listbox.get(self.listbox.curselection()))



#         =========================================
import tkinter as tk


class StudentInfoForm(tk.Frame):
    def __init__(self, master, on_submit=None):
        super().__init__(master)

        self.on_submit = on_submit

        # Create labels for input fields
        tk.Label(self, text="Name:").grid(row=0, column=0)
        tk.Label(self, text="Age:").grid(row=1, column=0)
        tk.Label(self, text="Course of Study:").grid(row=2, column=0)
        tk.Label(self, text="School:").grid(row=3, column=0)
        tk.Label(self, text="Days of Week:").grid(row=4, column=0)
        tk.Label(self, text="Sex Type:").grid(row=5, column=0)
        tk.Label(self, text="Favorite Programming Language:").grid(row=6, column=0)

        # Create input fields
        self.name_entry = tk.Entry(self)
        self.age_scale = tk.Scale(self, from_=16, to=100, orient=tk.HORIZONTAL)
        self.course_entry = tk.Entry(self)
        self.school_entry = tk.Entry(self)
        self.days_entry = tk.Entry(self)
        self.sex_var = tk.StringVar(value="Male")
        self.sex_male_radio = tk.Radiobutton(self, text="Male", variable=self.sex_var, value="Male")
        self.sex_female_radio = tk.Radiobutton(self, text="Female", variable=self.sex_var, value="Female")
        self.language_var = tk.StringVar(value="Python")
        self.language_checkbutton = tk.Checkbutton(self, text="Python", variable=self.language_var)

        # Add input fields to grid
        self.name_entry.grid(row=0, column=1)
        self.age_scale.grid(row=1, column=1)
        self.course_entry.grid(row=2, column=1)
        self.school_entry.grid(row=3, column=1)
        self.days_entry.grid(row=4, column=1)
        self.sex_male_radio.grid(row=5, column=1)
        self.sex_female_radio.grid(row=5, column=2)
        self.language_checkbutton.grid(row=6, column=1)

        # Create submit button
        tk.Button(self, text="Submit", command=self.show_info).grid(row=7, column=1, pady=10)

        # Create labels to display student information
        self.result_label_top = tk.Label(self, text="")
        self.result_label_bottom = tk.Label(self, text="")
        self.result_label_top.grid(row=8, columnspan=2, pady=10)
        self.result_label_bottom.grid(row=9, columnspan=2, pady=10)

    def show_info(self):
        # Get input field values
        name = self.name_entry.get()
        age = self.age_scale.get()
        course = self.course_entry.get()
        school = self.school_entry.get()
        days = self.days_entry.get()
        sex = self.sex_var.get()
        language = self.language_var.get()

        # Format student information string
        student_info = f"Name: {name}\nAge: {age}\nCourse of Study: {course}\nSchool: {school}\nDays of Week: {days}\nSex Type: {sex}\nFavorite Programming Language: {language}"

        # Display student information in result labels
        self.result_label_top.config(text=student_info)
        self.result_label_bottom.config(text=student_info)

        # Call the on_submit callback function if provided
        if self.on_submit is not None:
            self.on_submit(name, age, course, school, days, sex, language)

class MyGUI:
    def __init__(self, master):
        self.master = master

        # Create a label for the title
        tk.Label(self.master, text="Student Information Form", font=("Arial", 20)).pack(pady=20)

        # Create a student information form and attach it to the master frame
        self.student_info_form = StudentInfoForm(self.master, on_submit=self.handle_submit)
        self.student_info_form.pack()

    def handle_submit(self, name, age, course, school, days, sex, language):
        # Display the student information in the console
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Course of Study: {course}")
        print(f"School: {school}")
        print(f"Days of Week: {days}")
        print(f"Sex Type: {sex}")
        print(f"Favorite Programming Language: {language}")


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("My GUI")

# Create an instance of MyGUI
# my_gui = MyGUI(root)

# ======================================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fruit GUI")
    root.title("My GUI")

    # Create an instance of FruitGUI
    fruit_gui = FruitGUI(root)
    my_gui = MyGUI(root)

    # Run the GUI
    root.mainloop()

