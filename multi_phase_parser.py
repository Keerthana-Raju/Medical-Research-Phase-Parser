import re

# Input list of strings
string_list = [
    'Phase I - PSORIASIS,Moderate to severe Graves\' orbitopathy,AXIAL SPONDYLOARTHRITIS;Pre-registration - Active ankylosing spondylitis;Phase II - LUPUS NEPHRITIS,CHRONIC PLAQUE PSORIASIS,PSORIATIC ARTHRITIS;Launched - MODERATE TO SEVERE PLAQUE PSORIASIS',
    'Phase I - Colorectal cancer,SQUAMOUS CELL CARCINOMA OF THE HEAD AND NECK,GASTROESOPHAGEAL JUNCTION ADENOCARCINOMA,PIK3CA-mutated solid tumors,NON-SMALL CELL LUNG CANCER,GASTRIC ADENOCARCINOMA,ADVANCED SOLID TUMOR,ENDOMETRIAL CANCER,UROTHELIAL CANCER;Phase II - COLORECTAL CARCINOMA,Endometrial carcinoma'
]

# Case 1: Extract from the beginning till the first occurrence of " - "
def extract_before_dash(s):
    match = re.search(r'^(.*?)\s-\s', s)
    if match:
        return match.group(1).strip()
    return None

# Case 2: Extract every time a ";" is encountered till the next " - "
def extract_after_semicolon_before_dash(s):
    matches = re.findall(r';(.*?)\s-\s', s)
    return [match.strip() for match in matches]

# Process the list of strings
for string in string_list:
    # Case 1: Extract the string before " - "
    result_case1 = extract_before_dash(string)
    
    # Case 2: Extract all strings after ";" till " - "
    result_case2_list = extract_after_semicolon_before_dash(string)
    
    # Combine the results into a single string with ";" separator
    combined_result = result_case1 + ";" + ";".join(result_case2_list) if result_case2_list else result_case1
    
    # Print the final result for each string
    print(combined_result)
