// 🟥 StateMachine.c
// ✅ Minimal pipeline-based state machine implementation for Isaac Espinosa

#include <stdio.h>

typedef enum {
    InitPState,
    Awake,
    PhoneMode,
    LabMode,
    Pause,
    EnlightenmentEvent,
    HomeMode,
    Sage,
    Sleep
} PipelineState_t;

PipelineState_t CurrentState = InitPState;

void RunStateMachine(const char *event) {
    switch (CurrentState) {

        case InitPState:
            if (strcmp(event, "ALARM") == 0) {
                CurrentState = Awake;
                printf("Transition: InitPState ➔ Awake\n");
            }
            break;

        case Awake:
            if (strcmp(event, "ENTER_LAB") == 0) {
                CurrentState = LabMode;
                printf("Transition: Awake ➔ LabMode\n");
            } else if (strcmp(event, "PHONE_USE") == 0) {
                CurrentState = PhoneMode;
                printf("Transition: Awake ➔ PhoneMode\n");
            } else if (strcmp(event, "TIRED") == 0) {
                CurrentState = Sleep;
                printf("Transition: Awake ➔ Sleep\n");
            } else if (strcmp(event, "ARRIVE_HOME") == 0) {
                CurrentState = HomeMode;
                printf("Transition: Awake ➔ HomeMode\n");
            }
            break;

        case PhoneMode:
            if (strcmp(event, "ARRIVE_LAB") == 0) {
                CurrentState = LabMode;
                printf("Transition: PhoneMode ➔ LabMode\n");
            } else if (strcmp(event, "SLEEP_SIGNAL") == 0) {
                CurrentState = Sleep;
                printf("Transition: PhoneMode ➔ Sleep\n");
            }
            break;

        case LabMode:
            if (strcmp(event, "FATIGUE") == 0) {
                CurrentState = Pause;
                printf("Transition: LabMode ➔ Pause\n");
            } else if (strcmp(event, "ENLIGHTENMENT") == 0) {
                CurrentState = EnlightenmentEvent;
                printf("Transition: LabMode ➔ EnlightenmentEvent\n");
            }
            break;

        case Pause:
            if (strcmp(event, "READY") == 0) {
                CurrentState = LabMode;
                printf("Transition: Pause ➔ LabMode\n");
            } else if (strcmp(event, "READY") == 0) {
                CurrentState = Awake;
                printf("Transition: Pause ➔ Awake\n");
            }
            break;

        case EnlightenmentEvent:
            if (strcmp(event, "ANY") == 0) {
                CurrentState = Sleep;
                printf("Transition: EnlightenmentEvent ➔ Sleep\n");
            } else if (strcmp(event, "ANY") == 0) {
                CurrentState = Awake;
                printf("Transition: EnlightenmentEvent ➔ Awake\n");
            } else if (strcmp(event, "ANY") == 0) {
                CurrentState = LabMode;
                printf("Transition: EnlightenmentEvent ➔ LabMode\n");
            } else if (strcmp(event, "ANY") == 0) {
                CurrentState = PhoneMode;
                printf("Transition: EnlightenmentEvent ➔ PhoneMode\n");
            } else if (strcmp(event, "ANY") == 0) {
                CurrentState = HomeMode;
                printf("Transition: EnlightenmentEvent ➔ HomeMode\n");
            } else if (strcmp(event, "ANY") == 0) {
                CurrentState = Sage;
                printf("Transition: EnlightenmentEvent ➔ Sage\n");
            }
            break;

        case HomeMode:
            if (strcmp(event, "STABILIZED") == 0) {
                CurrentState = Awake;
                printf("Transition: HomeMode ➔ Awake\n");
            } else if (strcmp(event, "SLEEP_SIGNAL") == 0) {
                CurrentState = Sleep;
                printf("Transition: HomeMode ➔ Sleep\n");
            }
            break;

        case Sage:
            if (strcmp(event, "STABILIZED") == 0) {
                CurrentState = Awake;
                printf("Transition: Sage ➔ Awake\n");
            }
            break;

        case Sleep:
            // No transitions defined from Sleep in current pipeline
            break;
    }
}

int main() {
    RunStateMachine("ALARM");
    RunStateMachine("ENTER_LAB");
    RunStateMachine("ENLIGHTENMENT");
    RunStateMachine("ANY");
    return 0;
}
