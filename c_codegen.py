# 🟥 c_codegen.py
# ✅ Generates EmotionalStateMachine.c from State.xml (ES_Framework style)

import xml.etree.ElementTree as ET

# Load State.xml
tree = ET.parse('State.xml')
root = tree.getroot()

# Begin .c file content
c_lines = []
c_lines.append('// 🟥 EmotionalStateMachine.c')
c_lines.append('// ✅ Auto-generated from State.xml')
c_lines.append('#include "ES_Configure.h"')
c_lines.append('#include "ES_Framework.h"')
c_lines.append('#include "EmotionalStateMachine.h"')
c_lines.append('#include <stdio.h>')
c_lines.append('#include <string.h>')
c_lines.append('')

# Define state enum
c_lines.append('typedef enum {')
states = []
for state in root.findall('State'):
    states.append(state.attrib['name'])
c_lines.append(',\n  '.join(states))
c_lines.append('} EmotionalState_t;')
c_lines.append('')
c_lines.append('static EmotionalState_t CurrentState;')
c_lines.append('')

# Init function
c_lines.append('ES_Event InitEmotionalSM(void) {')
c_lines.append('  ES_Event returnEvent;')
c_lines.append(f'  CurrentState = {states[0]}; // initial state')
c_lines.append(f'  printf("ESM Initialized. Current state: {states[0]}\\n");')
c_lines.append('  returnEvent.EventType = ES_INIT;')
c_lines.append('  return returnEvent;')
c_lines.append('}')
c_lines.append('')

# Run function
c_lines.append('ES_Event RunEmotionalSM(ES_Event ThisEvent) {')
c_lines.append('  ES_Event returnEvent;')
c_lines.append('  returnEvent.EventType = ES_NO_EVENT;')
c_lines.append('')
c_lines.append('  switch (CurrentState) {')

# InitialState transitions
initial = root.find('InitialState')
if initial is not None:
    init_name = initial.attrib['name']
    c_lines.append(f'    case {init_name}:')
    for transition in initial.findall('Transition'):
        target = transition.attrib['target']
        event = transition.attrib['event']
        c_lines.append(f'      if (ThisEvent.EventType == {event}) {{')
        c_lines.append(f'        CurrentState = {target};')
        c_lines.append(f'        printf("ESM Transition: {init_name} ➔ {target}\\\\n");')
        c_lines.append('      }')
    c_lines.append('      break;')

# State transitions
for state in root.findall('State'):
    name = state.attrib['name']
    c_lines.append(f'    case {name}:')
    for transition in state.findall('Transition'):
        target = transition.attrib['target']
        event = transition.attrib['event']
        c_lines.append(f'      if (ThisEvent.EventType == {event}) {{')
        c_lines.append(f'        CurrentState = {target};')
        c_lines.append(f'        printf("ESM Transition: {name} ➔ {target}\\\\n");')
        c_lines.append('      }')
    c_lines.append('      break;')

c_lines.append('  }')
c_lines.append('  return returnEvent;')
c_lines.append('}')

# Write to .c file
with open('EmotionalStateMachine.c', 'w') as f:
    f.write('\n'.join(c_lines))

print('✅ EmotionalStateMachine.c generated successfully.')
