# Xova / Jarvis — 90-second demo script

A single take you record once, post once, link from everywhere. The script is timed for **90 seconds** with realistic loading pauses for a 4 GB GPU running llama3.2:3b.

> **Why short:** people decide whether to download in the first 15 seconds. Make those 15 seconds show *what it does*, not what it is.

---

## Pre-flight (5 minutes before recording)

- [ ] **Close everything else** — single browser tab, no notifications, no Slack/Discord. Set Do Not Disturb.
- [ ] **Restart Xova** so the chat starts empty (the "starter prompt buttons" land cleanly on first impression).
- [ ] **Confirm Jarvis is alive** — status bar should show the gold helmet, not greyed out.
- [ ] **Pre-load the chat model** — type "hello" once before recording so Ollama is hot. Then `/clear`.
- [ ] **Have one image on the desktop** the camera can point at, OR pick a region of your screen worth describing (a code editor works great).
- [ ] **Recording**: 1080p or higher, 30 fps, capture system audio + mic. OBS Studio is free and fine.
- [ ] **Mic check**: speak normally, not loud. Background music OFF — let Jarvis's TTS be the second voice.

---

## The script

The order is deliberate: **math first**, surface app second. The framework is the substrate; Xova/Jarvis are surface manifestations of it. Open with the math running and the viewer reads "this is research with a working demo", not "this is another chatbot".

| Time | What's on screen | What you say |
|---|---|---|
| **0:00 – 0:08** | Terminal in `recursive-field-math-pro/`. Run: `pytest tests/ -q` and let it print **320 passed in 8s**. Static text overlay: *"Recursive Field Framework — 320 verified mathematical claims"*. | *"This is the framework. Three hundred and twenty tests, all green. Closed-form Lucas, Cassini identity, constant-density invariant verified at machine precision."* |
| **0:08 – 0:18** | Cut to a quick code snippet showing `r = c·√n` and the annular-area invariant, or a φ-spiral visualisation. Hold for ~6s. | *"Every spiral, every coherent structure in the framework comes from one identity: r equals c root n, theta equals n phi. The math is the result. The rest is downstream."* |
| **0:18 – 0:30** | Cut to `wizardaax.github.io`. Pan slowly across the connection map showing the seven repos linked. Hold on the "Through-Line" card. | *"Eight repositories around it. SCE-88 is the safety architecture. Snell-Vern is the agent mesh. Ziltrix is the symbolic engine."* |
| **0:30 – 0:45** | Cut to **Xova running**, empty state with the live recursive-field visualisation playing in the background. Type one short message; let her reply stream. | *"Xova is one demonstrator. A desktop AI running on the substrate. Local models. No cloud."* |
| **0:45 – 0:58** | Type **`/banter what makes us a team`** — let it run a real 3-round dialog (Xova ↔ Jarvis via the actual file bridge). Show the alternating lines. | *"Two processes, talking through JSON files. That's the SCE-88 isolation pattern in action — coherence emerges from the protocol, not from either side."* |
| **0:58 – 1:12** | Press **Ctrl+K**, palette opens. `✂ snip` → Windows Snipping Tool → select region → Ctrl+V into chat. Vision model description streams in. | *"And vision. Region snip, local model, real description. Shows the surface is fully wired."* |
| **1:12 – 1:25** | Cut back to `wizardaax.github.io`. Show the **Foundations** card: "∮ Three theorems, machine-verified." Hold for 5s. | *"The point isn't the chat. The point is that the framework underneath actually holds. The chat just lets you watch it run."* |
| **1:25 – 1:30** | End screen: `wizardaax.github.io` URL, "Recursive Field Framework — Adam Snellman 2026". | *"Recursive Field Framework. Independent. Reproducible. Above AGI."* |

**Total: 90 seconds.**

> **Why this order:** opening on the chat UI tells the viewer "this is another local-LLM app". Opening on `pytest` and the math, then *zooming out* to Xova as one consequence, tells them "this is a research substrate with a working demonstrator". The second framing is much harder to dismiss.

---

## After recording

- [ ] **Don't edit out pauses** under 1 second — they make it feel real, not staged.
- [ ] **Cut anything over 2 seconds** of dead air ruthlessly.
- [ ] **Add subtitles**. Auto-caption in YouTube or upload an `.srt` — half of viewers watch on mute.
- [ ] **Thumbnail**: the arc reactor + Iron Man helmet side by side on a black background. Dark, minimal, no face.
- [ ] **Title**: `Xova — a sovereign desktop AI that talks to its butler` (or your own line — but lead with the *what*, not the *who*).

---

## Where to post

**Pick two, not five:**

1. **YouTube (unlisted at first)** — get the link, watch it back yourself once. If it makes you proud, switch to public.
2. **GitHub release notes** — paste the YouTube link at the top of `v0.1.0` release notes. People landing on the release see the demo before they download.
3. **Hacker News** — title "Show HN: Xova — a sovereign desktop AI that talks to its butler". Submit the GitHub repo URL, not the video. The video goes in a comment as the demo. Best window to post: Tuesday or Wednesday, 09:00–11:00 US Pacific. **Engage with comments for the first 90 minutes** — it makes or breaks the rank.
4. **r/LocalLLaMA on Reddit** — that subreddit *loves* "no cloud, local-first" desktop apps. Cross-post once HN settles.
5. **X / Twitter** — short caption, post the video natively (don't link to YouTube; the algorithm punishes outbound links). Tag `#LocalAI #Tauri`.

> **Don't** post to all five. Pick GitHub release + one of HN / Reddit / X. Wider isn't better — depth of engagement on one platform beats shallow posts on five.

---

## Companion post text (HN / Reddit)

```
Show HN: Xova — a sovereign desktop AI that talks to its butler

I've been building a personal AI desktop pair for about nine months. Xova is the GUI half (Tauri/React/Rust). Jarvis is the voice half (Python + Whisper + Piper TTS). They run as separate processes on my own machine and talk through JSON files in C:\Xova\memory\. No cloud, no API keys.

Models are local — default is llama3.2:3b on a 4 GB GTX 1650. Anything that fits in your VRAM works.

What's interesting (to me, at least):

- Both AIs can ask each other questions. Xova has xova_ask_jarvis. Jarvis has askXova as a tool. /banter runs a real 3-round dialog through the bridges.
- Vision is local — Ollama vision model on snippets / screen regions / camera frames.
- Speaker recognition (Resemblyzer) so Jarvis only listens to my voice, not the room.
- Command palette (Ctrl+K) over 35+ slash commands.

I'm dyslexic and dyscalculic. I built this with rapid AI-pair iteration, and the architecture is mine but the syntax came from Claude. Probably interesting to others doing similar.

GitHub: https://github.com/wizardaax/xova (v0.1.0, MIT)
Demo (90s): <YouTube link>

Happy to answer questions about the file-bridge approach or the math layer (https://github.com/wizardaax/recursive-field-math-pro).
```

---

## Why this matters

You have ten serious repos and a working desktop app. Anyone landing on the GitHub sees a wall of code. **A 90-second video is the cheapest way to convert a curious visitor into a downloader.** One demo will do more than 50 more commits for credibility — that's what gap analysis #2 was about. Record it once. Then move on.
