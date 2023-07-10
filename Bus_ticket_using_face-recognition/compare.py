from deepface import DeepFace
import pandas

import warnings
warnings.filterwarnings("ignore")


def compare():
    src=r"newimage/saved_img-final.jpg"
    repo=r"Image_repo"
    res=DeepFace.find(src,repo)[0].values.tolist()
    if res==[]:
        return "False"
    res=res[0][0].split(".")
    res=res[0].split("/")
    res=res[1]

    return res
    



# print(compare())



