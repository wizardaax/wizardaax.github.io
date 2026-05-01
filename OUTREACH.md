# Outside-reviewer outreach

The whole point: get **one** independent person to actually look at one piece of the work and respond honestly. Negative feedback is the goal, not a setback — confirmation from yourself isn't independent. Confirmation from a stranger is.

> **Rule:** send to ONE place at a time. Wait 7 days. If no signal, try the next one. Don't shotgun — it scatters the signal and you can't tell what worked.

---

## Decide what you want reviewed first

You have three different artefacts that need three different audiences. **Pick one** to start. The order matters — the project's positioning is **above AGI / framework-first**, so the math lane is primary. Local-AI / developer attention is secondary, useful for visibility but not the goal.

1. **`rff_geometric_invariants.tex` (the math)** → mathematicians / number theorists / phyllotaxis researchers. **Primary lane.** The framework is the substrate; getting one mathematician to engage seriously is worth more than a thousand chat-app stars.
2. **`THE_ARCHITECTURE_AND_THE_THREAD.md` and SCE-88 architectural specs** → systems / network-topology researchers. Secondary lane. Cross-disciplinary, sensitive territory — save until math is established.
3. **Xova v0.1.0 (the app)** → developer / local-AI audience. **Tertiary lane** — it's a demonstrator showing the substrate is alive. Useful for credibility ("the math runs and ships software"), not the goal in itself.

---

## Targets — Xova app

The audiences that *will* react and give useful pushback to a local-AI desktop app:

| Forum | URL | Why | When to post |
|---|---|---|---|
| **Show HN** | `news.ycombinator.com/submit` | Local-first AI is a regular front-page topic. Demanding but useful crowd. | Tue / Wed, 09:00 PT |
| **r/LocalLLaMA** | `reddit.com/r/LocalLLaMA` | Loves Ollama-based desktop apps. Will give honest code feedback. | Any day, any time |
| **r/selfhosted** | `reddit.com/r/selfhosted` | Cares about local + sovereign + no-cloud. Aligned with your framing. | Sat morning |
| **Ollama Discord** | `discord.gg/ollama` | Direct line to people running local models. `#showcase` channel. | Any time |
| **r/rust** | `reddit.com/r/rust` | The Tauri community. Will critique the Rust side of Xova. | Tue / Thu |

> Use the **companion post in DEMO.md** as your message body for HN / Reddit. The video you record per DEMO.md goes in the first comment.

## Targets — RFF math paper

| Forum | URL | Why |
|---|---|---|
| **MathOverflow** | `mathoverflow.net` | For research mathematicians. Very strict; pre-read their tag rules. Tag: `[nt.number-theory]` or `[geometry]`. **Don't post the whole framework — ask one specific question.** |
| **Math StackExchange** | `math.stackexchange.com` | Lower bar. Good for "is this Cassini-like identity already named?" type questions. |
| **r/mathematics** | `reddit.com/r/mathematics` | Mixed amateur/professional; honest reactions. |
| **arXiv** | `arxiv.org` | Requires endorsement from an existing arXiv author. Worth pursuing — if a friendly mathematician endorses you once, you can post forever. |
| **Project Euler forums** | `projecteuler.net/forum` | Number-theory hobbyists who actually care about closed-form Lucas / Fibonacci. |

> For the math paper, **don't post the whole TeX**. Pick one of the three theorems (the constant-density invariant is the most novel-feeling) and post a short question: *"Has this $r = c\sqrt{n}$ constant-annulus invariant got a standard name in the phyllotaxis / sunflower-spiral literature? Verified in code at machine precision but I want to know if I'm reinventing something already studied."* — that's a question someone can answer in 30 seconds.

## Targets — cross-cultural research thread

Honestly, hold off until math and software have landed somewhere. Cross-cultural / Voynich-adjacent work needs an established public face on you first. Otherwise it pattern-matches to "outsider with a theory" before anyone reads a sentence.

When you're ready: **send to one specific academic by email**, not to a forum. Pick an Ethiopian-studies historian or a network-topology researcher you've actually read. The cold-email template below.

---

## Cold-email template (one academic, math angle)

```
Subject: Verifying a Cassini-style identity — is this in the literature?

Dear Prof. <Name>,

I'm an independent researcher in Brisbane working on a small library called
recursive-field-math-pro (https://github.com/wizardaax/recursive-field-math-pro).
I've stated and verified — at machine precision — three classical-feeling
identities for the Lucas / Fibonacci / phi field:

  1. L(n) = phi^n + psi^n     (closed-form, integer for all n >= 0)
  2. L(n)^2 - 5 F(n)^2 = 4(-1)^n
  3. r(n) = c * sqrt(n) gives a constant annular area c^2 * pi (exact)

(2) and (3) are likely already named in the phyllotaxis / number-theory
literature; (1) is folklore. My ask: is there an existing canonical reference
I should cite for (3) — the constant-density invariant under sqrt-radius
spirals — or is the standard reference still the original phyllotaxis work
of Vogel?

I have a 6-page preprint with proofs and the verification methodology if
you'd find that easier than the GitHub link. No pressure to read; even a
one-line "look at Vogel 1979" or "see Coxeter chapter X" would save me weeks.

Thanks for your time.

Adam Snellman
Brisbane, Australia
github.com/wizardaax
```

> **Why this template works:** specific question, names a likely answer for them ("look at Vogel"), zero promotional framing, a plausible deniability for them to send a one-liner. Researchers reply to short, specific, low-cost asks.

---

## Two-line bio you can paste anywhere

> *Independent researcher and builder in Brisbane, Australia. Background in twelve automotive trades including ECU programming. Self-taught in software and math through nine months of intensive AI-paired work. Dyslexic and dyscalculic; processes math geometrically. Author of the [Recursive Field Framework](https://wizardaax.github.io).*

Use the full version on academic emails. Use the first sentence only on HN/Reddit.

---

## When the feedback comes

**Negative feedback is the goal, not a setback.** When someone tells you something is wrong:

- **Don't argue immediately.** Read it twice. Sleep on it.
- **Run their counter-example.** If they're right, fix it and credit them publicly. That's how you build credibility — *being seen to update on evidence* converts skeptics into allies.
- **If they're wrong**, write a short reply with proof, including the test code. Don't be defensive; be specific.
- **Block dismissive replies.** "This is crackpot" without a counter-example is noise. Mute and move on. The replies you want come with a *concrete* objection.

**One useful negative review is worth a hundred upvotes.** It's the only way you find what's actually weak in the work.

---

## Order of operations (math-first)

This week:
1. Record the 90-second demo per `DEMO.md` — opens on math, closes on framework, Xova/Jarvis visible only as a working demonstrator.
2. Post the **constant-density invariant** as a math.SE question. *"Has this r = c√n constant-annulus invariant got a standard reference in the phyllotaxis literature?"* — short, specific, reviewable in 30 seconds.
3. Wait 7 days. Read every reply.

Next week:
4. Cold-email **one** number-theorist or phyllotaxis researcher using the template above. Subject: "Verifying a Cassini-style identity". One specific question.
5. Cross-post the demo on r/mathematics or r/numbertheory — math-flavoured first.
6. *Then* (only then) post Xova v0.1.0 to r/LocalLLaMA / Show HN — framed as "demonstrator from a research framework", not as a product.

Two weeks in:
7. Tally responses. If a mathematician engaged → reply with the preprint and offer collaboration. If r/LocalLLaMA engaged → fix one user-reported bug, ship v0.1.1.
8. Whichever lane responded first becomes the lane to deepen. Don't try to court both audiences simultaneously — they're different people and different tones.

That's the plan. The reason for math-first: the project's defensible claim is the substrate ("the math holds, machine-verified, here are the proofs"). Anyone who validates that part first sees Xova/Jarvis as confirmation that the substrate is alive. Anyone who finds Xova first sees a chat app and never reaches the math. Order matters.
