from PIL import Image
import os

def simulate_tryon(user_image_path, outfit_image_name):
    try:
        person = Image.open(user_image_path).convert("RGBA")
        outfit_path = os.path.join("static", "outfits", outfit_image_name)
        shirt = Image.open(outfit_path).convert("RGBA")

        shirt_width = int(person.width * 0.55)
        scale_factor = shirt_width / shirt.width
        shirt_height = int(shirt.height * scale_factor)
        shirt = shirt.resize((shirt_width, shirt_height), Image.ANTIALIAS)

        x_offset = int((person.width - shirt_width) / 2)
        y_offset = int(person.height * 0.28)

        person.paste(shirt, (x_offset, y_offset), shirt)
        output_path = "static/tryon_results/tryon_result.png"
        person.save(output_path)

        return "/" + output_path
    except Exception as e:
        print(f"[TryOn Error] {e}")
        return None
