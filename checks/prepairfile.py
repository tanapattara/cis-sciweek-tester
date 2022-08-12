import os
import shutil

def getAnswersFileList(dir_path = "./answers/"):
    originals = os.listdir(dir_path)
    for old_filename in originals:
        
        filename = old_filename.split('-')[0].strip()
        teamname = old_filename.split('-')[1].strip()
        teamname = teamname.split('.')[0].strip()

        newpath = "./input/" + teamname
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        shutil.copyfile(dir_path + old_filename, newpath + "/" + filename + ".py")
    return originals
    
getAnswersFileList()