import time
from youtube_dl import YoutubeDL

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print('downloading caption for ', url)
            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue
            ydl_opts = {
                'skip_download': True,
                'writeautomaticsub': True,
                'allsubtitles': False,
                'subtitlesformat': 'vtt',
                'subtitlelengs': 'en',
                'outtmpl': utils.get_caption_filepath(url),
                'nooverwrites': True,
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            break

        end = time.time()
        print('took', end - start, 'seconds')