def calculate_paracetamol_volume(weight, strength):
    # Check weight is within the allowed range
    if weight < 10 or weight > 100:
        raise ValueError(f"Weight {weight} kg is out of the allowed range (10-100 kg).")
    # Check strength is valid
    if strength !=120 and strength !=250:
        raise ValueError(f"Invalid strength '{strength}'. Must be either 120 mg/5ml or 250 mg/5ml.")
    # Calculate the required volume in ml
    volume_ml = (15 * weight * 5) / strength
    return volume_ml

# Example of how to call the function
print(calculate_paracetamol_volume(20, 120))  # Expected output: 12.5