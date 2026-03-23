import pyautogui
import time
import random
import sys

print("=== 防休眠滑鼠移動程式啟動 ===")
print("按 Ctrl+C 可以隨時關閉程式")
print("目前設定為：每 60 秒到 180 秒隨機移動一次滑鼠")

# 這裡設定螢幕解析度的中心點，避免滑鼠跑到螢幕外面
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 2, screen_height // 2

try:
    while True:
        # 決定要移動的偏移量 (隨機微調)
        offset_x = random.randint(-50, 50)
        offset_y = random.randint(-50, 50)
        
        target_x = center_x + offset_x
        target_y = center_y + offset_y
        
        # 移動滑鼠，duration 是移動花費的時間，讓動作稍微自然一點
        pyautogui.moveTo(target_x, target_y, duration=0.5)
        
        # 隨機捲動頁面 (模擬人類滾動滾輪，正數向上，負數向下)
        scroll_amount = random.randint(-5, 5) * 10
        if scroll_amount != 0:
            pyautogui.scroll(scroll_amount)
            
        # 輕微點擊一下鍵盤 (Shift) 也是防止休眠的好方法，不會影響大部分操作
        pyautogui.press('shift')
        
        # 印出時間讓您知道程式還活著
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"[{current_time}] 滑鼠移動至 ({target_x}, {target_y})，捲動了 {scroll_amount} 單位，並觸發 Shift 鍵")
        
        # 隨機等待 1 到 3 分鐘 (60~180 秒) 不等，讓動作不像機器人
        sleep_time = random.randint(60, 180)
        print(f"等待 {sleep_time} 秒後進行下一次移動...")
        time.sleep(sleep_time)

except KeyboardInterrupt:
    print("\n\n=== 程式已手動終止 ===")
    sys.exit()
