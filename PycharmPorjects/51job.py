# -*- coding: utf-8 -*-
from selenium import webdriver
import  time,datetime
import linecache,os

d1 = datetime.datetime.now()
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
os.system("rd /s /q %temp% >nul  2>nul")
job_company=[]
job_name=u"软件测试工程师"
job_city="深圳"
job_page_num=8 #设置需要投递几页的公司

def read_company():
    with open('exclude_company.txt','r') as f:
        for line in f:
            line=line.strip()
            job_company.append(line)
            
def login():
    if driver.find_element_by_id("verifyPic_img").is_displayed():
        driver.delete_all_cookies()
        time.sleep(5)
        driver.refresh()
    else:   
        #print driver.get_cookies()
        pass
    driver.find_element_by_id('loginname').click()
    driver.find_element_by_id("loginname").send_keys(user_data[0])
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").send_keys(user_data[1])
    driver.find_element_by_id("login_btn").click()

   

def seach_job():
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/p/a[1]").click()
    driver.find_element_by_id("kwdselectid").clear()
    driver.find_element_by_id("kwdselectid").send_keys(u"软件测试工程师")
    driver.find_element_by_id("work_position_input").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"work_position_layer\"]/div[1]/div[2]/div[1]/div[1]").click()
    driver.find_element_by_id("work_position_click_bottom_save").click()
    driver.find_element_by_css_selector("body > div.content > div > div.fltr.radius_5 > div > button").click()
    time.sleep(2)
    driver._switch_to.window(driver.window_handles[0])


def select_job():
    #点击全选按钮
    driver.find_element_by_xpath('html/body/div[2]/div[4]/div[2]/div[1]/span/em').click()
    #查找页面所有checkbox
    inputs = driver.find_elements_by_name('delivery_em')
    list_check=[]
    for input_checkbox in inputs:
        if input_checkbox.get_attribute("name")=="delivery_em":
            list_check.append(input_checkbox)
    # print len(list_check)  #50勾选框
    
    count = 0
    en=driver.find_elements_by_class_name("t2")
    # print len(en)  #51公司名字
    del en[0]
    # print len(en)
    
    for i in en:
        if i.text.encode('utf-8') in job_company:
            list_check[count].click()
            time.sleep(3)
        count += 1
    
    #点击申请职位
    try:
        driver.find_element_by_xpath("html/body/div[2]/div[4]/div[2]/div[2]/span[1]").click()
        driver.find_element_by_id('apply_now').click()
    except:
        pass
    
    #处理投递成功后的弹窗
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    
    #关闭重复提交简历的窗口
    try:
        driver.find_element_by_id('window_close_apply').click()
    except:
        pass

def custom_select_job():
    #自定义工作的选择，设定工作循环投递几页
    for select_job_num in range(1,job_page_num):
        if select_job_num !=1:
            driver.find_element_by_link_text(str(select_job_num)).click()
        try:
            select_job()
        except:
            pass
    output.write(user_data[0]+'   is success!!!\n')

if __name__ == "__main__":
    read_company()#读取屏蔽公司名单到list
    output = open('.//log//51job_'+now+'_log.txt', 'a')  
    count = len(open('51job_stu_info.txt','rU').readlines())
    for user_num in range(1,count+1):
        try:
            driver = webdriver.Chrome()
            driver.get("http://my.51job.com/my/My_SignIn.php")
            driver.implicitly_wait(10)
            driver.maximize_window()  #将浏览器最大化显示
            driver.delete_all_cookies()
            user_data = linecache.getline('51job_stu_info.txt',user_num).strip('\n')
            user_data  = user_data.split('\t')
            login()
            seach_job()
            custom_select_job()
            driver.quit() 
        except:
            driver.quit()
            output.write(user_data[0]+" is failed!!!\n") 
             
    d2 = datetime.datetime.now()-d1
    output.write('本次投递 '+str(count)+' 个学生的简历共计用时：'+str(d2))
    output.close()
    driver.quit()