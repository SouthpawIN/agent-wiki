#!/usr/bin/env python3
"""Synth a boom-bap lo-fi → jungle breakcore bed. PS1-era grit: 12-bit crush, tape wobble, vinyl hiss.
Usage: beat.py <seconds> <out.wav> [--jungle a-b,c-d]   (jungle windows in seconds)"""
import sys, numpy as np
from scipy.signal import butter, lfilter, resample_poly
SR = 44100
rng = np.random.default_rng(7)

def lp(x, f, o=2):  b,a = butter(o, f/(SR/2)); return lfilter(b,a,x)
def hp(x, f, o=2):  b,a = butter(o, f/(SR/2), 'high'); return lfilter(b,a,x)
def env(n, a=0.002, d=0.25, curve=6):
    t = np.arange(n)/SR; e = np.exp(-t*curve/d); e[:int(a*SR)] *= np.linspace(0,1,int(a*SR)); return e
def kick(n=int(SR*0.35)):
    t=np.arange(n)/SR; f=55*np.exp(-t*18)+48; ph=np.cumsum(2*np.pi*f/SR)
    return np.tanh(np.sin(ph)*2.4)*env(n,0.001,0.28)*0.9 + rng.normal(0,.1,n)*env(n,0.0005,0.02)
def snare(n=int(SR*0.28)):
    t=np.arange(n)/SR; body=np.sin(2*np.pi*185*t)*env(n,0.001,0.09)*.5
    noise=hp(rng.normal(0,1,n),1800)*env(n,0.001,0.16)*.55
    return np.tanh((body+noise)*1.6)*.8
def hat(n=int(SR*0.06), open_=False):
    x=hp(rng.normal(0,1,n),7000)*env(n,0.0005,0.09 if open_ else 0.035); return x*.32
def rim(n=int(SR*0.08)):
    t=np.arange(n)/SR; return (np.sin(2*np.pi*820*t)+np.sin(2*np.pi*1230*t)*.5)*env(n,0.0005,0.03)*.35
def bass(freq, n):
    t=np.arange(n)/SR; x=np.sign(np.sin(2*np.pi*freq*t))*.35+np.sin(2*np.pi*freq*t)*.65
    return lp(x,240)*env(n,0.004,max(0.25,n/SR),3)*.55
def chord(freqs, n, wob=0.0):
    t=np.arange(n)/SR; out=np.zeros(n)
    for i,f in enumerate(freqs):
        det=f*(1+0.004*np.sin(2*np.pi*(0.3+i*.11)*t))*(1+wob*np.sin(2*np.pi*0.7*t))
        ph=np.cumsum(2*np.pi*det/SR); out+=np.sin(ph)*(1+.3*np.sin(ph*2))*.5
    return lp(out,1800)*env(n,0.02,n/SR*.9,2.2)*.28
def crush(x, bits=12, down=2):
    q=2**(bits-1); y=np.round(np.clip(x,-1,1)*q)/q
    if down>1: y=np.repeat(y[::down],down)[:len(x)]
    return y
def tape(x):
    n=len(x); t=np.arange(n)/SR; wow=1+0.0018*np.sin(2*np.pi*0.42*t)+0.0006*np.sin(2*np.pi*5.7*t)
    idx=np.clip(np.cumsum(wow),0,n-1); y=np.interp(idx,np.arange(n),x)
    hiss=lp(rng.normal(0,1,n),9000)*.006; crackle=(rng.random(n)<0.00012)*rng.normal(0,.35,n)
    return np.tanh(y*1.25)*.85+hiss+crackle

def render(total, jungle=()):
    N=int(total*SR); mix=np.zeros(N+SR*2)
    def put(s, at):  i=int(at*SR); L=min(len(s),len(mix)-i); mix[i:i+L]+=s[:L]
    BPM=86; beat=60/BPM; bar=beat*4
    # chords: i–VI–iv–v in D minor, dusty
    prog=[[146.8,174.6,220,261.6],[116.5,146.8,174.6,220],[98,123.5,146.8,174.6],[110,130.8,164.8,196]]
    roots=[36.7,29.1,24.5,27.5]
    t=0.0; bi=0
    while t<total:
        in_j=any(a<=t<b for a,b in jungle)
        ch=prog[bi%4]; root=roots[bi%4]
        put(chord(ch,int(bar*SR),wob=.002 if in_j else 0), t)
        if not in_j:
            # boom bap: k . s . k k s .  swung hats
            for k in (0, 2.5, 3.0): put(kick(), t+k*beat)
            for s in (1.0, 3.0): put(snare(), t+s*beat)
            for h in range(8):
                sw = 0.06 if h%2 else 0
                put(hat(open_=(h==7)), t+h*beat/2+sw)
            if bi%2: put(rim(), t+1.75*beat)
            put(bass(root, int(beat*1.6*SR)), t); put(bass(root*1.5, int(beat*.6*SR)), t+2.5*beat)
        else:
            # jungle: double-time amen chops, ghost snares, sub bass
            db=beat/2
            pat=[('k',0),('k',1.5),('s',2),('s',3.5),('k',4),('s',5),('k',5.5),('s',6),('s',7.5)]
            for typ,pos in pat: put(kick()*.9 if typ=='k' else snare()*(.55 if pos in (3.5,7.5) else 1), t+pos*db)
            for h in range(16): put(hat(open_=(h in (6,14)))*.7, t+h*db/2)
            # a quick roll into bar end
            for r in range(4): put(snare()[:int(SR*.05)]*.5, t+7*db+r*db/4)
            put(bass(root/2, int(bar*.8*SR))*1.3, t)
        t+=bar; bi+=1
    y=mix[:N]
    y=crush(y, 12, 2)
    y=tape(y)
    # sidechain-ish duck in the very low end so VO sits on top
    y=y/np.max(np.abs(y))*.8
    return y

if __name__=='__main__':
    total=float(sys.argv[1]); out=sys.argv[2]
    j=[]
    if len(sys.argv)>4 and sys.argv[3]=='--jungle':
        for w in sys.argv[4].split(','):
            a,b=w.split('-'); j.append((float(a),float(b)))
    y=render(total,j)
    import wave, struct
    with wave.open(out,'w') as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((y*32767).astype('<i2').tobytes())
    print('wrote',out,round(total,1),'s jungle',j)
