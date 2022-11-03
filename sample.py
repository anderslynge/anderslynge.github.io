from diffusers import StableDiffusionPipeline
import datetime

YOUR_TOKEN="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"

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", use_auth_token=YOUR_TOKEN)

prompt = "Viking in the style of Raphael"

image = pipe(prompt)["sample"][0]

saveName= prompt.replace(" ", "-")
image.save(f"" + saveName + str(datetime.datetime.now()).replace(":", "-") + ".png")
