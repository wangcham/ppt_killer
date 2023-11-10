FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3.9 python3-pip

RUN apt-get install -y tesseract-ocr

RUN apt-get install -y wget
RUN wget https://github.com/tesseract-ocr/tessdata_best/blob/main/chi_sim.traineddata
RUN mv chi_sim.traineddata /usr/share/tesseract-ocr/4.00/tessdata/

WORKDIR /app

COPY backend ./backend
COPY frontend/dist ./frontend/dist

RUN pip3 install -r backend/requirements.txt

EXPOSE 5000

ENV API_KEY=""
ENV API_BASE=""

CMD [ "python3","backend/app.py" ]