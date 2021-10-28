# 이 프로그램은 블랙홀 수에 대한 것입니다.
# 블랙홀 수란 단순히 한 수에서 숫자를 내림차로 정렬한것에서 오름차로 정렬한것을 빼는 과정을 반복해서 변하는 과정의 종작점을 말합니다.
# 예를 들어 모든 3자리 수는 이 과정을 반복하면 459로 끝나게 됩니다.
# 계산하려는 자릿수를 마스터 사이즈를 통해 바꿉니다.


masterSize = 5
map = {}
    
# 내림차에서 오름차를 빼는 함수를 만듭니다.
def subtract(i):
    size = len(str(i))
    numbers = []
    down = 0
    up = 0

    while i > 0:
        numbers.append(i % 10)
        i = i // 10

    if masterSize > size:
        for i in range(0, masterSize - size):
            numbers.append(0)
    numbers.sort()

    for number in numbers:
        up = up * 10
        up += number
    numbers.reverse()

    for number in numbers:
        down = down * 10
        down += number

    return down - up

# 모든 수에 함수를 한번 적용시킨 쌍을 가진 딕셔너리를 만드는 함수를 만듭니다.
def mapping():
    for i in range(1, 10 ** masterSize):
        map[i] = subtract(i)

# 숫자를 정렬하는 함수를 만듭니다. (다른 순서의 같은 숫자를 구분하지 못해 촌수를 세는데 어려움이 생기는것을 막기 위함)
def lineup(numb):
    numb_list = []
    output = 0
    while (numb != 0):
        numb_list.append(numb % 10)
        numb = numb // 10
    size = len(numb_list)
    if masterSize > size:
        for i in (0, masterSize - size):
            numb_list.append(0)
    numb_list.sort()
    for number in numb_list:
        output = output * 10
        output += number
    return output


# 입력받은 수의 경로를 보여주는 함수를 생성합니다.
def getquestion():
    question = input("{}자리 숫자를 입력하세요> ".format(masterSize))
    question = int(question)
    question = lineup(question)
    original_question = question
    distance = 0
    previous_result = 0
    caculation_history = []

    while question != previous_result and question not in caculation_history:
        caculation_history.append(question)
        previous_result = question
        question = map[question]
        question = lineup(question)
        distance += 1
    distance -= 1

    if question == previous_result:
        print("{}은(는) {}로 끝납니다.".format(original_question, question), "촌수는 {}입니다.".format(distance), caculation_history, sep = '\n')
    elif question in caculation_history:
        caculation_history.append(lineup(map[question]))
        print("{}은(는) 무한으로 순환하는 숫자입니다.".format(original_question), "순환고리를 출력합니다.", caculation_history, sep ='\n')

# 모든 맵을 보여주는 함수를 생성합니다.  << 여기 작업중
# def clear_map():
#     newmap = map
#     for i in range(1, 10 ** masterSize):
#         if i in map

# --- 뭔가 존나 잘못하고있는 느낌인데
# 모든 수를 한번 거쳐낸 결과를 먼저 다 계산하고 굴리는거라 뭔가
mapping()

ask = input("맵을 보려면 m, 특정 경로는 r을 입력하세요> ")
if ask == "r":
    while True:
        getquestion()
if ask == "m":
    print("아직 구현되지 않은 부분입니다.")     # 여기에 맵을 보여주는 함수를 넣어야 함