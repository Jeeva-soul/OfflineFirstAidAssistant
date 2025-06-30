
# 🩺 Offline First Aid Assistant (GEMMA-2B)

A fully offline, AI-powered assistant built with Google's **Gemma-2B-IT** model to guide users through emergency **first aid** procedures — without requiring internet access.

---

## 🚀 Features (Current Version)

- ✅ **Runs Fully Offline** using locally downloaded Gemma-2B-IT model
- ✅ **Natural Language Q&A** on emergency first aid topics
- ✅ **Gradio UI** interface for easy interaction
- ✅ **Ethical Response Control** (includes AI warning for medical limits)
- ✅ Modular Python code (ready for future voice/image integration)

---

## 🧠 How It Works

- The project loads the **Gemma-2B-IT** model using Hugging Face's `transformers` library.
- A custom Gradio-based interface receives user queries.
- The model provides step-by-step guidance for emergency situations (e.g., bleeding, choking, CPR).
- All inference is performed **entirely offline**, using your **local CPU** and disk-stored weights.

---

## 🗂️ Folder Structure

```
OfflineFirstAidAssistant/
│
├── models/
│   └── gemma-2-2b-it/                # Locally downloaded model files (.safetensors, tokenizer, config)
│
├── app.py                            # Gradio frontend with Gemma inference backend
├── convert_to_onnx.py (deprecated)   # Initially attempted ONNX conversion (Gemma unsupported)
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
```

---

## 🧪 Sample Response

**Q:** What should I do if someone has a deep cut and is bleeding?

**A:**  
```
I'm an AI and cannot give medical advice. Call emergency services immediately.

However, while waiting for help to arrive, you can follow these steps to help control the bleeding:

1. Ensure Safety:
   - Assess the situation
   - Protect yourself (wear gloves if available)
2. Control the Bleeding:
   - Apply direct pressure with clean cloth or gauze
   - Elevate the injured area if possible
...
```

---

## 🛠️ Tech Stack

| Layer        | Technology              |
|--------------|--------------------------|
| 🧠 Model      | Google Gemma-2B-IT (local .safetensors) |
| 🔍 Inference  | PyTorch (CPU-only)       |
| 📚 NLP        | Hugging Face Transformers |
| 🧰 UI         | Gradio                   |
| 💾 Offline    | Entire project works without internet |

---

## ❌ Known Limitations

- 🐌 First response takes ~6 mins (large model + no GPU)
- ⚠️ ONNX export is not currently supported for Gemma
- 📱 Mobile deployment is not feasible for 2B models due to size
- 🎤 Voice input and 🖼️ generative visuals are planned but not implemented yet

---

## 📈 Future Plans

- 🗣️ Add offline **voice input** using Vosk
- 🖼️ Generate step-by-step **illustrations** for procedures
- 🔊 Integrate **text-to-speech** for response playback
- 📦 Package app as a portable `.exe` for Windows use

---

## 📌 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/OfflineFirstAidAssistant.git
cd OfflineFirstAidAssistant
```

### 2. Create and activate environment
```bash
python -m venv firstaid_env
firstaid_env\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Ensure model is placed locally:
```
models/gemma-2-2b-it/
  ├── config.json
  ├── tokenizer.json
  ├── tokenizer.model
  ├── tokenizer_config.json
  ├── model-00001-of-00002.safetensors
  ├── model-00002-of-00002.safetensors
```

### 5. Run the app
```bash
python app.py
```

Visit `http://127.0.0.1:7860` in your browser.

---

## 👨‍💻 Author

**Jeeva Manavalan**  
Data Scientist | UTA Alumnus  
*First-generation engineer building tools to save lives with offline AI.*

---

## 🛡️ Disclaimer

This assistant is for **informational purposes only** and does not replace professional medical advice or emergency services.

---
 
