import qrcode
from qrcode.image.pil import PilImage
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
    image_name=content[1].strip()
    back_color=content[2].strip()
    front_color=content[3].strip()
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    
    )
    qr.add_data(url)
    qr.make(fit=True)

    image=qr.make_image(
        back_color=back_color,
        fill_color=front_color,
        image_factory=PilImage
        )
    image.save(image_name)
    print(f"qr save as {image_name}")
    
    # qr_code=qrcode.make(url)
    # qr_code.save(image_name)
user_input("file.txt")
qr_generator("file.txt") 
        