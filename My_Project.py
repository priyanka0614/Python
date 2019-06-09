from PIL import Image,ImageDraw,ImageFont #importing  libraries
import sys

#creating an image
img = Image.new('RGB',(350,200),color = 'white')


vk = Image.open("Mask.jpg").convert('RGBA')
img.paste(vk,(100,40),vk)

#Initialising a Font 
fnt = ImageFont.truetype("arial.ttf",14) 

#passing img to the Draw method
d = ImageDraw.Draw(img)




#Displaying Name Field
d.text((20,50),"NAME:",font = fnt,fill=(0,0,0,0))
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\tID CARD GENERATOR WITH LIVE PHOTOGRAPH AND QR CODE")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t\t\tFILL THE FIELDS IN CAPITAL LETTERS")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#Taking Name from user
name =  input("Enter Your Name:")
if all(x.isalpha() or x.isspace() for x in name):
    #Pasting name to the Image
    d.text((70,50),name,font = fnt,fill=(0,0,0,0))
else:
    print("Enter valid name!")
    sys.exit()


#Displaying BRANCH Field
d.text((20,80),"BRANCH:",font = fnt,fill=(0,0,0,0))
#Taking BRACH from user
branch =  input("Enter Your Branch:")
if(len(branch) == 3 or len(branch)== 4 and branch.isalpha()):
    #Pasting BRANCH to the Image
    d.text((85,80),branch,font = fnt,fill=(0,0,0,0))
else:
    print("Enter valid Branch code!")
    sys.exit()



#Displaying IDNO Field
d.text((20,110),"ID NO:",font = fnt,fill=(0,0,0,0))
y=0
year = int(input("Enter current studying year(1/2/3/4):"))
if(year==1):
    y=18
elif(year==2):
    y=17
elif(year==3):
    y=16
elif(year==4):
    y=15
else:
    print("Enter valid year(1-4)!")
    sys.exit()


import random
no=random.randint(1,99)
if(branch=="CSE"):
    b=5
if(branch=="ECE"):
    b=4
if(branch=="EEE"):
    b=3
if(branch=="MECH"):
    b=2
if(no == 1 or no == 2 or no == 3 or no == 4 or no == 5 or no == 6 or no == 7 or no == 8 or no == 9):
    f=0
    d.text((70,110),"{}KD1A0{}{}{}".format(y,b,f,no),font = fnt,fill=(0,0,0,0))
else:
    d.text((70,110),"{}KD1A0{}{}".format(y,b,no),font = fnt,fill=(0,0,0,0))

#Displaying DOB Field
d.text((20,140),"D.O.B:",font = fnt,fill=(0,0,0,0))
#Taking DOB from user

dob =  input("Enter Your D.O.B(DD-MM-YYYY):")


#Pasting DOB to the Image
d.text((70,140),dob,font = fnt,fill=(0,0,0,0))

#Displaying PHNO Field
d.text((20,170),"PH NO:",font = fnt,fill=(0,0,0,0))
#Taking PHNO from user
phno =input("Enter Your 10 digit Phone Number:")
if(len(phno) == 10):
    #Pasting PHNO to the Image
    d.text((70,170),phno,font = fnt,fill=(0,0,0,0))
else:
    print("Invalid phone number!")
    sys.exit()


try:
    img2 = Image.open("College logo.png")
    img.paste(img2,(0,0))
except IOError:
    pass


import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('Q'):
        out = cv2.imwrite("captured.jpg", frame)
        break
cap.release()
cv2.destroyAllWindows()

open1 = cv2.imread("captured.jpg")
resized = cv2.resize(open1,(75,75))
cv2.imwrite("resized.jpg",resized)

try:
    cam = Image.open("resized.jpg")
    img.paste(cam,(245,50))
except IOError:
    pass





import qrcode
# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size =1.90,
    border = 0,
)

# The data that you want to store
data = "The Data that you need to store in the QR Code"

# Add data
qr.add_data(name)
qr.add_data(dob)
qr.add_data(branch)
qr.add_data(phno)
qr.add_data("{}KD1A0{}{}".format(y,b,no))
qr.make(fit=True)

# Create an image from the QR Code instance
img3 = qr.make_image()
try:
    img.paste(img3,(275,140))
except IOError:
    pass
img.save(str(name)+"."+"png")
print("YOUR ID CARD HAS BEEN GENERATED SUCCESSFULLY, CHECK YOUR DIRECTORY FOR FURTHER INFORMATION!")
