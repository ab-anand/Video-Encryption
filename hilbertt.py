import json
from hilbertcurve.hilbertcurve import HilbertCurve


p=10; N=2

hilbert_curve = HilbertCurve(p, N)

def create_dict(p, N, width):

	pix = {}
	po = 0
	count = 0
	max_x = 0
	max_y = 0
	for ii in range(1048576):
		row = ii//width
		col = ii%width
		coordinates = [row, col]
		try:
			pos = hilbert_curve.distance_from_coordinates(coordinates)
			coords = hilbert_curve.coordinates_from_distance(ii)
			row_n = pos//width
			col_n = pos%width
			pix[ii] = coords
			if max_x < coords[0]:
				max_x = coords[0]
			if max_y < coords[1]:
				max_y = coords[1]
			count += 1
			# print(ii)
		# print(f'coords(h={ii}) = {coords}')
		except ValueError as v:
			print(str(v))
			pass
	print(count, len(pix))
	print(max_x, max_y)
	dump_file(pix)


def dump_file(diction):
	with open('pixels.json', 'w') as json_file:
  		json.dump(diction, json_file, indent=4)

create_dict(p, N, 1024)