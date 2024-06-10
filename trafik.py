import cv2 as cv
import threading
from playsound import playsound

cam = cv.VideoCapture("D:\\Kodlama\\Goruntu isleme\\projem\\levhalar5.mp4")
# cam = cv.VideoCapture(0)

parkYapmakYasak = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\parkYapmakYasak\\classifier\\cascade.xml")
yayaGecidi = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\yayaGecidi\\classifier\\cascade.xml")
sagaYolVar = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\sagaYolVar\\classifier\\cascade.xml")
trafikIsigi = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\trafikIsigi\\classifier\\cascade.xml")
sagaDonusYapilamaz = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\sagaDonusYapilamaz\\classifier\\cascade.xml")
yolVer = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\yolVer\\classifier\\cascade.xml")
hizSiniri50 = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\hizSiniri50\\classifier\\cascade.xml")
kasisVar = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\kasisVar\\classifier\\cascade.xml")
okulGecidi = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\okulGecidi\\classifier\\cascade.xml")
tersYon = cv.CascadeClassifier("D:\\Kodlama\\Goruntu isleme\\projem\\tersYon\\classifier\\cascade.xml")

font1 = cv.FONT_HERSHEY_SIMPLEX

def play_alert():
    playsound("D:\\Kodlama\\Goruntu isleme\\projem\\alert.mp3")
while True:
    ret, frame = cam.read()
    if not ret:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if parkYapmakYasak:
        levha = parkYapmakYasak.detectMultiScale(gray, 1.3, 15)
        for (x, y, w, h) in levha:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.putText(frame, "Park Yapmak Yasak!", (x, y), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if yayaGecidi:
        levha2 = yayaGecidi.detectMultiScale(gray, 1.3, 15)
        for (x1, y1, w1, h1) in levha2:
            cv.rectangle(frame, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)
            cv.putText(frame, "Yaya Gecidi", (x1, y1), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if sagaYolVar:
        levha3 = sagaYolVar.detectMultiScale(gray, 1.3, 13)
        for (x2, y2, w2, h2) in levha3:
            cv.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
            cv.putText(frame, "Saga Yol Var", (x2, y2), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if trafikIsigi:
        levha4 = trafikIsigi.detectMultiScale(gray, 1.3, 10)
        for (x2, y2, w2, h2) in levha4:
            cv.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
            cv.putText(frame, "Trafik Isigi", (x2, y2), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if sagaDonusYapilamaz:
        levha5 = sagaDonusYapilamaz.detectMultiScale(gray, 1.3, 12)
        for (x2, y2, w2, h2) in levha5:
            cv.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
            cv.putText(frame, "Saga Donus Yapilamaz", (x2, y2), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if yolVer:
        levha6 = yolVer.detectMultiScale(gray, 1.3, 15)
        for (x2, y2, w2, h2) in levha6:
            cv.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
            cv.putText(frame, "Yol Ver", (x2, y2), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if hizSiniri50:
        levha7 = hizSiniri50.detectMultiScale(gray, 1.3, 12)
        for (x2, y2, w2, h2) in levha7:
            cv.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
            cv.putText(frame, "Hiz Siniri 50", (x2, y2), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if kasisVar:
        levha8 = kasisVar.detectMultiScale(gray, 1.3, 15)
        for (x2, y2, w2, h2) in levha8:
            cv.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
            cv.putText(frame, "Kasis Var", (x2, y2), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if okulGecidi:
        levha9 = okulGecidi.detectMultiScale(gray, 1.3, 8)
        for (x2, y2, w2, h2) in levha9:
            cv.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
            cv.putText(frame, "Okul Gecidi", (x2, y2), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()
    if tersYon:
        levha10 = tersYon.detectMultiScale(gray, 1.3, 13)
        for (x2, y2, w2, h2) in levha10:
            cv.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
            cv.putText(frame, "Ters Yon", (x2, y2), font1, 1, (0, 0, 255), 2)
            threading.Thread(target=play_alert).start()

    cv.namedWindow("Tabela", cv.WINDOW_NORMAL)
    cv.imshow("Tabela", frame)

    if cv.waitKey(16) & 0xFF == ord("k"):
        break

cam.release()
cv.destroyAllWindows()
