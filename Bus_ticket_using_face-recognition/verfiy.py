from capture import capture
from compare import compare
import verify_result
def verify():
    capture()
    path="newimage/saved_img-final.jpg"
    res=compare()

    verify_result.verify_res(res)




    
    