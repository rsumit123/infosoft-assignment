# Infosoft Assignment

This project was created as part of an assignment provided by InfoSoft. It contains solutions to three distinct problems, each addressing different aspects of software design and debugging. The project demonstrates proficiency in Python programming, problem-solving, and code optimization.

# Table of Contents

* [Problem 1: Data Stream](#problem-1-data-stream)
* [Problem 2: Fuel Station Design](#problem-2-fuel-station-design)
* [Problem 3: Calendar Debugging](#problem-3-calendar-debugging)
* [Contributing](#contributing)
* [License](#license)

## Problem 1: Data Stream

**Description:**

Design a system that processes a stream of strings with timestamps, ensuring that each unique string is printed at most once every 5 seconds to prevent double printing.

**Solution:**

Implemented the `DataStream` class using a dictionary to track the last printed timestamp for each string, ensuring efficient O(1) time complexity for insertion and lookup operations.

**Details:**

* Language: Python 3
* Technologies Used: Python standard libraries with type hints compatible with Mypy.
* Read More: [ReadMe_problem1.md](Problem1_README.md)

## Problem 2: Fuel Station Design

**Description:**

Design a fuel station accommodating three types of vehicles—Diesel, Petrol, and Electric—with a fixed number of parking slots for each type. The system should manage slot allocation to prevent overbooking.

**Solution:**

Developed the `FuelStation` class utilizing dictionaries to manage available and total slots for each fuel type. The class provides methods to fuel vehicles and release slots, ensuring accurate slot tracking and preventing double bookings.

**Details:**

* Language: Python 3
* Technologies Used: Python standard libraries with type hints compatible with Mypy.
* Read More: [ReadMe_problem2.md](Problem2_README.md)

## Problem 3: Calendar Debugging

**Description:**

Debug and fix an existing calendar program that is intended to prevent double bookings by ensuring no two events overlap in time.

**Solution:**

Analyzed and corrected the `calendar.py` module by fixing logical errors in overlap detection, adjusting binary search tree insertion logic, and ensuring proper type hinting and imports. Enhanced the code with comprehensive test cases and detailed documentation.

**Details:**

* Language: Python 3
* Technologies Used: Python standard libraries with type hints compatible with Mypy.
* Read More: [ReadMe_problem3.md](Problem3_README.md)

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to submit a pull request or open an issue.

**How to Contribute**

1. **Fork the Repository:** Click the "Fork" button at the top right of this page to create your own copy of the repository.
2. **Clone the Repository:** Use `git clone` to clone your forked repository to your local machine.
3. **Create a Branch:** Create a new branch for your feature or bugfix.

```bash
git checkout -b feature/your-feature-name
```
## License

This project is licensed under the MIT License. The full license text can be found in the LICENSE file located at the root of this repository.

## Contact

For any inquiries or feedback, please feel free to contact us at [rsumit123@gmail.com](mailto:rsumit123@gmail.com).