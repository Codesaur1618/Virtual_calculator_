import cv2
from cvzone.HandTrackingModule import HandDetector
class Button:
    def __init__(self,pos,width,height,value):
        self.pos = pos
        self.width = width
        self.value = value
        self.height = height
    def draw(self,img):
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(255, 255, 255), cv2.FILLED)
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)
    def click(self,x,y):

        if self.pos[0]<x<self.pos[0]+self.width and self.pos[1] <y<self.pos[1]+self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (255, 255, 255),
                          cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
            cv2.putText(img, self.value, (self.pos[0] + 23, self.pos[1] + 75), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0),
                        5)
            return True
        else:
            return False


#        x1<x<x1+width
#webcam
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9)
l=1280
h=720

#values fo rbutton
buttonListValues = [['7','8','9','*'],
                    ['6','5','4','.'],
                    ['1','2','3','+'],
                    ['0','/','-','='],
                    ['C.E','Q','**','<-']]
#creating button
buttonList =[]
for x in range(4):
    for y in range(5):
      xpos = x*100+150
      ypos = y*100+700
      buttonList.append(Button((ypos,xpos),100,100,buttonListValues[y][x]))
#variables
myeq = ""
delay= 0

while True:
    success, res = cap.read()
    img=cv2.resize(res,(l,h))
    img = cv2.flip(img,1)

    hands, img = detector.findHands(img,flipType=False)
    #draw all buttons
    cv2.rectangle(img, (700,70), (800 +400,70+100),(255, 255, 255), cv2.FILLED)
    cv2.rectangle(img, (700,70), (800 +400,70+100), (50, 50, 50), 3)

    for button in buttonList:
      button.draw(img)
    #check the hands
    if hands:
        lmList1 = hands[0]['lmList']
        lmList2 = hands[0]['lmList']
        length, info, img = detector.findDistance(lmList1[8][:2], lmList2[4][:2], img)
        x,y = lmList1[8][:2]
        if length<30:
            for i,button in enumerate(buttonList) :
                 if delay==0:
                    if button.click(x,y):
                        myValue=buttonListValues[int(i%5)][int(i/5)]
                        if myValue == "C.E":
                            myeq = ""
                            break
                        elif myValue == "Q":
                            quit()
                        elif myValue == "<-":
                            if myeq[-1] == "*" and myeq[-2] == "*":
                                myeq = myeq[:-2]
                            else:
                                myeq = myeq[:-1]
                        elif myValue == "=":
                            myeq = str(eval(myeq))
                        else:
                            myeq += myValue
                        delay =1
                        print(delay)
    #to avoid duplicates
    if delay !=0:
        delay +=1
        if delay >20:
            delay =0
    #display the res
    cv2.putText(img, myeq, (710,120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)


    cv2.waitKey(1)
    cv2.imshow("Image",img)
