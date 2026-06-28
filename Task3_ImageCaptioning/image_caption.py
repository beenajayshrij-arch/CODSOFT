import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from transformers.utils import logging
logging.set_verbosity_error()

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image

# Load model
model = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

feature_extractor = ViTImageProcessor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

tokenizer = AutoTokenizer.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)

# Function to generate caption
def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")

    pixel_values = feature_extractor(
        images=image,
        return_tensors="pt"
    ).pixel_values

    output_ids = model.generate(
        pixel_values,
        max_length=30,
        num_beams=4
    )

    caption = tokenizer.decode(
        output_ids[0],
        skip_special_tokens=True
    )

    print("\n==================================================")
    print("Image:", image_path)
    print("Caption:", caption)


# Run for all images
images = ["dog.jpg", "car.jpg", "dino.jpg"]

for img in images:
    generate_caption(img)