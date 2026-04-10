import requests
from broker import get_disk, get_memory, get_process

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"


def ask_ai(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )
    response.raise_for_status()
    data = response.json()
    return data.get("response", "").strip()


def main():
    print("AI local đã sẵn sàng. Gõ 'exit' để thoát.")

    while True:
        user_input = input("Bạn: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Thoát.")
            break

        try:
            text = user_input.lower()

            if "disk" in text or "ổ đĩa" in text:
                print("\n=== THÔNG TIN Ổ ĐĨA ===")
                print(get_disk())
                print()
                continue

            if "memory" in text or "ram" in text:
                print("\n=== THÔNG TIN RAM ===")
                print(get_memory())
                print()
                continue

            if "process" in text or "tiến trình" in text:
                print("\n=== DANH SÁCH TIẾN TRÌNH ===")
                print(get_process())
                print()
                continue

            reply = ask_ai(user_input)
            print("AI:", reply)

        except Exception as e:
            print("Lỗi:", e)


if __name__ == "__main__":
    main()