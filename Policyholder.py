class Policyholder:
    def __init__(self, name, policy_id):
        self.name = name
        self.policy_id = policy_id
        self.status = "active"

    def register_policyholder(self):
        print(f"Policyholder {self.name} registered successfully!")

    def suspend_policyholder(self):
        self.status = "suspended"
        print(f"Policyholder {self.name} has been suspended.")

    def reactivate_policyholder(self):
        self.status = "active"
        print(f"Policyholder {self.name} has been reactivated.")
