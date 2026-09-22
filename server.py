from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data: 5 students
students = [
    {"id": 1, "name": "Juan Dela Cruz", "course": "BSIT", "year": 4},
    {"id": 2, "name": "Maria Santos", "course": "BSIT", "year": 3},
    {"id": 3, "name": "Pedro Penduko", "course": "BSCS", "year": 2},
    {"id": 4, "name": "Ana Reyes", "course": "BSIS", "year": 1},
    {"id": 5, "name": "Luis Manzano", "course": "BSIT", "year": 4}
]

# Helper function to find a student by ID
def find_student(student_id):
    return next((s for s in students if s["id"] == student_id), None)

# Endpoint 1: Retrieve all students
@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(students)

# Endpoint 2: Retrieve a specific student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = find_student(student_id)
    if student:
        return jsonify(student), 200
    else:
        return jsonify({"error": "Student not found"}), 404

# Endpoint 3: Update a specific student by ID (Option C - PUT)
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = find_student(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    
    data = request.get_json()
    if data:
        # Update fields if provided in the request payload
        student["name"] = data.get("name", student["name"])
        student["course"] = data.get("course", student["course"])
        if "year" in data:
            student["year"] = int(data["year"])
            
    return jsonify({"message": f"Student {student_id} updated successfully.", "student": student}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)