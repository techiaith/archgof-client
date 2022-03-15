# ArchGof Client

Llyfrgell Python ac offer gorchymyn llinell ar gyfer lawrwlytho cofion
cyfieithu o gwasanaeth API [Archgof][1]. |
Python client library and CLI for downloading translation memories
from the [Archgof][1] API service.


## Defnydd a datblygu | Use and development

```bash
mkdir ~/.virtualenvs
python -m venv ~/.virtualenvs/archgof_client
source ~/.virtualenvs/archgof_client/bin/activate
pip install '.[dev]' -r requirements.txt
python -m archgof.cli download --output-dir=data/tmx
```

[1]: https://cofion.techiaith.cymru
