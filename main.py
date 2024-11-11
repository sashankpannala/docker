import qrcode
import argparse
import os

def generate_qr_code(url, filename, output_dir='qr_codes'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    img = qrcode.make(url)
    img_path = os.path.join(output_dir, filename)
    img.save(img_path)
    print(f"QR code saved at {img_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate QR codes for multiple URLs")
    parser.add_argument("--url1", type=str, required=True, help="The first URL to encode in a QR code")
    parser.add_argument("--url2", type=str, required=True, help="The second URL to encode in a QR code")
    parser.add_argument("--filename1", type=str, default="qr_code1.png", help="The filename for the first QR code image")
    parser.add_argument("--filename2", type=str, default="qr_code2.png", help="The filename for the second QR code image")
    args = parser.parse_args()
    
    # Generate the first QR code
    generate_qr_code(args.url1, args.filename1)
    
    # Generate the second QR code
    generate_qr_code(args.url2, args.filename2)

