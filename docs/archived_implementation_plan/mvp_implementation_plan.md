# MVP Health Companion Agents — Implementation Plan

## Goal
Build a minimal but functional health companion app that:
1. Logs structured health data from user conversation.
2. Recalls relevant history from stored logs.
3. Provides basic health tips or supportive coaching.

This MVP focuses on **small, separate agents first**, then adds an orchestrator later.

---

## Step 1 — Three Small Agents

### 1. Logger Agent
**Purpose**  
Extract structured health information from a user message and store it in a local data file (CSV or JSON).

**Inputs**  
- User message (e.g., "I had a migraine after wine last night.")
- Current date/time
- Optional file attachments

**Outputs**  
- Structured data entry (e.g., `{date, condition: migraine, severity: 6, possible_trigger: wine}`)
- Confirmation message back to the user.

**Storage**  
- Append to `health_log.json` or `health_log.csv` in a simple flat structure.

---

### 2. Recall Agent
**Purpose**  
Answer fact-based questions about the user’s past logs.

**Inputs**  
- User question (e.g., "Did I get migraines every time I had wine?")
- Stored health log file.

**Outputs**  
- Answer derived from the logs (simple search or filter).
- If needed, list matching entries.

**Logic**  
- For MVP: keyword search + date filtering.
- Later: LLM-powered query interpretation.

---

### 3. Coach Agent
**Purpose**  
Offer empathetic, safe, general health tips relevant to the logged data or user’s direct request.

**Inputs**  
- User request (e.g., "How can I manage my migraine?")
- Optional context from latest log entry.

**Outputs**  
- 1–2 general, evidence-based suggestions.
- Supportive tone.

**Logic**  
- For MVP: simple mapping from keywords → tip templates.
- Later: LLM-powered, personalized suggestions.

---

## Step 2 — Orchestrator (Future)
After all 3 agents work reliably:
1. Add a **Router Agent** that:
   - Classifies the user’s intent as `"log"`, `"query"`, or `"coach"`.
   - Routes the request to the correct agent.
2. Start with rule-based classification (keywords like "how", "did I", "when" for queries; symptom/diet words for logging; advice/help words for coaching).
3. Later upgrade to LLM-based intent classification for more flexibility.

---

## Step 3 — Integration in UI
- For MVP, use a **dropdown** in the chat interface to manually choose the agent.
- Pass the user input + optional files to the selected agent.
- Show the agent’s output in the chat window.
- Once Orchestrator is ready, remove the dropdown and let routing happen automatically.

---

## Step 4 — Testing Checklist
- [ ] Logger Agent correctly extracts and stores structured entries.
- [ ] Recall Agent retrieves correct entries for test queries.
- [ ] Coach Agent returns relevant and safe suggestions.
- [ ] UI displays conversation clearly for each agent.
- [ ] Local storage file updates consistently.

---

## Notes
- **Scope control**: Don’t add reminders, scheduling, or multi-condition reasoning yet.
- **Safety**: Keep coaching advice generic and safe; no deep clinical recommendations for MVP.
- **Flexibility**: Logs should accept any health-related data, not just migraine info.
