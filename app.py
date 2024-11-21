from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/launch-gui')
def launch_gui():
    try:
        # Get the absolute path to GUI.py
        gui_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GUI.py')
        # Launch GUI.py
        subprocess.Popen(['python', gui_path])
        return jsonify({"status": "success", "message": "GUI launched successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)