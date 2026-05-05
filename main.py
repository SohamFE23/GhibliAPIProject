API_KEY="AIzaSyACA8_-UBreH9T80cflvJ3GKzh0nQdiiu8"

from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO as bytesIo

client=genai.Client(api_key=API_KEY)

image_path=Image.open("vedu(2).jpg")
prompt="Convert the attached Image into Ghibli Style"

response =client.models._generate_content(
    model='gemini-2.0-flash-exp-image-generation',
    contents=[prompt, image_path],
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image']
    )

)
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image=Image.open(bytesIo(part.inline_data.data))
        image.save("Ghibli.jpg")
        image.show()
