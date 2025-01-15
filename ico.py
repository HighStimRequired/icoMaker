import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog, messagebox
from PIL import Image, ImageFont  # ImageFont to verify font file

class IconConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("icoMaker")
        self.root.geometry("440x330")
        self.root.resizable(False, False)

        self.setup_theme()  # Load theme and fonts
        self.setup_ui()     # Set up UI components

    def setup_theme(self):
        """Set up the theme colors and load a custom font."""
        self.dark_bg = "#09000f"      # Main background
        self.dark_fg = "#ffffff"      # Text color
        self.input_bg = "#6b4a5e"     # Input field background
        self.input_fg = "#ffffff"     # Input text color
        self.accent_color = "#6b4a5e" # Button color
        self.check_bg = "#2c1e2e"     # Checkbox background when selected
        self.check_fg = "#ffffff"     # Check mark color
        self.root.configure(bg=self.dark_bg)

        # 🎨 Load Custom Font (or fallback to Arial)
        font_path = "Roboto-Black.ttf"  # Adjust the path if needed
        if self.register_custom_font(font_path):
            self.custom_font = tkFont.Font(family="Roboto-Black.ttf", size=12)
        else:
            self.custom_font = tkFont.Font(family="Arial", size=12)  # Fallback

        # ✅ Apply the custom font globally
        self.root.option_add("*Font", self.custom_font)

    def register_custom_font(self, font_path):
        """Verify and load a custom font."""
        try:
            ImageFont.truetype(font_path, 12)  # Test font availability
            return True
        except:
            print(f"⚠️ Warning: Could not load {font_path}, using default font.")
            return False

    def setup_ui(self):
        """Set up the user interface components."""
        button_font = tkFont.Font(family="Arial", size=12, weight="bold")  # Button font remains separate

        tk.Label(self.root, text="", fg=self.dark_fg, bg=self.dark_bg, font=self.custom_font).pack(pady=0)

        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()

        button_width = 13

        tk.Button(self.root, text="Choose Images", command=self.select_images, 
                  bg=self.accent_color, fg=self.dark_fg, width=button_width, 
                  font=button_font).pack(pady=1)
        tk.Label(self.root, textvariable=self.input_path, fg=self.dark_fg, 
                 bg=self.dark_bg, wraplength=400).pack(pady=1)

        tk.Button(self.root, text="Choose Folder", command=self.select_output_folder, 
                  bg=self.accent_color, fg=self.dark_fg, width=button_width, 
                  font=button_font).pack(pady=1)
        tk.Label(self.root, textvariable=self.output_path, fg=self.dark_fg, 
                 bg=self.dark_bg, wraplength=400).pack(pady=1)

        self.filename_var = tk.StringVar()
        tk.Label(self.root, text="Output File Name (optional):", fg=self.dark_fg, 
                 bg=self.dark_bg).pack()
        tk.Entry(self.root, textvariable=self.filename_var, width=30, 
                 bg=self.input_bg, fg=self.input_fg, insertbackground=self.input_fg).pack(pady=10)

        self.size_vars = [tk.IntVar(value=1) for _ in range(5)]
        self.size_labels = ["16x16", "32x32", "48x48", "64x64", "128x128"]
        size_frame = tk.Frame(self.root, bg=self.dark_bg)
        size_frame.pack()

        for size_label, var in zip(self.size_labels, self.size_vars):
            tk.Checkbutton(size_frame, text=size_label, variable=var, 
                           fg=self.dark_fg, bg=self.dark_bg, 
                           selectcolor=self.check_bg, activebackground=self.check_bg, 
                           activeforeground=self.check_fg).pack(side="left", padx=5)
               
        tk.Label(self.root, text="", fg=self.dark_fg, bg=self.dark_bg, font=self.custom_font).pack(pady=1)

        self.convert_button = tk.Button(self.root, text="Convert to .ico", command=self.convert_to_ico, 
                                        bg=self.accent_color, fg=self.dark_fg, 
                                        font=("Arial", 12, "bold"), width=20)
        self.convert_button.pack(pady=5)

        tk.Label(self.root, text="", fg=self.dark_fg, bg=self.dark_bg, font=self.custom_font).pack(pady=1)

    def select_images(self):
        files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.webp;*.tiff")])
        if files:
            self.input_path.set("; ".join(files))

    def select_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_path.set(folder)

    def convert_to_ico(self):
        input_files = self.input_path.get().split("; ")
        output_folder = self.output_path.get()
        output_filename = self.filename_var.get()

        if not input_files or not input_files[0]:
            messagebox.showerror("Error", "Please select an image file.")
            return
        if not output_folder:
            messagebox.showerror("Error", "Please select an output folder.")
            return

        selected_sizes = [size for size, var in zip([(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)], self.size_vars) if var.get() == 1]
        if not selected_sizes:
            messagebox.showerror("Error", "Please select at least one icon size.")
            return

        self.convert_button.config(state=tk.DISABLED)

        for input_file in input_files:
            try:
                img = Image.open(input_file).convert("RGBA")
                available_sizes = [s for s in selected_sizes if s[0] <= img.size[0] and s[1] <= img.size[1]]
                if not available_sizes:
                    available_sizes = [(16, 16)]
                if output_filename:
                    output_file = os.path.join(output_folder, output_filename + ".ico")
                else:
                    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".ico")
                img.save(output_file, format="ICO", sizes=available_sizes)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        self.convert_button.config(state=tk.NORMAL)
        messagebox.showinfo("Success", "All images converted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = IconConverterApp(root)
    root.mainloop()
