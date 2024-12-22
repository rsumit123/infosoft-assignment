from typing import Dict

class DataStream:
    """
    DataStream processes a stream of strings with timestamps and determines
    whether to print each string based on a 5-second rule.
    """
    
    def __init__(self) -> None:
        # Dictionary to store the last printed timestamp for each string
        self.last_printed: Dict[str, int] = {}
    
    def should_output_data_str(self, timestamp: int, data_str: str) -> bool:
        """
        Determines whether to print the given data_str at the provided timestamp.

        Args:
            timestamp (int): The current timestamp in seconds.
            data_str (str): The string to be evaluated.

        Returns:
            bool: True if the string should be printed, False otherwise.
        """
        if data_str not in self.last_printed:
            # First occurrence of the string; should print
            self.last_printed[data_str] = timestamp
            return True
        else:
            # Calculate time difference since last print
            time_diff = timestamp - self.last_printed[data_str]
            if time_diff >= 5:
                # Enough time has passed; should print
                self.last_printed[data_str] = timestamp
                return True
            else:
                # Not enough time has passed; should not print
                return False

# Test the solution
if __name__ == "__main__":
    data_stream = DataStream()
    inputs = [ # Sample Test case
        (0, "hello"),
        (1, "world"),
        (6, "hello"),
        (7, "hello"),
        (8, "world")
    ]
    
    outputs = []
    for timestamp, data_str in inputs:
        result = data_stream.should_output_data_str(timestamp, data_str)
        outputs.append(result)
    
    print(outputs)
