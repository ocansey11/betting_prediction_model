# Install PyMuPDF using pip

import subprocess
subprocess.check_call(["pip", "install", "PyMuPDF"])

import re
import pandas as pd
import pymupdf as fitz


filename ='Betway Share a Bet'
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_betslip_text(text):
    bet_data = []
    # Split the text into lines
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if "Total Odds:" in line:
            total_odds = float(line.split(':')[1].strip())
        elif "Wager Amount:" in line:
            wager_amount = lines[i].split(':')[1].strip()
        elif "Potential Return:" in line:
            potential_return = lines[i].split(':')[1].strip()
        elif "Actual Return:" in line:
            actual_return = lines[i].split(':')[1].strip()
        elif "Multibet" in line:
            i += 1  # Skip the "Multibet" line
            while i < len(lines) and lines[i].strip() != "":
                if "1X2" in lines[i]:
                    # Extract the match data
                    match_info = lines[i-1].strip()
                    prediction_info = lines[i].strip()
                    
                    # Parse match data
                    home_team, away_team = match_info.split(' - ')
                    odds = prediction_info.split()[-1]
                    prediction = prediction_info.split()[-2]
                    
                    # Move to the next line to get the match date and time
                    i += 1
                    date_time = lines[i].split(", ")
                    date = date_time[1].split(" ")[0]
                    time = date_time[1].split(" ")[1]
                    
                    # Append parsed data
                    bet_data.append({
                        'home_team': home_team,
                        'away_team': away_team,
                        'date': date,
                        'time': time,
                        'prediction': prediction,
                        'odds': odds,
                        'total_odds': total_odds,
                        'wager_amount': wager_amount,
                        'potential_return': potential_return,
                        'actual_return': actual_return
                    })
                i += 1
        i += 1
    
    return bet_data

def extract_text_with_color(filename):
    doc = fitz.open(filename)
    text_with_color = []
    
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"]
                        color = span["color"]
                        text_with_color.append((text, color))
    return text_with_color

# Example usage
pdf_path = './Betway Share a Bet.pdf'
text_with_color = extract_text_with_color(pdf_path)
print(text_with_color)

# Path to your PDF file
pdf_path = './Betway Share a Bet.pdf'

# Extract text from the PDF
text = extract_text_from_pdf(pdf_path)

# Parse the extracted text
bet_data = parse_betslip_text(text)

# Convert to DataFrame
bet_df = pd.DataFrame(bet_data)
print(bet_df)

