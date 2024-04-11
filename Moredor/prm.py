import binascii
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# ans = "01101011001011010"
# # ans = "011010110010110101100101101001011001010110010110100"
# y = len(ans)
# print(len(ans))
# byte_data = int(ans, 2).to_bytes((y + 7) // 8, byteorder='big')

# print(byte_data)
# # Decode bytes using UTF-8 encoding
# decoded_text = byte_data.decode('utf-8')
# print(decoded_text)
flag = "CSeC{"
bin_flag = flag.encode('utf-8')
hex_flag = binascii.hexlify(bin_flag)
int_flag = int(hex_flag, 16)
print(bin(int_flag)[2:])
digits = "100001101010011011001010100001101111011"
def extract_lsb(image_path):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Initialize an empty string to store the LSBs
    lsb_string = ""

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the pixel
            r, g, b = img.getpixel((x, y))

            # Extract the LSBs from the RGB values
            lsb_string += str(r & 1)
            lsb_string += str(g & 1)
            lsb_string += str(b & 1)

    return lsb_string


# Example usage
image_path = "moredor.png"
lsb_message = extract_lsb(image_path)
# print("Extracted LSB message:", lsb_message)
