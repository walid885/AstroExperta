# AstoExperta.py
from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')  # Move your HTML to templates folder

@app.route('/launch-gui')
def launch_gui():
    try:
        # Launch GUI.py
        subprocess.Popen(['python', 'GUI.py'])
        return jsonify({"status": "success", "message": "GUI launched successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)