// 🟥 EmotionalStateMachine.c
// ✅ ES_Framework Hierarchical State Machine for Emotional Pipeline

#include "ES_Configure.h"
#include "ES_Framework.h"
#include "EmotionalStateMachine.h"
#include <stdio.h>

// Define emotional states
typedef enum {
  Calm,
  Joy,
  Fatigue,
  Overwhelm,
  Sage
} EmotionalState_t;

static EmotionalState_t CurrentState;

// Initialization function
ES_Event InitEmotionalSM(void) {
  ES_Event returnEvent;

  CurrentState = Calm; // initial state

  printf("ESM Initialized. Current state: Calm.\n");

  returnEvent.EventType = ES_INIT;
  return returnEvent;
}

// Run function
ES_Event RunEmotionalSM(ES_Event ThisEvent) {
  ES_Event returnEvent;
  returnEvent.EventType = ES_NO_EVENT;

  switch (CurrentState) {
    case Calm:
      if (ThisEvent.EventType == ENERGIZE) {
        CurrentState = Joy;
        printf("ESM Transition: Calm ➔ Joy\n");
      } else if (ThisEvent.EventType == TIRED) {
        CurrentState = Fatigue;
        printf("ESM Transition: Calm ➔ Fatigue\n");
      }
      break;

    case Joy:
      if (ThisEvent.EventType == CALM_DOWN) {
        CurrentState = Calm;
        printf("ESM Transition: Joy ➔ Calm\n");
      } else if (ThisEvent.EventType == OVERLOAD) {
        CurrentState = Overwhelm;
        printf("ESM Transition: Joy ➔ Overwhelm\n");
      }
      break;

    case Fatigue:
      if (ThisEvent.EventType == REST) {
        CurrentState = Calm;
        printf("ESM Transition: Fatigue ➔ Calm\n");
      } else if (ThisEvent.EventType == EXHAUSTION) {
        CurrentState = Overwhelm;
        printf("ESM Transition: Fatigue ➔ Overwhelm\n");
      }
      break;

    case Overwhelm:
      if (ThisEvent.EventType == STABILIZE) {
        CurrentState = Calm;
        printf("ESM Transition: Overwhelm ➔ Calm\n");
      } else if (ThisEvent.EventType == INSIGHT) {
        CurrentState = Sage;
        printf("ESM Transition: Overwhelm ➔ Sage\n");
      }
      break;

    case Sage:
      if (ThisEvent.EventType == RETURN) {
        CurrentState = Calm;
        printf("ESM Transition: Sage ➔ Calm\n");
      }
      break;
  }

  return returnEvent;
}
