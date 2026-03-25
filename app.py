from flask import Flask, request, jsonify
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


def success_response(operation: str, a: float, b: float, result: float):
    return jsonify({
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }), 200


def error_response(message: str, status: int = 400):
    return jsonify({"error": message}), status


@app.route("/add", methods=["POST"])
def add():
    """POST /add  — Body: {"a": number, "b": number}"""
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("addition", a, b, calc.add(a, b))
    except ValueError as e:
        return error_response(str(e))


@app.route("/subtract", methods=["POST"])
def subtract():
    """POST /subtract  — Body: {"a": number, "b": number}"""
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("subtraction", a, b, calc.subtract(a, b))
    except ValueError as e:
        return error_response(str(e))


@app.route("/multiply", methods=["POST"])
def multiply():
    """POST /multiply  — Body: {"a": number, "b": number}"""
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("multiplication", a, b, calc.multiply(a, b))
    except ValueError as e:
        return error_response(str(e))


@app.route("/divide", methods=["POST"])
def divide():
    """POST /divide  — Body: {"a": number, "b": number}"""
    try:
        a, b = parse_operands(request.get_json(force=True) or {})
        return success_response("division", a, b, calc.divide(a, b))
    except ValueError as e:
        return error_response(str(e))


@app.route("/calculate", methods=["POST"])
def calculate():
    """
    POST /calculate  — unified endpoint.
    Body: {"operation": "add|subtract|multiply|divide", "a": number, "b": number}
    """
    data = request.get_json(force=True) or {}
    operation = data.get("operation", "").strip().lower()
    ops = {
        "add":      calc.add,
        "subtract": calc.subtract,
        "multiply": calc.multiply,
        "divide":   calc.divide,
    }
    if operation not in ops:
        return error_response(
            f"Invalid operation '{operation}'. Choose from: {', '.join(ops)}."
        )
    try:
        a, b = parse_operands(data)
        return success_response(operation, a, b, ops[operation](a, b))
    except ValueError as e:
        return error_response(str(e))


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Simple Calculator REST API",
        "endpoints": {
            "POST /add":       {"body": {"a": "number", "b": "number"}},
            "POST /subtract":  {"body": {"a": "number", "b": "number"}},
            "POST /multiply":  {"body": {"a": "number", "b": "number"}},
            "POST /divide":    {"body": {"a": "number", "b": "number"}},
            "POST /calculate": {"body": {"operation": "add|subtract|multiply|divide", "a": "number", "b": "number"}},
        }
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
