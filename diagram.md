```mermaid
graph TD
    A[Start] --> B{Launch Browser};
    B --> C{Navigate to Login Page};
    C --> D{Accept Cookie Consent?};
    D -- Yes --> E[Click Accept Button];
    D -- No --> F{Click Login Button};
    E --> F; 
    F --> G{Enter Username};
    G --> H{Enter Password};
    H --> I[Submit Login Form];
    I --> J{Login Successful?};
    J -- Yes --> K[Click &quot;Tchat&quot; Button];
    J -- No --> Z[End with Error];
    K --> L[Retrieve Conversation List];
    L --> M{Iterate Conversations};
    M --> N[Click Conversation];
    N --> O{Extract Username};
    O --> P{Extract New Messages};
    P --> Q{New Messages Found?};
    Q -- Yes --> R[Print New Messages];
    Q -- No --> S[Skip to Next Conversation];
    R --> T[Click Back Button];
    S --> T;
    T --> U{Back to Conversation List?};
    U -- Yes --> M;
    U -- No --> V[Refresh Page];
    V --> M;
    M -- No More Conversations --> W[Close Browser];
    W --> X[End];

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style X fill:#f9f,stroke:#333,stroke-width:2px
    style Z fill:#f99,stroke:#333,stroke-width:2px
    style J stroke:#f00,stroke-width:2px
    style D stroke:#f00,stroke-width:2px
    style Q stroke:#f00,stroke-width:2px
    style U stroke:#f00,stroke-width:2px