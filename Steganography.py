import tkinter as tk
from tkinter import filedialog
from PIL import Image


def encode_text(image, text):
    # Convert text to binary
    binary_text = "".join(format(ord(char), "08b") for char in text)

    # Get image dimensions
    width, height = image.size

    # Create a copy of the image to modify
    encoded_image = image.copy()

    # Initialize pixel index
    index = 0

    # Iterate over image pixels and encode binary text
    for y in range(height):
        for x in range(width):
            # Get pixel value
            pixel = list(encoded_image.getpixel((x, y)))

            # Encode binary text into least significant bits
            for i in range(3):
                if index < len(binary_text):
                    pixel[i] = (pixel[i] & ~1) | int(binary_text[index])
                    index += 1

            # Update pixel value
            encoded_image.putpixel((x, y), tuple(pixel))

            # Stop encoding if all bits have been encoded
            if index >= len(binary_text):
                return encoded_image

    return encoded_image


def decode_text(image):
    # Get image dimensions
    width, height = image.size

    # Initialize binary text
    binary_text = ""

    # Iterate over image pixels and decode binary text
    for y in range(height):
        for x in range(width):
            # Get pixel value
            pixel = image.getpixel((x, y))

            # Extract least significant bits from each color channel
            for i in range(3):
                binary_text += str(pixel[i] & 1)

    # Convert binary text to string
    decoded_text = "".join(
        chr(int(binary_text[i : i + 8], 2)) for i in range(0, len(binary_text), 8)
    )

    return decoded_text


def encode_message():
    # Open image file
    image_file = filedialog.askopenfilename(title="Select Image File")
    if not image_file:
        return

    # Get secret message
    secret_message = message_entry.get("1.0", "end-1c")
    if not secret_message:
        message_label.config(text="Please enter a secret message.")
        return

    # Open image and encode message
    try:
        image = Image.open(image_file)
        encoded_image = encode_text(image, secret_message)
        save_file = filedialog.asksaveasfilename(
            defaultextension=".png", title="Save Encoded Image"
        )
        if save_file:
            encoded_image.save(save_file)
            message_label.config(text="Message encoded successfully!")
    except Exception as e:
        message_label.config(text=f"Error: {str(e)}")


def decode_message():
    # Open encoded image file
    image_file = filedialog.askopenfilename(title="Select Encoded Image File")
    if not image_file:
        return

    # Open image and decode message
    try:
        image = Image.open(image_file)
        decoded_text = decode_text(image)
        decoded_label = tk.Toplevel(root)
        decoded_label.title("Decoded Message")
        message_text = tk.Text(decoded_label, height=10, width=40)
        message_text.pack()
        message_text.insert("1.0", decoded_text)
    except Exception as e:
        message_label.config(text=f"Error: {str(e)}")


# Create Tkinter window
root = tk.Tk()
root.title("Steganography")

# Create GUI elements
message_label = tk.Label(root, text="Enter secret message:")
message_label.pack()

message_entry = tk.Text(root, height=5, width=40)
message_entry.pack()

encode_button = tk.Button(root, text="Encode Message", command=encode_message)
encode_button.pack()

decode_button = tk.Button(root, text="Decode Message", command=decode_message)
decode_button.pack()

message_label = tk.Label(root, text="")
message_label.pack()

# Run Tkinter event loop
root.mainloop()
