import os,sys,subprocess;Д=os.path.dirname(os.path.abspath(__file__));Г=os.path.join(Д,'код');бЮ=os.path.join(Д,'build');os.makedirs(бЮ,exist_ok=True)
def ба(*ж):subprocess.run([sys.executable,*ж],cwd=Д,check=True)
ба(os.path.join(Г,'рен.py'),'video','video_silent.mp4');ба(os.path.join(Г,'зв.py'));т=os.path.join(Д,'video.mp4');subprocess.run(['ffmpeg','-y','-v','error','-i',os.path.join(бЮ,'video_silent.mp4'),'-i',os.path.join(бЮ,'audio.wav'),'-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-t','33.5',т],check=True);print('VIDEO:',т)
