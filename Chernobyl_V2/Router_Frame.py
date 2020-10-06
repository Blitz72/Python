from tkinter import Frame, Label, Button
import router_info as router

class Router_Frame:
    
    def __init__(self, router_info):
        self.router_info = router_info
        print(self.router_info['img_URL'])
        
    def print_info(self):
        print(self.router_info)
        

frame1 = Router_Frame(router.router1)
#print(frame1.router_info)