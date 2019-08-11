import os, glob

def Processing():
    print ()
    print ("Current directory: ", os.getcwd())
    cur_dir = input("Input your dir: ")
    os.chdir(cur_dir)
    ask_ori_ext = '*.' + input("Please input your current file extension: ")
    ask_ext_dest = input("Please input your extension you wish to change to: ")
    print ()
    for file in glob.glob(ask_ori_ext):
        name_without_ext = os.path.splitext(file)[0]
        new_ext = '.' + ask_ext_dest
        new_name = name_without_ext + new_ext
        print (new_name)
        os.rename(os.path.join(cur_dir,file),os.path.join(cur_dir,new_name))
    print ()
    print ("Conversion completed!")
    
#execution
selection = 1
while selection != 0 :
    print ("Do you want to change extension?")
    print ("0. No\t1. Yes")
    selection = int(input())
    if selection == 1:
        Processing()
print ()
print ("Thanks for using!")