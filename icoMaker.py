import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, StringVar, Checkbutton, IntVar
from PIL import Image

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        input_path.set(file_path)

def select_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_path.set(folder)

def convert_to_ico():
    input_file = input_path.get()
    output_folder = output_path.get()

    if not input_file:
        messagebox.showerror("Error", "Please select an image file.")
        return

    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder.")
        return

    try:
        # Open the image file
        img = Image.open(input_file)

        # Ensure the image is in RGBA mode
        img = img.convert("RGBA")

        # Create a list of sizes for the .ico file
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]

        # Filter sizes based on user selection
        selected_sizes = [size for size, var in zip(sizes, size_vars) if var.get() == 1]

        if not selected_sizes:
            messagebox.showerror("Error", "Please select at least one icon size.")
            return

        # Generate the .ico file
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".ico")
        img.save(output_file, format="ICO", sizes=selected_sizes)

        messagebox.showinfo("Success", f"Icon file saved to {output_file}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create GUI
app = Tk()
app.title("Image to ICO Converter")
app.geometry("500x400")

input_path = StringVar()
output_path = StringVar()

# Icon sizes selection
size_vars = [IntVar(value=1) for _ in range(5)]
size_labels = ["16x16", "32x32", "48x48", "64x64", "128x128"]

Label(app, text="Select Image:").pack(pady=5)
Button(app, text="Choose Image", command=select_image).pack(pady=5)
Label(app, textvariable=input_path).pack(pady=5)

Label(app, text="Select Output Folder:").pack(pady=5)
Button(app, text="Choose Folder", command=select_output_folder).pack(pady=5)
Label(app, textvariable=output_path).pack(pady=5)

Label(app, text="Select Icon Sizes:").pack(pady=5)
for size_label, var in zip(size_labels, size_vars):
    Checkbutton(app, text=size_label, variable=var).pack(anchor="w", padx=20)

Button(app, text="Convert to ICO", command=convert_to_ico).pack(pady=20)

app.mainloop()
