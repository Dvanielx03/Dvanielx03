"""Genera los SVG locales del perfil. Solo usa la biblioteca estándar.

Uso desde la raíz: python assets/profile/generate.py
Aurora Veil adaptada en vendor/; fuentes y decisiones en docs/PROFILE-DESIGN.md.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
C = {"bg": "#070B22", "surface": "#0E1B3A", "primary": "#3FFFE6",
     "action": "#3FFFE6", "secondary": "#A78BFA", "accent": "#FF3D8A",
     "white": "#FEF3C7", "muted": "#CBD5E1", "line": "#3B335F"}
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
    s += rect(w-10,0,10,h,"primary")
    s += text(36,42,"D / M",18,"secondary",700,MONO)
    s += text(36,80,"CREATIVIDAD · APRENDIZAJE · TECNOLOGÍA",22 if mobile else 16,"muted",400,MONO)
    if mobile:
        s += text(32,151,"Ideas nuevas.",62,"white",700,extra='letter-spacing="-2"')
        s += text(32,215,"Ganas de crecer.",62,"white",700,extra='letter-spacing="-2"')
        y=307
        xvals=[72,320,568]
        labels=["EXPLORAR","COMPARTIR","CREAR"]
        s += line(72,y,568,y,"primary",3)
        for i,x in enumerate(xvals):
            s += circle(x,y,10,"secondary" if i==1 else "primary")
            s += text(x,y+47,labels[i],24,"muted",400,MONO,extra='text-anchor="middle"')
        s += text(36,398,"Creatividad para aportar.",24,"white")
        s += text(36,429,"Curiosidad para aprender.",24,"white")
    else:
        s += text(32,158,"Ideas nuevas.",68,"white",700,extra='letter-spacing="-2.3"')
        s += text(32,230,"Ganas de crecer.",68,"white",700,extra='letter-spacing="-2.3"')
        s += text(36,294,"Creatividad para aportar. Curiosidad para aprender.",22,"muted")
        # Conexión visual entre explorar, compartir y crear.
        s += '<g fill="none" stroke="#3B335F" stroke-width="1">'
        for x in range(680,940,26):
            s += f'<path d="M{x} 70V290"/>'
        for y in range(80,300,26):
            s += f'<path d="M674 {y}H930"/>'
        s += '</g>'
        s += '<path d="M694 110H750V176H842V240H900" fill="none" stroke="#3FFFE6" stroke-width="4"/>'
        s += rect(695,90,36,36,"bg",8,extra='stroke="#3FFFE6" stroke-width="2"')
        s += rect(762,144,64,64,"primary",12)
        s += text(794,186,"{ }",25,"bg",700,MONO,extra='text-anchor="middle"')
        s += rect(874,220,40,40,"bg",10,extra='stroke="#A78BFA" stroke-width="2"')
        s += circle(900,240,5,"secondary")
        s += text(696,314,"EXPLORAR / COMPARTIR / CREAR",12,"muted",400,MONO)
    write("hero-mobile" if mobile else "hero",w,h,s,
          "Ideas nuevas. Ganas de crecer. Creatividad para aportar y curiosidad para aprender.")

def divider():
    s = line(0,16,960,16,"line",1)
    s += '<path d="M0 16H180L192 4H224L236 16H350" fill="none" stroke="#3FFFE6" stroke-width="2"/>'
    s += circle(224,4,3,"accent")
    write("divider",960,32,s,"Separador decorativo")

def project(key, tag, labels, mobile=False):
    w,h = (640,184) if mobile else (960,172)
    s = rect(0,0,w,h,"bg",14)
    s += rect(0,20,4,h-40,"primary",2)
    s += text(28,37,tag,24 if mobile else 19,"secondary",700,MONO)
    y = 90 if mobile else 89
    positions = [92,320,548] if mobile else [124,480,836]
    s += line(positions[0],y,positions[-1],y,"line",2)
    for i,(x,label) in enumerate(zip(positions, labels)):
        s += circle(x,y,16,"bg",extra='stroke="#3FFFE6" stroke-width="2"')
        if i==1:
            s += '<path d="M'+str(x-5)+' '+str(y-6)+'l-6 6 6 6m10-12 6 6-6 6" fill="none" stroke="#A78BFA" stroke-width="2"/>'
        else:
            s += rect(x-5,y-5,10,10,"secondary" if i==2 else "primary",2)
        s += text(x,y+46,label,26 if mobile else 24,"white",600,extra='text-anchor="middle"')
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
        s += rect(x+18,y+20,4,ch-40,"secondary" if i%3==2 else "primary",2)
        s += text(x+38,y+43,name,34 if mobile else 28,"white",700)
        s += text(x+38,y+82 if mobile else y+77,caption,24 if mobile else 15,"muted",400,MONO)
    write("technologies-mobile" if mobile else "technologies",w,h,s,
          "Tecnologías principales: Java, Spring Boot, Python, FastAPI, PostgreSQL y Docker")

def contact(mobile=False):
    w,h = (640,220) if mobile else (960,190)
    s=rect(0,0,w,h,"surface",16,extra='stroke="#A78BFA" stroke-width="2"')
    s+=text(30,44,"TODO EMPIEZA CON UNA CONVERSACIÓN",22 if mobile else 16,"primary",700,MONO)
    s+=text(28,105,"¿Y si creamos algo juntos?",42 if mobile else 52,"white",700,extra='letter-spacing="-1"')
    s+=text(30,160 if mobile else 153,"Una idea, un reto o una oportunidad.",26 if mobile else 22,"white")
    s+='<path d="M'+str(w-75)+' 38h30m-12-12 12 12-12 12" fill="none" stroke="#3FFFE6" stroke-width="3"/>'
    write("contact-mobile" if mobile else "contact",w,h,s,
          "¿Y si creamos algo juntos? Una idea, un reto o una oportunidad.")

def button():
    s=rect(0,0,296,48,"action",8)
    s+=text(20,30,"Compartamos una idea",18,"bg",700)
    s+='<path d="M259 24h18m-7-7 7 7-7 7" stroke="#070B22" stroke-width="2" fill="none"/>'
    write("contact-button",296,48,s,"Compartamos una idea por correo")

def icon(name,paths):
    s='<g fill="none" stroke="#3FFFE6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+paths+'</g>'
    write("icon-"+name,28,28,rect(0,0,28,28,"surface",6)+s,"")


def aurora(mobile=False, still=False):
    """Personaliza Aurora Veil; la escena y sus filtros proceden de vendor/."""
    ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", ns)
    original = ET.parse(ROOT / "vendor" / "aurora-veil.svg").getroot()
    w = 640 if mobile else 1200
    svg = ET.Element(f"{{{ns}}}svg", {
        "viewBox": f"0 0 {w} 420", "width": str(w), "height": "420",
        "role": "img", "aria-label": "Daniel Santiago Mayorga, Junior Backend Developer"
    })
    svg.append(ET.Comment(
        "Adapted from Aurora Veil, beydemirfurkan/awesome-github-profile.\n"
        + (ROOT / "vendor" / "LICENSE").read_text(encoding="utf-8").strip()
    ))
    ET.SubElement(svg, f"{{{ns}}}title").text = "Daniel Santiago Mayorga"
    ET.SubElement(svg, f"{{{ns}}}desc").text = (
        "Junior Backend Developer. Java, Python y SQL. "
        "Aurora en turquesa, violeta y magenta sobre un paisaje nocturno."
    )
    children = list(original)
    svg.append(children[0])
    scene = ET.SubElement(svg, f"{{{ns}}}g",
                          {"transform": "translate(-280 0)"} if mobile else {})
    for child in children[1:]:
        # La primera familia Fraunces inicia el bloque de identidad original.
        if "Fraunces" in child.get("font-family", ""):
            break
        scene.append(child)

    serif = "Fraunces, Playfair Display, Georgia, serif"
    if mobile:
        labels = text(32,42,"Dvanielx03",20,"muted",400,MONO)
        labels += text(32,316,"Daniel Santiago",54,"white",500,serif,
                       extra='font-style="italic" letter-spacing="-1.2"')
        labels += text(32,374,"Mayorga",58,"white",500,serif,
                       extra='font-style="italic" letter-spacing="-1.2"')
        labels += text(36,410,"JUNIOR BACKEND DEVELOPER",22,"primary",400,MONO,
                       extra='letter-spacing="2"')
    else:
        labels = text(80,42,"JAVA / PYTHON / SQL",14,"muted",400,MONO,
                      extra='letter-spacing="3"')
        labels += text(80,368,"Daniel Santiago Mayorga",68,"white",500,serif,
                       extra='font-style="italic" letter-spacing="-1.5"')
        labels += text(82,400,"JUNIOR BACKEND DEVELOPER",18,"primary",400,MONO,
                       extra='letter-spacing="3"')
        labels += text(1120,400,"github.com/Dvanielx03",16,"muted",400,MONO,
                       extra='text-anchor="end"')
    parsed = ET.fromstring(f'<g xmlns="{ns}">{labels}</g>')
    svg.append(parsed)
    if still:
        for parent in svg.iter():
            for child in list(parent):
                if child.tag == f"{{{ns}}}animate":
                    parent.remove(child)
    name = "aurora-name" + ("-mobile" if mobile else "") + ("-static" if still else "")
    (ROOT / (name + ".svg")).write_text(
        "\n".join(row.rstrip() for row in ET.tostring(svg, encoding="unicode").splitlines())
        + "\n", encoding="utf-8"
    )

for mobile in (False,True):
    aurora(mobile)
    aurora(mobile, still=True)
    hero(mobile)
    project("xeon","COTIZACIÓN ASISTIDA",["Conversación","Reglas","Borrador"],mobile)
    project("rental","GESTIÓN DE ALQUILERES",["Catálogo","Reserva","Devolución"],mobile)
    project("motion","VIDEO CON CÓDIGO",["Guion","Fotograma","MP4"],mobile)
    technologies(mobile)
    contact(mobile)
divider()
button()
icon("about",'<circle cx="14" cy="8" r="5"/><path d="M4 25v-3a10 10 0 0 1 20 0v3"/>')
icon("projects",'<path d="M4 8h7l2-3h11v18H4z"/><path d="M4 11h20"/>')
icon("tech",'<rect x="6" y="6" width="16" height="16" rx="3"/><path d="M10 2v4m8-4v4m-8 16v4m8-4v4M2 10h4m-4 8h4m16-8h4m-4 8h4"/><path d="m12 11-3 3 3 3m4-6 3 3-3 3"/>')
icon("collaboration",'<circle cx="8" cy="6" r="3"/><circle cx="20" cy="6" r="3"/><circle cx="14" cy="22" r="3"/><path d="M8 9v4q0 4 6 6m6-10v4q0 4-6 6"/>')
icon("formation",'<path d="m2 10 12-6 12 6-12 6z"/><path d="M6 12v7q8 7 16 0v-7m3 0v9"/>')
icon("languages",'<circle cx="14" cy="14" r="11"/><path d="M3 14h22M14 3q-10 11 0 22M14 3q10 11 0 22"/>')
icon("method",'<path d="M5 6h5v5H5zM18 17h5v5h-5zM10 8h8v6m-3-3 3 3 3-3M8 11v9h10"/>')
icon("portfolio",'<rect x="3" y="5" width="22" height="18" rx="2"/><path d="M3 10h22m-18-3h1m3 0h1m3 0h1m-5 7-3 3 3 3m6-6 3 3-3 3"/>')
icon("resume",'<path d="M6 3h10l6 6v16H6zM16 3v7h6M14 13v8m-3-3 3 3 3-3"/>')
icon("contact",'<rect x="3" y="6" width="22" height="16" rx="3"/><path d="m4 8 10 8L24 8"/>')
print("Generados",len(list(ROOT.glob("*.svg"))),"SVG locales.")
