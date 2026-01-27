# 🚀 Recent Development WebUI
WebUI for recent development

## 🛠 Installation & Setup

### 1. Install uv

Before running the project, ensure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed. 

### 2. Run the Application

```bash
uv run streamlit run main.py
```

### 3. Development (Hot Reload)
To see your changes instantly while developing on localhost, enable the Run on Save feature in the browser:

```
1. Open the Web UI (running the command mentioned above).
2. Click the three dots (⋮) icon in the top-right corner.
3. Go to Settings.
4. Enable the Run on save checkbox.
```

## 📂 Project Structure
`main.py`: Primary Streamlit application script edit here to change  the UI.

`json data/`: Contains the json data generated beforehand. Make sure the name of the file has the feature name as a substring (To search the feature name is lowercased and '_' are added to replace any space)
