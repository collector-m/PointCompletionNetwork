import os
import numpy as np
import shutil

#recursively list the name of file based on type
def ListFilesToTxt(dir_file,txt_file,type,recursion):
    exts = type.split(" ")
    files = os.listdir(dir_file)
    for name in files:
        fullname=os.path.join(dir_file,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,txt_file,type,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    print(dir_file+"/"+name + "\n")
                    txt_file.write(dir_file+"/"+name + "\n")
                    break

def file2txt(dir_file,txt_file,type):

  file = open(txt_file,"w")
  if not file:
    print ("cannot open the file %s for writing" % txt_file)

  ListFilesToTxt(dir_file,file,type, 1)

  file.close()
  return txt_file

# def cp_pcd(source_file,destination_dir):




if __name__ == '__main__':
    #copy pcd file to target file
    type_obj = "allParts.pcd"
    objfiles='/home/zq/zq/partnet_chair/chair_partial'#source obj file
    txt_obj='./txt_pcd_source.txt'#source obj file list
    file2txt(objfiles, txt_obj, type_obj)#obj file-> obj file list

    pcd_file=open(txt_obj,'r')
    for line in pcd_file:
        line=line.strip("\n")# delete "\n" in line
        source_file=os.path.splitext(line)[0]#delete the ext
        number_pcd=source_file.split("/")[-2]#the number in the path
        target_dir=os.path.join('./pcd/chair/',number_pcd)# clarify the name of the target file
        print(target_dir)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)#mkdir target_dir
        shutil.copy(line,target_dir)#cp source->target

    ## txt_pcd='./txt_obj.txt'
    ## file2txt('/home/zq/zq/git-space/pcn/data/data_preprocess/chair_obj',txt_pcd,'allParts.obj')

    # #generate list.txt
    # txt_s='./txt_obj.txt'
    # target='./list.txt'
    # file_s=open(txt_s,'r')
    # file_t=open(target,'w')
    # for line in file_s:
    #     line=line.strip("\n")
    #     s=os.path.splitext(line)[0]
    #     file_t.write("chair"+"/"+s.split("/")[-2]+"\n")