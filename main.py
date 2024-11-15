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

def generate_qr(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
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

def main():
    print_banner()
    print("\n[+] Type 'exit' to quit the program")
    print("[+] QR codes will be saved in 'qrcodes' folder")
    
    while True:
        print("\n" + "="*50)
        url = input("\n[>] Enter URL: ").strip()
        
        if url.lower() == 'exit':
            print("\n[+] Thanks for using QR Generator!")
            print("[+] Created by Abhiyan (github.com/abhiyanpa)")
            break
            
        if url:
            try:
                filepath = generate_qr(url)
                print(f"\n[✓] Success! QR Code saved as: {filepath}")
            except Exception as e:
                print(f"\n[✗] Error: {str(e)}")
        else:
            print("\n[✗] Please enter a valid URL")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Program terminated by user")
        print("[+] Created by Abhiyan (github.com/abhiyanpa)")
