# Caption Catch

Find unusually fast subtitle cues and return straight to their location in the edit.

Go straight to the line that is hard to read at playback speed. The timestamp and characters per second tell the editor where to look and how much extra time a rewrite might buy.

## Screen transitions

Move from the caption file to its fastest passage, then check the retimed file.

![Caption Catch front display. Move from the caption file to its fastest passage, then check the retimed file.](media/guide/screen-transitions.gif)

<details>

<summary>Watch the rear display</summary>

![Caption Catch rear display during the recorded controls](media/guide/screen-transitions-rear.gif)

</details>

## Find the fastest caption

1. Point the companion at a UTF-8 `.srt` file and set the reading-speed threshold. The example threshold is 20 characters per second.
2. Read the number on **FAST CAPTIONS**. Turn once to inspect the highest-rate cue.
3. Locate the timestamp in your editor. The front shows 47.0 characters per second in the recorded example. The rear includes the cue excerpt and duration.

![One fast caption gives way to its timestamp at 00:05 and rate of 47.0 c/s.](media/guide/open-fast-cue.gif)

## Check the file after retiming

1. Lengthen the cue in your subtitle editor or reduce its text, then save the SRT.
2. Return to **FAST CAPTIONS** and refresh to check how many cues still exceed your limit. More detail pages list the fastest cues and the longest caption.
3. Keep the threshold consistent between edits so the before-and-after counts are comparable.

![The timestamped cue gives way to the fast-caption count of one.](media/guide/return-to-cue-count.gif)

## Example from the emulator

In the two-cue file, exactly one cue exceeded the threshold. A 47-character cue shown for one second reads at 47 characters per second. At three seconds the same text would come in under 20. Markup tags are left out of the count. The companion read a local SubRip file containing the two test cues.

## Set up the source

Set file to a UTF-8 SubRip .srt file and max_cps to the desired characters per second. Pages rank the 15 fastest cues with start time, character count and duration, followed by the longest caption. Markup tags are excluded. Cue text stays on the local device and companion.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run in the emulator

Open BUSY Bar Emulator. From this repository, run:

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

Press **Back** to exit.

The GIFs are excerpts from the emulator recording. Each LED occupies a 16 × 16 cell with a black border. The end frames pause for reading.

[Full recording](media/controls.mp4) · [Rear display](screenshots/back-1.png) · [Firmware test](EMULATOR-QA.md) · [MIT license](LICENSE)
