import pandas as pd
import cv2
img_path=r'c:\Users\Siddharth Pareek\Downloads\R (1).jpg'
img=cv2.imread(img_path)
clicked=False
r=g=b=x_position=y_position=0
colors_df=pd.read_csv('https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv')
#colors_df.head()
index=["color","color_name","hex_decimal","R","G","B"]
colors_df=pd.read_csv('https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv',names=index,header=None)
#colors_df.head()
#img=cv2.resize(img,(800,600))
def find_bgr(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global x_position,y_position,clicked,r,g,b
        clicked=True
        b,g,r=img[y,x]
        y_position=y
        x_position=x
        b=int(b)
        g=int(g)
        r=int(r)
def get_color_name(R,G,B):
    min=1000
    for i in range(len(colors_df)):
        d=abs(R-colors_df.loc[i,"R"])+abs(B-colors_df.loc[i,"B"])+abs(G-colors_df.loc[i,"G"])
        if d<=min:
            min=d
            color_name=colors_df.loc[d,"color_name"]
            return color_name
cv2.namedWindow('image')
cv2.setMouseCallback('image',find_bgr)
while True:
    cv2.imshow('image',img)
    if clicked:
        cv2.rectangle(img,(20,20),(600,60),(b,g,r),-1)
        text=get_color_name(r,g,b)+'R='+str(r)+','+'G='+str(g)+','+'B='+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r+g+b<=600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        
    if cv2.waitKey(20) & 0XFF == 27:
        break
cv2.destroyAllWindows()        
