# ProjectNM-TNSDC-cybersecurity

This Python code is a Tkinter GUI application that provides functionality for steganography, which is the practice of hiding secret messages within image files.
The application allows users to encode and decode secret messages within image files using steganography techniques. It provides a user-friendly interface for selecting image files, entering messages, and saving or viewing the encoded or decoded messages.

Here are the prerequisites for running this Tkinter GUI steganography application:

1. **Python**:
   - This application is written in Python, so you need to have Python installed on your system. The code should work with Python 3.x versions.

2. **Required Python Libraries**:
   - The application uses the following Python libraries, which need to be installed:
     - **Tkinter**: This is a standard Python library for creating graphical user interfaces (GUIs). It's typically pre-installed with most Python distributions.
     - **Pillow (PIL)**: This is a Python Imaging Library (PIL) that provides support for opening, manipulating, and saving images. You can install it using pip:

     ```
     pip install pillow
     ```

3. **Image Files**:
   - To use the application, you'll need image files that can be used for encoding and decoding secret messages. The code supports PNG image files, but you can modify it to work with other image formats supported by the Pillow library.


4. **Text Editor or Integrated Development Environment (IDE)**:
   - You'll need a text editor or an IDE to open and run the Python code. Popular options include IDLE (comes with Python), Visual Studio Code, PyCharm, Sublime Text, and others.

Once you have Python and the required libraries installed, you can save the provided code to a Python file (e.g., `steganography.py`) and run it from your text editor, IDE, or the command line.

For example, if you're using the command line, navigate to the directory where you saved the `steganography.py` file and run the following command:

```
python steganography.py
```

This should launch the Tkinter GUI application, and you can start using it to encode and decode secret messages within image files.

Here's a breakdown of the main components and functions in this code:

1. Encoding Text into an Image:

   - The `encode_text` function takes an image object and a secret text message as input.
   - It converts the text message into a binary string and then encodes the binary data into the least significant bits of the RGB pixel values of the image.
   - The function returns a new image object with the encoded message.

2. Decoding Text from an Image:

   - The `decode_text` function takes an image object as input.
   - It iterates over the image pixels and extracts the least significant bits from each color channel, reconstructing the binary data.
   - The binary data is then converted back into a text string, which represents the decoded message.

3. Encoding a Message:

   - The `encode_message` function is triggered when the "Encode Message" button is clicked.
   - It prompts the user to select an image file using a file dialog.
   - The user enters a secret message in the provided text box.
   - The function encodes the message into the selected image using `encode_text`.
   - The encoded image is then saved to a new file specified by the user.

4. Decoding a Message:

   - The `decode_message` function is triggered when the "Decode Message" button is clicked.
   - It prompts the user to select an encoded image file using a file dialog.
   - The function decodes the message from the selected image using `decode_text`.
   - The decoded message is displayed in a new window using a `Toplevel` widget and a `Text` widget.

5. Graphical User Interface (GUI):
   - The GUI is created using the Tkinter library.
   - It consists of a main window with a label, a text box for entering the secret message, and two buttons ("Encode Message" and "Decode Message").
   - There is also a label at the bottom of the window that displays status messages or error messages related to the encoding or decoding process.
