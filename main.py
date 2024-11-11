import qrcode
import argparse
import os

def generate_qr_code(url, output_dir='qr_codes'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    img = qrcode.make(url)
    img_path = os.path.join(output_dir, 'qr_code.png')
    img.save(img_path)
    print(f"QR code saved at {img_path}")  # Confirmation message

if __name__ == "__main__":
    print("Starting QR code generation...")  # Added for confirmation
    parser = argparse.ArgumentParser(description="Generate a QR code for a given URL")
    parser.add_argument("--url", type=str, required=True, help="The URL to encode in the QR code")
    args = parser.parse_args()
    generate_qr_code(args.url)

