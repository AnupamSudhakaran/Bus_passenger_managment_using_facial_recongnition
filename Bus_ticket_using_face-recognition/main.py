import register
import verfiy
import os

def reg_subp(name):
    myfile="image_repo/representations_vgg_face.pkl"
    register.register(name)
    if os.path.isfile(myfile):
        print("True")
        os.remove(myfile)

# print("HEllo note S is used for clicking the image")
# op=int(input("1 for register"))
# if op==1:
#     reg_subp()
    
    
    
# else:
#     verfiy.verify()
    

