import qrcode
from datetime import datetime
import os
import random
import string

def print_banner():
    banner = """
    ╔═══════════════════════════════════════╗
    ║      URL to QR Code Generator         ║
    ║        Created by Abhiyan             ║
    ║     github.com/abhiyanpa              ║
    ╚═══════════════════════════════════════╝
    """
    print(banner)

def print_menu():
    menu = """
    [1] URL QR Code
    [2] Email QR Code
    [3] SMS QR Code
    [4] WiFi QR Code
    [5] Text QR Code
    [0] Exit
    """
    print(menu)

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    qrcodes_dir = os.path.join(script_dir, 'qrcodes')
    
    if not os.path.exists(qrcodes_dir):
        os.makedirs(qrcodes_dir)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    filename = f'qr_{timestamp}_{random_string}.png'
    
    file_path = os.path.join(qrcodes_dir, filename)
    qr_image.save(file_path)
    
    return os.path.join('qrcodes', filename)

def handle_url():
    url = input("\n[>] Enter URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url

def handle_email():
    email = input("\n[>] Enter Email: ").strip()
    subject = input("[>] Enter Subject (optional): ").strip()
    body = input("[>] Enter Message (optional): ").strip()
    
    mailto = f"mailto:{email}"
    if subject or body:
        params = []
        if subject:
            params.append(f"subject={subject}")
        if body:
            params.append(f"body={body}")
        mailto += "?" + "&".join(params)
    return mailto

def handle_sms():
    phone = input("\n[>] Enter Phone Number: ").strip()
    message = input("[>] Enter Message (optional): ").strip()
    sms = f"sms:{phone}"
    if message:
        sms += f"?body={message}"
    return sms

def handle_wifi():
    ssid = input("\n[>] Enter WiFi Name (SSID): ").strip()
    password = input("[>] Enter Password: ").strip()
    security = input("[>] Security Type (WPA/WEP/none): ").strip().upper() or "WPA"
    hidden = input("[>] Hidden Network? (y/N): ").strip().lower() == 'y'
    
    wifi = f"WIFI:S:{ssid};T:{security};P:{password}"
    if hidden:
        wifi += ";H:true"
    wifi += ";;"
    return wifi

def handle_text():
    text = input("\n[>] Enter Text: ").strip()
    return text

def main():
    print_banner()
    print("[+] QR codes will be saved in 'qrcodes' folder")
    
    while True:
        print("\n" + "="*50)
        print_menu()
        choice = input("\n[>] Select option: ").strip()
        
        try:
            if choice == '0':
                print("\n[+] Thanks for using QR Generator!")
                print("[+] Created by Abhiyan (github.com/abhiyanpa)")
                break
                
            handlers = {
                '1': ('URL', handle_url),
                '2': ('Email', handle_email),
                '3': ('SMS', handle_sms),
                '4': ('WiFi', handle_wifi),
                '5': ('Text', handle_text)
            }
            
            if choice in handlers:
                type_name, handler = handlers[choice]
                data = handler()
                if data:
                    filepath = generate_qr(data)
                    print(f"\n[✓] Success! {type_name} QR Code saved as: {filepath}")
                else:
                    print("\n[✗] No data provided")
            else:
                print("\n[✗] Invalid option")
                
        except Exception as e:
            print(f"\n[✗] Error: {str(e)}")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Program terminated by user")
        print("[+] Created by Abhiyan (github.com/abhiyanpa)")
