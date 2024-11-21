import re

def is_valid_html(s):
    # 태그 추출, regex, <>를 단위로 추출
    tag_pattern = re.compile(r'</?[\w\s="\'#./:-]+>')
    
    # 태그 목록 추출
    tags = tag_pattern.findall(s)

    # 스택을 사용하여 태그 검증
    stack = []

    for tag in tags:
        # 빈 태그 (<br /> 같이 />로 끝나는 태그)
        if tag.endswith('/>'):
            continue
        
        # 종료 태그 </tag>
        elif tag.startswith('</'):
            # 여는 태그가 없는 경우 잘못된 구조
            if not stack:
                return False
            
            # 종료 태그에서 태그 이름만 추출
            closing_tag_name = tag[2:-1]
            print("closing: {}".format(closing_tag_name))
            
            # 스택에서 가장 최근에 연 태그와 비교
            opening_tag_name = stack.pop()
            if opening_tag_name != closing_tag_name:
                return False
        
        # 시작 태그 <tag>
        else:
            # 태그 이름만 추출하여 스택에 저장
            index = tag.find(" ")
            opening_tag_name = tag[1:index]

            print("opening: {}".format(opening_tag_name))
            stack.append(opening_tag_name)

    # 스택이 비어 있어야 모든 태그가 정상적으로 닫힌 것
    return len(stack) == 0

# 입력 처리 및 결과 출력
input_string = input().strip()

if is_valid_html(input_string):
    print("true")
else:
    print("false")



# 태그 구조 검증
# HTML 태그를 포함한 문자열이 주어질 때, 해당 문자열이 올바른 태그 구조를 갖추고 있는지 검증하는 프로그램을 작성해. 
# 태그는 <tag> 형식으로 주어지며, 시작 태그와 종료 태그는 다음과 같은 규칙을 따른다:

# 규칙
# 시작 태그는 <tag> 형식이고, 종료 태그는 </tag> 형식이다.
# (<a href="#"></a> 와 같이 시작 태그, 종료 태그가 쌍을 이루는 경우도 있다.)
#  태그는 중첩될 수 있으며, 올바른 순서로 닫혀야 한다.
#  빈 태그는 <tag/> 형식으로 나타낼 수 있다.
# 입력
# 문자열 s (1 ≤ |s| ≤ 1000): HTML 태그가 포함된 문자열

# 출력
# 문자열이 올바른 태그 구조를 갖추고 있으면 true를, 그렇지 않으면 false를 출력한다.

# For example:

# Input	Result

# <div><span></span></div>
# true

# <div><span></div></span>
# false

# <br/><img/>
# true



# <div class="box">와 같은 태그를 예외처리 했어야함
# startswith, endswith 과 같은 함수 사용

