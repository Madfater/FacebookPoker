import random
import time
import os
from patchright.sync_api import Page, sync_playwright

def login_facebook(page: Page, max_retries: int = 3, wait_time: int = 10):
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    
    for attempt in range(max_retries):
        try:
            print(f"嘗試登入，當前重試次數: {attempt + 1}/{max_retries}")
            
            # 前往 Facebook 登入頁面
            page.goto("https://www.facebook.com")
            
            # 填寫帳號和密碼
            page.query_selector("#email").type(
                email, delay=(random.randint(4, 6) + (random.randint(0, 9) / 10)) * 100
            )
            page.query_selector("#pass").type(
                password, delay=(random.randint(4, 6) + (random.randint(0, 9) / 10)) * 100
            )
            
            page.keyboard.press("Enter")
            
            page.wait_for_selector("div > div:nth-child(1) > div > div:nth-child(3) > div > a > svg", timeout=wait_time * 1000)
            print("登入成功！")
            return
        
        except Exception as e:
            print(f"嘗試失敗: {e}")
            if attempt < max_retries - 1:
                print("等待後重試...")
                time.sleep(wait_time)
            else:
                print("多次嘗試後仍然失敗，請檢查設定或網站狀態。")
                raise
    

def poke(page: Page, email_list: list):
    print("開始執行戳操作...")
    page.goto("https://www.facebook.com/pokes")
    page.wait_for_selector("div._b5a")

    poke_list = page.query_selector_all(
        "div > div:nth-child(1) > div._b5a > div._b5a > div > div._b5a"
    )

    for element in poke_list:
        if element is None:
            continue

        should_poke = False
        for email in email_list:
            find_element = f'a[href="https://www.facebook.com/{email}"]'
            try:
                if element.query_selector(find_element) is not None:
                    should_poke = True
            except Exception as e:
                print(f"查找 email 時出現錯誤: {e}")
                should_poke = False

        if not should_poke:
            continue

        try:
            poke_button = element.query_selector('div[aria-label="戳回去"]')
            if poke_button:
                poke_button.click()
                print("已成功戳回去")
        except Exception as e:
            print(f"戳回去時出現錯誤: {e}")
    
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        login_facebook(page)

        env_list = os.getenv('MY_LIST', '')
        email_list = env_list.split(',') if env_list else []
        interval = 30

        try:
            while True:
                poke(page, email_list)
                print(f"等待 {interval} 秒後重新執行...")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("程式已手動終止")
        finally:
            browser.close()

if __name__ == "__main__":
    main()
