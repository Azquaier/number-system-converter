# Number System Converter

A simple Flask web application to convert numbers between different numeral systems (bases 2-36).
[→ Live Demo](https://azquaier.xyz/number-system-converter)

## Features

- Convert numbers from any base (2-36) to any other base (2-36).
- User-friendly web interface with a modern, terminal-inspired design.
- Input validation and error handling.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/number-system-converter.git
   cd number-system-converter
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install Flask
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python number_system_converter.py
   ```

2. **Access the converter:**

   Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Files

- `number_system_converter.py`: Main Flask application with the conversion logic.
- `templates/number-system-converter.html`: HTML template for the web interface.
