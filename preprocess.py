import glob, math
import face_recognition


CROPPED_IMG_PATH = "trimmed/"
IMG_SIZE = 50
IMG_RATIO = 2    # 顔の検知から、どれだけの倍率大きくとるか

def findFace(img_path):
    img_data = face_recognition.load_image_file(img_path)
    loc = face_recognition.face_locations(img_data, model='cnn') # 'hog'よりmodel='cnn'の方が高精度ではある
    print(loc)
    return loc

def trimImg(img_path, loc):
    from PIL import Image

    Image = Image.open(img_path)
    top = loc[0]
    left = loc[3]
    bottom = loc[2]
    right = loc[1]
    width = right - left
    height = top - bottom
    length = max(width, height) * IMG_RATIO // 2
    center_x = (right + left) / 2
    center_y = (top + bottom) / 2
    # croppedIm = Image.crop((top, left, bottom, right))
    croppedIm = Image.crop((center_x-length,center_y-length, center_x+length,center_y+length))
    resizeIm = croppedIm.resize((IMG_SIZE, IMG_SIZE))
    resizeIm.save(CROPPED_IMG_PATH + img_path)

def main():
    # FOLDER_TRUE = "dataset_true/"
    # FOLDER_FALSE = "dataset_false/"
    # true_files = glob.glob(FOLDER_TRUE + "*")
    # false_files = glob.glob(FOLDER_FALSE + "*")
    # print(true_files)
    
    # 実験
    path = "dataset_true/minami_hoshino-003.jpeg"
    locs = findFace(path)
    if (len(locs) != 1):
        print("うまく取得できなかったピヨ")
        return
    trimImg(path, locs[0])


if __name__ == '__main__':
    main()
