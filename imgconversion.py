from PIL import Image

def conversion(input_file, output_file):
    try:
        with Image.open(input_file) as img:
            img.save(output_file, "PNG")
        print("Conversion successful.")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

input_file = "logo.jpg"
output_file = "logo_converted.png"

conversion(input_file, output_file)
