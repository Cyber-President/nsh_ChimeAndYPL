# -*- coding: utf-8 -*-

import schedule
import time
from pygame import mixer
from mutagen.mp3 import MP3 as mp3
import play_yttlist
import pyautogui as pgui

# ソースパス

se_honrei = "./sounds/Japanese_School_Bell.ogg"  # 本鈴
se_yorei = "./sounds/harp.ogg"  # 予鈴
bgm_waltz = "./sounds/the_Farewell_Waltz.ogg"  # 別れのワルツ


# 本鈴
def play_honrei():
    mixer.init()  # 初期化
    mixer.music.load(se_honrei)
    # mp3_length = mp3(se_chime).info.length
    mixer.music.play(1)
    # time.sleep(mp3_length + 0.25)  # bug fix
    time.sleep(16)  #ogg用
    mixer.music.stop()


# 予鈴
def play_yorei():
    mixer.init()  # 初期化
    mixer.music.load(se_yorei)
    # mp3_length = mp3(se_yorei).info.length
    mixer.music.play(1)
    # time.sleep(mp3_length + 0.25)  # bug fix
    time.sleep(6)   #ogg用
    mixer.music.stop()


# 別れのワルツ
def play_waltz():
    mixer.init()  # 初期化
    mixer.music.load(bgm_waltz)
    # mp3_length = mp3(bgm_waltz).info.length
    mixer.music.play(1)
    # time.sleep(mp3_length + 0.25)  # bug fix
    time.sleep(276)   #ogg用
    mixer.music.stop()


def lunch_time():
    play_honrei()
    play_yttlist.play()


def main():
    schedule.every().day.at("09:00").do(play_honrei)  # 開門
    schedule.every().day.at("09:25").do(play_yorei)  # 朝礼開始予鈴
    schedule.every().day.at("09:30").do(play_honrei)  # 朝礼開始
    schedule.every().day.at("09:45").do(play_honrei)  # 一限開始、朝礼終了
    # schedule.every().day.at("10:30").do(play_yorei)  #一限終了予鈴
    schedule.every().day.at("10:35").do(play_honrei)  # 一限終了
    schedule.every().day.at("10:45").do(play_honrei)  # 二限開始
    # schedule.every().day.at("11:30").do(play_yorei)  #一限終了予鈴
    schedule.every().day.at("11:35").do(play_honrei)  # 二限終了
    schedule.every().day.at("11:45").do(play_honrei)  # 三限開始
    schedule.every().day.at("12:30").do(play_yorei)  # 三限終了予鈴
    schedule.every().day.at("12:35").do(lunch_time)  # 三限終了
    # schedule.every().day.at("12:35").do(play_honrei)  # 三限終了
    # schedule.every().day.at("13:10").do(play_yorei)  # 昼休み終了予鈴
    schedule.every().day.at("13:15").do(play_honrei)  # 四限開始
    schedule.every().day.at("14:00").do(play_yorei)  # 四限終了予鈴
    schedule.every().day.at("14:05").do(play_honrei)  # 四限終了
    schedule.every().day.at("14:15").do(play_honrei)  # 五限開始
    schedule.every().day.at("15:00").do(play_yorei)  # 五限終了予鈴
    schedule.every().day.at("15:05").do(play_honrei)  # 五限終了
    schedule.every().day.at("15:15").do(play_honrei)  # 六限開始
    schedule.every().day.at("16:00").do(play_yorei)  # 四限終了予鈴
    schedule.every().day.at("16:05").do(play_honrei)  # 六限終了
    # schedule.every().day.at("16:10").do(play_honrei)  # 終礼開始
    schedule.every().day.at("17:15").do(play_yorei)  # 下校予鈴、清掃開始
    schedule.every().day.at("17:25").do(play_waltz)  # 別れのワルツ
    schedule.every().day.at("17:30").do(play_honrei)  # 閉門
    # schedule.every().day.at("14:10:30").do(lunch_time) # test
    # schedule.every().day.at("22:37:00").do(play_waltz) # test

    print("****定刻アナウンスシステムへようこそ！")
    print("システムを終了するには[コントロールキー]+[C]を押してください。")
    print("システムについてのお問い合わせ、改善案はSlackへ。")

    # jobの実行監視、指定時間になったらjob関数を実行
    # 100秒に１回、カーソルを１ピクセル動かすー＞スクリーンセーバーキラー
    n = 0
    while True:
        schedule.run_pending()
        n += 1
        if n % 100 == 0:
            pgui.moveRel(1, 0, duration=0)
        time.sleep(1)


main()
