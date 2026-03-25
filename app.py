from flask import Flask, request, jsonify, render_template
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()


def parse_operands(data: dict):
    """Extract and validate 'a' and 'b' from request JSON."""
    a = data.get("a")
    b = data.get("b")
    if a is None or b is None:
        raise ValueError("Both 'a' and 'b' fields are required.")
    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        raise ValueError("'a' and 'b' must be numeric values.")
    return a, b


def parse_single(data: dict):
    """Extract and validate only 'a' from request JSON (unary ops)."""
    a = data.get("a")
    if a is None:
        raise ValueError("Field 'a' is required.")
    try:
        a = float(a)
    except (TypeError, ValueError):
        raise ValueError("'a' must be a numeric value.")
    return a


def success_response(operation: str, result: float, **kwargs):
    payload = {"operation": operation, "result": result}
    payload.update(kwargs)
    return jsonify(payload), 200


def error_response(message: str, status: int = 400):
    return jsonify({"error": message}), status


# ── Basic operations ──────────────────────────────────────────────────────────

@app.route("/add", methods=["POST"])
def add():
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("addition", calc.add(a, b), a=a, b=b)
    except ValueError as e:
        return error_response(str(e))


@app.route("/subtract", methods=["POST"])
def subtract():
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("subtraction", calc.subtract(a, b), a=a, b=b)
    except ValueError as e:
        return error_response(str(e))


@app.route("/multiply", methods=["POST"])
def multiply():
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("multiplication", calc.multiply(a, b), a=a, b=b)
    except ValueError as e:
        return error_response(str(e))


@app.route("/divide", methods=["POST"])
def divide():
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("division", calc.divide(a, b), a=a, b=b)
    except ValueError as e:
        return error_response(str(e))


# ── Extended operations ───────────────────────────────────────────────────────

@app.route("/modulus", methods=["POST"])
def modulus():
    """POST /modulus  — remainder of a ÷ b"""
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("modulus", calc.modulus(a, b), a=a, b=b)
    except ValueError as e:
        return error_response(str(e))


@app.route("/power", methods=["POST"])
def power():
    """POST /power  — a raised to the power b"""
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("power", calc.power(a, b), a=a, b=b)
    except ValueError as e:
        return error_response(str(e))


@app.route("/floor_divide", methods=["POST"])
def floor_divide():
    """POST /floor_divide  — integer division of a ÷ b"""
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("floor_division", calc.floor_divide(a, b), a=a, b=b)
    except ValueError as e:
        return error_response(str(e))


@app.route("/percentage", methods=["POST"])
def percentage():
    """POST /percentage  — a% of b"""
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("percentage", calc.percentage(a, b), a=a, b=b)
    except ValueError as e:
        return error_response(str(e))


@app.route("/sqrt", methods=["POST"])
def sqrt():
    """POST /sqrt  — square root of a  (unary, only 'a' required)"""
    try:
        a = parse_single(request.get_json(force=True) or {})
        return success_response("square_root", calc.sqrt(a), a=a)
    except ValueError as e:
        return error_response(str(e))


@app.route("/absolute", methods=["POST"])
def absolute():
    """POST /absolute  — absolute value of a  (unary, only 'a' required)"""
    try:
        a = parse_single(request.get_json(force=True) or {})
        return success_response("absolute_value", calc.absolute(a), a=a)
    except ValueError as e:
        return error_response(str(e))


# ── Unified endpoint ──────────────────────────────────────────────────────────

@app.route("/calculate", methods=["POST"])
def calculate():
    """
    POST /calculate  — pick any operation.
    Binary body : {"operation": "...", "a": number, "b": number}
    Unary body  : {"operation": "sqrt|absolute", "a": number}
    """
    data = request.get_json(force=True) or {}
    operation = data.get("operation", "").strip().lower()

    binary_ops = {
        "add":          calc.add,
        "subtract":     calc.subtract,
        "multiply":     calc.multiply,
        "divide":       calc.divide,
        "modulus":      calc.modulus,
        "power":        calc.power,
        "floor_divide": calc.floor_divide,
        "percentage":   calc.percentage,
    }
    unary_ops = {
        "sqrt":     calc.sqrt,
        "absolute": calc.absolute,
    }

    if operation in binary_ops:
        try:
            a, b = parse_operands(data)
            return success_response(operation, binary_ops[operation](a, b), a=a, b=b)
        except ValueError as e:
            return error_response(str(e))
    elif operation in unary_ops:
        try:
            a = parse_single(data)
            return success_response(operation, unary_ops[operation](a), a=a)
        except ValueError as e:
            return error_response(str(e))
    else:
        all_ops = list(binary_ops) + list(unary_ops)
        return error_response(f"Invalid operation '{operation}'. Choose from: {', '.join(all_ops)}.")


# ── UI & API info ─────────────────────────────────────────────────────────────

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api", methods=["GET"])
def api_info():
    return jsonify({
        "message": "Simple Calculator REST API",
        "binary_endpoints": {
            "POST /add":          {"body": {"a": "number", "b": "number"}},
            "POST /subtract":     {"body": {"a": "number", "b": "number"}},
            "POST /multiply":     {"body": {"a": "number", "b": "number"}},
            "POST /divide":       {"body": {"a": "number", "b": "number"}},
            "POST /modulus":      {"body": {"a": "number", "b": "number"}},
            "POST /power":        {"body": {"a": "number", "b": "number"}},
            "POST /floor_divide": {"body": {"a": "number", "b": "number"}},
            "POST /percentage":   {"body": {"a": "number", "b": "number"}},
        },
        "unary_endpoints": {
            "POST /sqrt":     {"body": {"a": "number"}},
            "POST /absolute": {"body": {"a": "number"}},
        },
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
