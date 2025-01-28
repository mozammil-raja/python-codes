def swap_numbers():
    # Taking input from the user
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
    
    print(f"Before swapping: a = {a}, b = {b}")
    
    # Calculate the number of bits needed to represent b
    num_bits = b.bit_length()  # Get the minimum number of bits to represent b
    
    # Step 1: Shift a to the left by `num_bits` and combine it with b
    a = (a << num_bits) | b  # Use bitwise OR to combine
    
    # Step 2: Extract b from the combined value
    b = a & ((1 << num_bits) - 1)  # Mask to isolate b
    
    # Step 3: Extract a from the combined value
    a = a >> num_bits  # Right-shift to isolate a
    
    print(f"After swapping: a = {a}, b = {b}")

# Call the function
swap_numbers()
