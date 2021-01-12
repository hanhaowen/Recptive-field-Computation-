# backbone            kernel_size,stride,padding, the first number in the brackets is the attribute of X axis, the second is along with y axis
network_structure = [[(6, 3), (1, 1), (3, 1)],[(6, 3), (1, 1), (3, 1)],[(6, 3), (2, 2), (3, 1)],[(3, 3), (1, 1), (1, 1)],
                     [(6, 3), (1, 1), (3, 1)],[(6, 3), (1, 1), (3, 1)],[(6, 3), (2, 2), (3, 1)],[(3, 3), (1, 1), (1, 1)],
                     [(6, 3), (1, 1), (3, 1)],[(6, 3), (1, 1), (3, 1)],[(6, 3), (2, 2), (3, 1)],[(3, 3), (1, 1), (1, 1)],
                     [(6, 3), (1, 1), (3, 1)],[(6, 3), (1, 1), (3, 1)],[(6, 3), (2, 2), (3, 1)],[(3, 3), (1, 1), (1, 1)]
                     ]
layer_name = ['conv1_1', 'conv1_2', 'conv1_3', 'pool_1',
              'conv2_1', 'conv2_2', 'conv2_3', 'pool_2',
              'conv3_1', 'conv3_2', 'conv3_3', 'pool_3',
              'conv4_1', 'conv4_2', 'conv4_3', 'pool_4']

image_size = (1920, 1080)
#x length and y length

def RF_Compute(netword_structure, layer_name):
    X_RF = 1
    Y_RF = 1
    X_stride = 1
    Y_stride = 1
    layernum = len(layer_name)
    for layer in reversed(range(layernum)):
        fsize, stride, pad = netword_structure[layer]
        X_RF = ((X_RF - 1) * stride[0]) + fsize[0]
        Y_RF = ((Y_RF - 1) * stride[1]) + fsize[1]
        X_stride = X_stride * stride[0]
        Y_stride = Y_stride * stride[1]
    return X_RF, Y_RF, X_stride, Y_stride


def Size_Compute(image_size, network_structure, layer_name):
    x_insize = image_size[0]
    y_insize = image_size[1]
    layernum = len(layer_name)
    x_outsize = 0
    y_outsize = 0
    for layer in range(layernum):
        fsize, stride, pad = network_structure[layer]
        x_outsize = int((x_insize - fsize[0] + 2 * pad[0]) / stride[0] + 1)  ###############
        x_insize = x_outsize
        y_outsize = int((y_insize - fsize[1] + 2 * pad[1]) / stride[1] + 1)  ###############
        y_insize = y_outsize
    return x_outsize, y_outsize


for i in range(len(layer_name)):
    x, y, x_stride, y_stride = RF_Compute(network_structure[0:i+1], layer_name[0:i+1])
    x_size, y_size = Size_Compute(image_size, network_structure[0:i+1], layer_name[0:i+1])
    print("                  it is ", layer_name[i],'            ')
    print('X_RF=', x, '  ', 'Y_RF=', y, "   ",'X_stride=', x_stride, '  ','Y_stride=', y_stride, '  ', "    x_size=", x_size, '  ', "y_size=", y_size)
