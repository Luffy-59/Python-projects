# ============================================================
# PS Number: 79
# Project Title: Vehicle Service Management System
# Student Name: Hemraj verma
# Email: himanshupatel5599@gmail.com
# Section: BCA 1A
# ERP: RU-26-01328
# ============================================================

# Defining the file used to store service records
FILE_NAME = "services.txt"

# Storing the service prices before adding GST
# Service prices before adding GST
prices = {
    "Oil Change": 1500,
    "Wheel Alignment": 800,
    "Full Service": 4500,
    "Brake Repair": 2200
}

# Defining the available service statuses
statuses = ["Pending", "In Progress", "Completed"]


# Class 1: Store the details of a vehicle service record
class ServiceRecord:
    # Initializing the service record details
    def __init__(self, reg_no, owner, vehicle, service, status="Pending"):
        self.reg_no = reg_no
        self.owner = owner
        self.vehicle = vehicle
        self.service = service
        self.status = status

    # Function 1: Calculate the service cost including GST
    def calculate_cost(self):
        # Getting the price of the selected service
        price = prices[self.service]
        # Calculating 18 percent GST on the service price
        gst = price * 18 / 100
        # Adding GST to the original service price
        total = price + gst
        return total

    # Function 2: Display all details of a service record
    def display(self):
        # Displaying the registration number and record details
        print("Reg no:", self.reg_no)
        print("Owner:", self.owner)
        print("Vehicle:", self.vehicle)
        print("Service:", self.service)
        print("Cost incl. 18% GST: Rs.", format(self.calculate_cost(), ".2f"))
        print("Status:", self.status)


# Function 3: Save all service records into a text file
def save_records(records):
    # Opening the file in write mode
    file = open(FILE_NAME, "w")

    # Going through each service record
    for reg_no in records:
        # Getting the record using its registration number
        record = records[reg_no]
        # Combining the record details into a single line
        line = (record.reg_no + "|" + record.owner + "|" +
                record.vehicle + "|" + record.service + "|" +
                record.status)
        # Writing the record into the file
        file.write(line + "\n")

    # Closing the file after saving the records
    file.close()


# Function 4: Load saved service records from the text file
def load_records():
    # Creating an empty dictionary to store service records
    records = {}

    try:
        # Opening the file in read mode
        file = open(FILE_NAME, "r")

        # Reading each saved record one line at a time
        for line in file:
            # Splitting the line into individual record details
            details = line.strip().split("|")

            # Checking whether all five record fields are present
            if len(details) == 5:
                reg_no = details[0]
                owner = details[1]
                vehicle = details[2]
                service = details[3]
                status = details[4]

                # Checking whether service and status values are valid
                if service in prices and status in statuses:
                    # Creating a service record object from saved details
                    record = ServiceRecord(reg_no, owner, vehicle, service, status)
                    # Adding the loaded record to the dictionary
                    # Adding the new record to the dictionary
                    records[reg_no] = record

        file.close()

    except FileNotFoundError:
        # It is normal if the file does not exist before the first save.
        pass

    return records


# Function 5: Add a new vehicle service record
def add_record(records):
    # Taking the vehicle registration number from the user
    reg_no = input("Reg no: ").strip().upper()

    # Checking whether the registration number is empty
    if reg_no == "":
        print("Registration number cannot be empty.")
        return

    # Checking whether a record already exists for this registration number
    # Checking whether the registration number exists in the records
    if reg_no in records:
        print("Record already exists.")
        return

    # Taking the vehicle owner's name and vehicle details
    owner = input("Owner: ").strip()
    vehicle = input("Vehicle (Car/Bike): ").strip().title()
    # Taking the requested service type from the user
    service_input = input("Service: ").strip()

    # Initializing the service name before validation
    service = ""

    # Matching the entered service with the available services
    for name in prices:
        if name.lower() == service_input.lower():
            service = name

    # Checking whether the entered service type is valid
    if service == "":
        print("Invalid service type. Choose from:")
        for name in prices:
            print("-", name)
        return

    # Creating a new service record
    record = ServiceRecord(reg_no, owner, vehicle, service)
    records[reg_no] = record
    save_records(records)

    print("Record added.")
    print(reg_no, "|", service, "| Cost incl. 18% GST: Rs.",
          format(record.calculate_cost(), ".2f"), "| Status:", record.status)


# Function 6: View one service record or all service records
def view_records(records):
    # Taking a registration number or allowing the user to view all records
    reg_no = input("Reg no (press Enter to view all): ").strip().upper()

    # Checking whether any service records are available
    if len(records) == 0:
        print("No records available.")

    # Displaying all records when no registration number is entered
    elif reg_no == "":
        for record in records.values():
            record.display()

    # Displaying the record matching the entered registration number
    elif reg_no in records:
        records[reg_no].display()

    else:
        print("No record found for", reg_no)


# Function 7: Update the status of an existing service record
def update_status(records):
    reg_no = input("Reg no: ").strip().upper()

    # Checking whether the requested service record exists
    if reg_no not in records:
        print("No record found for", reg_no)
        return

    # Showing the available service statuses
    print("Available statuses: Pending, In Progress, Completed")
    # Taking the new status from the user
    new_status_input = input("New status: ").strip()
    # Initializing the new status before validation
    new_status = ""

    # Matching the entered status with the available status list
    for status in statuses:
        if status.lower() == new_status_input.lower():
            new_status = status

    # Checking whether the entered status is valid
    if new_status == "":
        print("Invalid status. Please choose a listed status.")
        return

    # Storing the previous status before updating it
    old_status = records[reg_no].status
    # Updating the service record with the new status
    records[reg_no].status = new_status
    save_records(records)

    print("Status updated:", old_status, "->", new_status)


# Function 8: Delete a service record using its registration number
def delete_record(records):
    reg_no = input("Reg no: ").strip().upper()

    if reg_no in records:
        # Removing the selected service record
        del records[reg_no]
        save_records(records)
        print("Record", reg_no, "deleted.")

    else:
        print("No record found for", reg_no)


# Function 9: Main function to control the service management menu
def main():
    # Loading previously saved service records when the program starts
    records = load_records()

    # Repeating the menu until the user chooses to exit
    while True:
        # Displaying the main menu options
        print("\n=== Vehicle Service Management System ===")
        print("1. Add record")
        print("2. View record(s)")
        print("3. Update status")
        print("4. Delete record")
        print("5. Exit")

        # Taking the user's menu choice
        choice = input("Choose an option: ").strip()

        # Calling the function to add a service record
        if choice == "1":
            add_record(records)

        # Calling the function to view service records
        elif choice == "2":
            view_records(records)

        # Calling the function to update a service status
        elif choice == "3":
            update_status(records)

        # Calling the function to delete a service record
        elif choice == "4":
            delete_record(records)

        # Exiting the program
        elif choice == "5":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 5.")


# Starting the program by calling the main function
if __name__ == "__main__":
    main()