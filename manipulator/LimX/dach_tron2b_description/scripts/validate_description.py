"""Expand supported xacro variants and compare the articulated factory URDF."""
import argparse
import math
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path


def run(factory, output):
    package = Path(__file__).resolve().parents[1]
    output.mkdir(parents=True, exist_ok=True)
    variants = []
    for mode in ("false", "true"):
        visual = f"isaac:={mode}"
        variants.append((f"robot-{mode}", "robot.xacro", [visual]))
        for component in ("body", "head", "arm", "gripper"):
            for side in ("L", "R"):
                variants.append((f"{component}-{side}-{mode}", "component.xacro",
                                 [visual, f"type:={component}", f"side:={side}"]))
        for backend in ("mock_components", "isaac", "gz", "isaac_sim"):
            variants.append((f"control-{backend}-{mode}", "ros2_control/robot.xacro",
                             [visual, f"ros2_control_hardware_type:={backend}"]))
    files = []
    for label, entry, args in variants:
        urdf = output / f"{label}.urdf"
        with urdf.open("w") as stream:
            subprocess.run(["xacro", str(package / "xacro" / entry), *args],
                           check=True, stdout=stream)
        subprocess.run(["check_urdf", str(urdf)], check=True, stdout=subprocess.DEVNULL)
        files.append(urdf)
    verify(files, package, factory)


def key(e):
    if e is None:
        return None
    attrs={}
    for name,val in e.attrib.items():
        try: attrs[name]=tuple(map(float,val.split()))
        except ValueError: attrs[name]=val
    return e.tag, attrs, [key(c) for c in e]
def equal(a,b):
    if isinstance(a,float) and isinstance(b,float):
        return math.isclose(a,b,rel_tol=1e-6,abs_tol=1e-8)
    if type(a)!=type(b): return False
    if isinstance(a,(list,tuple)): return len(a)==len(b) and all(map(lambda pair:equal(*pair),zip(a,b)))
    if isinstance(a,dict): return a.keys()==b.keys() and all(equal(v,b[k]) for k,v in a.items())
    return a==b


def verify(files, p, up):
    for f in files:
        r=ET.parse(f).getroot()
        meshes=[e.get('filename') for e in r.iter('mesh')]
        missing=[m for m in meshes if not m.startswith('package://dach_tron2b_description/')
                 or not (p/m.split('/',3)[-1]).is_file()]
        plugins=[e.text for e in r.findall('./ros2_control/hardware/plugin')]
        print(f.stem, len(r.findall('link')), len(r.findall('joint')), 'meshes',len(meshes), 'missing',missing,'plugins',plugins)
        assert not missing
        if f.stem.startswith('control-'): assert len(plugins)==1 and plugins[0]
    ours=ET.parse(next(f for f in files if f.stem == 'robot-false')).getroot()
    source=ET.parse(up/'robot_grasper.urdf').getroot()
    for kind in ('joint','link'):
        a={e.get('name'):e for e in source.findall(kind)}
        b={e.get('name'):e for e in ours.findall(kind)}
        print(kind,'source only',sorted(a.keys()-b.keys()),'ours only',sorted(b.keys()-a.keys()))
        diffs=Counter()
        fields=('parent','child','origin','axis','limit','mimic','dynamics') if kind=='joint' else ('inertial','visual','collision')
        for name in sorted(a.keys()&b.keys()):
            if kind=='joint' and a[name].get('type')!=b[name].get('type'): print(name,'type',a[name].get('type'),b[name].get('type'))
            for field in fields:
                if not equal([key(e) for e in a[name].findall(field)],[key(e) for e in b[name].findall(field)]):
                    diffs[field]+=1
                    if field not in ('visual','collision'):
                        print(name,field,a[name].find(field).attrib if a[name].find(field) is not None else None,
                              b[name].find(field).attrib if b[name].find(field) is not None else None)
        print('diff totals',diffs)
    for fn in ('robot_grasper.urdf','robot_zeromass_graser.urdf'):
        for j in ET.parse(up/fn).getroot().findall('joint'):
            if 'ee_link' in (j.find('child').get('link')):
                print(fn,j.get('name'),j.find('origin').attrib,j.find('parent').attrib)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("factory_urdf_directory", type=Path)
    parser.add_argument("--output", type=Path, help="Keep expanded URDFs here")
    args = parser.parse_args()
    if args.output:
        run(args.factory_urdf_directory, args.output)
    else:
        with tempfile.TemporaryDirectory(prefix="tron2b-urdf-") as work:
            run(args.factory_urdf_directory, Path(work))


if __name__ == "__main__":
    main()
