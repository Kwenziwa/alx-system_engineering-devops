import requests
import sys

# Function to fetch employee data
def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    employee_data = employee_response.json()
    todos_data = todos_response.json()
    return employee_data, todos_data

# Function to calculate and display progress
def display_progress(employee_data, todos_data):
    employee_name = employee_data["name"]
    completed_tasks = [task for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todos_data = get_employee_data(employee_id)
    display_progress(employee_data, todos_data)
