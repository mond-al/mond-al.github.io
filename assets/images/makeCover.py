import os
import random
import requests
from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image


width = 800
height = 540
pageLimit = 10
textSizeFat = 1.2
textSoruce = "FragmentPagerAdapter"
query = "desk"

def linkFetch():
    page = random.randint(1, pageLimit)
    url = f"https://api.unsplash.com/search/photos?fm=png&page={page}&query={query}&client_id=yzDacpHm8YTM53AXHxeFh_PwnCFPfPlzrCgI2TWhX1Y"
    print(url)
    response_ = requests.get(url)
    results_ = response_.json()["results"]
    limit = len(results_)
    rand = random.randint(1, int(limit))
    full_ = results_[rand]["urls"]["full"]
    data = full_ + f"&w={width}&h={height}&fit=crop"
    print(f"data:{data}")
    return data


def link2():
    return f"https://source.unsplash.com/{width}x{height}/?{query}"


folderName = 'cover'
fontFileName = 'NotoSansKR-Bold.otf'
tempFileName = "temp.jpg"
tempFileOutput = f"{folderName}/{tempFileName}"
fontFile = f"font/{fontFileName}"


def genFile(retryCount=0):
    try:
        print(f"------ > {retryCount}")
        if retryCount >= 10:
            return "None"
        img_url = link2()  # linkFetch()
        response = requests.get(img_url)
        BytesIO(response.content)
        g = (BytesIO(response.content))
        with open(tempFileOutput, 'wb') as out:
            out.write(g.read())
        im = Image.open(tempFileOutput)
        textSize = int(width / (len(textSoruce)) * (textSizeFat))
        font = ImageFont.truetype(fontFile, textSize)
        draw = ImageDraw.Draw(im)
        textWidth, textHeight = draw.textsize(textSoruce, font)
        textX = ((width - textWidth) / 2)
        textY = ((height - textHeight) / 2)
        draw.text((textX, textY), textSoruce, (255, 255, 255), font)
        outputFile: str = folderName + f"/_{query}_" + textSoruce + ".png"
        im.save(outputFile, format="JPEG", quality=82, optimize=True)
        os.remove(tempFileOutput)
        return outputFile
    except:
        genFile(retryCount + 1)


filePath = genFile()
if "None" == filePath:
    print("Failue")
else:
    join = os.path.join(os.path.dirname(__file__), filePath)
    print(join)
    open(join)
