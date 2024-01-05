import stix2
import json

# Creating a simple STIX indicator with additional custom properties
risk_level = '"{}"'.format(encrypted_input_risk_level)
ioc_severity = '"{}"'.format(encrypted_input_IOC_sev)

indicator = stix2.Indicator(
    name="Malicious File Indicator",
    pattern="[file:hashes.md5 = 'd41d8cd98f00b204e9800998ecf8427e']",
    labels=["malicious-indicator"],
    pattern_type="stix",
    custom_properties={
        "risk_level": risk_level,
        "ioc_severity": ioc_severity
    }
)

# Convert STIX Indicator to JSON format
indicator_json = stix2.serialization.serialize(indicator, indent=2)

# Save JSON to a file
with open("/content/data.json", "w") as json_file:
    json_file.write(indicator_json)

print("STIX Indicator saved to 'data.json'")
