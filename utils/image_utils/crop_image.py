def crop_center(img, ropx, cropy):
    y, x, channels = img.shape
    startx = x // 2 - (cropx // 2)
    starty = y // 2 - (cropy // 2)

    return img[starty : starty + cropy, startx : startx + cropx]
