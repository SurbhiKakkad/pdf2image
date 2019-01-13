from wand.image import Image as Img

with Img(filename='sample.pdf',resolution=300) as img:
    img.compression_quality = 99
    img.save(filename='image.png')
