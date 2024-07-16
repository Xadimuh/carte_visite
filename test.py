import qrcode
import base64
from PIL import Image
from io import BytesIO

# Réduire la taille de l'image et convertir en mode RGB
image = Image.open("photo.png")
image = image.resize((50, 50)).convert('RGB')  # Redimensionner et convertir en mode RGB
buffered = BytesIO()
image.save(buffered, format="JPEG")
encoded_string = base64.b64encode(buffered.getvalue()).decode('utf-8')

# Définir les informations de votre vCard avec l'URL incluse
vcard = f"""BEGIN:VCARD
VERSION:3.0
N:G.;Khadim;;;
FN:Khadim G.
ORG:VotreEntreprise
TITLE:Co-founder | fullstack developer | Système embarqué | IoT | Data analyst
TEL;TYPE=WORK,VOICE:0769965230
EMAIL:kgueye.dev@gmail.com
ADR;TYPE=WORK:;;Montbéliard;Bourgogne-Franche-Comté;;France
URL:http://www.khadimg.com
PHOTO;ENCODING=b;TYPE=JPEG:{encoded_string}
END:VCARD"""

# Créez l'objet QRCode
qr = qrcode.QRCode(
    version=None,  # Laissez la bibliothèque choisir la meilleure version
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Ajoutez les données
qr.add_data(vcard)
qr.make(fit=True)

# Générez l'image du code QR
img = qr.make_image(fill_color="black", back_color="white")

# Sauvegardez l'image
img.save("carte_de_visite_qr.png")
