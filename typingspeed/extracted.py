from zipfile import ZipFile
file_path="ggg.zip"
with ZipFile (file_path,"r") as zip_:
    zip_.printdir()
    zip_.extractall()
