import tenseal as ts
import numpy as np
import time


def context():
    context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, coeff_mod_bit_sizes=[60, 40, 40, 60])
    context.global_scale = pow(2, 40)
    context.generate_galois_keys()
    return context

context = context()

def map_to_list(list1, list2):

    # Initialize a list with zeros
    IOC_severity = [0] * len(list2)

    # Map the input caste category to the list
    try:
        index = list1.index(list1)
        IOC_severity[index] = 1
    except ValueError:
        print("Invalid value.")

    return IOC_severity
	

risk_level = ["Critical", "High", "medium", "low", "Unknown"]

input_IOC_sev = "8.055"

input_risk_level = "High"


#output_IOC_sev = map_to_list(input_IOC_sev, IOC_sev)
output_risk_level = map_to_list(input_risk_level, risk_level)


print(f"IOC severity: {input_IOC_sev}")
print(f"risk: {output_risk_level}")

start_time = time.time()

encrypted_input_IOC_sev = ts.ckks_tensor(context, [input_IOC_sev])
encrypted_input_risk_level = ts.ckks_tensor(context, ts.plain_tensor(output_risk_level, [len(output_risk_level), 1]))

print("Encrypted severity",encrypted_input_IOC_sev)
print("Encrypted risk level", encrypted_input_risk_level )

end_time = time.time()

print(end_time - start_time)