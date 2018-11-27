# from colorthief import ColorThief
from haishoku.haishoku import Haishoku
image = './1341543305665_.pic_hd.jpg'
# image = './1331543305664_.pic_hd.jpg'
dominant = Haishoku.getDominant(image)
print(dominant)
# Haishoku.showDominant( image )

palette = Haishoku.getPalette( image )
print(palette)
# Haishoku.showPalette( image )