import subprocess

# 문장 파일 읽기
with open('sentences.txt', 'r') as file:
    sentences = file.readlines()

# 분석 결과 저장할 파일 열기
with open('results.txt', 'w') as results_file:
    for sentence in sentences:
        try:
            result = subprocess.run(
                ['ollama', 'llama', '--prompt', f"Analyze this sentence: \"{sentence.strip()}\""],
                capture_output=True, text=True, shell=True, timeout=10  # 10초로 제한
            )
            results_file.write(result.stdout + '\n')
        except subprocess.TimeoutExpired:
            print(f"Command timed out for sentence: {sentence.strip()}")
