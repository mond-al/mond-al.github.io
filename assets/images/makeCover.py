import os
import random
import requests
from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

apiMode = False

folderName = 'cover'
width = 600
height = 400
pageLimit = 20
textSizeMultiple = 1
textSoruce = "Kotlin Sequence"
query = "Sequence"


def linkByApi():
    page = random.randint(1, pageLimit)
    url = f"https://api.unsplash.com/search/photos?fm=png&page={page}&query={query}&client_id=yzDacpHm8YTM53AXHxeFh_PwnCFPfPlzrCgI2TWhX1Y"
    apiResponse = requests.get(url)
    resultObj = apiResponse.json()["results"]
    randomLimit = len(resultObj)
    rand = random.randint(1, int(randomLimit))
    sourceUrl = resultObj[rand]["urls"]["full"]
    data = sourceUrl + f"&w={width}&h={height}&fit=crop"
    return data


def linkByUrl():
    return f"https://source.unsplash.com/{width}x{height}/?{query}"


def setUrl():
    if apiMode:
        img_url = linkByApi()
    else:
        img_url = linkByUrl()
    return img_url


def genFile(retryCount=0):
    tempFileName = "temp.jpg"
    tempFileOutput = f"{folderName}/{tempFileName}"
    fontFileName = 'NotoSansKR-Bold.otf'
    fontFile = f"font/{fontFileName}"
    try:
        print(f"------ > {retryCount}")
        if retryCount >= 10:
            return None
        img_url = setUrl()
        print(img_url)

        response = requests.get(img_url)
        BytesIO(response.content)
        sourceImage = (BytesIO(response.content))
        with open(tempFileOutput, 'wb') as out:
            out.write(sourceImage.read())
        im = Image.open(tempFileOutput)
        textSize = int(width / (len(textSoruce)) * (textSizeMultiple))
        font = ImageFont.truetype(fontFile, textSize)
        draw = ImageDraw.Draw(im)
        textWidth, textHeight = draw.textsize(textSoruce, font)
        textX = ((width - textWidth) / 2)
        textY = ((height - textHeight) / 2)
        draw.text((textX, textY), textSoruce, (255, 255, 255), font)
        outputFile: str = folderName + f"/_new.png"
        im.save(outputFile, format="JPEG", quality=82, optimize=True)
        os.remove(tempFileOutput)
        return outputFile
    except:
        genFile(retryCount + 1)


filePath = genFile()
if None == filePath:
    print("Failue")
else:
    join = os.path.join(os.path.dirname(__file__), filePath)
    print(join)
    os.system(f"open {join}")
