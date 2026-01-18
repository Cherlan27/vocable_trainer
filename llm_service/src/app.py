import torch
from fastapi import FastAPI
from src.models.api_models import PromptData
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "./openchat_model"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float16
).to(  # noqa: E501
    device
)
model.eval()

app = FastAPI()


@app.post("/generate")
def generate(req: PromptData) -> dict:
    prompt = tokenizer.apply_chat_template(
        [m.dict() for m in req.messages],
        tokenize=False,
        add_generation_prompt=True,  # noqa: E501
    )
    print(prompt)

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=req.max_new_tokens)

        output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return {"response": output_text}
