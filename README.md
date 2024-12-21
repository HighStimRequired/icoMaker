# icoMaker

icoMaker is a simple, GUI-based Python application that converts standard image formats (e.g., PNG, JPEG, BMP) into `.ico` files suitable for use as icons in Windows. Users can select their desired image, specify output folder location, and choose from multiple icon sizes to generate a versatile `.ico` file.

---

## Features
- **GUI Interface**: Easy-to-use interface built with `tkinter`.
- **Multiple Image Formats**: Supports `.png`, `.jpg`, `.jpeg`, `.bmp`.
- **Customizable Icon Sizes**: Select from 16x16, 32x32, 48x48, 64x64, or 128x128.
- **Dark Mode**: Modern dark-themed design for improved aesthetics.

---

## Requirements
- **Python 3.x**
- **Pillow** library for image processing

Install dependencies using:
```bash
pip install pillow
```

---

## How to Use
1. Clone or download the repository.
2. Run the setup.bat script
3. Run the run.bat script OR
   Run the script:
   ```bash
   python icoMaker.py
   ```
5. Follow these steps in the GUI:
   - Click "Choose Image" to select an image file.
   - Click "Choose Folder" to specify the output directory.
   - Select the desired icon sizes using the checkboxes.
   - Click "Convert to ICO" to generate the `.ico` file.
6. The application will notify you when the conversion is successful.

---

## Notes
- The input image must be in `.png`, `.jpg`, `.jpeg`, or `.bmp` format.
- Ensure you have write permissions for the selected output folder.
- Error messages will appear if invalid inputs or selections are made.

---

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it.

---

## Contribution
Feel free to contribute or do whatever you want with it!

---

### Author
Built with ❤️ by [Pickle](https://github.com/HighStimRequired) and powered by Python.
