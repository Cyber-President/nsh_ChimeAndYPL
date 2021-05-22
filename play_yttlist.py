# -*- coding: utf-8 -*-

from selenium.webdriver import Chrome, ChromeOptions
import pyautogui
import time

# Youtube再生リスト
url = ""


def play():
    # 画面上部｢自動テストソフトソフトウェアによって制御されています｣の表示を消す
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])  # ['disable-automation']にすると戻る

    # 拡張機能のCRXパス、ChromeDriverの絶対パスを指定しChromeを起動
    options.add_extension('ChromeExtensions/2.0.0_0.crx')
    driver = Chrome('/Users/commuteta76/Documents/AnnounceSystem/ChromeExtensions/chromedriver', options=options)

    # ウィンドウを開く
    driver.maximize_window()
    driver.get(url)

    # 再生ページへ遷移
    time.sleep(1)
    driver.find_element_by_link_text("すべて再生").click()

    # 全画面表示
    time.sleep(1)
    pyautogui.press('f')

    # 起動時間を指定（秒)
    time.sleep(2350)

    # セッション終了
    driver.close()

