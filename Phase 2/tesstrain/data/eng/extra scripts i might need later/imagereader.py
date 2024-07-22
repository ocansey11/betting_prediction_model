# # Install PyMuPDF using pip
# import subprocess
# subprocess.check_call(["pip", "install", "pytesseract"])

import pytesseract
from PIL import Image
import re
import pandas as pd


# Path to the image
image_path = './Betway Share a Bet long.png'

# Open the image file
img = Image.open(image_path)

# Use pytesseract to extract text
extracted_text = pytesseract.image_to_string(img)

print(extracted_text)





# def parse_betslip_text(text):
#     bet_data = []
#     # Split the text into lines
#     lines = text.split('\n')
    
#     for i in range(len(lines)):
#         line = lines[i].strip()
#         if "Matches" in line:
#             team_info = lines[i-1].strip()
#             match_info = line.split("Matches, ")
#             date_time = match_info[1].strip()
#             date, time = date_time.split(" - ")
            
#             prediction = lines[i+1].strip()
#             odds = prediction.split()[-1]
#             result_type = prediction.split()[-2]
            
#             home_team, away_team = team_info.split(" - ")
            
#             bet_data.append({
#                 'home_team': home_team,
#                 'away_team': away_team,
#                 'date': date,
#                 'time': time,
#                 'prediction': result_type,
#                 'odds': odds
#             })
    
#     return bet_data

# parsed_data = parse_betslip_text(extracted_text)

# # Convert to DataFrame
# bet_df = pd.DataFrame(parsed_data)
# print(bet_df)
