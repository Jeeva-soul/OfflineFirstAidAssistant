import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import gradio as gr

# Load model and tokenizer from local folder
model_path = "models/gemma-2-2b-it"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float32)
model.eval()  # Set model to inference mode

# Format prompt using Gemma's chat template
def format_chat_prompt(message):
    messages = [{"role": "user", "content": message}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    return prompt

# Generate first aid response
def generate_response(user_input):
    prompt = format_chat_prompt(user_input)
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=150, do_sample=True, temperature=0.7)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.split("<start_of_turn>model")[1].strip() if "<start_of_turn>model" in answer else answer

# Launch the Gradio UI
demo = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Describe your emergency..."),
    outputs=gr.Textbox(),
    title="🩺 Offline First Aid Assistant",
    description="Ask your first aid questions even without internet. Powered by Google's Gemma 2B."
)

if __name__ == "__main__":
    demo.launch(share=True)

