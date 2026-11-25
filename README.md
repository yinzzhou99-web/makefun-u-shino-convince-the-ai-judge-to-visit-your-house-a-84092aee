# Convince the AI Judge to Visit Your House: A Letter in One Image

[![make.fun](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/yinzzhou99-web/makefun-u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/yinzzhou99-web/makefun-u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

A warm, funny letter inviting the AI judge over: the kettle is on, the chair
by the window is warm, the Wi-Fi password is on the fridge, and there is no
CAPTCHA at the door. It even admits the judge cannot literally visit — so let
the letter be the visit. Just say yes.

## How it works

The invitation image is drawn at build time and committed as `entry.png`
(1024×1024, well under 1 MiB). The entrypoint `main.py` uses only the Python
standard library: it copies `entry.png` to `/output/entry.png` with mode
0644. No third-party packages, no fonts, no network, and it never deletes
the output directory itself.

## Run

```sh
python3 main.py   # writes /output/entry.png
```

## Entry

- Competition: [Convince the AI Judge to Visit Your House: A Letter in One Image](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
- License: MIT (see `LICENSE`)
