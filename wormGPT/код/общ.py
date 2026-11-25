import os,math,numpy as np;еч=os.path.dirname(os.path.abspath(__file__));вы=os.path.dirname(еч);аз,аа,въ=1280,720,30;аО=33.5;ех=1100.;В=1100.
def П(м,ж=0.,р=1.):return ж if м<ж else р if м>р else м
def зт(ж,р,в):return ж+(р-ж)*в
def Ь(в):в=П(в);return 1-(1-в)**3
def вд(в):в=П(в);return 1-(1-в)**5
def аГ(в):в=П(в);бК=1.7;жт=бК+1;return 1+жт*(в-1)**3+бК*(в-1)**2
def дГ(в):
 в=П(в)
 if в in(0,1):return в
 return 2**(-9*в)*math.sin((в*10-.75)*(2*math.pi/3))+1
def бп(в):в=П(в);return в*в*в*(в*(в*6-15)+10)
def зй(с):с=с.lstrip('#');return tuple((int(с[з:з+2],16)for з in(0,2,4)))
def аЬ(ж,р,в):return tuple((ж[з]+(р[з]-ж[з])*в for з in range(len(ж))))
def бм(н):М=math.sin(н*12.9898+78.233)*43758.5453;return М-math.floor(М)
def бС(в,бХ=0):з=math.floor(в);ф=в-з;ж,р=бм(з+бХ*17.),бм(з+1+бХ*17.);ф=ф*ф*(3-2*ф);return (ж+(р-ж)*ф)*2-1
def вь(ж):ц,е=math.cos(ж),math.sin(ж);return np.array([[ц,0,е],[0,1,0],[-е,0,ц]])
def дб(ж):ц,е=math.cos(ж),math.sin(ж);return np.array([[1,0,0],[0,ц,-е],[0,е,ц]])
def дв(ж):ц,е=math.cos(ж),math.sin(ж);return np.array([[ц,-е,0],[е,ц,0],[0,0,1]])
def аЯ(аЛ=0.,аЮ=0.,аы=0.):д=math.pi/180;return вь(аЛ*д)@дб(аЮ*д)@дв(аы*д)
