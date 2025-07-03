// 🟥 ES_Configure.h
// ✅ Configuration header for ES_Framework pipelines

#ifndef ES_CONFIGURE_H
#define ES_CONFIGURE_H

// Include standard libraries
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

// Define custom events as needed for your EmotionalStateMachine
typedef enum {
  ES_NO_EVENT,
  ES_INIT,
  ENERGIZE,
  TIRED,
  CALM_DOWN,
  OVERLOAD,
  REST,
  EXHAUSTION,
  STABILIZE,
  INSIGHT,
  RETURN
} ES_EventType_t;

// Define ES_Event struct
typedef struct {
  ES_EventType_t EventType;
  uint16_t EventParam;
} ES_Event;

#endif /* ES_CONFIGURE_H */
