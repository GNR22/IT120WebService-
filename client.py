import requests

BASE_URL = "http://127.0.0.1:5000/students"

def main():
    print("===== STUDENT INFORMATION CLIENT =====")
    
    while True:
        try:
            print("\nOptions:")
            print(" - Type a Student ID (e.g., 1) to search for one student")
            print(" - Type 'all' to get all 5 students")
            print(" - Type 'add' to add a new student")
            print(" - Type 'update' to edit a student")
            print(" - Type 'delete' to remove a student")
            print(" - Type 'q' to quit")
            
            user_input = input("\nEnter your choice: ").strip().lower()
            
            if user_input == 'q':
                break
                
            elif user_input == 'all':
                print("Sending request for ALL students...")
                response = requests.get(BASE_URL)
                if response.status_code == 200:
                    students = response.json()
                    print(f"\n--- ALL STUDENTS ({len(students)}) ---")
                    for s in students:
                        print(f"[{s['id']}] {s['name']} - {s['course']} Year {s['year']}")
                else:
                    print("Failed to retrieve students.")
            
            elif user_input == 'add':
                print("\n--- ADD STUDENT ---")
                name = input("Name: ").strip()
                course = input("Course: ").strip()
                year = input("Year level: ").strip()
                
                new_student = {
                    "name": name, 
                    "course": course, 
                    "year": int(year)
                }
                
                print("Sending POST request...")
                response = requests.post(BASE_URL, json=new_student)
                
                if response.status_code == 201:
                    print("Successfully added!")
                    print(response.json())
                else:
                    print("Failed to add.")
                    
            elif user_input == 'update':
                print("\n--- UPDATE STUDENT ---")
                update_id = input("Enter Student ID to update: ").strip()
                print("Enter new details (leave blank to skip a field):")
                name = input("New name: ").strip()
                course = input("New course: ").strip()
                year = input("New year level: ").strip()
                
                payload = {}
                if name: payload["name"] = name
                if course: payload["course"] = course
                if year: payload["year"] = int(year)
                
                print(f"Sending PUT request for ID {update_id}...")
                response = requests.put(f"{BASE_URL}/{update_id}", json=payload)
                
                if response.status_code == 200:
                    print("Update success!")
                    print(response.json())
                elif response.status_code == 404:
                    print("Update failed: Student not found.")
                else:
                    print(f"Update failed. HTTP Status: {response.status_code}")
                    
            elif user_input == 'delete':
                print("\n--- DELETE STUDENT ---")
                delete_id = input("Enter Student ID to delete: ").strip()
                print(f"Sending DELETE request for ID {delete_id}...")
                response = requests.delete(f"{BASE_URL}/{delete_id}")
                
                if response.status_code == 200:
                    print("Successfully deleted!")
                elif response.status_code == 404: 
                    print("Delete failed: Student not found.")
                else: 
                    print(f"Delete failed. HTTP Status: {response.status_code}")
                    
            else:
                # Assume the user typed an ID to search
                if not user_input.isdigit():
                    print("Invalid option. Please try again.")
                    continue
                    
                print("Connecting to Student Web Service...")
                response = requests.get(f"{BASE_URL}/{user_input}")
                
                if response.status_code == 200:
                    student_data = response.json()
                    print("\n--- STUDENT FOUND ---")
                    print(f"ID: {student_data['id']}")
                    print(f"Name: {student_data['name']}")
                    print(f"Course: {student_data['course']}")
                    print(f"Year Level: {student_data['year']}")
                elif response.status_code == 404:
                    print("Student not found.")
                else:
                    print(f"Unexpected error. HTTP Status: {response.status_code}")
                    
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to the server. Is the Flask app running?")
            break
        except ValueError:
            print("Invalid number entered for year.")

if __name__ == '__main__':
    main()