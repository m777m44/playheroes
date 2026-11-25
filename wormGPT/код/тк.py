import os,re,glob,unicodedata,math;import numpy as np,cv2;from PIL import Image,ImageDraw,ImageFont,features;from общ import*;га=features.check('raqm');еш=ImageFont.Layout.RAQM if га else ImageFont.Layout.BASIC;гЯ=re.compile('[\u0600-ۿݐ-ݿ]')
def до(зЖ):
 for и in зЖ:
  for Н in sorted(glob.glob(и)):
   if os.path.isfile(Н):return Н
 return None
аВ=os.path.join(вы,'fonts');дй={'ui':[аВ+'/*Bold*.ttf',аВ+'/*Bold*.otf',аВ+'/*.ttf',аВ+'/*.otf','C:/Windows/Fonts/segoeuib.ttf','C:/Windows/Fonts/tahomabd.ttf','C:/Windows/Fonts/arialbd.ttf','/System/Library/Fonts/SFArabic.ttf','/Library/Fonts/Arial Unicode.ttf','/usr/share/fonts/**/NotoSansArabic-Bold.ttf','/usr/share/fonts/truetype/noto/NotoSansArabic*Bold*.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/TTF/DejaVuSans-Bold.ttf'],'ser':[аВ+'/*.ttf',аВ+'/*.otf',аВ+'/*Serif*Bold*.ttf',аВ+'/*Naskh*Bold*.ttf',аВ+'/*Amiri*Bold*.ttf','C:/Windows/Fonts/timesbd.ttf','/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'],'mono':[аВ+'/*.ttf',аВ+'/*.otf','C:/Windows/Fonts/consolab.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf','/System/Library/Fonts/Menlo.ttc','/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf']};вя={}
def жТ(а):
 if а not in вя:
  вя[а]=до(дй[а])or(до(дй['ui'])if а!='ui'else None)
  if вя[а]is None:raise SystemExit('Folder: "fonts"')
 return вя[а]
гв={}
def зв(а,Я):
 аЖ=а,int(Я)
 if аЖ not in гв:гв[аЖ]=ImageFont.truetype(жТ(а),int(Я),layout_engine=еш)
 return гв[аЖ]
бЁ={}
for дм in range(65136,65280):
 дн=unicodedata.decomposition(chr(дм))
 if дн.startswith('<'):еК,еЙ=дн.split(' ',1);еИ=''.join((chr(int(м,16))for м in еЙ.split()));бЁ.setdefault(еИ,{})[еК.strip('<>')]=chr(дм)
еЗ=set('آأؤإاةدذرزوٱژ');еЖ=set((chr(ц)for ц in list(range(1611,1632))+[1648]));еЕ={'آ','أ','إ','ا'}
def дп(ак):return ак in бЁ and ак not in еЗ and(ак!='ء')
def дл(ак):return ак in бЁ and ак!='ء'
def зЪ(е):
 е=''.join((ц for ц in е if ц not in еЖ));т,з,н=[],0,len(е);бЦ=[]
 while з<н:
  ц=е[з]
  if ц=='ل'and з+1<н and(е[з+1]in еЕ):бЦ.append(ц+е[з+1]);з+=2
  else:бЦ.append(ц);з+=1
 for а,ц in enumerate(бЦ):
  if ц not in бЁ:т.append(ц);continue
  Х=бЦ[а-1]if а>0 else'';дЮ=бЦ[а+1]if а+1<len(бЦ)else'';вС=bool(Х)and(дп(Х[0]if len(Х)==1 else'ل')and len(Х)==1)and дл(ц[0]);дЬ=bool(дЮ)and дл(дЮ[0])and(дп(ц[0])if len(ц)==1 else False);ф=бЁ[ц]
  if len(ц)==2:т.append(ф.get('final'if вС else'isolated',ф.get('isolated')))
  else:аЖ='medial'if вС and дЬ else'final'if вС else'initial'if дЬ else'isolated';т.append(ф.get(аЖ)or ф.get('final'if вС else'isolated')or ф.get('isolated')or ц)
 гЙ,ба=[],[]
 def дЙ():
  if ба:гЙ.append(''.join(ба));ба.clear()
 for ак in т:
  if ак.isascii()and(ак.isalnum()or ак in'.-_'):ба.append(ак)
  else:дЙ();гЙ.append(ак)
 дЙ();return ''.join(reversed(гЙ))
def зЛ(ай):
 if not гЯ.search(ай):return ай,{}
 if га:return ай,dict(direction='rtl',language='ar')
 return зЪ(ай),{}
class еА:
 __slots__='Ы','п','с','л','pad','Ф','бк','ви'
 def __init__(е,Ы,л,pad=0,Ф=0,бк=0,ви=0):е.Ы=Ы;е.л=л;е.с,е.п=Ы.shape[0]/л,Ы.shape[1]/л;е.pad,е.Ф,е.бк,е.ви=pad,Ф,бк,ви
ат=1.3
def бь(гр,бШ):return бШ+гр*(1-бШ[...,3:4])
def бщ(Ч,Е,вА=1.):
 с,п=Ч.shape
 if isinstance(Е[0],(tuple,list)):в=np.linspace(0,1,с,dtype=np.float32)[:,None,None];ц=np.array(Е[0],np.float32)*(1-в)+np.array(Е[1],np.float32)*в;ц=np.broadcast_to(ц,(с,п,3))/255.
 else:ц=np.broadcast_to(np.array(Е,np.float32)/255.,(с,п,3))
 ж=(Ч*вА)[...,None].astype(np.float32);return np.concatenate([ц*ж,ж],axis=2)
def аё(о,л=ат,**аЫ):Ы=np.empty(о.shape,np.uint8);Ы[...,0]=np.clip(о[...,2]*255,0,255);Ы[...,1]=np.clip(о[...,1]*255,0,255);Ы[...,2]=np.clip(о[...,0]*255,0,255);Ы[...,3]=np.clip(о[...,3]*255,0,255);return еА(Ы,л,**аЫ)
def З(ай,аЖ='ui',Я=60,Е=(255,255,255),аш=None,бл=16,зд=.8,вЖ=0,жК=(30,30,40),л=ат,вк=None,вВ=None):
 вИ=зв(аЖ,Я*л);е,аЫ=зЛ(ай);бк,дэ=вИ.getmetrics();Ф=вИ.getlength(е,**аЫ)if аЫ else вИ.getlength(е);pad=int(бл*2.2*л+вЖ*л+6);бЖ,вЯ=int(Ф)+2*pad,бк+дэ+2*pad;дЫ=Image.new('L',(бЖ,вЯ),0);ImageDraw.Draw(дЫ).text((pad,pad+бк),е,font=вИ,fill=255,anchor='ls',**аЫ);Ч=np.asarray(дЫ,np.float32)/255.
 if вВ is None:вВ=1. if гЯ.search(ай)else 0
 if вВ:Ч=cv2.dilate(Ч,np.ones((3,3),np.uint8),iterations=max(1,int(round(вВ*л))))
 о=np.zeros((вЯ,бЖ,4),np.float32)
 if аш:щ=cv2.GaussianBlur(Ч,(0,0),max(1.,бл*л/2.2));о=бь(о,бщ(np.clip(щ*1.6,0,1),аш,зд))
 if вЖ:
  for а in range(вЖ,0,-1):аМ=np.float32([[1,0,а*.55*л],[0,1,а*.8*л]]);зщ=cv2.warpAffine(Ч,аМ,(бЖ,вЯ),flags=cv2.INTER_LINEAR);Ш=np.array(жК,np.float32)*(.55+.45*(1-а/вЖ));о=бь(о,бщ(зщ,tuple(Ш)))
 if вк:зш=cv2.dilate(Ч,np.ones((3,3),np.uint8),iterations=max(1,int(л*1.5)));о=бь(о,бщ(зш,вк))
 о=бь(о,бщ(Ч,Е));return аё(о,л,pad=pad/л,Ф=Ф/л,бк=бк/л,ви=(бк+дэ)/л)
def аЦ(Ы):ж=np.asarray(Ы.convert('RGBA'),np.float32)/255.;о=np.empty_like(ж);о[...,:3]=ж[...,:3]*ж[...,3:4];о[...,3]=ж[...,3];return о
def бу(п,с,л=ат,бт=2):а=л*бт;return Image.new('RGBA',(int(п*а),int(с*а)),(0,0,0,0)),а
def бф(Ы,л=ат,бт=2):return Ы.resize((Ы.width//бт,Ы.height//бт),Image.LANCZOS)
def аХ(о,зП,Е,за=.9):ж=cv2.GaussianBlur(о[...,3],(0,0),зП);return бь(бщ(np.clip(ж*за,0,1),Е,.7),о)
def зА(о,и):return np.pad(о,((и,и),(и,и),(0,0)))
def бО(п,с,ё=30,ил=(255,255,255),ж=.09,жб=(255,255,255),гз=.38,аш=None,бл=24,л=ат):
 и=int(бл*1.6)if аш else 6;Л,а=бу(п+2*и,с+2*и,л);д=ImageDraw.Draw(Л);бЙ=[и*а,и*а,(и+п)*а,(и+с)*а];д.rounded_rectangle(бЙ,ё*а,fill=(*ил,int(255*ж)));дФ=Image.new('RGBA',Л.size,(0,0,0,0));жъ=ImageDraw.Draw(дФ);жъ.rounded_rectangle([бЙ[0],бЙ[1],бЙ[2],бЙ[1]+с*.5*а],ё*а,fill=(255,255,255,int(255*.06)));Л=Image.alpha_composite(Л,дФ);д=ImageDraw.Draw(Л);д.rounded_rectangle(бЙ,ё*а,outline=(*жб,int(255*гз)),width=max(2,int(2.2*а)));о=аЦ(бф(Л,л))
 if аш:о=аХ(о,бл*л/2,аш,.55)
 return аё(о,л)
def гп(ё,Е,ж=1.,л=1.):н=int(ё*2*л);ш,м=np.mgrid[:н,:н].astype(np.float32);д=np.hypot(м-н/2,ш-н/2)/(н/2);Ч=np.clip(1-д,0,1)**2.2*ж;return аё(бщ(Ч,Е),л)
def ей(ё,Е,л=ат,дР=None,зг='ser',зи=None):
 н=int(ё*2*л)+4;ш,м=np.mgrid[:н,:н].astype(np.float32);Ъ=бц=н/2;аЁ=ё*л;ац,аЧ=(м-Ъ)/аЁ,(ш-бц)/аЁ;ды=ац*ац+аЧ*аЧ;дЦ=np.clip((1-np.sqrt(ды))*аЁ/1.5,0,1);А=np.sqrt(np.clip(1-ды,0,1));Щ=np.array([-.45,-.55,.7]);Щ/=np.linalg.norm(Щ);дю=np.clip(ац*Щ[0]+аЧ*Щ[1]+А*Щ[2],0,1);гМ=np.clip(дю,0,1)**26;ц=np.array(Е,np.float32);С=ц[None,None]*(.25+.95*дю[...,None])+255*гМ[...,None]*.75;зУ=(np.clip(1-А,0,1)**3)[...,None]*np.array([255,255,255],np.float32)*.25;С=np.clip(С+зУ,0,255);о=np.concatenate([С/255*дЦ[...,None],дЦ[...,None]],axis=2)
 if дР:в=З(дР,зг,зи or ё*1.25,(255,255,255),л=л);ве=в.Ы.astype(np.float32)/255;аЩ=np.empty_like(ве);аЩ[...,0]=ве[...,2];аЩ[...,1]=ве[...,1];аЩ[...,2]=ве[...,0];аЩ[...,3]=ве[...,3];гВ,гБ=(н-аЩ.shape[0])//2,(н-аЩ.shape[1])//2;дЛ=np.zeros_like(о);дЛ[max(0,гВ):max(0,гВ)+аЩ.shape[0],max(0,гБ):max(0,гБ)+аЩ.shape[1]]=аЩ[:н-max(0,гВ),:н-max(0,гБ)];о=бь(о,дЛ)
 о=аХ(зА(о,int(ё*.5*л)),ё*.22*л,Е,.6);return аё(о,л)
def ва(п,с,Е,л=ат,аш=True):
 и=14 if аш else 2;Л,а=бу(п+2*и,с+2*и,л);ImageDraw.Draw(Л).rounded_rectangle([и*а,и*а,(и+п)*а,(и+с)*а],с*а/2,fill=(*Е,255));о=аЦ(бф(Л,л))
 if аш:о=аХ(о,5*л,Е,1.)
 return аё(о,л)
def зД(п,с,еО,иВ=7,л=ат):и=40;Л,а=бу(п+2*и,с+2*и,л);д=ImageDraw.Draw(Л);д.rounded_rectangle([и*а,и*а,(и+п)*а,(и+с)*а],16*а,fill=(226,222,210,255));д.rounded_rectangle([и*а,и*а,(и+п)*а,(и+12)*а],10*а,fill=(*еО,255));о=аЦ(бф(Л,л));Ш=cv2.GaussianBlur(о[...,3],(0,0),18*л);Ш=np.roll(Ш,int(26*л),axis=0);о=бь(бщ(Ш,(0,0,0),.55),о);return аё(о,л)
def зЭ(п,с,Е,л=ат):и=40;Л,а=бу(п+2*и,с+2*и,л);д=ImageDraw.Draw(Л);Ю=[(.5,0),(.95,.13),(.95,.5),(.5,1.),(.05,.5),(.05,.13)];гД=[((и+м*п)*а,(и+ш*с)*а)for м,ш in Ю];д.polygon(гД,fill=(*Е,70));д.line(гД+[гД[0]],fill=(*Е,255),width=int(7*а),joint='curve');Ъ,бц=(и+п*.5)*а,(и+с*.45)*а;д.line([(Ъ-п*.17*а,бц),(Ъ-п*.04*а,бц+с*.12*а),(Ъ+п*.2*а,бц-с*.13*а)],fill=(255,255,255,255),width=int(14*а),joint='curve');о=аЦ(бф(Л,л));о=аХ(о,12*л,Е,.9);return аё(о,л)
def зч(п,Е,л=ат):с=п*1.25;и=30;Л,а=бу(п+2*и,с+2*и,л);д=ImageDraw.Draw(Л);жл,жо,жм,жп=и+п*.08,и+с*.46,и+п*.92,и+с;д.rounded_rectangle([жл*а,жо*а,жм*а,жп*а],п*.12*а,fill=(*Е,255));Ъ=и+п*.5;д.arc([(Ъ-п*.3)*а,(и+с*.02)*а,(Ъ+п*.3)*а,(и+с*.66)*а],200,360,fill=(235,235,240,255),width=int(п*.11*а));д.line([((Ъ+п*.3)*а,(и+с*.34)*а),((Ъ+п*.3)*а,(и+с*.5)*а)],fill=(235,235,240,255),width=int(п*.11*а));д.ellipse([(Ъ-п*.08)*а,(и+с*.66)*а,(Ъ+п*.08)*а,(и+с*.82)*а],fill=(20,8,10,255));о=аЦ(бф(Л,л));о=аХ(о,10*л,Е,.9);return аё(о,л)
def иу(п,Е,л=ат):с=п*.9;и=36;Л,а=бу(п+2*и,с+2*и,л);д=ImageDraw.Draw(Л);Ю=[((и+п/2)*а,(и+6)*а),((и+п-6)*а,(и+с-6)*а),((и+6)*а,(и+с-6)*а)];д.polygon(Ю,fill=(*Е,60));д.line(Ю+[Ю[0]],fill=(*Е,255),width=int(9*а),joint='curve');Ъ=(и+п/2)*а;д.rounded_rectangle([Ъ-7*а,(и+с*.34)*а,Ъ+7*а,(и+с*.66)*а],6*а,fill=(255,255,255,255));д.ellipse([Ъ-8*а,(и+с*.74)*а,Ъ+8*а,(и+с*.74+16)*а],fill=(255,255,255,255));о=аЦ(бф(Л,л));о=аХ(о,14*л,Е,1.);return аё(о,л)
def вп(ё,Е,вЭ=6,л=ат):и=22;н=int((2*ё+2*и)*л*2);Л=Image.new('RGBA',(н,н),(0,0,0,0));д=ImageDraw.Draw(Л);ц=н/2;д.ellipse([ц-ё*л*2,ц-ё*л*2,ц+ё*л*2,ц+ё*л*2],outline=(*Е,255),width=int(вЭ*л*2));о=аЦ(Л.resize((н//2,н//2),Image.LANCZOS));о=аХ(о,6*л,Е,.8);return аё(о,л)
def гО(ё,Е,л=ат):
 и=40;н=int((2*ё+2*и)*л*2);Л=Image.new('RGBA',(н,н),(0,0,0,0));д=ImageDraw.Draw(Л);ц=н/2;Ю=[]
 for з in range(8):ж=з*math.pi/4-math.pi/2;аЁ=ё*л*2*(1 if з%2==0 else.28);Ю.append((ц+аЁ*math.cos(ж),ц+аЁ*math.sin(ж)))
 д.polygon(Ю,fill=(*Е,255));о=аЦ(Л.resize((н//2,н//2),Image.LANCZOS));о=аХ(о,12*л,Е,1.);return аё(о,л)
def ау(п,с,ё,Е,ж=1.,л=ат,аш=None,бл=10,вк=None,зё=3):
 и=int(бл*1.6)if аш else 4;Л,а=бу(п+2*и,с+2*и,л);д=ImageDraw.Draw(Л);д.rounded_rectangle([и*а,и*а,(и+п)*а,(и+с)*а],ё*а,fill=(*Е,int(255*ж)),outline=(*вк,255)if вк else None,width=int(зё*а));о=аЦ(бф(Л,л))
 if аш:о=аХ(о,бл*л/2,аш,.8)
 return аё(о,л)
