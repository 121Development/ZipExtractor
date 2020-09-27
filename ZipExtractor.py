# https://www.techrepublic.com/article/reading-zip-archives-in-python/from zipfile import ZipFile

from zipfile import ZipFile
import zipfile
import os
import glob
from pathlib import Path


# https://stackoverflow.com/questions/8844781/get-file-list-of-files-contained-in-a-zip-file
latestzip = input("Enter name of first zip-file, including .zip: ")
latestzip = zipfile.ZipFile(latestzip)
n = 0
while True:
    nameofzipinsidelatestzip = latestzip.namelist()
    pw = str(nameofzipinsidelatestzip[0])[:4]
    print(f'Password for {latestzip} is: {pw}')
    with zipfile.ZipFile(latestzip.filename) as file:
            file.extractall(pwd=bytes(pw, 'utf-8'))
    n += 1
    # break if filename starts with flag
    if pw == "flag":
        print(f"Extracted {n} ZIP files")
        break
    # Get latest file from folder
    files_path = os.path.join(os.getcwd(), '*')
    latest_file = ""
    latest_file = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
    latestzip = zipfile.ZipFile(f'{Path(latest_file[0]).name}')


