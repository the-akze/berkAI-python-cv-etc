from google import genai
from google.genai import types
import base64
from os import getenv

systemprompt = ""

with open("./systemprompt.txt", "r") as systemprompt_file:
  systemprompt = systemprompt_file.read()

def generate_response_from_image(b64img, img_ext="png"):
  client = genai.Client(
      vertexai=True,
      project=getenv("GOOGLE_AI_PROJECT_NAME"),
      location="us-central1",
  )

  image1 = types.Part.from_bytes(
      data=base64.b64decode(b64img),
      mime_type="image/" + img_ext,
  )

  si_text1 = systemprompt

  model = "gemini-2.5-flash"
  contents = [
    types.Content(
      role="user",
      parts=[
        image1,
        types.Part.from_text(text="Describe the scene and any relevant updates, if applicable.")
      ]
    )
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 1,
    top_p = 1,
    seed = 0,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    system_instruction=[types.Part.from_text(text=si_text1)],
    thinking_config=types.ThinkingConfig(
      thinking_budget=-1,
    ),
  )

  for chunk in client.models.generate_content_stream(
    model = model,
    contents = contents,
    config = generate_content_config,
    ):

    return chunk.text

if __name__ == "__main__":
    from time import sleep
    import base64

    img1data = ""
    img2data = ""
    img3data = ""

    with open("test1.png", "rb") as test_img1:
      img_data = test_img1.read()
      img1data = base64.b64encode(img_data)

    with open("test2.png", "rb") as test_img2:
      img_data = test_img2.read()
      img2data = base64.b64encode(img_data)

    with open("test3.png", "rb") as test_img3:
      img_data = test_img3.read()
      img3data = base64.b64encode(img_data)

    generate_response_from_image(img1data)
    print("\ngenerated 1\n")
    sleep(3)

    generate_response_from_image(img2data)
    print("\ngenerated 2\n")
    sleep(3)

    generate_response_from_image(img3data)
    print("\ngenerated 3\n")
    sleep(3)