from PIL import Image

import os


def fill_image(image):
    width, height = image.size
    new_len = max(width, height)

    # 生成新图片是正方形，长度为原宽高中长的 保证可以覆盖全图内容
    new_image = Image.new(image.mode, (new_len, new_len), color='white')

    # 根据两种不同的情况，将原图片放入新建的空白图片中部
    if width > height:
        new_image.paste(image, (0, int((new_len - height) / 2)))
    else:
        new_image.paste(image, (int((new_len - width) / 2), 0))
    return new_image


def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)

    # 保存每一个小切图的区域
    box_list = []

    for i in range(3):
        for j in range(3):
            # 切图区域是矩形，位置由对角线的两个点(左上和右下)确定
            box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    return image_list


def save_images(image_list, out_dir):
    for (index, image) in enumerate(image_list):
        image.save(f"{out_dir}/{index}.png", "PNG")


def to9img(file_path, out_dir='.'):
    image = Image.open(file_path)
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list, out_dir)


if __name__ == '__main__':
    to9img('IMG_E3692.JPG')