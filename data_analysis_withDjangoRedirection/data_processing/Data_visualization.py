from ast import Bytes
import data_processing.data_Cleaning_4w as fw
import data_processing.dataCleaning_EV as ev
import matplotlib as plt
import base64
from io import BytesIO
import numpy as np

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph 

def fw_visualization():
    # creating the dataset
    data = {'C':20, 'C++':15, 'Java':30,
            'Python':35}
    courses = list(data.keys())
    values = list(data.values())
    
    plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(courses, values, color ='maroon',
            width = 0.4)
    
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")
    graph=get_graph()
    return graph

def ev_visualization():
    y = np.array([35, 25, 25, 15])
    plt.figure(figsize = (10, 5))
    plt.pie(y)
    graph=get_graph()
    return graph

def visualization(ch):
    #ch=input("ENter your choice:")
    if(ch==1):
        fw.cleaning()
        graph=fw_visualization()
    
    if(ch==2):
        ev.cleaning()
        graph=ev_visualization()

    return graph

if __name__=='__main__':
    ch=input("Enter your choice:")
    visualization(ch)