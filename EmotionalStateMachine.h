// 🟥 EmotionalStateMachine.h
// ✅ Header for EmotionalStateMachine.c ES_Framework HSM

#ifndef EMOTIONAL_STATE_MACHINE_H
#define EMOTIONAL_STATE_MACHINE_H

#include "ES_Configure.h"
#include "ES_Framework.h"

// Public function prototypes
ES_Event InitEmotionalSM(void);
ES_Event RunEmotionalSM(ES_Event ThisEvent);

#endif /* EMOTIONAL_STATE_MACHINE_H */
