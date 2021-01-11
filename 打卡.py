from selenium import webdriver
import os
import datetime
import time

path_init = os.path.dirname(os.path.realpath(__file__))

def get():
	with open(path_init + '\\用户名和密码.txt', 'r', encoding = 'utf-8') as f:
		content = f.read()

	content_list = content.split('：')

	username = content_list[1].split( )[0]
	password = content_list[2]
	return username, password

def main():
	driver = webdriver.Chrome(executable_path = r'C:\Users\pc\anaconda3\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')   # 声明一个浏览器对象   指定使用chromedriver.exe路径
	username, password = get()#获取用户名和密码
	print(username)
	print(password)
	url = 'https://ehall.jlu.edu.cn/infoplus/form/BKSMRDK/start'
	driver.get(url)  # 打开Chrome

	input = driver.find_element_by_id('username')  # 通过id定位到input框
	input.send_keys(username)   # 在输入框内输入用户名
	input = driver.find_element_by_id('password')  # 通过id定位到input框
	input.send_keys(password)   # 在输入框内输入密码

	button_log_in = driver.find_element_by_id('login-submit')  # 获取登录按钮
	button_log_in.click()  # 点击登录

	driver.implicitly_wait(5)#隐式等待5秒

	radio_button = driver.find_element_by_css_selector('[for="V1_CTRL53"]')# 获取校内按钮
	radio_button.click()  # 点击校内

	button_hand_in = driver.find_element_by_css_selector('.commandBar [class="command_button_content"]')  # 获取提交按钮
	button_hand_in.click()  # 点击提交

	driver.implicitly_wait(5)#隐式等待5秒

	button_good = driver.find_element_by_css_selector('.dialog_footer button')  # 获取好按钮
	button_good.click()  # 点击好

	driver.implicitly_wait(5)#隐式等待5秒

	button_ok = driver.find_element_by_css_selector('.dialog_footer button')  # 获取确定按钮
	button_ok.click()  # 点击确定
	driver.close()               # 关闭浏览器

sign_in_morning = False
sign_in_night = False

if __name__ == '__main__':
	while True:
		time_now = datetime.datetime.now()
		if time_now.hour == 8 or time_now.hour == 9 or time_now.hour == 10:
			sign_in_morning = True
			if sign_in_morning == True and sign_in_night == False:
				main()
				sign_in_morning = False
				sign_in_night = True
				print('早打卡完成')
				time.sleep(3*60*60)
		elif time_now.hour == 21 or time_now.hour == 22:
			sign_in_night=True
			if sign_in_night == True and sign_in_morning == False:
				main()
				sign_in_morning = True
				sign_in_night = False
				print('晚打卡完成')
				time.sleep(3*60*60)
		else:
			print(time_now)
			time.sleep(60)
			