from PIL import Image
image_url = '/Users/huangrenming/Desktop/IMG_0634.jpeg'

char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    length = len(char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    unint = 256/length
    return char[int(gray/unint)]

if __name__ == "__main__":
    im = Image.open(image_url)
    w,h = im.size
    p = w/h
    im = im.resize((int(100*p),100),Image.NEAREST)
    text =''
    for i in range(100):
        for j in range(int(100*p)):
            text+=get_char(*im.getpixel((j,i)))
        text+= '\n'
    print(text)
    with open ('/Users/huangrenming/Desktop/out.txt','wb') as file:
        file.write(text.encode('utf-8'))

