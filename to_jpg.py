from tkinter import *
import shutil
import os
import cv2

def copy_files(src, dst, extension):
    src_files = os.listdir(src)
    for file_name in src_files:
        if '.git' in file_name or 'weight' in file_name:
            continue
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            if full_file_name[-4:] != extension:
                temp_img = cv2.imread(full_file_name)
                cv2.imwrite(os.path.join(dst,file_name[:-4]+extension), temp_img)
            else:
                shutil.copy(full_file_name, os.path.join(dst,file_name))
        if os.path.isdir(full_file_name):
            os.makedirs(os.path.join(dst, file_name), exist_ok=True)
            copy_files(full_file_name, os.path.join(dst, file_name), extension)

root = Tk()
root.title("Image type converter")
root.geometry("320x120") # 가로x세로
# root.geometry("640x480+100+300") # 가로, 세로, x좌표, y좌표

label1 = Label(root, text="Type directory path")
label1.pack()

e = Entry(root, width=30) # entry -> 한줄로 충분할때
e.pack()

def btncmd_jpg():
    dirpath = e.get()
    if dirpath == "":
        return
    os.mkdir(dirpath+'_jpg')
    copy_files(dirpath, dirpath+'_jpg', '.jpg')
    print("변환 완료!")

def quit():
    root.destroy()

btn = Button(root, text="Convert to jpg", command=btncmd_jpg)
btn.pack()

btn_end = Button(root, text="Quit", command=quit)
btn_end.pack()
root.resizable(False,False) # 크기 변경 불가
root.mainloop()

# ./> pyinstaller -w ./to_jpg.py