from flask import Flask, render_template, jsonify, request
import pyshorteners
import qrcode

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Generate QR Code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    img = qrcode.make(data)
    img.save('static/qr_code.png')
    return jsonify({'message': 'QR Code generated successfully', 'image_url': '/static/qr_code.png'})

# Shorten URL
@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    data = request.json.get('url')
    if not data:
        return jsonify({'error': 'No URL provided'}), 400
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(data)
    return jsonify({'shortened_url': short_url})

if __name__ == '__main__':
    app.run(debug=True)
