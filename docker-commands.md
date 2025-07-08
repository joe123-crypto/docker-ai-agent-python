
#Docker model runner

_From host terminal_
```bash
curl -Uri "http://localhost:12434/engines/llama.cpp/v1/chat/completions" `
    -Method POST `
    -ContentType "application/json" `
    -Body '{
        "model": "ai/smollm2",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
```
_From within a container_
```bash
curl -Uri "http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions" `
    -Method POST `
    -ContentType "application/json" `
    -Body '{
        "model": "ai/smollm2",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
    
curl http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/smollm2",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
```