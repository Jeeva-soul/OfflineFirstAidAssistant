
# 🩺 Offline First Aid Assistant (GEMMA-2B)

An AI-powered, **fully offline emergency assistant** built using **Google's Gemma-2B-IT** model, designed to guide users in first aid scenarios without internet access. Whether you’re in a remote location or caught in a natural disaster, this tool ensures help is never out of reach.

---

## 🧠 Why This Project?

I built this project out of necessity — imagining a world where critical information like **"how to stop bleeding"** or **"how to help someone choking"** should never require an internet connection.  
> "In the age of AI, life-saving help shouldn’t depend on WiFi."

---

## 🚀 What It Does (Current Version)

- ✅ Uses **Gemma-2B-IT** — a 2 billion parameter LLM from Google
- ✅ Runs **entirely offline** on CPU (no internet needed)
- ✅ Provides **step-by-step first aid guidance** through natural conversation
- ✅ Minimalist UI using **Gradio**
- ✅ Based on **PyTorch** + Hugging Face Transformers

---

## 🧪 What’s Working Now

- 🔹 Downloaded and stored **Gemma-2B-IT** model locally (`.safetensors`, tokenizer, config)
- 🔹 Loaded the model using `transformers.AutoModelForCausalLM` and `AutoTokenizer`
- 🔹 Built a **Gradio app** to take user input and generate text
- 🔹 Tested a prompt:  
  > “What should I do if someone has a deep cut and is bleeding?”  
  ✅ Returned a fully structured, ethical, and helpful response in ~6 minutes (first inference)

---

## 📁 Folder Structure

```
OfflineFirstAidAssistant/
├── models/
│   └── gemma-2-2b-it/              # Local model directory with all required files
├── app.py                          # Gradio + PyTorch application script
├── requirements.txt                # Dependencies (torch, transformers, gradio)
├── README.md                       # You're here
```

---

## 🔧 Tech Stack

| Layer           | Tool / Library           |
|------------------|--------------------------|
| 🧠 LLM Model      | Google Gemma-2B-IT        |
| ⚙️ Framework      | PyTorch                   |
| 📚 NLP Toolkit    | Hugging Face Transformers |
| 🌐 UI             | Gradio                    |
| 💻 Mode           | CPU-only, 100% offline    |
| 🧱 Model Format   | `.safetensors`            |

---

## ⏱️ Performance Note

- First inference takes ~6 minutes on a **16 GB RAM** CPU system
- After that, responses are cached and faster
- Memory usage is heavy — not suitable for mobile or low-end machines *yet*

---

## 🧩 Why GEMMA, Not ONNX or Others?

- ❌ ONNX not supported for Gemma (error: custom ONNX config required)
- ❌ GGUF/Llama.cpp not used due to C++ complexity and mobile limitations
- ✅ Stuck with **PyTorch (CPU)** for full control + transparency
- ✅ Hugging Face ecosystem made it easy to prototype and deploy

---

## 🔐 Fully Offline Setup

- No external API
- No model downloads at runtime
- Internet can be completely disabled once model is set up

---

## 👣 Steps to Run

### 1. Clone the repo & setup virtual environment
```bash
git clone https://github.com/yourname/OfflineFirstAidAssistant.git
cd OfflineFirstAidAssistant
python -m venv firstaid_env
firstaid_env\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Gemma-2B-IT manually into:
```
models/gemma-2-2b-it/
├── config.json
├── tokenizer.json
├── tokenizer.model
├── tokenizer_config.json
├── model-00001-of-00002.safetensors
├── model-00002-of-00002.safetensors
```

### 4. Launch the app
```bash
python app.py
```

App will run at: `http://127.0.0.1:7860`

---

## 📌 Example Output

**Prompt:**  
> “What should I do if someone has a deep cut and is bleeding?”

**Response:**  
```
I'm an AI and cannot give medical advice. Call emergency services immediately (911 in the US, 999 in the UK).

While waiting for help, here’s what you can do:
1. Ensure Safety: Check surroundings. Wear gloves if available.
2. Control Bleeding: Apply pressure with a clean cloth.
3. Do Not Remove Objects: If embedded, do not remove sharp objects.
4. Keep Person Calm and Still.
...
```

---

## 📉 Limitations (for now)

| Area              | Status |
|-------------------|--------|
| ONNX Export       | ❌ Not supported by Gemma |
| Voice Input       | ❌ Not yet implemented |
| Generative Images | ❌ Not yet added |
| Mobile Execution  | ❌ Not feasible (model too large) |

---

## 🔮 Upcoming Features

- 🎙️ Offline voice input using Vosk or Whisper.cpp
- 🖼️ Step-by-step visual generation (first aid illustrations)
- 🔊 Text-to-speech playback
- 📦 `.exe` app bundling (for field/off-grid devices)

---

## 🧠 Author

**Jeeva Manavalan**  
> Data Scientist | UTA Alumnus | First-generation engineer  
> *"Using local AI to save lives where the cloud can't reach."*

---

## ⚠️ Disclaimer

This is an educational AI tool and **not a substitute for professional medical care**. Always call emergency services in real-life situations.

---
