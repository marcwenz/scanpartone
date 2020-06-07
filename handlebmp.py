from PIL import Image

if __name__ == "__main__":
    ii = Image.open("1.bmp")
    ii.save("tt.tif")
