from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
import re

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    # Read image bytes
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # Use pytesseract to extract text
    text = pytesseract.image_to_string(image)

    # Find numbers and multiplication symbol
    match = re.findall(r"\d+", text)
    if len(match) >= 2:
        try:
            num1 = int(match[0])
            num2 = int(match[1])
            result = num1 * num2
            return JSONResponse({
                "answer": result,
                "email": "24f2004829@ds.study.iitm.ac.in"
            })
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)
    else:
        return JSONResponse({"error": "Could not read multiplication task"}, status_code=400)
