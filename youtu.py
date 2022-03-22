from pytube import YouTube

link = "https://www.youtube.com/watch?v=SiIMadgiv_g&ab_channel=EHPMusicChannel"
yt = YouTube(link).streams
yt.filter(subtype="mp4").first().download('./youtube')