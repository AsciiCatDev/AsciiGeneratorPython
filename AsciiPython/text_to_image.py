# this code converts the ascii strings to a actual png image
# this code was adapted by the Ascii Cats devs from the orginal which was created by user wrongu and can be found here: https://gist.github.com/wrongu/10670571

from PIL import Image
import numpy as np
import cv2 as cv

class TextToPixel:
	font_file = "img/InvertedFont8x8.png" # change this to font-8x8.png if you want a white background with black text 
	font_img = Image.open(font_file)

	# map from character to zero-indexed (x,y) index.
	glyphs = {
		'!' : (1, 2),
		'#' : (3, 2),
		'$' : (4, 2),
		'%' : (5, 2),
		'&' : (6, 2),
		'(' : (8, 2),
		')' : (9, 2),
		'*' : (10, 2),
		'+' : (11, 2),
		',' : (12, 2),
		'-' : (13, 2),
		'.' : (14, 2),
		'/' : (15, 2),
		'0' : (0, 3),
		'1' : (1, 3),
		'2' : (2, 3),
		'3' : (3, 3),
		'4' : (4, 3),
		'5' : (5, 3),
		'6' : (6, 3),
		'7' : (7, 3),
		'8' : (8, 3),
		'9' : (9, 3),
		':' : (10, 3),
		';' : (11, 3),
		'<' : (12, 3),
		'=' : (13, 3),
		'>' : (14, 3),
		'?' : (15, 3),
		'@' : (0, 4),
		'A' : (1, 4),
		'B' : (2, 4),
		'C' : (3, 4),
		'D' : (4, 4),
		'E' : (5, 4),
		'F' : (6, 4),
		'G' : (7, 4),
		'H' : (8, 4),
		'I' : (9, 4),
		'J' : (10, 4),
		'K' : (11, 4),
		'L' : (12, 4),
		'M' : (13, 4),
		'N' : (14, 4),
		'O' : (15, 4),
		'P' : (0, 5),
		'Q' : (1, 5),
		'R' : (2, 5),
		'S' : (3, 5),
		'T' : (4, 5),
		'U' : (5, 5),
		'V' : (6, 5),
		'W' : (7, 5),
		'X' : (8, 5),
		'Y' : (9, 5),
		'Z' : (10, 5),
		'[' : (11, 5),
		'\\' : (12, 5),
		']' : (13, 5),
		'^' : (14, 5),
		'_' : (15, 5),
		'`' : (0, 6),
		'a' : (1, 6),
		'b' : (2, 6),
		'c' : (3, 6),
		'd' : (4, 6),
		'e' : (5, 6),
		'f' : (6, 6),
		'g' : (7, 6),
		'h' : (8, 6),
		'i' : (9, 6),
		'j' : (10, 6),
		'k' : (11, 6),
		'l' : (12, 6),
		'm' : (13, 6),
		'n' : (14, 6),
		'o' : (15, 6),
		'p' : (0, 7),
		'q' : (1, 7),
		'r' : (2, 7),
		's' : (3, 7),
		't' : (4, 7),
		'u' : (5, 7),
		'v' : (6, 7),
		'w' : (7, 7),
		'x' : (8, 7),
		'y' : (9, 7),
		'z' : (10, 7),
		'{' : (11, 7),
		'|' : (12, 7),
		'}' : (13, 7),
		'~' : (14, 7),
		' ' : (15, 7),
	}

	def bbox(self, row, col):
		# 8x8 glyphs
		# left, top, right, bottom
		return (col*8, row*8, (col+1)*8, (row+1)*8)

	def crop_glyph(self, ch):
		if ch in self.glyphs:
			x, y = self.glyphs[ch]
			return self.font_img.crop(self.bbox(y, x))
		else:
			return self.crop_glyph(' ') # default to space

	def create_img(self, text):
		# create destination image
		lines = text.split('\n')
		width = max(len(l) for l in lines)
		dest = Image.new("RGB", (width*8, len(lines)*8), "black")
		# iterate over text
		x = 0 # current 'cursor'
		y = 0 # position
		for ch in text:
			if ch == '\n':
				x = 0
				y += 1
				continue
			if ch in self.glyphs:
				glyph_img = self.crop_glyph(ch)
				dest.paste(glyph_img, self.bbox(y, x))
			x += 1
		return dest

