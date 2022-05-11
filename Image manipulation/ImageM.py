#image manipulator
from PIL import Image, ImageFilter
import os

size_300 = (300,300)
size_700 = (700,700)


for f in os.listdir('.'):
    if f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splittext(f)

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn,fext))

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn,fext))

image1= Image.open("pic1.jpg")
image1.rotate(90).show("pic1.jpg")

image2 = Image.open("pic2.jpg")
image2.convert(mode = 'L').show("pic2.jpg")

image3 = Image.open("pic3.jpg")
image3.rotate(180).show("pic3.jpg")

image4 = Image.open("pic4.jpg")
image4.filter(ImageFilter.GaussianBlur(10)).show("pic4.jpg")

image5 = Image.open("pic5.jpg")
image5.convert(mode = 'L').show("pic5.jpg")

image6 = Image.open("pic6.jpg")
image6.rotate(20).show("pic6.jpg")

image7 = Image.open("pic7.jpg")
image7.filter(ImageFilter.GaussianBlur(15)).show("pic7.jpg")

image8 = Image.open("pic8.jpg")
image8.convert(mode = 'L').show("pic8.jpg")

image9 = Image.open("pic9.jpg")
image9.rotate(90).show(r'pics\ImageM.py\pic9.jpg')

image10 = Image.open("pic10.jpg")
image10 .show("pic10.jpg")

j_list = ['pic1', 'pic2', 'pic3','pic4', 'pic5', 'pic6','pic7', 'pic8', 'pic9', 'pic10']
a_list = ['rotate', 'resize', 'png', 'blur', 'black and white']
def display_list(x):
    for i in x:
        print(i)
    print('')
def run():
    while True:
        print ("Images: ")
        display_list(j_list)
        choice = input("Which image should we change?: ").lower()
        if choice in j_list:
            userImage = Image.open(f"{choice}.jpg")
            userImage.show()
            if userconfirm() == True:
                break
            else:
                print("Invalid Input\n")
        alterimage()

def userconfirm():
    choice = input ("Should we edit this image? (yes) or (no): ").lower()
    if choice == "yes":
        return True
    elif choice == 'no':
        print("")
        run()
    else:
        print('invalid input')

def alterimage():
    while True:
        print ("Alter options: ")
        display_list(a_list)
        choice = input('Select alter mode: ').lower()
        if choice in a_list:
            if userconfirm() == True:
                if choice == a_list[0]:
                    choice.rotate()
                if choice == a_list[1]:
                    choice.resize()
                if choice == a_list[2]:
                    choice.png()
                if choice == a_list[3]:
                    choice.blur()
                if choice == a_list[4]:
                    choice.blacknwhite()