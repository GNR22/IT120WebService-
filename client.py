import requests

base_url = "http://127.0.0.1:5000/students"

def main():
    print("===== STUDENT INFORMATION CLIENT =====")
    
    while True:
        try:
            user_input = input("\nEnter Student ID to search, 'update' to edit a student (or 'q' to quit): ")
            
            if user_input.lower() == 'q':
                break
            #MODIFY HERE
            # --- OPTION C: UPDATE STUDENT LOGIC ---
            elif user_input.lower() == 'update':
                update_id = input("Enter Student ID to update: ").strip()
                print("Enter new details (leave blank to skip a field):")
                
                name = input("New name: ").strip()
                course = input("New course: ").strip()
                year = input("New year level: ").strip()
                
                # Only include fields that the user actually typed values into
                payload = {}
                if name:
                    payload["name"] = name
                if course:
                    payload["course"] = course
                if year:
                    payload["year"] = int(year)
                
                print(f"Sending PUT request for ID {update_id}...")
                response = requests.put(f"{base_url}/{update_id}", json=payload)
                
                if response.status_code == 200:
                    print("Update success!")
                    print(response.json())
                elif response.status_code == 404:
                    print("Update failed: Student not found.")
                else:
                    print(f"Update failed. HTTP Status: {response.status_code}")
                    
                continue  # Skip search logic and restart loop
            
            # DO NOT TOUCH BELOW 
            # --- SEARCH STUDENT LOGIC ---
            print("Connecting to Student Web Service...")
            
            response = requests.get(f"{base_url}/{user_input}")
            
            if response.status_code == 200:
                student_data = response.json()
                
                print("Student Found!")
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
            print("Please enter a valid numeric ID or year.")

if __name__ == '__main__':
    main()