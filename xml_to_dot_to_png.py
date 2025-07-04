import sys
import xml.etree.ElementTree as ET
from graphviz import Source
import os
import subprocess

def parse_xml_to_dot(input_xml, output_dot):
    tree = ET.parse(input_xml)
    root = tree.getroot()

    dot_lines = []
    dot_lines.append(f'digraph {root.attrib["name"]} {{')
    dot_lines.append('  rankdir=TB;')
    dot_lines.append('  node [fontname="Helvetica", shape=box, style=rounded, fontsize=10];')

    # InitialState as Tao (no label visible, Entry Actions printed only to console)
    initial = root.find('InitialState')
    if initial is not None:
        init_name = initial.attrib.get('name', 'InitPState')
        entry_actions = initial.findall('Entry')

        # Render as pure circle with no label
        dot_lines.append(f'  {init_name} [shape=circle, fixedsize=true, width=0.2, style=filled, fillcolor=black, label=""];')

        # Add transitions with actions
        for transition in initial.findall('Transition'):
            target = transition.attrib['target']
            event = transition.attrib['event']

            actions = [action.text for action in transition.findall('Action') if action.text]

            label = event
            for action_text in actions:
                label += f"\\n{action_text}"

            dot_lines.append(f'  {init_name} -> {target} [label="{label}"];')

        for entry in entry_actions:
            if entry is not None and entry.text:
                print(f"🔧 InitPState Entry Action: {entry.text}")

    # States with visible labels, single bottom border under name, no inner table borders
    for state in root.findall('State'):
        name = state.attrib['name']
        subhsm = state.find('SubHSM')
        entry = state.find('Entry')
        exit = state.find('Exit')

        label_html = "<TABLE BORDER=\"0\" CELLBORDER=\"0\" CELLSPACING=\"0\" CELLPADDING=\"6\">"
        label_html += f"<TR><TD BORDER=\"1\" SIDES=\"B\"><B>{name}</B></TD></TR>"

        if subhsm is not None and subhsm.text:
            label_html += f"<TR><TD ALIGN=\"LEFT\">▶ {subhsm.text}</TD></TR>"
        if entry is not None and entry.text:
            label_html += f"<TR><TD ALIGN=\"LEFT\">/Entry: {entry.text}</TD></TR>"
        if exit is not None and exit.text:
            label_html += f"<TR><TD ALIGN=\"LEFT\">/Exit: {exit.text}</TD></TR>"

        label_html += "</TABLE>"

        dot_lines.append(f'  {name} [label=<{label_html}>];')

        for transition in state.findall('Transition'):
            target = transition.attrib['target']
            event = transition.attrib['event']

            actions = [action.text for action in transition.findall('Action') if action.text]

            label = event
            for action_text in actions:
                label += f"\\n{action_text}"

            dot_lines.append(f'  {name} -> {target} [label="{label}"];')

    dot_lines.append('}')

    with open(output_dot, 'w') as f:
        f.write('\n'.join(dot_lines))

    print(f"✅ DOT file generated at: {output_dot}")

def render_dot_to_png(dot_file, png_file):
    try:
        subprocess.run(['dot', '-Tpng', dot_file, '-o', png_file], check=True)
        print(f"✅ PNG file rendered at: {png_file}")
    except Exception as e:
        print(f"⚠️ Silent fail: PNG render failed. {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python state_pipeline_render.py input.xml output.dot")
        sys.exit(1)

    input_xml = sys.argv[1]
    output_dot = sys.argv[2]
    output_png_tmp = output_dot.replace('.dot', '_TMP.png')

    parse_xml_to_dot(input_xml, output_dot)
    render_dot_to_png(output_dot, output_png_tmp)
