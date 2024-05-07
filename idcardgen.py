import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
import os # Import os module for file operations

# Load employee data from CSV
employee_data = pd.read_csv('employee_data.csv')

# Function to create ID card
def create_id_card(template_path, photo_path, name, title):
    # Open the template image
    id_card = Image.open(template_path)
    draw = ImageDraw.Draw(id_card)
    
    # Load font - adjust path and size as needed
    font1 = ImageFont.truetype('arial.ttf', 24)
    font2 = ImageFont.truetype('arial.ttf', 18)
    
    # Swap places of titles and names
    draw.text((215, 166), title.title(), fill=(255, 100, 0), font=font2) # Title
    draw.text((75, 200), name.title(), fill=(255, 255, 255), font=font1) # Name
    
    # Open employee photo and convert to RGB
    photo = Image.open(photo_path).convert("RGB")
    
    # Define the target size and position for the photo
    target_width, target_height = 150, 150
    target_x, target_y = id_card.width - target_width - 33, 14 # Adjust the x and y position as needed
    
    # Resize the photo to fit the target size
    photo.thumbnail((target_width, target_height))
    
    # Paste photo onto template at the target position
    id_card.paste(photo, (target_x, target_y))
    
    # Convert to RGB mode before saving as JPEG
    id_card = id_card.convert("RGB")
    
    return id_card

# Create PDF with one ID per page using reportlab
c = canvas.Canvas("employee_ids.pdf")

# Assuming A4 page size (595 x 842 points)
page_width, page_height = 595, 842

# Desired ID card size (increase as needed)
id_card_width, id_card_height = 200, 120

for index, row in employee_data.iterrows():
    # Use a unique temporary file name for each employee
    temp_img_path = f'temp_img_{index}.jpg'
    create_id_card('ID_Card_Template.png', row['Photo_Location'], row['Name'], row['Title']).save(temp_img_path)
    
    # Calculate the center position for the ID card
    x = (page_width - id_card_width) / 2
    y = (page_height - id_card_height) / 2
    
    c.drawImage(temp_img_path, x, y, width=id_card_width, height=id_card_height) # Adjust size if necessary
    c.showPage() # Add a new page for the next ID card
    
    # Delete the temporary image file after it has been used
    if os.path.exists(temp_img_path):
        os.remove(temp_img_path)

c.save()

print("Employee ID cards generated successfully!")
