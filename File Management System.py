# Import the os module to interact with the file system/operating system
import os

# Define a function to create the project structure
def create_project_structure(root_dir):
    # Create the main project directory if it doesn't exist
    os.makedirs(root_dir, exist_ok=True)

    # Defining a list subdirectories/folders for the project
    folders = ['documents', 'source_code', 'data', 'reports']
    
    # Iterating through each folder and Create subdirectories within the main project directory
    for folder in folders:
        os.makedirs(os.path.join(root_dir, folder), exist_ok=True)

    # Create specific files within each folder
    with open(os.path.join(root_dir, 'documents', 'README.md'), 'w') as f:
        f.write("# Solar Energy Sharing DApp\n\nThis folder contains project documents.")

    with open(os.path.join(root_dir, 'source_code', 'main.py'), 'w') as f:
        f.write("# DApp Codes - Main Code\n\n# Add your main code here")

    with open(os.path.join(root_dir, 'data', 'data.csv'), 'w') as f:
        f.write("Placeholder,data\n1,example_data")

    with open(os.path.join(root_dir, 'reports', 'progress_report.txt'), 'w') as f:
        f.write("Progress Report\n\n- Week 1: Started project planning.")

    # Print a message indicating the successful creation of the project structure
    print("Project structure created successfully.")

# Define the main function
def main():
    # Prompt the user to input the project name
    project_name = input("Enter project name: ")
    
    # Define the root directory for the project based on the user input
    root_dir = os.path.join(os.getcwd(), project_name)
    
    # Call the function to create the project structure
    create_project_structure(root_dir)

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()
