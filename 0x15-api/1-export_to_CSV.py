import requests
import csv
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
    user_id = employee_data["id"]
    completed_tasks = [task for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)

    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

    # Write tasks to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            csv_writer.writerow([user_id, employee_name, task["completed"], task["title"]])

    print(f"Task data has been exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int
