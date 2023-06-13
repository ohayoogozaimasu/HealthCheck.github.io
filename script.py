input_count = input("あなたの年齢は？： ")

message = "あなたは"
input_count *= 2
if input_count >= 150:
    print("Your body is almost ash…")
elif input_count >= 120:
    print(message + "ばたっ…")
elif input_count >= 100:
    print(message + "シュン…")
elif input_count >= 75:
    print(message + "ちょっと元気かな！")
elif input_count >= 60:
    print(message + "元気ですよ！！")
elif input_count >= 45:
    print(message + "フレッシュですね！！！")
else:
    print(message + "産まれたてです！！！！！")
