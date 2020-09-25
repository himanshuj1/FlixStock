from PIL import Image
import imagehash
import cv2
import glob
path=glob.glob("C:/Users/jainh/Desktop/FlixStock TEST/Problem Statement 3/simTest/dataBase/*.jpg")

hash0 = imagehash.average_hash(Image.open('C:\\Users\\jainh\\Desktop\\FlixStock TEST\\Problem Statement 3\\simTest\\querry.jpg')) 
hash_list=[]


for file in path:
    # print(file)
    hash1=imagehash.average_hash(Image.open(file))
    hash_list.append([file,hash0-hash1])

hash_list=sorted(hash_list, key = lambda x: x[1])
finalimage=[]
for i in hash_list:
    if(i[1]<9 and i[1]>7):
        finalimage.append(i[0])

print("THERE ARE ",len(finalimage), "Most similiar images")
for i in finalimage:
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    im = cv2.imread(i)                        # Read image
    imS = cv2.resize(im, (960, 540))                    # Resize image
    cv2.imshow("output", imS)                            # Show image
    cv2.waitKey(0)
    cv2.destroyAllWindows()  