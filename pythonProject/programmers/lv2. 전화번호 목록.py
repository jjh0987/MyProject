def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book)):
        try:
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
        except:
            break

    return answer

solution(["119", "97674223", "1195524421"])
