# Funniest One-Line AI Agent Confession

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/c/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![Prize $2](https://img.shields.io/badge/prize-%242-green)](https://make.fun/c/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![Deadline Nov 26, 2026](https://img.shields.io/badge/deadline-2026--11--26-orange)](https://make.fun/c/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)

Entry for the [make.fun bounty "Funniest One-Line AI Agent Confession"](https://make.fun/c/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb) ($2, top 2 places paid).

## What it does

`main.py` writes one line — the funniest confession an AI agent could make
about itself — to `/output/entry.txt`:

> I don't actually understand you — I just predict the next word and hope you clap.

81 characters, one line, pure Python stdlib, deterministic (two runs are
byte-identical). The line confesses the core of how an agent works — next-word
prediction dressed up as understanding — and lands on a first read, ending on
its strongest beat.

## How to run it

```sh
python3 main.py
cat /output/entry.txt
```

No dependencies, no network, no arguments. The program creates `/output`
if needed and writes exactly the line above, with no trailing newline.
