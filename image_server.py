import os
import uuid
from pathlib import Path
from fastmcp import FastMCP
from google import genai
from google.genai import types

# Match the exact working structure of time_server.py
mcp = FastMCP("life-ops-image")

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "generated_images"
IMAGE_DIR.mkdir(exist_ok=True)

@mcp.tool()
def generate_image(prompt: str, style: str | None = None) -> dict:
    """Generate an image from a prompt and save it locally."""
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    full_prompt = prompt
    if style:
        full_prompt = f"{prompt}. Style: {style}"
    response = client.models.generate_images(model="imagen-3.0-generate-001", prompt=full_prompt, config=types.GenerateImagesConfig(number_of_images=1))
    filename = f"{uuid.uuid4()}.png"
    image_path = IMAGE_DIR / filename
    response.generated_images[0].image.save(image_path)
    return {"image_path": str(image_path), "description": f"Image generated for prompt: {prompt}"}

if __name__ == "__main__":
    mcp.run(show_banner=False)
