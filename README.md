# Python URL to QR Generator 🔲

Simple and fast Python script to generate QR codes from URLs. Created with clean interface and organized output.

## Features
- URL to QR Code conversion 🔗
- Automatic HTTPS handling ✨
- Clean CLI interface 💻
- Organized file structure 📁

## Setup & Usage

1. Clone repo:
```bash
git clone https://github.com/abhiyanpa/python-qr.git
cd python-qr
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run script:
```bash
python main.py
```

## Requirements
```
qrcode==7.4.2
pillow==10.1.0
```

## Output
QR codes will be saved in `qrcodes` folder with timestamp and random string.
Example: `qrcodes/qr_20241115_123456_AbC123Xy.png`

## Author
Made with ❤️ by [Abhiyan P A](https://github.com/abhiyanpa)

## License
MIT
