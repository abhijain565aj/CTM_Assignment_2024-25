
from stegano import lsb
import sys
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
message = lsb.reveal("moredor.png")
print(message)
