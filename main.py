import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")

files = os.listdir()
files.remove("main.exe")

createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Compress')
createIfNotExist('Software')
createIfNotExist('Codes')
createIfNotExist('Others')

imgExts = (".png",".jpg",".jpeg",".psd",".gif",".ai",".svg",".ico")
images = [file for file in files if os.path.splitext(file)[-1].lower() in imgExts]
docExts = (".pdf",".doc",".docx",".ppt",".pptx",".csv")
docs = [file for file in files if os.path.splitext(file)[-1].lower() in docExts]
medExts = (".mp4",".mp3",".wav",".mkv",".webm")
medias = [file for file in files if os.path.splitext(file)[-1].lower() in medExts]
compExts = (".rar",".zip")
compress = [file for file in files if os.path.splitext(file)[-1].lower() in compExts]
softExts = (".exe",".msi")
software = [file for file in files if os.path.splitext(file)[-1].lower() in softExts]
codeExts = (".html",".js",".css",".sql",".cpp",".py",".whl",".txt",".c",".java")
codes = [file for file in files if os.path.splitext(file)[-1].lower() in codeExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in medExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in compExts) and (ext not in softExts) and (ext not in codeExts) and os.path.isfile(file):
        others.append(file)

# print(others)
move("Images",images)
move("Docs",docs)
move("Media",medias)
move("Others",others)
move("Compress",compress)
move("Software",software)
move("Codes",codes)