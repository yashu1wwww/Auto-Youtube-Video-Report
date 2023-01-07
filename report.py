import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'youtube123@gmail.com\n'   #replace with your your gmail
password = 'pass123$%\n'           #enter your gmail pass

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)

time.sleep(3)

url = 'https://youtu.be/kLHTtiwP4G8' #replace video which you want to report it....
driver.get(url)

time.sleep(5)

driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()

time.sleep(4)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()#dot click

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[2]/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-navigation-item-renderer/a/tp-yt-paper-item').click()#report

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[1]/yt-report-form-modal-renderer/tp-yt-paper-dialog-scrollable/div/yt-report-form-modal-content/div/yt-options-renderer/div/tp-yt-paper-radio-group/tp-yt-paper-radio-button[4]/div[2]/div/yt-formatted-string').click()#4/11(harrassment or bullying)

time.sleep(2)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/tp-yt-paper-dialog-scrollable/div/yt-report-form-modal-content/div/yt-options-renderer/div/tp-yt-paper-radio-group/tp-yt-paper-dropdown-menu[4]/tp-yt-paper-menu-button/div/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]').click()#auto choose option

time.sleep(2)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/tp-yt-paper-dialog-scrollable/div/yt-report-form-modal-content/div/yt-options-renderer/div/tp-yt-paper-radio-group/tp-yt-paper-dropdown-menu[4]/tp-yt-paper-menu-button/tp-yt-iron-dropdown/div/div/tp-yt-paper-listbox/tp-yt-paper-item[2]').click() #select first option

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-report-form-modal-renderer/div/yt-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()#next button

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[2]/yt-report-details-form-renderer/yt-report-details-form-content/div/div/tp-yt-paper-input-container/div[2]/div/tp-yt-iron-autogrow-textarea/div[2]/textarea').send_keys('these video harrassing someone')

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[2]/yt-report-details-form-renderer/div[2]/div[2]/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()#report

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[3]/yt-fancy-dismissible-dialog-renderer/div/yt-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()#close

time.sleep(30)


