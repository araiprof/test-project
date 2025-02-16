import os
from flask import Flask, render_template, request, send_file
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'

        if file and allowed_file(file.filename):
            try:
                # Secure the filename
                filename = secure_filename(file.filename)
                file_ext = filename.rsplit('.', 1)[1].lower()

                if file_ext in ['jpg', 'jpeg']:
                    # Save the JPEG file
                    jpeg_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(jpeg_path)

                    # Convert to PNG
                    png_filename = os.path.splitext(filename)[0] + '.png'
                    png_path = os.path.join(app.config['UPLOAD_FOLDER'], png_filename)

                    with Image.open(jpeg_path) as img:
                        img.save(png_path, 'PNG')

                    # Clean up the JPEG file
                    os.remove(jpeg_path)

                    # Verify PNG exists before sending
                    if os.path.exists(png_path):
                        return send_file(png_path, as_attachment=True)
                    else:
                        return 'Error: Converted file not found'

                elif file_ext == 'png':
                    # If it's already a PNG, just save and send it
                    png_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(png_path)
                    return send_file(png_path, as_attachment=True)

            except Exception as e:
                return f'Error processing file: {str(e)}'

        return 'Invalid file type. Please upload a JPEG or PNG file.'

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)