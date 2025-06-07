import requests
import time

# Danh sách endpoint cho chế độ chạy nhiều
endpoints = [
    "cron/momo.php",
    "cron/bank.php",
    "cron/thesieure.php",
    "cron/zalopay.php",
    "cron/cron.php",
    "cron/checklivefb.php",
    "cron/cron1.php",
    "cron/cron2.php",
    "cron/nowpayments.php",
    "cron/cron3.php",
    "cron/cron4.php",
    "cron/cron_dongvanfb.php",
    "cron/cron6.php",
    "cron/sending_email.php",
    "cron/cron7.php",
    "cron/UpdateRateService.php",
    "cron/UpdateHistoryService.php",
    "cron/cron8.php",
    "cron/cron9.php"
]

def run_single():
    url = input("Nhập URL cần chạy: ").strip()
    delay_ms = int(input("Nhập thời gian delay (ms): ").strip())

    print(f"👉 Đang chạy: {url} mỗi {delay_ms}ms. Nhấn Ctrl+C để dừng.")
    while True:
        try:
            response = requests.get(url)
            print(f"[{time.strftime('%H:%M:%S')}] ✅ {url} - {response.status_code}")
            time.sleep(delay_ms / 1000.0)
        except Exception as e:
            print(f"❌ Lỗi khi gọi {url}: {e}")
            time.sleep(delay_ms / 1000.0)

def run_multi():
    domain = input("Nhập domain (ví dụ: vessy.pro.vn): ").strip()
    delay_ms = 5000  # delay mặc định giữa mỗi vòng (5s)

    full_urls = [f"http://{domain}/{path}" for path in endpoints]

    print("👉 Bắt đầu chạy nhiều cron job. Nhấn Ctrl+C để dừng.")
    while True:
        for url in full_urls:
            try:
                response = requests.get(url)
                print(f"[{time.strftime('%H:%M:%S')}] ✅ {url} - {response.status_code}")
            except Exception as e:
                print(f"❌ {url} lỗi: {e}")
        print(f"⏳ Đợi {delay_ms}ms trước vòng tiếp theo...\n")
        time.sleep(delay_ms / 1000.0)

def main():
    print("=== TOOL CHẠY CRON ===")
    print("1. Chạy một link")
    print("2. Chạy nhiều link tự động")
    choice = input("Chọn chế độ (1 hoặc 2): ").strip()

    if choice == "1":
        run_single()
    elif choice == "2":
        run_multi()
    else:
        print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
    