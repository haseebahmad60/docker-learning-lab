from datetime import datetime

with open("counter.txt", "a") as file:
    file.write(
        f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    )

print("Counter updated!")