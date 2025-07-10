# UPI QR Code Generator

This is a simple Python script that generates a UPI payment QR code based on user input. It asks for your UPI ID, name, and the amount to request, then creates a QR code that can be scanned in any UPI-compatible payment app (like Google Pay, PhonePe, Paytm, etc.) for quick payment.

## 📌 Purpose

> ⚠️ **This is a basic test-run project** created as a foundational step toward a more feature-rich UPI-based payment system that will be part of a major project in the upcoming days.

## 🚀 Features

- Generate a UPI payment link using user input
- Create and save a scannable QR code as an image file (`upi_qr.png`)
- Minimal, clean CLI interaction

## 📦 Requirements

- Python 3.x
- `qrcode` library

To install the required package, run:

```
pip install qrcode[pil]
```

## 🛠️ How to Run

1. Clone or download this repository.
2. Open your terminal and navigate to the project folder.
3. Run the script:

```
python upi_qr_generator.py
```

4. Enter your:

 - UPI ID (e.g., yourname@upi) 
 - Name (for display in the payment app)
 - Amount (e.g., 150.00)

5. The script will:

- Display the UPI link in the console

- Save a QR code image as upi_qr.png

📂 Output
A file named upi_qr.png will be created in your working directory. You can scan this using any UPI app to initiate the payment.

## 📌 Note
This is just a prototype or test version. The final version will be integrated into a React-based website with UPI payment support for real-world applications.

Stay tuned for updates!