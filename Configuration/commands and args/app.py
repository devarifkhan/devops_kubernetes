from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def show_color():
    color = "blue"  # You can change this to any color you like
    html = f"""
    <html>
        <head>
            <title>Color Display</title>
        </head>
        <body style="background-color: {color};">
            <h1>The color is {color}</h1>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)