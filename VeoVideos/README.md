### Veo videos

Videos contained there are Veo Videos used for models validation, to ensure that player detection and tracking is wokrking properly. The 30 second slices of videos were extracted from web with use of ffmpeg tool as follows:

```
ffmpeg -ss 00:17:15 -to 00:17:45 -i https://c.veocdn.com/0917fd50-bae8-49a9-b12d-bad42d0f7236/standard/machine/e49850c6/video.mp4 -c copy veovideo.mp4
```

Afterwards, the videos were cut into frames, with 10 FPS frequency:

```
ffmpeg -i veovideo.mp4 -vf fps=10 img1/%06d.jpg
```
