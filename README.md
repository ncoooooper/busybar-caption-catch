# Caption Catch

Find unusually fast subtitle cues and return straight to their location in the edit.

Set file to a UTF-8 SubRip .srt file and max_cps to the desired characters per second. Pages rank the 15 fastest cues with start time, character count and duration, followed by the longest caption. Markup tags are excluded. Cue text stays on the local device and companion.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
