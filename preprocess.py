import glob, math
import face_recognition


FOLDER_TRUE = "dataset_true/"
FOLDER_FALSE = "dataset_false/"
CROPPED_IMG_PATH = "trimmed/"
IMG_SIZE = 50
IMG_RATIO = 2    # 顔の検知から、どれだけの倍率大きくとるか
IMG_RESOLUTION_LIMIT = 1080

def resizeImg(img_path):
    from PIL import Image

    img = Image.open(img_path)
    print("image size: ", img.width, img.height)
    if (img.height > IMG_RESOLUTION_LIMIT):
        ratio = img.height / IMG_RESOLUTION_LIMIT
    elif (img.width > IMG_RESOLUTION_LIMIT):
        ratio = img.width / IMG_RESOLUTION_LIMIT
    else:
        return
    img = img.resize((int(img.width/ratio), int(img.height/ratio)))
    img.save(img_path)

def findFace(img_path):
    resizeImg(img_path) # メモリの消費を抑えるためにリサイズする
    img_data = face_recognition.load_image_file(img_path)
    loc = face_recognition.face_locations(img_data, model='cnn') # 'hog'よりmodel='cnn'の方が高精度ではある
    print(loc)
    return loc

def trimImg(img_path, loc):
    from PIL import Image

    img = Image.open(img_path)
    top = loc[0]
    left = loc[3]
    bottom = loc[2]
    right = loc[1]
    width = right - left
    height = top - bottom
    length = max(width, height) * IMG_RATIO // 2
    center_x = (right + left) / 2
    center_y = (top + bottom) / 2
    img = img.crop((center_x-length,center_y-length, center_x+length,center_y+length))
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img.save(CROPPED_IMG_PATH + img_path)

def main():

    true_files = glob.glob(FOLDER_TRUE + "*")
    false_files = glob.glob(FOLDER_FALSE + "*")
    
    for path in true_files:
        print(path)
        locs = findFace(path)
        if (len(locs) != 1):
            print("うまく取得できなかったピヨ")
            continue
        trimImg(path, locs[0])

    for path in false_files:
        print(path)
        locs = findFace(path)
        if (len(locs) != 1):
            print("うまく取得できなかったピヨ")
            continue
        trimImg(path, locs[0])


if __name__ == '__main__':
    main()

    # test_path = "dataset_true/minami_hoshino-070.jpeg"
    # resizeImg(test_path)
