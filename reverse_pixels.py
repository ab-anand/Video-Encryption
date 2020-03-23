import json

def load_hilbert():
    with open('pixels.json') as f:
      data = json.load(f)
    # pix_dic = json.load("pixels.json")
    # print(data[str(0)][0])
    return data

def invert_values(pix_dic, width):
	inverted_pix = {}
	for key, value in pix_dic.items():
		row = int(key)//width
		col = int(key)%width
		n_key = width*value[0] + value[1]
		inverted_pix[n_key] = [row, col]
	print(len(inverted_pix))
	dump_file(inverted_pix)


def dump_file(diction):
	with open('inverted_pixels.json', 'w') as json_file:
  		json.dump(diction, json_file, sort_keys=True, indent=4)


hilbert_pix = load_hilbert()
invert_values(hilbert_pix, 1024)