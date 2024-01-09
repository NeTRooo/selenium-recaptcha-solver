from selenium.webdriver.common.by import By
import speech_recognition as sr
from pydub import AudioSegment
from time import sleep
import urllib.request
import os

class ReSolver:
    def __init__(self, driver):
        self.driver = driver
        self.r = sr.Recognizer()
    
    def css_find_element(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, css_selector)
    
    def mp(self, url):
        fullname = "audio"+".mp3"
        urllib.request.urlretrieve(url,fullname)
    
    def working_with_mp3_and_solving_captcha(self):
        sleep(1)
        wavlink = self.css_find_element("body > div > div > div.rc-audiochallenge-tdownload > a").get_attribute("href")
        sleep(1)
        self.mp(url=wavlink)
        dst = "audio.wav"
        audSeg = AudioSegment.from_mp3("audio.mp3")
        audSeg.export(dst, format="wav")
        
        with sr.AudioFile(r"audio.wav") as source:
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio)
                self.driver.find_element(By.CSS_SELECTOR, "#audio-response").send_keys(text)
                self.css_find_element("#audio-response").send_keys(text)
                self.css_find_element("#recaptcha-verify-button").click()
                self.driver.find_element(By.CSS_SELECTOR, "#recaptcha-verify-button").click()
            except:
                print("Ярік бачок потік!")
        
        os.remove(r"audio.wav")
        os.remove(r"audio.mp3")
    
    def firefox_solver(self):
        sleep(1)
        element = self.css_find_element("iframe[title='reCAPTCHA']")
        self.driver.switch_to.frame(element)
        element = self.css_find_element('input[type="hidden"]')
        self.driver.execute_script("arguments[0].removeAttribute('type');", element)
        self.css_find_element('#recaptcha-token').click()
        self.driver.switch_to.default_content()
        element = self.css_find_element("iframe[title='recaptcha challenge expires in two minutes']")
        self.driver.switch_to.frame(element)
        sleep(1)
        self.css_find_element("#recaptcha-audio-button").click()
        self.working_with_mp3_and_solving_captcha()
    
    def chrome_solver(self):
        qframe = self.css_find_element("iframe").get_attribute("name")
        self.css_find_element("iframe").click()
        self.driver.find_element(By.NAME, qframe).click()
        sleep(1)
        qframe = self.driver.find_elements(By.CSS_SELECTOR, "iframe")[2].get_attribute("name")
        self.driver.switch_to.frame(qframe)
        self.css_find_element("#recaptcha-audio-button").click()
        self.working_with_mp3_and_solving_captcha()