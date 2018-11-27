from colorthief import ColorThief

color_thief = ColorThief('./1341543305665_.pic_hd.jpg')
# get the dominant color
dominant_color = color_thief.get_color(quality=100)
# build a color palette
palette = color_thief.get_palette(color_count=6)

print(dominant_color)

print(palette)
