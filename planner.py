from data import subjects

def priority_score(subject):
    return len(subject["weak"]) * 2 + subject["credits"] + (6 - subject["confidence"])

def cognitive_load_level(subject):
    if subject["difficulty"] >= 4 and subject["confidence"] <= 3:
        return "HIGH"
    elif subject["difficulty"] >= 3:
        return "MEDIUM"
    else:
        return "LOW"

subjects_sorted = sorted(subjects, key=priority_score, reverse=True)
print("\n📘 AI Study Plan (Day-wise)\n")

focus_topics = []

for day, s in enumerate(subjects_sorted, start=1):
    topic = s["weak"][0] if s["weak"] else s["strong"][0]
    load = cognitive_load_level(s)

    focus_topics.append(topic)

    print(f"Day {day}")
    print(" Subject :", s["name"])
    print(" Focus   :", topic)
    print(" Load    :", load)
    print(" Reason  : Weak area & confidence-based prioritization")
    print("-" * 40)


print("\n🎯 NEXT 7 DAYS – KEY FOCUS AREAS\n")

for t in set(focus_topics):
    print("•", t)


print("\n✅ EXPECTED OUTCOME\n")
print("• Better coverage of weak & prerequisite-heavy topics")
print("• Reduced last-minute stress")
print("• Improved confidence through early focus on difficult areas")
