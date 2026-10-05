from pathlib import Path
import urllib.request,hashlib
p=Path('outputs/02_datos_estudio/raw/uci501.zip');p.parent.mkdir(parents=True,exist_ok=True)
if not p.exists():
    urllib.request.urlretrieve('https://archive.ics.uci.edu/static/public/501/beijing%2Bmulti%2Bsite%2Bair%2Bquality%2Bdata.zip',p)
assert hashlib.sha256(p.read_bytes()).hexdigest()=='b04da438b2f331ac0ffd45aebdfec0d20d2367feb5f6948c4b1f7ce1191e33c4', 'Source hash mismatch; do not silently replace the study data.'
print('Source archive verified.')
