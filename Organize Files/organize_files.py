from pathlib import Path
import shutil


# File type references to put the file in the corresponding folder
filetypes = {
    "Images": ["png", "jpg", "jiff", "jpeg", "bmp", "tiff", "tif", "gif", "raw", "psd"],
    "Documents": ["doc", "docx", "ppt", "pptx" "xls", "xlsx", "pdf", "txt"],
    "Videos": ["mp4", "mpeg", "mkv", "srt"],
    "Code": ["html", "css", "js", "py", "cpp", "c"],
    "Audio": ["mp3", "wav", "ogg"],
    "Compressed": ["zip", "tar", "rar"],
}
# Path where the files need to be sorted/organize
PATH = Path("C:/Users/Vivek/Downloads")
files = []
# A list to store all the files in the PATH

# All the files will go to the organized folder
dest = PATH / "Organized"
# Make the folder only if it does not exists
dest.mkdir(exist_ok=True)

# iterate every file and directory and store only the files in the 'files' list (line 16)
for i in PATH.iterdir():
    if i.is_file():
        files.append(i)

# traverse on every file check the file type and move it to the corresponding folder
for file in files:
    # done flag tells that the file belong to a dictionary value
    done = 0
    # iterate over the keys and check if the file belong to the particular key
    for k in filetypes.keys():
        # Check if the file extention is in the values of the key
        if file.suffix[1:] in filetypes[k]:
            done = 1
            # make a new folder with `key name` and move the file there
            destf = dest / f"{k}"
            destf.mkdir(exist_ok=True)
            shutil.move(str(file.resolve()), str(destf))

    if done != 1:
        # if the file was not present in the dictionary the make Others folder  and move the file there
        destf = dest / "Others"
        destf.mkdir(exist_ok=True)
        shutil.move(str(file.resolve()), str(destf))
