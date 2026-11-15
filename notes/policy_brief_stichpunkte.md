# Policy Brief – bullet points for writing (English)

*Status 15 Nov 2026. Structure follows the course guidance (`policy_brief_vorgaben_kurs.md`): Summary – Context – Project/Approach – Findings – Implications – Recommendations; one problem per paragraph; the context only raises problems that are answered later. The author writes the brief in English from these bullets; a German version is translated at the end. Figures are measured unless marked as estimate. Sources of every figure: `policy_brief_notes.md`, `results/`. First full draft from these bullets: `policy_brief_draft_en.md` (15 Nov); the earlier draft of 5 Nov is in git history (commit 147bfd5).*

## Audience (for the author, not part of the brief)

- **Who:** the commander; reads the brief to decide whether to endorse the idea and push it up the chain.
- **What they know:** AARs, how units file and use them, command and security processes. Little or no AI background.
- **Why it matters to them:** lessons learned that get lost cost time, money and safety; a decision now shapes whether the unit can use its own experience at scale.
- **What they need:** the problem, what was shown, how reliable it is, what it would take (hardware, cost order of magnitude, approvals), and what to decide.
- **Leave out:** technical terms (embeddings, tokens, prompts), version numbers, test mechanics. Use plain analogies ("index cards", "one large graphics card").

## Summary (4–5 sentences)

- After-action reports hold the unit's experience, but in practice the newest and most relevant lessons are hard to find.
- A working prototype shows that an AI assistant can answer plain-language questions across a whole AAR collection, cite the exact report for every statement, and prefer the most recent rule.
- It keeps working as the collection grows and runs without any internet connection – but only with a sufficiently large model on a dedicated server.
- A model that fits on a single large graphics card comes close to a leading commercial cloud model in our tests.
- Request: endorse the idea of an AI-supported AAR database on our own hardware inside our closed network and support a pilot with real, unclassified reports.

## Context – the problem and why it matters

*One paragraph each; every problem is answered later in Findings.*

1. **Lessons get lost.** Nobody can read every AAR; relevant experience from another unit or year stays unused. (→ Findings 1)
2. **Rules change, and the newest version is easy to miss.** Acting on an outdated procedure costs time and can create safety risks. (→ Findings 2)
3. **Answers must be trustworthy.** A soldier acting on an answer must be able to see where it comes from. (→ Findings 1)
4. **Collections keep growing.** Any solution has to cope with hundreds or thousands of reports and new ones every week, without extra work for the authors. (→ Findings 3)
5. **Our reports cannot leave our network.** A cloud service is not an option for sensitive material; a solution must run on our own hardware. (→ Findings 4 and 5)

## Project / Approach – what was done

- Built a working prototype: a simple browser chat on a standard laptop that answers questions about a folder of reports (Oct–Nov 2026, improved in about 20 test rounds).
- Test material: 58 fictional, unclassified reports written for the test, including 10 long reports from a fictional training and exercise environment (vehicle service, rations, bivouac, visitors' day, range safety).
- Built-in traps: rules that change without saying so, a new rule mentioned only on page 3, similar wording in other contexts, conflicting experiences, questions the reports cannot answer.
- 34 test questions, each round repeated three times, graded against criteria set in advance.
- Compared a leading commercial cloud model with freely available ("open") models of different sizes, including a fully offline run on the laptop.

## Findings – what was learned (incl. limits)

1. **Every answer is traceable.** Each statement comes with a word-for-word quote and a footnote (report title and date); the program checks every quote against the report. Since a safeguard was added, no invented sources occurred.
2. **The newest rule wins – most of the time.** With the cloud model, 95 % of answers were free of critical errors; in about 5 % an older rule still appeared as valid. The program then adds a warning ("possibly outdated – newer report dated …"), which catches part of these cases.
3. **It scales.** New reports dropped into the folder are picked up automatically and turned once into short "index cards" (2–9 US cents per report). After that, a question costs about 3 cents and 20 seconds, regardless of collection size. Ten reports added later were used immediately, including rule changes buried deep in long reports.
4. **Offline works technically.** A complete test run with the network disconnected showed zero outside connections. A small model on a laptop, however, gave unusable answers 59 % of the time.
5. **Model size decides quality – but the curve flattens (figure).** Unusable answers: 30 % (27 billion parameters) → 13 % (≈120 billion, one large graphics card) → 11 % (≈400 billion, server with eight cards); leading cloud model 5 %.
6. **Answers stay on the question.** The assistant answers for the situation asked (garrison vs. exercise, seminar vs. bivouac), says openly when the reports contain nothing, and keeps answers short.
7. **Limits of this evidence:** fictional reports written for the test; grading by AI against fixed criteria with spot checks by the author; open models measured via a provider, not on our own server; several users at once and access rights not tested; hardware prices only rough ranges; instructions were tuned on the cloud model, so the gap to open models is probably smaller than measured.

*Figure:* `notes/abbildungen/modellgroesse_fehler_en.png`

## Implications – what it means for the unit

- **The idea is feasible now,** not a future technology: the core functions work and are measurable.
- **Hardware is a manageable investment (estimate):** a model in the ≈120-billion class runs on one graphics card with 80–96 GB memory (card roughly 15,000–25,000 USD, plus server, operation and approval). Going to the 400-billion class (eight-card server, roughly 285,000–530,000 USD) adds little.
- **Faster than a manual search, and not worse than one (author's assessment, not measured):** finding and reading all relevant reports by hand takes an hour or more – if they are found at all. The assistant answers in about 20 seconds; users can do other work meanwhile. People make mistakes too: under time pressure and with hundreds of reports, a manual search also misses the newest rule. Better a good answer in seconds than a perhaps equally good one after an hour.
- **But its errors look different:** the AI states an outdated rule with full confidence. That is why footnotes and warnings matter – checking a cited source takes seconds, so the time saving holds.
- **Expect a residual error rate** of roughly one in ten answers with such a model; source footnotes and warnings let users check. The assistant guides users to the reports; it does not replace them.
- **How we file reports matters:** a fixed header with title and date makes the timeline reliable; scanned documents need extra effort.
- **Open questions sit outside the unit:** security approval, access rights in the network, model licences.

## Recommendations – what should happen next

1. **Endorse the idea** of an AI-supported AAR database on our own hardware inside our closed network, and support it at the next level.
2. **Approve a pilot** with real, unclassified AARs from one area, using an open model of the ≈120-billion class on one server; measure the same points as this study.
3. **Introduce a uniform filing format** for new AARs: fixed header with title and date, author at the end, context (unit, situation, type of training); no scanned PDFs.
4. **Make sources and warnings mandatory** in any system: footnotes, automatic quote check, warning on possibly outdated statements; brief users to follow the footnotes.
5. **Ask the responsible offices to clarify:** security approval for new hardware and software in the closed network; computing capacity; access rights (who may see which reports); licence terms of the chosen model.
6. **Plan the next steps with partners:** multi-user operation with log-in and access rights; involve Universität der Bundeswehr München through computer-science theses or a hackathon (server operation, access rights, real-data pilot, scanned documents, red teaming).
