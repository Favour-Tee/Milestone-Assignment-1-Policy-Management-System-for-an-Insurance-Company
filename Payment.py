class Payment:
    def __init__(self, policyholder_name, amount):
        self.policyholder_name = policyholder_name
        self.amount = amount

    def process_payment(self):
        print(f"Payment of {self.amount} for {self.policyholder_name} processed successfully!")

    def send_reminder(self):
        print(f"Reminder sent to {self.policyholder_name} for payment.")

    def apply_penalty(self):
        print(f"Penalty applied to {self.policyholder_name}'s account.")

