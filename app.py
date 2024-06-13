import requests as r
from PIL import Image
from io import BytesIO

response = r.get('https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
#print(response.status_code)
deck = response.json()
#print(deck)
deck_id = deck['deck_id']

response = r.get(f'https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1')
card = response.json()
print(card)

card_image_url = card['cards'][0]['image']
response = r.get(card_image_url)
img = Image.open(BytesIO(response.content))
img.show()