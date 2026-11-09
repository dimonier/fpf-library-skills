# Author's Recipes — quick-reference for the most-used patterns

A curated collection of the author's recipes: one recipe = one "use it to…" line
pointing at the pattern that does it. 25 Core patterns + 9 domain-framework (DPF)
entry points.

**Source:** Anatoly Levenchuk, "Шпаргалка по наиболее ходовым паттернам библиотеки FPF",
https://ailev.livejournal.com/1815855.html (CC BY 4.0). The "use it to…" phrasings are the author's.

This is an entry index, not a substitute for the patterns: it answers "what do I
reach for first"; you then read the pattern itself.

## How to use

1. Find the row whose "use it to…" matches what you want.
2. Load the target from the "Where" column and read only the section you need —
   each reference opens with a Trigger / Problem frame / First move block.
3. Core patterns are loaded from `references/<id>.md`. Paths below are relative to
   the skill root (the folder containing `SKILL.md`).

> **DPF patterns.** Rows whose "Where" says *outside this skill* are domain-basis
> patterns that live in separate DPFs, not in `fpf-core` (which holds only the
> Core — 404 patterns). They are shown without a file path: resolve the framework
> by name and load it there.

## Recipes

| Pattern | Use it to… | Where |
|---|---|---|
| `F.19` | strip bureaucratic stodge and woolly hedging out of a text, including the many unnecessary qualifiers | `references/F.19.md` |
| `C.11.DUA` | get an actual expert opinion instead of "not proven / not shown / not tested" — if all the data were already there, why ask? | `references/C.11.DUA.md` |
| `C.39.QR` | come back from a long dig into the details to the original question and finish what the conversation was for | `references/C.39.QR.md` |
| `GOALS.7` | delegate work so you stop nudging after every step: set the result, the means, the authority and a clear "done" | Goal Construction DPF — outside this skill |
| `A.15.10` | resume from the right place after a break or a handoff to another agent, with what's done and what's left accounted for | `references/A.15.10.md` |
| `B.5.RR` | redo the reasoning and conclusions that depended on your "no, I meant something else" | `references/B.5.RR.md` |
| `B.5.SD` | finally get somewhere in a discussion: work through the objections, join the useful ideas and land an answer | `references/B.5.SD.md` |
| `EXD` | explain exactly the place where you stopped understanding, with an example that shows how it works | Explanation Design DPF — outside this skill |
| `NSTD` | turn a heap of thoughts into a text you can follow and still hear your own voice in | Narrativization DPF — outside this skill |
| `A.6.3.CSC` | cut a text to a third without throwing away the important part or turning "sometimes helps" into "always works" | `references/A.6.3.CSC.md` |
| `C.39.WA` | make a twenty-section survey cohere into how the whole subject is arranged and why its parts connect that way | `references/C.39.WA.md` |
| `NOT` | make a table, diagram or formula legible: find what you need, trace a dependency, change a part | Notational Engineering DPF — outside this skill |
| `F.0.1` | first establish what an author means by familiar words, before inventing your own reading | `references/F.0.1.md` |
| `F.0.2` | move past "the first author says…, the second…" to a synthesis that shows what new understanding follows | `references/F.0.2.md` |
| `F.1` | select what is actually worth reading instead of drowning in "50 more random links from the internet" | `references/F.1.md` |
| `KCAE` | get past "nothing found": rephrase the query, read the sources themselves (knowledge-corpus access engineering) | Knowledge-Corpus Access DPF — outside this skill |
| `A.10` | trace each important claim to its source and check whether the source really supports it (agents love unread citations) | `references/A.10.md` |
| `RMP.7` | get from a pile of studies to where they agree, why they diverge, and what is independent versus a retelling of the same result | Research Method Practice DPF — outside this skill |
| `B.5.2` | stop falling in love with the first plausible explanation and compare serious alternatives | `references/B.5.2.md` |
| `C.28.CM` | turn "it is all because of X" into how X produces the result, what other causes are possible, and how to tell them apart | `references/C.28.CM.md` |
| `A.7` | stop passing off a plan as work done, a system description as a working system, tool availability as knowing how to use it | `references/A.7.md` |
| `C.39` | turn "set up the interaction" or "adopt AI" into who does what, with what, and how the actions connect | `references/C.39.md` |
| `C.40` | get five genuinely different options instead of one idea under five names | `references/C.40.md` |
| `PSDA` | escape "two options and both are bad": reformulate the problem, find other moves, compare consequences | Decision Design DPF — outside this skill |
| `A.1.STM` | make the four project questions converge — who needs it and why, how it works, what it is made of, who builds it (the systems mantra) | `references/A.1.STM.md` |
| `C.32` | get several system layouts, each with which part does what, how they connect, and what it sacrifices | `references/C.32.md` |
| `C.38` | compare buy / build / delegate-to-AI honestly for the same result but different faff in building, maintaining and later undoing it | `references/C.38.md` |
| `C.11.CRC` | compare a fashionable practice against how you already work: what really improves and what the switch costs ("better is the enemy of good") | `references/C.11.CRC.md` |
| `C.43` | turn "let's gather metrics and make a plan" into who picks which action from which observations, and when to change the decision itself | `references/C.43.md` |
| `STR.18` | bring the strategy in line with reality: what useful thing we want, how we will get it, and whether people and money cover all the promises at once | Strategy DPF — outside this skill |
| `C.39.WI` | pick what to improve next: where you lose energy or miss a result and which change pays for its faff | `references/C.39.WI.md` |
| `C.42` | cut avoidable faff and keep the needed result — especially after the agent "saved time" you now spend an hour fixing | `references/C.42.md` |
| `E.23` | make review actually improve the result: check the payoff of the edits, keep what worked, and stop the endless "could be better" in time | `references/E.23.md` |
| `HCD` | make learning land in real work: find out in advance what to teach, then verify the result in the job, not in a textbook retelling | Human Capability Development DPF — outside this skill |