grades = [
    {"seq": 11, "name": "남수만", "id": "nam", "subject": "파이썬 프로그래밍", "score": 95, "term": "2026-1", "date": "2026-04-15"},
    {"seq": 11, "name": "남수만", "id": "nam", "subject": "데이터베이스 응용", "score": 88, "term": "2026-1", "date": "2026-04-15"},
    {"seq": 22, "name": "홍길동", "id": "hong", "subject": "네트워크 보안", "score": 92, "term": "2026-1", "date": "2026-04-15"}
]

def select_all():
    print("\n--- [ 성적 전체 목록 ] ---")
    print("번호 | 이름(ID) | 과목명 | 점수 | 학기 | 등록일")
    print("-" * 60)
    for i, g in enumerate(grades, 1):
        print(f"{i} | {g['name']}({g['id']}) | {g['subject']} | {g['score']} | {g['term']} | {g['date']}")
    print(f"(총 {len(grades)}건의 성적이 조회되었습니다.)")

def select_one():
    seq = int(input("조회할 학생 번호(seq) 입력: "))
    found = [g for g in grades if g['seq'] == seq]
    if found:
        print(f"\n--- [ {found[0]['name']} 학생의 성적 리포트 ] ---")
        print(f"- 아이디: {found[0]['id']}")
        print(f"- 학기: {found[0]['term']}")
        print("-" * 30)
        total = 0
        for i, g in enumerate(found, 1):
            print(f"{i}. {g['subject']}: {g['score']}점")
            total += g['score']
        print("-" * 30)
        print(f"평균 점수: {total/len(found):.1f}점")

def insert_member():
    print("\n--- [ 성적 데이터 추가 ] ---")
    seq = int(input("- 학생 번호(seq) 입력: "))
    sub = input("- 과목명 입력: ")
    score = int(input("- 점수 입력: "))
    term = input("- 학기 입력: ")
    # 데이터 추가 (이름/ID는 예시로 고정)
    grades.append({"seq": seq, "name": "남수만", "id": "nam", "subject": sub, "score": score, "term": term, "date": "2026-04-15"})
    print(f"\n[시스템] 성적이 성공적으로 등록되었습니다.")

def delete_member():
    idx = int(input("삭제할 성적의 고유 ID 입력: "))
    if 1 <= idx <= len(grades):
        target = grades.pop(idx-1)
        print(f"\n[시스템] {idx}번 데이터가 삭제되었습니다. (대상: {target['subject']})")

def update_member():
    idx = int(input("수정할 성적의 고유 ID 입력: "))
    if 1 <= idx <= len(grades):
        print(f"--- 현재 정보: {grades[idx-1]['subject']} ({grades[idx-1]['score']}점) ---")
        new_score = int(input("- 수정할 점수 입력: "))
        old = grades[idx-1]['score']
        grades[idx-1]['score'] = new_score
        print(f"\n[시스템] 수정 완료! ({old}점 -> {new_score}점)")

def main_menu():
    while True:
        print("\n--- [ 성적 관리 시스템 ] ---")
        print("1. 전체조회  2. 번호조회  3. 성적 추가  4. 성적 삭제  5. 성적 수정  6. 종료")
        choice = input("메뉴 선택: ")
        if choice == '1': select_all()
        elif choice == '2': select_one()
        elif choice == '3': insert_member()
        elif choice == '4': delete_member()
        elif choice == '5': update_member()
        elif choice == '6': print("프로그램을 종료합니다."); break

if __name__ == "__main__":
    main_menu()