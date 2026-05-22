import json

# Load notebook
with open('transformers.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Function to convert TeX delimiters in a list of strings
def convert_cell(source_list):
    new_source = []
    for line in source_list:
        # Replace \( ... \) with $...$
        while '\\(' in line:
            left = line.find('\\(')
            right = line.find('\\)', left + 2)
            if right != -1:
                line = line[:left] + '$' + line[left+2:right] + '$' + line[right+2:]
        
        # Replace \[ ... \] with $$...$$
        while '\\[' in line:
            left = line.find('\\[')
            right = line.find('\\]', left + 2)
            if right != -1:
                line = line[:left] + '$$' + line[left+2:right] + '$$' + line[right+2:]
        
        new_source.append(line)
    return new_source

# Process all cells
for cell in nb.get('cells', []):
    if 'source' in cell and isinstance(cell['source'], list):
        cell['source'] = convert_cell(cell['source'])

# Save notebook
with open('transformers.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=2)

print("Done")