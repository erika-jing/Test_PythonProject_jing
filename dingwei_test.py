from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = '1900b0101eb60122'
desired_caps['appPackage'] = 'com.smartcar.music'
desired_caps['appActivity'] = 'com.smartcar.music.ui.activity.MainActivity'
desired_caps['dontStopAppOnRest']='true'
#客户端和服务端建立连接，发送desire_capsjson信息，被测设备信息
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

driver.find_element_by_id("com.smartcar.music:id/search_music").click()
#隐世等待
driver.implicitly_wait(2)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout").click()

#点击音乐搜索框，输入哈哈哈哈
driver.implicitly_wait(2)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout").send_keys("haha")
# driver.find_elements_by_link_text("后来").click()
#强制等待
time.sleep(4)
driver.quit()
