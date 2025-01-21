import asyncio
from random import randint
from PIL import Image
import requests
from pathlib import Path
from dotenv import load_dotenv
import os
from time import sleep

# Load environment variables
load_dotenv()
API_KEY = os.getenv("HuggingfaceAPIKey")
if not API_KEY:
    raise ValueError("Huggingface API Key is missing in the environment file.")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {API_KEY}"}

# Define paths
data_folder = Path("Data")
data_folder.mkdir(parents=True, exist_ok=True)
image_generation_file = Path("Frontend/Files/ImageGeneration.data")

async def query(payload):
    try:
        print(f"Sending payload: {payload}")
        response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)
        response.raise_for_status()
        print("API call successful")
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

async def generate_images(prompt: str):
    tasks = []
    for _ in range(4):
        payload = {
            "inputs": f"{prompt}, quality=4k, sharpness=maximum, Ultra High details, high resolution, seed={randint(0, 1000000)}"
        }
        tasks.append(asyncio.create_task(query(payload)))

    image_bytes_list = await asyncio.gather(*tasks)

    for i, image_bytes in enumerate(image_bytes_list):
        if image_bytes:
            file_path = data_folder / f"{prompt.replace(' ', '_')}{i+1}.jpg"
            print(f"Saving image: {file_path}")
            with file_path.open("wb") as f:
                f.write(image_bytes)

def open_images(prompt):
    prompt = prompt.replace(" ", "_")
    files = list(data_folder.glob(f"{prompt}*.jpg"))

    for image_path in files:
        try:
            img = Image.open(image_path)
            print(f"Opening Image: {image_path}")
            img.show()
            sleep(1)  # Optional delay
        except IOError:
            print(f"Unable to open {image_path}")

def GenerateImages(prompt: str):
    asyncio.run(generate_images(prompt))
    open_images(prompt)

# Main logic with debug logging
print("Starting the script...")
while True:
    try:
        if not image_generation_file.exists():
            print(f"File {image_generation_file} does not exist. Waiting...")
            sleep(1)
            continue

        with image_generation_file.open("r") as f:
            data = f.read().strip()
            print(f"Read from file: {data}")

        if not data:
            print("Data file is empty. Waiting...")
            sleep(1)
            continue

        prompt, status = data.split(",")
        print(f"Prompt: {prompt}, Status: {status}")

        if status == "True":
            print("Generating Images....")
            GenerateImages(prompt=prompt)

            with image_generation_file.open("w") as f:
                f.write("False,False")
            print("Image generation complete. Exiting loop.")
            break
        else:
            print("Waiting for the status to be True...")
            sleep(1)
    except Exception as e:
        print(f"Error occurred: {e}")
        sleep(1)
