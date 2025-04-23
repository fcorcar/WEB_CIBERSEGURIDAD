from mailjet_rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('MJ_API_KEY')
api_secret = os.getenv('MJ_API_SECRET')
email = os.getenv('EMAIL')

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

def enviar_correo(destinatario, nombre):
    data = {
      'Messages': [
        {
          "From": {
            "Email": email,
            "Name": "Ciberseguridad Noticias"
          },
          "To": [
            {
              "Email": destinatario,
              "Name": nombre
            }
          ],
          "Subject": "Gracias por suscribirte 🛡️",
          "TextPart": f"Hola {nombre}, gracias por unirte a nuestras noticias de ciberseguridad.",
          "HTMLPart": f"""
          <h3>¡Hola {nombre}!</h3>
          <p>Gracias por suscribirte a <b>nuestras noticias de ciberseguridad</b>.</p>
          <p>Te mantendremos informado con lo último en seguridad digital 🔐</p>
          <br><small>Si no te has suscrito, ignora este correo.</small>
          """
        }
      ]
    }

    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
