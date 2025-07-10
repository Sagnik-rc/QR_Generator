import qrcode

def generate_upi_qr(upi_id, name, amount):
    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"
    print(f"Generated UPI Link: {upi_link}")
    
    qr = qrcode.make(upi_link)
    
    filename = "upi_qr.png"
    qr.save(filename)
    print(f"QR Code saved as '{filename}'")

if __name__ == "__main__":
    upi_id = input("Enter your UPI ID (e.g. yourname@upi): ").strip()
    name = input("Enter your name (for display in the payment app): ").strip()
    amount = input("Enter amount to request (e.g. 150.00): ").strip()
    
    generate_upi_qr(upi_id, name, amount)
