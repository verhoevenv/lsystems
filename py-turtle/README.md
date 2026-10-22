# Setup (optional, for venv)
Create a venv
```
python3 -m venv venv/
```

Activate venv
```
source ./venv/bin/activate
```

Install (script)
```
python3 -m pip install -e .
```

# Run
With venv:
```
lsystem-turtle ../definitions/koch.toml 4
```

Without venv:
```
python3 fractal.py ../definitions/koch.toml 4
```
