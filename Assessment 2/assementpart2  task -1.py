# Manages requisitions from creation to approval.
class RequisitionSystem:

    next_id = 10001
    requisitions = []

    def __init__(self, date, staff_id, staff_name, items):
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.items = items
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"

        self.requisition_id = RequisitionSystem.next_id
        RequisitionSystem.next_id += 1

        RequisitionSystem.requisitions.append(self)

    def staff_info(self, date=None, staff_id=None, staff_name=None):

        if date:
            self.date = date

        if staff_id:
            self.staff_id = staff_id

        if staff_name:
            self.staff_name = staff_name

    def requisitions_details(self, items=None):
        # Add the cost of each item.
        if items is not None:
            self.items = items

        self.total = 0

        for item in self.items:
            description = item[0]
            cost = item[1]
            self.total = self.total + cost

        return self.total

    def requisition_approval(self):
        # Approve requests below the spending limit.
        if self.total < 500:
            self.status = "Approved"

            # Last 3 digits of requisition ID
            last_three = str(self.requisition_id)[-3:]

            self.approval_ref = self.staff_id + last_three

        else:
            self.status = "Pending"
            self.approval_ref = "Not available"

    def respond_requsition(self, decision):

        if self.status == "Pending":

            if decision == "Approved":
                self.status = "Approved"

                last_three = str(self.requisition_id)[-3:]
                self.approval_ref = self.staff_id + last_three

            elif decision == "Not approved":
                self.status = "Not approved"
                self.approval_ref = "Not available"

            else:
                print("Invalid decision.")

        else:
            print("This requisition is not pending.")

    @classmethod
    def display_requisitons(cls):

        if len(cls.requisitions) == 0:
            print("No requisitions to display.")
            return

        for req in cls.requisitions:

            print("Date:", req.date)
            print("Requisition ID:", req.requisition_id)
            print("Staff ID:", req.staff_id)
            print("Staff Name:", req.staff_name)
            print("Total: ${:.2f}".format(req.total))
            print("Status:", req.status)
            print("Approval Reference Number:", req.approval_ref)
            print()

    @classmethod
    def requisition_statistic(cls):

        total = len(cls.requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for req in cls.requisitions:

            if req.status == "Approved":
                approved = approved + 1

            elif req.status == "Pending":
                pending = pending + 1

            elif req.status == "Not approved":
                not_approved = not_approved + 1

        return total, approved, pending, not_approved

    @classmethod
    def print_statistics(cls):

        total, approved, pending, not_approved = cls.requisition_statistic()

        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", total)
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)
        print()


# ==================== TESTING ====================

if __name__ == "__main__":

    #  1
    items1 = [
        ("Laptop bag", 45),
        ("Mouse", 25)
    ]

    req1 = RequisitionSystem(
        "03/04/2024",
        "FN19",
        "John Paul",
        items1
    )

    req1.requisitions_details()
    req1.requisition_approval()


    items2 = [
        ("Monitor", 300),
        ("Keyboard", 120),
        ("Webcam", 80)
    ]

    req2 = RequisitionSystem(
        "05/04/2024",
        "FN20",
        "Tracy Brown",
        items2
    )

    req2.requisitions_details()
    req2.requisition_approval()


    items3 = [
        ("Printer", 350),
        ("Ink cartridges", 150),
        ("Paper", 50)
    ]

    req3 = RequisitionSystem(
        "07/05/2024",
        "FN15",
        "Emma Wellington",
        items3
    )

    req3.requisitions_details()
    req3.requisition_approval()


    
    items4 = [
        ("USB hub", 30),
        ("Cable", 15),
        ("Adapter", 25)
    ]

    req4 = RequisitionSystem(
        "03/05/2024",
        "FN02",
        "Catlin White",
        items4
    )

    req4.requisitions_details()
    req4.requisition_approval()


    
    items5 = [
        ("Tablet", 450),
        ("Stylus", 60),
        ("Screen protector", 30)
    ]

    req5 = RequisitionSystem(
        "10/05/2024",
        "FN25",
        "Michael Scott",
        items5
    )

    req5.requisitions_details()
    req5.requisition_approval()


    
    print("--- Initial Statistics ---")
    RequisitionSystem.print_statistics()


  
    print("--- All Requisitions ---")
    RequisitionSystem.display_requisitons()



    req2.respond_requsition("Approved")
    req3.respond_requsition("Not approved")


   
    print("--- After Manager Responses ---")
    RequisitionSystem.display_requisitons()

    print("--- Updated Statistics ---")
    RequisitionSystem.print_statistics()