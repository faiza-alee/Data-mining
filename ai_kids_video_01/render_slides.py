import os
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip

SLIDES = [
    ("Slide 1 — Title", 5),
    ("Did you use AI today?", 20),
    ("What is AI?", 35),
    ("Narrow AI", 15),
    ("AI → ML → DL", 35),
    ("How machines learn", 45),
    ("Real-life AI", 20),
    ("More examples", 20),
    ("Ethics: fair, private, safe", 20),
    ("Mini Activity: Paper Classifier", 15),
    ("Activity steps", 35),
    ("Features = clues", 20),
    ("Recap", 15),
    ("Next Episode", 15),
]

WIDTH, HEIGHT = 1920, 1080
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "build")


def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_slide_image(text: str, index: int) -> str:
    img = Image.new("RGB", (WIDTH, HEIGHT), color=(24, 27, 51))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 96)
    except Exception:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (WIDTH - w) // 2
    y = (HEIGHT - h) // 2
    draw.text((x, y), text, font=font, fill=(255, 234, 98))

    path = os.path.join(OUTPUT_DIR, f"slide_{index:02d}.png")
    img.save(path)
    return path


def build_placeholder_video(audio_path: str | None = None, out_path: str = "video_placeholder.mp4") -> str:
    ensure_dir(OUTPUT_DIR)

    clips = []
    for i, (text, duration) in enumerate(SLIDES, start=1):
        png_path = create_slide_image(text, i)
        clip = ImageClip(png_path).set_duration(duration)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    if audio_path and os.path.exists(audio_path):
        audio = AudioFileClip(audio_path)
        video = video.set_audio(audio)

    output = os.path.join(OUTPUT_DIR, out_path)
    video.write_videofile(output, fps=24)
    return output


if __name__ == "__main__":
    print("Rendering placeholder video...")
    path = build_placeholder_video()
    print(f"Saved: {path}")
