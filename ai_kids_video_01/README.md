# AI for Kids — Episode 1 Assets

This folder contains the script, slides, storyboard, captions, and a simple render script to generate a placeholder video from slide titles.

## Files
- outline_objectives.md
- script_voiceover.md
- slides_copy.md
- storyboard_shotlist.md
- quiz_activity.md
- captions_en.srt
- yt_metadata.md
- thumbnail_brief.md
- render_slides.py
- requirements.txt

## Quick Start (placeholder video)
1) Create a virtualenv (optional) and install dependencies:
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
2) Render the placeholder video:
```bash
python render_slides.py
```
3) Output will be in `build/video_placeholder.mp4`.

To add voiceover, export your audio file and pass the path in `build_placeholder_video(audio_path=...)` inside `render_slides.py`.