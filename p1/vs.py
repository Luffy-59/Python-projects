# Vehicle Service Management System
# Problem Statement 79
# Name: Hemraj Verma
# Erp: RU-26-01328
# Section : BCA AIML

FILE_NAME = "services.txt"

# Service prices before adding GST
prices = {
    "Oil Change": 1500,
    "Wheel Alignment": 800,
    "Full Service": 4500,
    "Brake Repair": 2200
}

statuses = ["Pending", "In Progress", "Completed"]


class ServiceRecord:
    def __init__(self, reg_no, owner, vehicle, service, status="Pending"):
        self.reg_no = reg_no
        self.owner = owner
        self.vehicle = vehicle
        self.service = service
        self.status = status

    def calculate_cost(self):
        price = prices[self.service]
        gst = price * 18 / 100
        total = price + gst
        return total

    def display(self):
        print("Reg no:", self.reg_no)
        print("Owner:", self.owner)
        print("Vehicle:", self.vehicle)
        print("Service:", self.service)
        print("Cost incl. 18% GST: Rs.", format(self.calculate_cost(), ".2f"))
        print("Status:", self.status)


def save_records(records):
    file = open(FILE_NAME, "w")

    for reg_no in records:
        record = records[reg_no]
        line = (record.reg_no + "|" + record.owner + "|" +
                record.vehicle + "|" + record.service + "|" +
                record.status)
        file.write(line + "\n")

    file.close()


def load_records():
    records = {}

    try:
        file = open(FILE_NAME, "r")

        for line in file:
            details = line.strip().split("|")

            if len(details) == 5:
                reg_no = details[0]
                owner = details[1]
                vehicle = details[2]
                service = details[3]
                status = details[4]

                if service in prices and status in statuses:
                    record = ServiceRecord(reg_no, owner, vehicle, service, status)
                    records[reg_no] = record

        file.close()

    except FileNotFoundError:
        # It is normal if the file does not exist before the first save.
        pass

    return records


def add_record(records):
    reg_no = input("Reg no: ").strip().upper()

    if reg_no == "":
        print("Registration number cannot be empty.")
        return

    if reg_no in records:
        print("Record already exists.")
        return

    owner = input("Owner: ").strip()
    vehicle = input("Vehicle (Car/Bike): ").strip().title()
    service_input = input("Service: ").strip()

    service = ""

    for name in prices:
        if name.lower() == service_input.lower():
            service = name

    if service == "":
        print("Invalid service type. Choose from:")
        for name in prices:
            print("-", name)
        return

    record = ServiceRecord(reg_no, owner, vehicle, service)
    records[reg_no] = record
    save_records(records)

    print("Record added.")
    print(reg_no, "|", service, "| Cost incl. 18% GST: Rs.",
          format(record.calculate_cost(), ".2f"), "| Status:", record.status)


def view_records(records):
    reg_no = input("Reg no (press Enter to view all): ").strip().upper()

    if len(records) == 0:
        print("No records available.")

    elif reg_no == "":
        for record in records.values():
            record.display()

    elif reg_no in records:
        records[reg_no].display()

    else:
        print("No record found for", reg_no)


def update_status(records):
    reg_no = input("Reg no: ").strip().upper()

    if reg_no not in records:
        print("No record found for", reg_no)
        return

    print("Available statuses: Pending, In Progress, Completed")
    new_status_input = input("New status: ").strip()
    new_status = ""

    for status in statuses:
        if status.lower() == new_status_input.lower():
            new_status = status

    if new_status == "":
        print("Invalid status. Please choose a listed status.")
        return

    old_status = records[reg_no].status
    records[reg_no].status = new_status
    save_records(records)

    print("Status updated:", old_status, "->", new_status)


def delete_record(records):
    reg_no = input("Reg no: ").strip().upper()

    if reg_no in records:
        del records[reg_no]
        save_records(records)
        print("Record", reg_no, "deleted.")

    else:
        print("No record found for", reg_no)


def main():
    records = load_records()

    while True:
        print("\n=== Vehicle Service Management System ===")
        print("1. Add record")
        print("2. View record(s)")
        print("3. Update status")
        print("4. Delete record")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_record(records)

        elif choice == "2":
            view_records(records)

        elif choice == "3":
            update_status(records)

        elif choice == "4":
            delete_record(records)

        elif choice == "5":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
