with open('../input.txt', 'r') as f:
    raw_image = f.read().strip()

pixels = list(map(int, raw_image))

layer_width, layer_height = 25, 6

pixels_per_layer = layer_width * layer_height
layer_count = len(pixels) // pixels_per_layer
layers = [pixels[layer_no*pixels_per_layer:(layer_no+1)*pixels_per_layer] for layer_no in range(layer_count)]

min_zeroes_layer = layers[0]
for layer in layers:
    if layer.count(0) < min_zeroes_layer.count(0):
        min_zeroes_layer = layer
    
# part 1
print(min_zeroes_layer.count(1)*min_zeroes_layer.count(2))


# part 2

# get top non-transparent pixel for each merged layer
top_pixel_layers = [[pixel for pixel in merged_layer if pixel != 2][0] for merged_layer in zip(*layers)]
image = [top_pixel_layers[i*layer_width:(i+1)*layer_width] for i in range(layer_height)]
for row in image:
    print(''.join(' █'[i] for i in row))
