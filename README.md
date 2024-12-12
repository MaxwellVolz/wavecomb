# wavecomb
python based wave catcher


## Install

```sh
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
## Run
```sh
python -m streamlit run app.py
```

## Get data

Press `Win + R`, type `taskschd.msc`, and press `Enter`.

```sh
# schedule it
schtasks /create /sc hourly /tn "Get Surfline Data" /tr "powershell -Command '& C:\Users\%USERNAME%\py\wavecomb\venv\Scripts\Activate.ps1; python C:\Users\%USERNAME%\py\wavecomb\get_surfline_data.py'"

# stop it (deletes?)
schtasks /end /tn "Get Surfline Data"

# disable it
schtasks /change /tn "Get Surfline Data" /disable

# enable it
schtasks /change /tn "Get Surfline Data" /enable

# query the task status using PowerShell:
schtasks /query /tn "Get Surfline Data" /fo LIST /v

```