# Python Multi-Format QR Generator 🔲

A Python CLI tool to generate QR codes in multiple formats. Clean interface with organized output structure.

## 📸 Screenshots

<details>
<summary>Click to see screenshots</summary>

### Main Menu
<img width="307" alt="{F19F01C8-59DE-40CB-9E8E-BADA6D926E85}" src="https://github.com/user-attachments/assets/8ba3f92a-bdae-4d17-9f55-56bca3ad6dd2">

### URL QR Generation
<img width="434" alt="{C10E7BDC-FB83-4341-A285-E3A750BE3FF7}" src="https://github.com/user-attachments/assets/44949030-bb74-47aa-91e7-0f27c9df6449">

### WiFi QR Generation
<img width="438" alt="{445C3324-54B0-4E57-9032-7BDFD1CFC8C1}" src="https://github.com/user-attachments/assets/ce012783-1011-4478-b972-1fabbd22650a">


</details>

## ✨ Features
- Multiple QR formats supported:
  - URL QR Codes 🔗
  - Email QR Codes 📧
  - SMS QR Codes 📱
  - WiFi QR Codes 📶
  - Text QR Codes 📝
- Automatic data formatting
- Clean CLI interface
- Organized output structure

## 🛠️ Setup & Usage

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

## 📋 Requirements
```
qrcode==7.4.2
pillow==10.1.0
```

## 📂 Output
QR codes are saved in `qrcodes` folder with timestamp.
Example: `qrcodes/qr_20241115_123456_AbC123Xy.png`

## 👤 Author
Made with ❤️ by [Abhiyan P A](https://github.com/abhiyanpa)

## 📄 License
MIT
