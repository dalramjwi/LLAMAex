from transformers import AutoModelForCausalLM, AutoTokenizer

# 모델과 토크나이저 로드
model_name = "meta-llama/Llama-8b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 입력 텍스트 준비
input_text = "Hello, how can I use Llama 8b?"

# 텍스트 토크나이즈
inputs = tokenizer(input_text, return_tensors="pt")

# 모델 추론
outputs = model.generate(**inputs)

# 결과 디코딩
result = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(result)
