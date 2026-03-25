# Simple Calculator REST API

A Python + Flask REST API that performs basic arithmetic operations: **addition**, **subtraction**, **multiplication**, and **division**.

---

## Project Structure

```
├── calculator.py   # Core Calculator class (pure logic, no dependencies)
├── app.py          # Flask REST API application
├── requirements.txt
└── README.md
```

---

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the server
python app.py
```

The server runs at `http://127.0.0.1:5000` by default.

---

## API Reference

All endpoints accept **JSON** bodies and return **JSON** responses.

### Individual operation endpoints

| Method | Endpoint      | Description    |
|--------|---------------|----------------|
| POST   | `/add`        | a + b          |
| POST   | `/subtract`   | a − b          |
| POST   | `/multiply`   | a × b          |
| POST   | `/divide`     | a ÷ b          |

**Request body (all four endpoints):**
```json
{ "a": 10, "b": 4 }
```

**Success response (200):**
```json
{
  "operation": "addition",
  "a": 10,
  "b": 4,
  "result": 14
}
```

**Error response (400):**
```json
{ "error": "Division by zero is not allowed." }
```

---

### Unified endpoint

| Method | Endpoint      | Description                        |
|--------|---------------|------------------------------------|
| POST   | `/calculate`  | Pick any operation in the body     |

**Request body:**
```json
{ "operation": "divide", "a": 10, "b": 4 }
```
`operation` must be one of: `add`, `subtract`, `multiply`, `divide`.

---

## Example cURL Calls

```bash
# Addition
curl -X POST http://127.0.0.1:5000/add \
     -H "Content-Type: application/json" \
     -d "{\"a\": 10, \"b\": 5}"

# Subtraction
curl -X POST http://127.0.0.1:5000/subtract \
     -H "Content-Type: application/json" \
     -d "{\"a\": 10, \"b\": 5}"

# Multiplication
curl -X POST http://127.0.0.1:5000/multiply \
     -H "Content-Type: application/json" \
     -d "{\"a\": 10, \"b\": 5}"

# Division
curl -X POST http://127.0.0.1:5000/divide \
     -H "Content-Type: application/json" \
     -d "{\"a\": 10, \"b\": 5}"

# Unified endpoint
curl -X POST http://127.0.0.1:5000/calculate \
     -H "Content-Type: application/json" \
     -d "{\"operation\": \"multiply\", \"a\": 6, \"b\": 7}"
```
