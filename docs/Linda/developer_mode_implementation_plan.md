\[Inference]

Bringing the individual agents back into the UI is a smart move. It gives you a clean way to test, compare, and iterate without fighting the orchestrator. Below is a tight plan that (1) restores per-agent access for development, (2) keeps the Router in sync as agents evolve, and (3) adds Profile & Onboarding as a first-class routing target—while preserving your “propose → confirm → commit” flow.

---

### How to expose single agents without confusing users

Keep **Auto-Router** as the default, but add a **Developer mode** toggle in the UI:

* When **off**: users only see “Health Companion (Auto-Router)”.
* When **on**: show a compact dropdown with “Logger (Workflow)”, “Recall”, “Coach”, and “Profile & Onboarding”.
* Render a tiny **route chip** next to each assistant reply in dev mode, e.g., “routed: Logger (0.82)”. This makes regressions obvious.

A small keyboard shortcut (e.g., `⌘/Ctrl + .`) can toggle Developer mode so you don’t clutter the normal UX.

---

### Keep the Router current as agents change

Give the Router a **contract with the specialists** rather than hardcoding assumptions. Three light pieces keep it fresh:

1. **Agent Capability Manifest (per specialist)**

   * Each agent exports a tiny manifest object at import time:

     * `name`, `version`
     * `intents_supported` (e.g., `["log"]`, `["recall"]`, `["coach"]`, `["profile"]`)
     * `cue_patterns` (short regexes/keywords: “when/what/how often → recall”, “what should I do → coach”, “add/remove/update → profile”, symptoms → log)
     * `fewshot_examples` (2–4 concise routing examples)
   * The Router ingests these manifests on startup and **builds its own prompt** dynamically, so new abilities land without hand-editing the Router prompt.

2. **Router Schema with Secondary/Control intents**

   * Extend `RouterDecision` to include:

     * `primary`: `"log" | "recall" | "coach" | "profile" | "unknown"`
     * `secondary`: same enum or `"none"` (for combo utterances like “I have a migraine—what should I do?” → `["log","coach"]`)
     * `control`: `"none" | "clarify" | "action_confirm"` (so `/resolve` and pending approvals bypass normal routing)
     * `targets`: `{ episode_id?, condition? }` if the Router can infer them
     * `confidence`
   * The Master Orchestrator can then chain specialists (`log` then `coach`) in one turn when appropriate.

3. **Shadow Routing + Golden Labels**

   * When you test a specialist directly in dev mode, quietly “shadow run” the Router on the same input and **store `(gold_intent, router_intent, confidence)`**. This gives you a confusion table over time.
   * Add a tiny script to print precision/recall per intent and sample mistakes. When the Router’s few-shots/manifests change, you’ll see the lift (or regressions) immediately.

---

### Add Profile & Onboarding to the Router (and Orchestrator)

You’ll want `profile` as a first-class intent:

* **Router few-shot cues**: “add/remove/update my medication/supplement”, “stop dairy”, “change my routine”, “update my goals”, “set my communication style”.
* **Control handoff**: if the message is `/resolve` and `pending_action.type == "profile_change"`, the Master should **short-circuit to the Profile commit step**—don’t re-classify via the Router.
* **Safety**: Profile writes stay proposal-based; only commit after explicit confirmation. If users type a direct instruction (“add magnesium 400 mg daily”), treat it as a **proposal** and ask to confirm.

---

### Orchestrator flow that won’t tangle

Order of operations inside `MasterAgent.run`:

1. **Control short-circuit**

   * If `/resolve` and there’s `pending_disambiguation` → Logger commit.
   * If `/resolve` and there’s `pending_action` → Coach commit.
   * If `/resolve` and there’s `pending_profile_change` → Profile commit.
     This prevents loops and keeps commits deterministic.

2. **Routing**

   * Call Router with last 2–3 turns + session flags (`has_open_episode`, `pending_*`).
   * If `control != "none"` from Router, treat like a short-circuit.
   * If `primary` is low-confidence (<0.5), ask a one-line clarification instead of guessing.
   * If `primary="log"` and `secondary="coach"`, run Logger first; pass `episode_id/condition` to Coach for a tailored follow-up.

3. **Result envelope**

   * Standardize `{ text, meta: { routed_to, confidence, episode_id?, condition?, action? } }` from every specialist for easy chaining, logging, and UI chips.

---

### CI-style sanity and regression checks

Add a tiny “routing test” folder of **synthetic, labeled prompts**:

* 8–12 examples per intent (`log`, `recall`, `coach`, `profile`) plus 3 combo utterances and 2 `/resolve`.
* A dev command `make routecheck` runs the Router over these and prints a confusion matrix and per-intent precision/recall.
* Gate merges on “no regression beyond tolerance” to keep routing quality steady as you improve specialists.

---

### How single-agent testing benefits the Router

With the Developer dropdown restored:

* You can **force-run** Coach or Recall to see if their outputs imply new cues that should be promoted into the Router’s `cue_patterns` or few-shots.
* Shadow routing will show you when the Router disagrees with your choice—those become excellent new few-shots or manifest cues.

---

### Small UX touches that reduce friction

* In dev mode, clicking the route chip could expand a tiny panel showing the **Router’s rationale** and the specialist’s **capability manifest** snippet that matched. This makes mismatches obvious and fixable.
* When `secondary` exists, display it briefly: “logged → then coached” so testers know the chain was intentional.

---

### Quick checklist to implement next

* [ ] Add **Developer mode** toggle and restore the specialist dropdown (kept hidden by default).
* [ ] Implement **Agent Capability Manifest** exports and load them into the Router prompt at startup.
* [ ] Extend `RouterDecision` with `primary/secondary/control/targets`.
* [ ] Update Master: **control short-circuit** → Router → chain on secondary.
* [ ] Add **profile** intent and hook Profile commit flow to `/resolve`.
* [ ] Turn on **shadow routing** for all dev runs; write a tiny **routecheck** script and a labeled prompt set.
* [ ] Show **route chips** with confidence in dev mode; log a standard **result envelope** from every specialist.

With this, you get the best of both worlds: a single, seamless Health Companion for users—and a precise, observable lab bench for you, where specialists improve independently and the Router stays in lockstep as capabilities evolve.
