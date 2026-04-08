import time
import sys

def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def main():
    print("=== シンプルタイマー ===")
    print("Enter でスタート / Ctrl+C でストップ / r でリセット / q で終了")
    print()

    total = 0

    while True:
        try:
            cmd = input("▶ Enter でスタート: ").strip().lower()
            if cmd == "q":
                print("終了します。")
                break

            print("⏱ 計測中... (Ctrl+C でストップ)")
            while True:
                total += 1
                sys.stdout.write(f"\r  {format_time(total)} ")
                sys.stdout.flush()
                time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n⏸ ストップ: {format_time(total)}")
            cmd = input("  Enter で再開 / r でリセット / q で終了: ").strip().lower()
            if cmd == "q":
                print("終了します。")
                break
            elif cmd == "r":
                total = 0
                print("🔄 リセットしました。")

if __name__ == "__main__":
    main()
