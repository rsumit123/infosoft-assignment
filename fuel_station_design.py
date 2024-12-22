from typing import Dict

class FuelStation:
    """
    FuelStation manages fueling slots for Diesel, Petrol, and Electric vehicles.
    Each fuel type has a fixed number of slots that can be occupied or released.
    """

    def __init__(self, diesel: int, petrol: int, electric: int) -> None:
        """
        Initializes the FuelStation with specified slots for each fuel type.

        Args:
            diesel (int): Number of Diesel slots.
            petrol (int): Number of Petrol slots.
            electric (int): Number of Electric slots.
        """
        self.total_slots: Dict[str, int] = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }
        self.available_slots: Dict[str, int] = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }

    def fuel_vehicle(self, fuel_type: str) -> bool:
        """
        Attempts to fuel a vehicle of the specified fuel type.

        Args:
            fuel_type (str): The type of fuel required by the vehicle.

        Returns:
            bool: True if fueling is successful (slot occupied), False otherwise.
        """
        if fuel_type not in self.available_slots:
            # Invalid fuel type
            print(f"Error: '{fuel_type}' is not a recognized fuel type.")
            return False

        if self.available_slots[fuel_type] > 0:
            self.available_slots[fuel_type] -= 1
            print(f"Fueled a {fuel_type} vehicle. Slots remaining: {self.available_slots[fuel_type]}")
            return True
        else:
            print(f"No available {fuel_type} slots to fuel the vehicle.")
            return False

    def open_fuel_slot(self, fuel_type: str) -> bool:
        """
        Releases a fuel slot of the specified fuel type, making it available for future use.

        Args:
            fuel_type (str): The type of fuel slot to release.

        Returns:
            bool: True if a slot was successfully released, False otherwise.
        """
        if fuel_type not in self.available_slots:
            # Invalid fuel type
            print(f"Error: '{fuel_type}' is not a recognized fuel type.")
            return False

        if self.available_slots[fuel_type] < self.total_slots[fuel_type]:
            self.available_slots[fuel_type] += 1
            print(f"Released a {fuel_type} slot. Slots available: {self.available_slots[fuel_type]}")
            return True
        else:
            print(f"All {fuel_type} slots are already available. Cannot release more.")
            return False

# Test Case
if __name__ == "__main__":
    fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
    
    operations = [
        ("fuel_vehicle", "diesel"),
        ("fuel_vehicle", "petrol"),
        ("fuel_vehicle", "diesel"),
        ("fuel_vehicle", "electric"),
        ("fuel_vehicle", "diesel"),
        ("open_fuel_slot", "diesel"),
        ("fuel_vehicle", "diesel"),
        ("open_fuel_slot", "electric"),
        ("open_fuel_slot", "electric")
    ]
    
    expected_output = [True, True, True, True, False, True, True, True, False]
    actual_output = []
    
    for operation, fuel_type in operations:
        if operation == "fuel_vehicle":
            result = fuel_station.fuel_vehicle(fuel_type)
            actual_output.append(result)
        elif operation == "open_fuel_slot":
            result = fuel_station.open_fuel_slot(fuel_type)
            actual_output.append(result)
    
    print("Actual Output:", actual_output)
    print("Expected Output:", expected_output)
    assert actual_output == expected_output, "Test case failed!"
    print("Test case passed!")
