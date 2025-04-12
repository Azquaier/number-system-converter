"""
Module: number_system_converter
Description: A Flask web application for converting numbers between different bases.
             It supports conversion from any base between 2 and 36 to any other base within the same range.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

def convert_number(number: str, from_base: int, to_base: int) -> str:
    """
    Convert a number string from one numerical base to another.

    Args:
        number (str): The number as a string in the source base.
        from_base (int): The base of the input number (2-36).
        to_base (int): The target base for conversion (2-36).

    Returns:
        str: The converted number as a string in the target base.
             Returns error messages if conversion fails due to invalid bases or input.

    Raises:
        None: All exceptions are caught and handled gracefully.
    """
    try:
        # Convert the input number from the given base to decimal.
        decimal_number = int(number, from_base)
        
        # Ensure the target base is within supported range.
        if to_base < 2 or to_base > 36:
            return "Invalid target base! (Supported range: 2-36)"
        
        # Edge-case for zero.
        if decimal_number == 0:
            return "0"
        
        # Characters for bases up to 36.
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        # Convert from decimal to the target base.
        while decimal_number > 0:
            result = digits[decimal_number % to_base] + result
            decimal_number //= to_base
        
        return result
    except ValueError:
        # Catch conversion errors if the input number is invalid for the given base.
        return "Invalid input!"

@app.route("/", methods=["GET"])
def root():
    """
    Render the home page of the number system converter.
    
    This view renders the initial page with empty input fields and result.
    """
    return render_template("number-system-converter.html",
                           result="",
                           from_base="",
                           to_base="",
                           number="")

@app.route('/number-system-converter', methods=['GET', 'POST'])
def convert():
    """
    Handle GET and POST requests for number conversion.

    For POST requests:
        - Retrieves user input from the form.
        - Uses convert_number() to perform the conversion.
        - Renders the template with the conversion result and input values.

    For GET requests:
        - Renders the template with default empty fields.
    """
    if request.method == 'POST':
        # Retrieve base values and the number to convert from the form submission.
        try:
            from_base = int(request.form.get('fromBase', 10))
            to_base = int(request.form.get('toBase', 2))
        except ValueError:
            # If provided base values are invalid, render an error message.
            return render_template('number-system-converter.html',
                                   result="Invalid base values provided!",
                                   from_base="",
                                   to_base="",
                                   number="")
        
        number = request.form.get('inputNumber', '')
        # Get conversion result from helper function.
        result = convert_number(number, from_base, to_base)
    else:
        # GET request: initialize variables with default values.
        result, from_base, to_base, number = None, None, None, None

    return render_template('number-system-converter.html',
                           result=result,
                           from_base=from_base,
                           to_base=to_base,
                           number=number)

if __name__ == '__main__':
    # Run the Flask application. Set debug to False for production environments.
    app.run(debug=False)
