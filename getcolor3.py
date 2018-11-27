from palletize import extract_dominant_colors
# image = './1341543305665_.pic_hd.jpg'
image = './1331543305664_.pic_hd.jpg'

color = extract_dominant_colors(image, count=3, clusters=None, iterations=30, resize_to=300)
print(color)
