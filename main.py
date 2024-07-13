# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Form results
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # getting the selected image
        selected_image = request.form.get('image-selector')

        # Assignment #2.Receiving the text
        top_text = request.form.get('textTop')
        bottom_text = request.form.get('textBottom')

        # Assignment #3. Receiving the text's positioning
        selected_color = request.form.get('color-selector')
        top_text_y = request.form.get('textTop_y')
        bottom_text_y = request.form.get('textBottom_y')

        # Assignment #3. Receiving the text's colour
        

        return render_template('index.html', 
                               # Displaying the selected  image
                               selected_image=selected_image, 

                               # Assignment #2. Displaying the text
                               top_text=top_text,
                               bottom_text=bottom_text,

                               # Assignment #3. Displaying the colour 
                               selected_color=selected_color,
                               top_text_y=top_text_y,
                               bottom_text_y=bottom_text_y
                               
                               # Assignment #3. Displaying the text's positioning

                               )
    else:
        # Displaying the first image by default
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
