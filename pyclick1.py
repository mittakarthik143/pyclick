import pyautogui as p,time
class a_c:
    def auto_click(self,h=3):
        self.h=h
        #self.t=t
        try:
            h=int(input("How many times to click: "))
            k=input("Enter key to start[s]: ")
        except:
            h=10
            k=input("Enter key to start[s]: ")
            #auto_click()
            #k='s'
        if k=='s':
            x,y=p.position()
            if h!=0:
                try:
                    t=int(input("Enter time: "))
                except:
                    t=0
                if t==0:
                    while h>0:
                        p.moveTo(x,y)
                        p.click()
                        h-=1
                    p.alert(button="stop")
                    #p.hotkey('esc')
                elif t!=0:
                    while h>0:
                        p.moveTo(x,y,t)
                        p.click(interval=t)
                        h-=1
                    #p.hotkey('esc')
                    p.alert(button='stop')
                    #print("Stop")
                else:
                    print('fail')
            elif self.h==3:
                while self.h>0:
                    p.moveTo(x,y,1)
                    p.click(interval=1)
                    self.h-=1
                p.hotkey('esc')
        elif k!='s':
            print("plz enter start key")
        
cli=a_c()
cli.auto_click()
