import yt_dlp
class begin():
    def __init__(self,url):
        self.urls=str(url)
    def convert(self):
        video_url =self.urls   #url
        video_info =yt_dlp.YoutubeDL().extract_info(
            url = video_url,download=False
        )                                   #file name
        string=str(video_info['title'])
        string=string.replace('"','')
        string=string.replace('|','')
        string=string.replace('/','')
        filename = f"music/{string}.mp4"         #расширение
        options={
            'format':'best',                #bestaudio/best, bestvideo/best
            'keepvideo':True,               #нужно ли видео
            'outtmpl':filename,
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])
        print("Download complete... {}".format(filename))
    def name(self):
        video_url = self.urls  # url
        video_info =yt_dlp.YoutubeDL().extract_info(
            url=video_url, download=False
        )  # file name
        string = str(video_info['title'])
        string = string.replace('"', '')
        string=string.replace('|','')
        string = string.replace('/', '')
        filename = f"music/{string}.mp4"  # расширение
        return filename