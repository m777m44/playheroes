import os,json,numpy as np;from scipy.signal import butter,sosfilt,fftconvolve;from scipy.io import wavfile;from общ import вы,аО;Б=44100;бз=os.path.join(вы,'build');Ж=np.random.default_rng(7)
class де(np.ndarray):
 def __add__(ж,р):
  if isinstance(р,np.ndarray)and р.ndim==1 and(ж.ndim==1)and(len(ж)!=len(р)):н=max(len(ж),len(р));м=np.zeros(н);м[:len(ж)]+=np.asarray(ж);м[:len(р)]+=np.asarray(р);return м.view(де)
  return np.ndarray.__add__(ж,р)
 __radd__=__add__
def аП(ф):
 def щ(*ж,**а):return np.asarray(ф(*ж,**а)).view(де)
 щ.__name__=ф.__name__;return щ
def аЙ(д):return np.arange(int(д*Б))/Б
@аП
def ащ(д):return Ж.standard_normal(int(д*Б))
@аП
def И(м,ф,гА=2):return sosfilt(butter(гА,ф,'low',fs=Б,output='sos'),м)
@аП
def гй(м,зф,гщ,гА=2):return sosfilt(butter(гА,[зф,min(гщ,Б/2-100)],'band',fs=Б,output='sos'),м)
@аП
def бТ(м):return м/(np.max(np.abs(м))+1e-09)
@аП
def аШ(д,аУ):return np.exp(-аЙ(д)/аУ)
@аП
def аэ(м,ж=.004):
 н=int(ж*Б);м=м.copy()
 if н>0 and н<len(м):м[:н]*=np.linspace(0,1,н)
 return м
@аП
def ву(ф,д,аУ=None,ао=0):м=np.sin(2*np.pi*ф*аЙ(д)+ао);return м*аШ(д,аУ)if аУ else м
@аП
def ан(бч,вЗ,д,аУ=None,жЛ=True):в=аЙ(д);й=в/д;ф=бч*(вЗ/бч)**й if жЛ else бч+(вЗ-бч)*й;м=np.sin(2*np.pi*np.cumsum(ф)/Б);return м*np.exp(-в/аУ)if аУ else м
@аП
def из(д,бч,вЗ,дф=.9,н=12,дч=None):
 в=аЙ(д);й=в/д;жП=дч(й)if дч else бч*(вЗ/бч)**й;т=np.zeros_like(в);бШ=ащ(д);еЬ=np.geomspace(150,9000,н)
 for р in еЬ:ш=гй(бШ,р/(1+дф*.5),р*(1+дф*.5));п=np.exp(-(np.log(жП/р)/.38)**2);т+=ш*п
 return бТ(т)
@аП
def ги(ф,д=1.,зР=3.5,вН=2.5,аУ=.35):в=аЙ(д);Ч=np.sin(2*np.pi*ф*зР*в)*вН*np.exp(-в/(аУ*.5));return np.sin(2*np.pi*ф*в+Ч)*np.exp(-в/аУ)
def зВ(и):ж=(и+1)*np.pi/4;return np.cos(ж),np.sin(ж)
class ещ:
 def __init__(е,н):е.дБ=np.zeros((2,н));е.бИ=np.zeros((2,н));е.еж=np.zeros((2,н));е.н=н
 def put(е,м,в,щ=1.,вл=0.,гм='dry',вУ=.15,дЯ=None):
  з=int(в*Б)
  if з>=е.н or з+len(м)<0:return
  if з<0:м=м[-з:];з=0
  Щ=min(len(м),е.н-з);м=м[:Щ]
  if дЯ is None:бН,зж=зВ(вл);гы=бН*м,зж*м
  else:й=np.linspace(0,1,Щ);и=вл+(дЯ-вл)*й;ж=(и+1)*np.pi/4;гы=np.cos(ж)*м,np.sin(ж)*м
  ик=е.бИ if гм=='big'else е.дБ
  for ц in(0,1):ик[ц,з:з+Щ]+=гы[ц]*щ;е.еж[ц,з:з+Щ]+=гы[ц]*щ*вУ
def жЬ():
 д=3.2;в=аЙ(д);ш=np.zeros_like(в)
 for ф,щ in((130.8,.6),(196.,.5),(261.6,.5),(329.6,.35)):ш+=np.sin(2*np.pi*ф*в)*np.sin(np.pi*np.clip(в/д,0,1))**1.4*щ
 return аэ(ш*.4,.05)
def жЩ():д=1.3;н=int(д*Б);й=np.linspace(0,1,н);ш=из(д,400,3000)*np.sin(np.pi*й)**1.5*.5+ан(90,220,д)*й**1.5*.25;return аэ(ш,.02)
def жШ(а=0,бИ=False):щ=1. if бИ else.55;вв=ан(80+а*4,28,1.3,.38)*1.3;вг=И(ащ(.5),2600-а*150)*аШ(.5,.1)*.9;иГ=ги(173+а*11,1.2,2.3,3.,.5)*.22+ги(261,1.,3.1,2.,.4)*.15;н=int(1.4*Б);ш=np.zeros(н);ш[:len(вв)]+=вв;ш[:len(вг)]+=вг;вУ=ан(300,1600,.25)*np.linspace(0,1,int(.25*Б))**2*.35;еб=np.zeros(н+int(.25*Б));еб[int(.25*Б):]=ш;return аэ(еб*щ,.0005)
def жХ(д=11.):
 н=int(д*Б);в=аЙ(д);й=np.linspace(0,1,н);ах=np.sin(2*np.pi*55*в)+.8*np.sin(2*np.pi*55.6*в)+.5*np.sin(2*np.pi*82.4*в+np.sin(2*np.pi*.13*в));дь=И(ащ(д),380)*(.6+.4*np.sin(2*np.pi*.21*в));вЕ=np.minimum(1,й*6)*np.minimum(1,(1-й)*8);ш=бТ(ах)*.6+бТ(дь)*.5;дС=np.zeros(н);гГ=.86;а=0
 while а*гГ<д-.4:
  for бУ,щ in((0,1.),(.2,.7)):
   з=int((а*гГ+бУ)*Б);р=ан(95,40,.22,.06)*щ
   if з+len(р)<н:дС[з:з+len(р)]+=р*(.4+.6*а*гГ/д)
  а+=1
 return (ш*.5+дС*.9)*вЕ
def бЧ(м,щ=1.15):return np.tanh(м*щ)/np.tanh(щ)
def жФ(д=1.9):н=int(д*Б);й=np.linspace(0,1,н);вЕ=np.sin(np.pi*й)**2;ж,еХ,ц=И(ащ(д),220),И(ащ(д),800),И(ащ(д),2200);п=np.sin(np.pi*й);иб=бТ(ж*(1-п)+еХ*п+ц*п**3*.6)*вЕ;return аэ(иб*.75+ан(150,60,д)*вЕ*.22,.06)
def гц(а=0,бИ=False):щ=1. if бИ else.7;ш=ан(78,30,1.5,.42)*1.1+ву(46,1.5,.5)*.5+И(ащ(.4),700)*аШ(.4,.07)*.7;return аэ(бЧ(ш*щ),.002)
def жЫ(а=0):
 if а==0:return аэ((ву(660,.09,.03)+.8*ву(880,.14,.05))*.7,.003)
 return аэ(ан(230,120,.3,.12)*.9+И(ащ(.06),900)*аШ(.06,.02)*.4,.003)
def жЪ():return аэ(гй(ащ(.015),900,3500)*аШ(.015,.004)*.8+ву(640,.02,.006)*.3,.0005)
def дМ(гд=1.):д=.9;в=аЙ(д);жС=np.sin(2*np.pi*55*в+4.5*np.sin(2*np.pi*110*в));щ=(np.sin(2*np.pi*9*в)>-.1).astype(float);щ=И(щ,120,1);return аэ(И(жС,1400)*щ*аШ(д,.5)*гд*.9,.004)
def жЭ(д=2.4):в=аЙ(д);й=в/д;зЦ=(ан(50,340,д)+.6*ан(100,680,д))*й**2.6;return аэ(бЧ(зЦ*.8+И(ащ(д),700)*й**3*.35),.02)
def жЮ():д=1.8;н=int(д*Б);в=аЙ(д);ш=np.zeros(н);вг=гй(ащ(.25),1800,9000)*аШ(.25,.05)*1.1;ш[:len(вг)]+=вг;дс=ан(95,24,1.6,.5)*1.6;ш[:len(дс)]+=дс;зъ=(np.sin(2*np.pi*233*в)+.7*np.sin(2*np.pi*349.6*в)+.5*np.sin(2*np.pi*551*в))*np.exp(-в/.5)*.35;ш+=зъ;бБ=ан(2400,90,.45,.1)*.5;ш[:len(бБ)]+=бБ;return аэ(бЧ(ш,1.2),.001)
def жЦ():return бЧ(гц(5,True)*1.+дМ(1.)*.9+ан(900,60,.5,.18)*.3,1.1)
def жЧ():
 д=3.;н=int(д*Б);в=аЙ(д);ш=np.zeros(н);вв=ан(70,22,2.4,.8)*1.8;ш[:len(вв)]+=вв;гП=ву(36,2.8,1.)*.8;ш[:len(гП)]+=гП;гФ=(np.sin(2*np.pi*55*в)+np.sin(2*np.pi*77.8*в)*.8)*np.exp(-в/1.6)*.6;ш+=гФ;зЁ=(np.sin(2*np.pi*1760*в)+np.sin(2*np.pi*1864*в)+np.sin(2*np.pi*2093*в*1.01))*(.6+.4*np.sin(2*np.pi*7*в))*np.exp(-в/.9)*.13;ш+=зЁ;ак=И(ащ(.7),1800)*аШ(.7,.18)*1.1;ш[:len(ак)]+=ак
 for Т,(ф,жГ)in enumerate(((523.25,.55),(554.37,.95),(466.16,1.35),(493.88,1.9))):р=ги(ф*.995,1.1,3.01,1.4,.4)*.2;з=int(жГ*Б);ш[з:з+len(р)]+=р[:н-з]
 for зп,бУ in enumerate((.9,1.75,2.7)):р=ан(90,38,.3,.1)*(.6-.12*зп);з=int(бУ*Б);ш[з:з+len(р)]+=р[:н-з]
 return аэ(бЧ(ш,1.3),.001)
def жЙ(у):
 if у['type']=='hi_dear':return жЧ(),1.,0,'big',.5
 if у.get('old'):
  а=у.get('k',0);бс=у['type']
  if бс=='hit':
   м=жШ(а,у.get('big'))
   if а==4:н=len(м)+int(1.6*Б);А=np.zeros(н);А[:len(м)]+=м;ее=ан(62,20,2.6,.8)*1.1;А[int(.25*Б):int(.25*Б)+len(ее)]+=ее;дц=И(ащ(.9),1800)*аШ(.9,.25)*.6;А[int(.25*Б):int(.25*Б)+len(дц)]+=дц;А=бЧ(А,1.1);return А,.95,0,'big',.5
   return м,.6+.06*а,0,'big',.25
  if бс=='drone':м=жХ(у.get('dur',11));г=np.arange(len(м))/Б;return м*np.where(г<5.,1.,.3),.38,0,'big',.3
  if бс=='intro':return жЩ(),.7,0,'dry',.3
 бс=у['type']
 if у['type']=='xslam':return жЮ(),1.,0,'big',.4
 бы={'hit':(гц,.8),'whoosh':(lambda у:жФ(у.get('dur',1.9)),.8),'bloop':(lambda у:жЫ(у.get('k',0)),.55),'type':(lambda у:жЪ(),.3),'dsname':(lambda у:жЦ(),.9),'glitch':(lambda у:дМ(у.get('amp',1)),.45),'riser':(lambda у:жЭ(у.get('dur',2.4)),.55)}
 if бс in бы:ф,щ=бы[бс];м=гц(у.get('k',0),у.get('big'))if бс=='hit'else ф(у);return м,щ,0,'big'if бс in('hit','dsname','riser','whoosh')else'dry',.3
def вй():
 ч=json.load(open(os.path.join(бз,'events.json'),encoding='utf-8'));н=int((аО+.3)*Б);Ч=ещ(н)
 for у in ч['events']:м,щ,вл,гм,вУ=жЙ(у);Ч.put(м,у['t'],щ,вл,гм,вУ)
 Ч.put(жЬ(),аО-3.4,.6,0,'big',.4);а=int(.95*Б);гъ=И(Ж.standard_normal(а),3500)*np.exp(-np.arange(а)/Б/.26);гъ/=np.sqrt((гъ**2).sum());иф=np.stack([fftconvolve(ц,гъ)[:н]for ц in Ч.еж])*1.4;гК=Ч.дБ+Ч.бИ+иф
 for жр,бК in((8.5,9.5),):вЛ,вМ=int(жр*Б),int(бК*Б);с=np.ones(н);с[вЛ:вМ]=.12;с=np.convolve(с,np.ones(int(.12*Б))/int(.12*Б),'same');гК=гК*с
 т=гК;дВ=[у['t']for у in ч['events']if у['type']=='hi_dear']
 if дВ:ы=дВ[-1];вЛ,вМ=int((ы-.42)*Б),int(ы*Б);дя=np.ones(н);дя[вЛ:вМ]=np.linspace(.04,0.,вМ-вЛ)+.03;т=т*дя
 т=np.tanh(т*1.15)/1.15;т=т[:,:int(аО*Б)];аД=int(.08*Б);дК=int(1.*Б);т[:,:аД]*=np.linspace(0,1,аД);т[:,-дК:]*=np.linspace(1,0,дК);т=т/max(1.,np.max(np.abs(т))/.92);wavfile.write(os.path.join(бз,'audio.wav'),Б,(т.T*32767).astype(np.int16));print('audio written',т.shape[1]/Б,'s;',len(ч['events']),'events')
if __name__=='__main__':вй()
