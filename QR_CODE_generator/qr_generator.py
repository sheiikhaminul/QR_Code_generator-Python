import qrcode #for making qr
from qrcode.image.pil import PilImage #for get output in desired format
def user_input(filepath):
    url=input("give the text or URL you want to convert to QR : ")
    image_name=input("give the filename with which you want to save the QR : ")
    qr_back=input("give the color you want as the qr background : ")
    qr_front=input("give the color you want as the qr foreground : ")

    with open("file.txt","w") as file:
        file.write(f"{url}\n")
        file.write(f"{image_name}\n")
        file.write(f"{qr_back}\n")
        file.write(f"{qr_front}\n")
    print("requirement saved!!")

def qr_generator(filepath):
    with open("file.txt","r") as file:
        content=file.readlines()
    url=content[0].strip()
    image_name=content[1].strip()#remove spaces,tabs,newline from both ends(not inside)
    back_color=content[2].strip()
    front_color=content[3].strip()
    qr=qrcode.QRCode(  #qris object,QRcode is an class of qrcode python library(which we have imported)
        version=1, #refers size of QR ranging 1-40..1 means the smallest  
        error_correction=qrcode.constants.ERROR_CORRECT_H, #QR codes have built-in error correction.L- (7% error recovery), M- (15%), Q- (25%), H- (30%, highest error recovery means most robust).
        box_size=10, #Each box (or pixel block) in the QR will be 10x10 pixels in the final image.
        border=4, #Minimum border width (in boxes). So this means your QR will have a white border 4 boxes thick.
    
    )
    qr.add_data(url) #encode the URL to QR code
    qr.make(fit=True) #This line generates the QR code structure (layout of squares).fit=true automatically picks the smallest qr version to fits the data 

    image=qr.make_image( #make_image is a method provided by the qrcode library
        back_color=back_color, #color of the QR
        fill_color=front_color, #color of the bg
        image_factory=PilImage # PilImage tells the qrcode library to create the QR code as a regular image (PNG, JPG, etc.) using Pillow (PIL).
        ) #pilimage ta use na korle qrcode output ta as a txt or csv dito oita access korte prtam na tai pilImage is used
    image.save(image_name)
    print(f"qr save as {image_name}")
    
    # qr_code=qrcode.make(url)
    # qr_code.save(image_name)
user_input("file.txt")
qr_generator("file.txt") 
        
