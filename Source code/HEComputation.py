import tenseal as ts

# Create a CKKS context
context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, coeff_mod_bit_sizes=[60, 40, 40, 60])
context.global_scale = pow(2, 40)
context.generate_galois_keys()

# Encrypt the numbers

number2 = 3.0
number3 = 6.0
encrypted_number1 = encrypted_input_IOC_sev
encrypted_number2 = ts.ckks_tensor(context, [number2])
encrypted_number3 = ts.ckks_tensor(context, [number3])

print(encrypted_input_IOC_sev.decrypt())
# Subtract the numbers (effectively performing a comparison)
result_tensor12 = encrypted_number2 - encrypted_number1
result_tensor13 = encrypted_number3 - encrypted_number1
print(result_tensor12)

# Decrypt the difference
decrypted_result12 = result_tensor12.decrypt().tolist()[0]  # Correct extraction
decrypted_result13 = result_tensor13.decrypt().tolist()[0]  # Correct extraction
print(decrypted_result12)

# Interpret the decrypted result to determine which number is greater

if decrypted_result13 < 0:
  print("Critical IOC")
elif decrypted_result12 < 0 and decrypted_result13 > 0:
  print("High priority IOC")
else: print("Low priority IOC")