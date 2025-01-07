import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image

class IconConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to ICO Converter")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.setup_theme()
        self.setup_ui()

    def setup_theme(self):
        """Set up the dark theme colors."""
        self.dark_bg = "#1e1e1e"  # Dark background
        self.dark_fg = "#ffffff"  # Light text
        self.button_bg = "#333333"  # Button background
        self.highlight_bg = "#444444"  # Slightly lighter background for contrast
        self.accent_color = "#5e9fff"  # Accent color for buttons

        self.root.configure(bg=self.dark_bg)

    def setup_ui(self):
        """Set up the user interface components."""
        # Title Label
        tk.Label(self.root, text="Image to ICO Converter", fg=self.dark_fg, bg=self.dark_bg, font=("Arial", 14, "bold")).pack(pady=10)

        # File selection
        self.input_path = tk.StringVar()
        tk.Label(self.root, text="Select Image(s):", fg=self.dark_fg, bg=self.dark_bg).pack()
        tk.Button(self.root, text="Choose Images", command=self.select_images, bg=self.accent_color, fg=self.dark_fg, relief="flat").pack(pady=5)
        tk.Label(self.root, textvariable=self.input_path, fg=self.dark_fg, bg=self.highlight_bg, wraplength=400).pack(pady=5, padx=10, fill="x")

        # Output selection
        self.output_path = tk.StringVar()
        tk.Label(self.root, text="Select Output Folder:", fg=self.dark_fg, bg=self.dark_bg).pack()
        tk.Button(self.root, text="Choose Folder", command=self.select_output_folder, bg=self.accent_color, fg=self.dark_fg, relief="flat").pack(pady=5)
        tk.Label(self.root, textvariable=self.output_path, fg=self.dark_fg, bg=self.highlight_bg, wraplength=400).pack(pady=5, padx=10, fill="x")

        # Icon size selection
        tk.Label(self.root, text="Select Icon Sizes:", fg=self.dark_fg, bg=self.dark_bg).pack(pady=5)
        self.size_vars = [tk.IntVar(value=1) for _ in range(5)]
        self.size_labels = ["16x16", "32x32", "48x48", "64x64", "128x128"]
        
        size_frame = tk.Frame(self.root, bg=self.dark_bg)
        size_frame.pack()
        for size_label, var in zip(self.size_labels, self.size_vars):
            tk.Checkbutton(size_frame, text=size_label, variable=var, fg=self.dark_fg, bg=self.dark_bg, selectcolor=self.dark_bg).pack(side="left", padx=5)

        # Convert button
        tk.Button(self.root, text="Convert to ICO", command=self.convert_to_ico, bg=self.accent_color, fg=self.dark_fg, relief="flat", font=("Arial", 12, "bold"), width=20).pack(pady=20)

    def select_images(self):
        """Allow user to select multiple image files."""
        files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if files:
            self.input_path.set("; ".join(files))

    def select_output_folder(self):
        """Allow user to select an output folder."""
        folder = filedialog.askdirectory()
        if folder:
            self.output_path.set(folder)

    def convert_to_ico(self):
        """Convert selected images to .ico format."""
        input_files = self.input_path.get().split("; ")
        output_folder = self.output_path.get()

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

        for input_file in input_files:
            try:
                img = Image.open(input_file).convert("RGBA")
                output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".ico")
                img.save(output_file, format="ICO", sizes=selected_sizes)
                messagebox.showinfo("Success", f"Icon file saved to {output_file}")

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = IconConverterApp(root)
    root.mainloop()
