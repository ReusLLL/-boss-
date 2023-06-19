# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:02:35 2023

@author: User
"""

from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.by import By
import random
#import pandas as pd
import time
import re
#from tkinter import (Tk, Text, Scrollbar,Frame,Button)
#from tkinter.constants import (HORIZONTAL, VERTICAL, RIGHT, LEFT, X, Y, BOTH, BOTTOM, YES, NONE, END, CURRENT,E,W,S)

city_dic = {'北京':'101010100',
            '上海':'101020100',
            '广州':'101280100',
            '深圳':'101280600',
            '杭州':'101210100',
            '天津':'101030100',
            '西安':'101110100',
            '苏州':'101190400',
            '武汉':'101200100',
            '厦门':'101230200',
            '长沙':'101250100',
            '成都':'101270100',
            '郑州':'101180100',
            '重庆':'101040100'}
job_name = input('请输入要搜索的职位名:')
page = int(input('请输入要搜索页码范围:'))+1
city = city_dic[input('请输入要搜索的城市名:')]
URL = 'https://www.zhipin.com/web/geek/job?query='+job_name+'&city='+city+'&page=%s'
jobname_list = []
jobarea_list = []
salary_list = []
jobtag_list = []
companyname_list = []
companytag_list = []

for i in range(1,page):
    url = URL % i
    opt = ChromeOptions() # 创建Chrome参数对象
#    opt.add_argument('--headless') # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
    driver = Chrome(options=opt) # 创建Chrome无界面对象
    driver.get(url)
    time.sleep(random.randint(3,7))
    html = BS(driver.page_source,features="html.parser")
    jobname_target = html.select('.job-name')      #职位名列表
    jobarea_target = html.select('.job-area')      #工作地点列表
    salary_target = html.select('.salary')      #薪酬列表
    jobtag_target = html.select('.tag-list')      #标签列表
    companyname_target = html.select('.company-name')      #公司名列表
    companytag_target = html.select('.company-tag-list')      #公司标签列表
    for j in range(30):        #每页默认30条结果
        jobname_list.append(jobname_target[j].text)
        jobarea_list.append(jobarea_target[j].text)
        salary_list.append(salary_target[j].text)
        jobtag_list.append(jobtag_target[j].text)
        companyname_list.append(companyname_target[j].text)
        companytag_list.append(companytag_target[j].text)
    driver.close()


    
'''    for j in JobInfo:
        company = re.split('</a>',re.split('custompage">',str(j.find('h3',class_ = 'company-name')))[1])[0]
        jobname = re.split('</span>',re.split('job-name">',str(j.find('span',class_ = 'job-name')))[1])[0]
        salary = re.split('</span>',re.split('salary">',str(j.find('span',class_ = 'salary')))[1])[0]
        location = re.split('</span>',re.split('job-area">',str(j.find('span',class_ = 'job-area')))[1])[0]
        info_list.append([jobname,salary,company,location])
    driver.close()
    time.sleep(1)
'''    
    
'''
def GUI():
    root=Tk ()
    root.title('爬取BOSS直聘岗位信息')
    def sendMessage() :
    #在聊天内容上方加一行，显示发送人及发送时间
        global answer 
        msgcontent ='我: ' + time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime())+'\n'
        text_msglist.insert (END, msgcontent, 'green')
        answer = ChatGPT(text_msg.get('0.0', END))
        text_msglist.insert (END, text_msg.get('0.0', END))
        text_msg.delete('0.0', END)
    #从chatgpt接收信息
    def receiveMessage():
        global answer
        msgcontent ='ChatGPT: ' + time.strftime ("%Y-%m-%d %H:%M:%S", time.localtime())+'\n'
        text_msglist.insert (END, msgcontent, 'red')
        text_msglist.insert (END, answer+'\n')
        text_msg.delete('0.0', END)
    #创建几个frame作为容器
    frame_left_top= Frame (width=400, height=270, bg='white')
    frame_left_center= Frame (width=400, height=130, bg='white' )
    frame_left_bottom= Frame (width=400,height=40)


    ##创建需要的几个元素
    text_msglist= Text (frame_left_top)
    text_msg= Text (frame_left_center)
    button_sendmsg= Button(frame_left_bottom, text=('发送') ,command= lambda:[sendMessage(),receiveMessage()])

    #创建一一个绿色的tag
    text_msglist.tag_config('green', foreground='#008B00')


    #使用grid设置各个容器的位置
    frame_left_top.grid (row=0,column=0, padx=2,pady=5)
    frame_left_center.grid (row=1, column=0, padx=2, pady=5)
    frame_left_bottom.grid (row=2,column=0)
    frame_left_top.grid_propagate (0)
    frame_left_center.grid_propagate (0)
    frame_left_bottom.grid_propagate (0)
    #把元素填充进frame
    text_msglist.grid()
    text_msg.grid()
    button_sendmsg.grid(sticky=E)
    #主事件循环
    root.mainloop ()    
'''   
    
    
    
    
    

#data = pd.DataFrame(info_list,columns=['职位名称','薪资','公司','工作地点'])
#data.to_csv('C:/Users/User/Desktop/个人文件/'+job_name+'职位信息爬虫.csv')

    
    
    

        
        