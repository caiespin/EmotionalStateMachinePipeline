# 🟥 pipeline_xml_to_dot_parser.py
# ✅ Universal XML ➔ DOT parser with philosophical reflections and enriched labels

import sys
import xml.etree.ElementTree as ET

# ==============================
# CONFIGURATION
# ==============================
if len(sys.argv) < 3:
    print("Usage: python3 pipeline_xml_to_dot_parser.py input.xml output.dot")
    sys.exit(1)

input_xml = sys.argv[1]
output_dot = sys.argv[2]

# ==============================
# XML ➔ DOT PARSING
# ==============================
tree = ET.parse(input_xml)
root = tree.getroot()

dot_lines = []
dot_lines.append(f'digraph {root.attrib["name"]} {{')
dot_lines.append('  rankdir=TB;')
dot_lines.append('  bgcolor="#0a192f";')
dot_lines.append('  node [shape=box, style="rounded,filled", fillcolor="#112240", fontcolor="#64ffda", fontname="Helvetica", fontsize=10, color="#64ffda"];')
dot_lines.append('  edge [color="#64ffda", fontname="Helvetica", fontsize=9, fontcolor="#64ffda", penwidth=1.2, arrowsize=1.5];')
dot_lines.append('')

# InitialState
initial = root.find('InitialState')
if initial is not None:
    init_name = initial.attrib['name']
    dot_lines.append(f'  {init_name} [shape=circle, fixedsize=true, width=0.3, style=filled, fillcolor="#64ffda", label=""];')
    for transition in initial.findall('Transition'):
        target = transition.attrib['target']
        event = transition.attrib['event']
        dot_lines.append(f'  {init_name} -> {target} [label="{event}"];')

# States
for state in root.findall('State'):
    name = state.attrib['name']
    dot_lines.append(f'  {name} [label="{name}"];')
    for transition in state.findall('Transition'):
        target = transition.attrib['target']
        event = transition.attrib['event']
        dot_lines.append(f'  {name} -> {target} [label="{event}"];')

dot_lines.append('}')

# ==============================
# Write DOT file
# ==============================
with open(output_dot, 'w') as f:
    f.write('\n'.join(dot_lines))

print(f"✅ Parsed {input_xml} ➔ {output_dot}")
