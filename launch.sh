!/bin/bash

# Set up virtual environment and project paths
PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_NAME=".venv"

# Function to check and activate virtual environment
activate_venv() {
    if [ ! -d "$PROJECT_DIR/$VENV_NAME" ]; then
        echo "Creating virtual environment..."
        python3 -m venv "$PROJECT_DIR/$VENV_NAME"
    fi

    source "$PROJECT_DIR/$VENV_NAME/bin/activate"
    echo "Virtual environment activated."
}

# Function to install dependencies
install_dependencies() {
    # Install required packages
    pip install flask pandas seaborn matplotlib
    echo "Dependencies installed successfully."
}

# Function to run the Flask application
run_flask_app() {
    echo "Starting Flask application..."
    python "$PROJECT_DIR/app.py" &
    FLASK_PID=$!
    sleep 2  # Give Flask a moment to start
}

# Main launch function
launch_project() {
    clear
    echo "🚀 AstroAcademy Project Launcher 🌌"
    echo "-----------------------------------"

    activate_venv
    install_dependencies

    run_flask_app

    echo "Open your web browser and navigate to http://localhost:5000"
    echo "PID of Flask application: $FLASK_PID"

    # Keep script running and allow graceful shutdown
    trap "kill $FLASK_PID; deactivate; exit 0" SIGINT SIGTERM

    # Wait for Flask process
    wait $FLASK_PID
}

# Execute the launch function
launch_project 