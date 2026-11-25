import os,sys,json,math,time,subprocess,multiprocessing as mp;import numpy as np,cv2;from общ import*;import мир as вю;from тьма import гл;бз=os.path.join(вы,'build');os.makedirs(бз,exist_ok=True);бЕ=None
def дШ():еГ=json.load(open(os.path.join(вы,'words.json'),encoding='utf-8'));return еГ
еМ,еЛ=np.mgrid[:аа,:аз].astype(np.float32);дк=np.hypot((еЛ-аз/2)/(аз/2),(еМ-аа/2)/(аа/2));еВ=(1-.55*np.clip(дк-.35,0,1.2)**1.6)[...,None].astype(np.float32);гЁ=(np.clip((дк-.3)/.95,0,1)**1.25)[...,None].astype(np.float32);вэ=90,160;вё,гг=np.mgrid[:вэ[0],:вэ[1]].astype(np.float32);гг/=вэ[1];вё/=вэ[0];ец=[np.random.default_rng(з).normal(0,3.2,(аа,аз,1)).astype(np.float32)for з in range(6)]
def еЫ(я,в,ах,к,К,О):аЛ=math.atan2(О[0,2],О[2,2]);Ъ=.5-аЛ*.45+.06*math.sin(в*.3);бц=.42+.03*math.cos(в*.23);ё=np.hypot((гг-Ъ)*1.35,вё-бц);жЯ=np.exp(-ё*ё*3.2)[...,None];жЁ=np.exp(-np.hypot((гг-(1-Ъ)*.9-.1)*1.3,вё-.85)**2*5.)[...,None];ах=np.array(ах,np.float32);к=np.array(к,np.float32);иЕ=np.array(аЬ(к,(255,255,255),0.),np.float32)[::-1][::-1];С=ах*(.85+.5*(1-вё)[...,None])+к*жЯ*.26+(к[[2,0,1]]*.6+30)*жЁ*.16;С=np.clip(С,0,255);Ы=cv2.resize(С,(аз,аа),interpolation=cv2.INTER_CUBIC);return np.ascontiguousarray(Ы[...,::-1]).astype(np.uint8)
def зТ(в,аД=None):
 аф=бЕ.го(в)[3]
 if аф>450:дХ=.014*П(аф/1400.,.4,1.);еН=sum((ег(в+д,аД).astype(np.float32)for д in(-дХ,0,дХ)))/3;return еН.astype(np.uint8)
 return ег(в,аД)
def ег(в,аД=None):я=бЕ;К,О,ф,вЩ=я.го(в);ах,к,иЗ=я.зБ(в);дь=0.;аА=еЫ(я,в,ах,к,К,О);ае=np.zeros((аа,аз,3),np.uint8);Х=я.го(в-.022);вю.жю(ае,в,К,О,ф,к,560.);вю.жА(ае,я,в,К,О,ф,к);вю.жё(ае,я,в,К,О,ф,(Х[0],Х[1],Х[2])if True else None,к,вЩ);аА=cv2.add(аА,ае);аЪ=вю.жч(я,в,К,О,ф);вю.жя(аА,аЪ,К,О,ф);return зК(я,аА,в,ае,к,аД if аД is not None else int(в*въ))
def зК(я,аА,в,ае,к,аД):
 бФ=я.аи['red'](в);бН=я.аи['glitch'](в);т=аА.astype(np.float32);ид=cv2.resize(аА,(320,180),interpolation=cv2.INTER_AREA).astype(np.float32);ду=np.clip(ид-150,0,None)*1.1;еЮ=cv2.GaussianBlur(ду,(0,0),6);еЯ=cv2.GaussianBlur(ду,(0,0),14);т+=cv2.resize(еЮ*.42+еЯ*.55,(аз,аа),interpolation=cv2.INTER_LINEAR);т*=еВ
 if бм(math.floor(в*17)+9)>.93 and в>1:т*=.72
 if бФ>.002:т=т*(1-np.clip(бФ*гЁ*.55,0,.8))+гЁ*бФ*np.array([14,8,190],np.float32)*.9;ез=np.ones((аа,1,1),np.float32);ез[::3]=1-.14*min(1,бФ*2);т*=ез
 if бН>.02:
  а=int(round(бН*14));р,иБ,гЗ=т[...,0],т[...,1],т[...,2];т[...,0]=np.roll(р,а,1);т[...,2]=np.roll(гЗ,-а,1);Ж=np.random.default_rng(аД*7+1)
  for ди in range(int(2+бН*5)):
   аь=int(Ж.integers(0,аа-40));дУ=int(Ж.integers(6,34));Ш=int(Ж.integers(-1,2)*(6+бН*36))
   if Ш:т[аь:аь+дУ]=np.roll(т[аь:аь+дУ],Ш,1)
 бш=я.аи['flash'](в)
 if бш>.01:т+=бш*np.array([70,40,255],np.float32)*.5
 т+=ец[аД%6]*(1+.6*бФ);т[:52]=0;т[-52:]=0;жО=бп(в/.55)*бп((аО-в)/.8);т*=жО;return np.clip(т,0,255).astype(np.uint8)
def зн():global бЕ;аК=дШ();бЕ=гл(аК)
def ич(з):return зТ(з/въ,з).tobytes()
def вй():
 global бЕ;иё=sys.argv[1]if len(sys.argv)>1 else'video';аК=дШ();бЕ=гл(аК);json.dump(dict(total=аО,events=бЕ.ач,scenes=[dict(id=е.зм,S=е.Г,dur=е.Р)for е in бЕ.Й]),open(os.path.join(бз,'events.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1);т=os.path.join(бз,sys.argv[2]if len(sys.argv)>2 else'video_silent.mp4');н=int(round(аО*въ));гу=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{аз}x{аа}','-r',str(въ),'-i','-','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p',т],stdin=subprocess.PIPE);ы=time.time();зэ=max(1,min(os.cpu_count()or 1,6));жш=mp.get_context('spawn'if sys.platform.startswith('win')or sys.platform=='darwin'else'fork')
 with жш.Pool(зэ,initializer=зн)as зЙ:
  for а,р in enumerate(зЙ.imap(ич,range(н),chunksize=4)):
   гу.stdin.write(р)
   if а%60==0:print(f'frame {а}/{н}  {time.time() - ы:.0f}s',flush=True)
 гу.stdin.close();гу.wait();print('video:',т)
if __name__=='__main__':вй()
