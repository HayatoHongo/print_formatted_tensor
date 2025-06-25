import torch
import torch.nn as nn

def print_formatted_tensor(*args, width=6, decimals=2):
    """
    Nicely formats and prints a PyTorch tensor along with its shape.

    Usage:
        print_formatted_tensor("name", tensor)
        print_formatted_tensor(tensor)

    Args:
        *args: If one argument is passed, it is treated as the tensor.
               If two arguments are passed, the first is treated as the name (str),
               and the second as the tensor (torch.Tensor).
        width (int): Width of each printed number (default: 6)
        decimals (int): Number of decimal places to display (default: 2)
    """
    # Determine tensor and optional name from args
    if not args:
        raise ValueError("At least one argument is required.")
    if isinstance(args[0], str):
        if len(args) < 2:
            raise ValueError("Tensor not provided.")
        name, tensor = args[0], args[1]
    else:
        name, tensor = None, args[0]

    # Convert tensor to list (detach and move to CPU if necessary)
    tensor_list = tensor.detach().cpu().tolist()

    def format_list(lst, indent):
        """
        Recursively formats nested lists into a nicely indented string.
        """
        # If elements are also lists, recurse further (multi-dimensional)
        if isinstance(lst, list) and lst and isinstance(lst[0], list):
            inner = ",\n".join(" " * indent + format_list(sub, indent + 2) for sub in lst)
            return "[\n" + inner + "\n" + " " * (indent - 2) + "]"
        # If it's a flat list of numbers
        return "[" + ", ".join(f"{v:{width}.{decimals}f}" for v in lst) + "]"

    # Format the tensor string and remove outermost brackets for alignment
    formatted = format_list(tensor_list, indent=9)
    inner_formatted = formatted[1:-1].strip()

    # Print result
    if name:
        print(name)
    print(f"Tensor Size: {list(tensor.size())}")
    print("tensor([")
    print(" " * 9 + inner_formatted)
    print(" " * 7 + "])")