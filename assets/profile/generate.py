"""Genera los SVG locales del perfil. Solo usa la biblioteca estándar.

Uso desde la raíz: python assets/profile/generate.py
Diseño propio; fuentes y decisiones en docs/PROFILE-DESIGN.md.
"""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
C = {"bg": "#152640", "blue": "#4D7CFE", "action": "#315DD9", "orange": "#F2B181",
     "white": "#F5F8FD", "muted": "#B7C9E2", "line": "#334B6C"}
SANS = "Arial, Helvetica, sans-serif"
MONO = "Consolas, Liberation Mono, monospace"

def text(x, y, value, size=24, color="white", weight=400, font=None, extra=""):
    return (f'<text x="{x}" y="{y}" fill="{C.get(color, color)}" '
            f'font-family="{font or SANS}" font-size="{size}" font-weight="{weight}" '
            f'{extra}>{escape(value)}</text>')

def rect(x, y, w, h, color, radius=0, extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" '
            f'fill="{C.get(color, color)}" {extra}/>')

def line(x1, y1, x2, y2, color="line", width=2, extra=""):
    return (f'<path d="M{x1} {y1}H{x2}" fill="none" stroke="{C.get(color,color)}" '
            f'stroke-width="{width}" {extra}/>' if y1 == y2 else
            f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{C.get(color,color)}" '
            f'stroke-width="{width}" {extra}/>')

def circle(x,y,r,color,extra=""):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C.get(color,color)}" {extra}/>'

def write(name,w,h,body,title):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
           f'<title>{escape(title)}</title>{body}</svg>\n')
    (ROOT / (name + ".svg")).write_text(svg,encoding="utf-8")

def hero(mobile=False):
    w,h = (640,440) if mobile else (960,340)
    s = rect(0,0,w,h,"bg",20)
    s += rect(w-10,0,10,h,"blue")
    s += text(36,42,"D / M",18,"orange",700,MONO)
    s += text(36,80,"BACKEND · DATOS · AUTOMATIZACIÓN",16,"muted",400,MONO)
    if mobile:
        s += text(32,151,"Tu operación,",62,"white",700,extra='letter-spacing="-2"')
        s += text(32,215,"bien conectada.",62,"white",700,extra='letter-spacing="-2"')
        y=307
        xvals=[56,320,584]
        labels=["PROCESO","REGLAS","SOFTWARE"]
        s += line(56,y,584,y,"blue",3)
        for i,x in enumerate(xvals):
            s += circle(x,y,10,"orange" if i==1 else "blue")
            s += text(x,y+47,labels[i],17,"muted",400,MONO,extra='text-anchor="middle"')
        s += text(36,405,"APIs para cotizar, reservar y gestionar datos.",21,"white")
    else:
        s += text(32,158,"Tu operación,",68,"white",700,extra='letter-spacing="-2.3"')
        s += text(32,230,"bien conectada.",68,"white",700,extra='letter-spacing="-2.3"')
        s += text(36,294,"APIs para cotizar, reservar y gestionar datos.",22,"muted")
        # Diagrama conceptual de entrada, reglas y salida.
        s += '<g fill="none" stroke="#334B6C" stroke-width="1">'
        for x in range(680,940,26):
            s += f'<path d="M{x} 70V290"/>'
        for y in range(80,300,26):
            s += f'<path d="M674 {y}H930"/>'
        s += '</g>'
        s += '<path d="M694 110H750V176H842V240H900" fill="none" stroke="#4D7CFE" stroke-width="4"/>'
        s += rect(695,90,36,36,"bg",8,extra='stroke="#4D7CFE" stroke-width="2"')
        s += rect(762,144,64,64,"blue",12)
        s += text(794,186,"{ }",25,"white",700,MONO,extra='text-anchor="middle"')
        s += rect(874,220,40,40,"bg",10,extra='stroke="#F2B181" stroke-width="2"')
        s += circle(900,240,5,"orange")
        s += text(696,314,"PROCESO / REGLAS / SOFTWARE",12,"muted",400,MONO)
    write("hero-mobile" if mobile else "hero",w,h,s,
          "Tu operación, bien conectada. APIs para cotizar, reservar y gestionar datos.")

def divider():
    s = line(0,16,960,16,"line",1)
    s += '<path d="M0 16H180L192 4H224L236 16H350" fill="none" stroke="#4D7CFE" stroke-width="2"/>'
    s += circle(224,4,3,"orange")
    write("divider",960,32,s,"Separador decorativo")

def project(key, tag, labels, mobile=False):
    w,h = (640,184) if mobile else (960,172)
    s = rect(0,0,w,h,"bg",14)
    s += rect(0,20,4,h-40,"blue",2)
    s += text(28,37,tag,17 if mobile else 19,"orange",700,MONO)
    y = 90 if mobile else 89
    positions = [92,320,548] if mobile else [124,480,836]
    s += line(positions[0],y,positions[-1],y,"line",2)
    for i,(x,label) in enumerate(zip(positions, labels)):
        s += circle(x,y,16,"bg",extra='stroke="#4D7CFE" stroke-width="2"')
        if i==1:
            s += '<path d="M'+str(x-5)+' '+str(y-6)+'l-6 6 6 6m10-12 6 6-6 6" fill="none" stroke="#F2B181" stroke-width="2"/>'
        else:
            s += rect(x-5,y-5,10,10,"orange" if i==2 else "blue",2)
        s += text(x,y+46,label,22 if mobile else 24,"white",600,extra='text-anchor="middle"')
    write(key+("-mobile" if mobile else ""),w,h,s,tag+": "+", ".join(labels))

def technologies(mobile=False):
    w = 640 if mobile else 960
    cols,rows = (2,3) if mobile else (3,2)
    gap,pad = 12,0
    ch = 106 if mobile else 98
    cw=(w-(cols-1)*gap)/cols
    h=rows*ch+(rows-1)*gap
    items=[("Java","LÓGICA DE NEGOCIO"),("Spring Boot","APIs"),
           ("Python","AGENTES"),("FastAPI","INTEGRACIONES"),
           ("PostgreSQL","DATOS"),("Docker","ENTORNOS")]
    s=""
    for i,(name,caption) in enumerate(items):
        x=(i%cols)*(cw+gap); y=(i//cols)*(ch+gap)
        s += rect(x,y,cw,ch,"bg",12)
        s += rect(x+18,y+20,4,ch-40,"orange" if i%3==2 else "blue",2)
        s += text(x+38,y+43,name,30 if mobile else 28,"white",700)
        s += text(x+38,y+77,caption,15,"muted",400,MONO)
    write("technologies-mobile" if mobile else "technologies",w,h,s,
          "Tecnologías principales: Java, Spring Boot, Python, FastAPI, PostgreSQL y Docker")

def contact(mobile=False):
    w,h = (640,220) if mobile else (960,190)
    s=rect(0,0,w,h,"action",16)
    s+=text(30,44,"HABLEMOS DE TU PROYECTO",16,"white",700,MONO)
    s+=text(28,105,"¿Qué quieres conectar?",42 if mobile else 52,"white",700,extra='letter-spacing="-1"')
    s+=text(30,160 if mobile else 153,"Cuéntame el proceso. Revisemos el alcance.",22,"white")
    s+='<path d="M'+str(w-75)+' 38h30m-12-12 12 12-12 12" fill="none" stroke="#F5F8FD" stroke-width="3"/>'
    write("contact-mobile" if mobile else "contact",w,h,s,
          "Hablemos de tu proyecto. Cuéntame qué proceso quieres conectar y revisemos el alcance.")

def button():
    s=rect(0,0,296,48,"action",8)
    s+=text(20,30,"Hablemos de tu proyecto",18,"white",700)
    s+='<path d="M259 24h18m-7-7 7 7-7 7" stroke="#F5F8FD" stroke-width="2" fill="none"/>'
    write("contact-button",296,48,s,"Hablemos de tu proyecto por correo")

def icon(name,paths):
    s='<g fill="none" stroke="#4D7CFE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+paths+'</g>'
    write("icon-"+name,28,28,s,"")
    
for mobile in (False,True):
    hero(mobile)
    project("xeon","COTIZACIÓN ASISTIDA",["Conversación","Reglas","Borrador"],mobile)
    project("rental","GESTIÓN DE ALQUILERES",["Catálogo","Reserva","Devolución"],mobile)
    project("motion","VIDEO CON CÓDIGO",["Guion","Fotograma","MP4"],mobile)
    technologies(mobile)
    contact(mobile)
divider()
button()
icon("projects",'<path d="M4 8h7l2-3h11v18H4z"/><path d="M4 11h20"/>')
icon("tech",'<rect x="6" y="6" width="16" height="16" rx="3"/><path d="M10 2v4m8-4v4m-8 16v4m8-4v4M2 10h4m-4 8h4m16-8h4m-4 8h4"/><path d="m12 11-3 3 3 3m4-6 3 3-3 3"/>')
icon("collaboration",'<circle cx="8" cy="6" r="3"/><circle cx="20" cy="6" r="3"/><circle cx="14" cy="22" r="3"/><path d="M8 9v4q0 4 6 6m6-10v4q0 4-6 6"/>')
icon("formation",'<path d="m2 10 12-6 12 6-12 6z"/><path d="M6 12v7q8 7 16 0v-7m3 0v9"/>')
icon("languages",'<circle cx="14" cy="14" r="11"/><path d="M3 14h22M14 3q-10 11 0 22M14 3q10 11 0 22"/>')
icon("method",'<path d="M5 6h5v5H5zM18 17h5v5h-5zM10 8h8v6m-3-3 3 3 3-3M8 11v9h10"/>')
icon("contact",'<rect x="3" y="6" width="22" height="16" rx="3"/><path d="m4 8 10 8L24 8"/>')
print("Generados",len(list(ROOT.glob("*.svg"))),"SVG locales.")
