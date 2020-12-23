from deep_translator import GoogleTranslator
import os

oldfileName = "download.php"  # here change file name


NewFileName = "abc.php"
os.system("clear")
f = open(NewFileName, "a", encoding='utf-8')
filePHP = open(oldfileName, 'r')
for line in filePHP.readlines():
    if line.find("=") > 0:
        line1 = line
        text = line[line1.find("= '")+3:line1.find("';")]
        translated = GoogleTranslator(
            source='auto', target='hi').translate(text)
        print(line.replace(line[line.find("= '") +
                                3:line.find("';")], translated))
        f.write(line.replace(
            line[line.find("= '") + 3:line.find("';")], translated))
    else:
        print(line)
        f.write(line)

filePHP.close()
f.close()
os.remove(oldfileName)
os.rename(NewFileName, oldfileName)
