import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator="\n", strip=True)
        return text
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

def get_img_from_url(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        img = soup.img
        return img.get('src')
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"

url = "https://www.villageharvest.org/volunteer"
text = get_text_from_url(url)

from google import genai
def answer(q):
    client = genai.Client(api_key="AIzaSyB-zXA1y2ENhEhG6DJmfiVESqc4AnXD4YY")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=text+q
    )
    return response.text

#print(answer("\n" +"js tell me Name of Organization, WRITE NOTHING ELSE"))
#print(answer("what's the volunteer opportunity title for example Volunteer at Berkeley Art Center, only write the volunteer title nothing else"))
#print(url)
#print(get_img_from_url(url))
#print(answer("\n"+"position date (ie on calendar ie March 25-29, put ongoing if not clear, ONLY ANSWER THE QUESTION WRITE NOTHING ELSE"))
#print(answer("pls summarise in 5 well written sentences for potential volunteers as a description, an example for a different organization would be Abrahamic Alliance International is a charitable non-profit organization uniting Jews, Christians, and Muslims for active peacebuilding and poverty relief. AAi began with a simple dream that compassionate collaboration between Jews, Christians, and Muslims can build lasting bridges of understanding and respect between our communities. By uniting to serve the poor in obedience to divine commands, our grassroots movement is showing the world that peaceful coexistence between Jews, Christians, and Muslims is not a naive and distant dream, but a growing and present reality here and now."))
#print(answer("age requirement, if none, say none--do not put nothing Always put a + after whatever number if necessary Examples: 15+ 12+13-18, ONLY ANSWER ACCORDING TO EXAMPLE NO EXTRA TEXT"))
#print(answer("\n"+"skill requirements, put none if there's none but never leave blank Possible skill requirements: Experienced with Adobe Design, Familiar Working with Children, etc. ONLY ANSWER ACCORDING TO EXAMPLE NO EXTRA TEXT"))
#print(answer("If its in-person ANSWER THE ADDRESS AND NOTHING ELSE otherwise write 'virtual' AND NOTHING ELSE thx"))
#print(answer("\n"+"Whats the training need, if none answer ONLY 'none' and WRITE NOTHING ELSE, otherwise write the training need and NOTHING ELSE"))
#print(answer("Which of these passion areas does it fit best? Government Arts and Culture Faith-Based Economic Animal Welfare Community Building Youth Services Environmental"+"\n"+"To answer write the multiple that u think fit comma seperated ie 'Government, Community Building, Youth Services' WRITE NOTHING ELSE"))

import pyperclip

# Assume these functions work as intended
# answer(prompt), get_img_from_url(url), url is a variable already defined

row = [
    answer("\n" + "js tell me Name of Organization, WRITE NOTHING ELSE"),
    answer(
        "what's the volunteer opportunity title for example Volunteer at Berkeley Art Center, only write the volunteer title nothing else"),
    url,
    get_img_from_url(url),
    answer(
        "\n" + "position date (ie on calendar ie March 25-29, put ongoing if not clear, ONLY ANSWER THE QUESTION WRITE NOTHING ELSE"),
    answer(
        "pls summarise in 5 well written sentences for potential volunteers as a description, an example for a different organization would be Abrahamic Alliance International is a charitable non-profit organization uniting Jews, Christians, and Muslims for active peacebuilding and poverty relief. AAi began with a simple dream that compassionate collaboration between Jews, Christians, and Muslims can build lasting bridges of understanding and respect between our communities. By uniting to serve the poor in obedience to divine commands, our grassroots movement is showing the world that peaceful coexistence between Jews, Christians, and Muslims is not a naive and distant dream, but a growing and present reality here and now."),
    answer(
        "age requirement, if none, say none--do not put nothing Always put a + after whatever number if necessary Examples: 15+ 12+13-18, ONLY ANSWER ACCORDING TO EXAMPLE NO EXTRA TEXT"),
    answer(
        "\n" + "skill requirements, put none if there's none but never leave blank Possible skill requirements: Experienced with Adobe Design, Familiar Working with Children, etc. ONLY ANSWER ACCORDING TO EXAMPLE NO EXTRA TEXT"),
    answer("If its in-person ANSWER THE ADDRESS AND NOTHING ELSE otherwise write 'virtual' AND NOTHING ELSE thx"),
    answer(
        "\n" + "Whats the training need, if none answer ONLY 'none' and WRITE NOTHING ELSE, otherwise write the training need and NOTHING ELSE"),
    answer(
        "Which of these passion areas does it fit best? Government Arts and Culture Faith-Based Economic Animal Welfare Community Building Youth Services Environmental" + "\n" + "To answer write the multiple that u think fit comma seperated ie 'Government, Community Building, Youth Services' WRITE NOTHING ELSE")
]

def clean(t):
    return t.replace('\n', ' ').replace('\r', ' ').strip()

for i in range(len(row)):
    row[i] = clean(row[i])

    # Format as tab-separated string for pasting into Google Sheets
tsv_row = "\t".join(row)

# Copy to clipboard
pyperclip.copy(tsv_row)

print("Row copied to clipboard!")
