# yujeon_be
내일배움캠프 프로젝트 유전 백엔드 원격저장소
# 📜 내일배움캠프 유화 제작 프로젝트 S.A
## 🙋‍♂️ 팀 황리와 아이둘
### 🙌 멤버
- 김태인 : kti0940@gmail.com
- 김희정 : khjhj3808@gmail.com
- 이민기 : psjlmk@gmail.com
- 황영상 : migdracios@gmail.com

게스트님 누구세요
## 💡 아이디어

### ☝ 브레인 스토밍
1. 목적
- Django Rest Framework 사용
- JWT를 활용한 회원가입/로그인
- 유화제작 머신러닝 모델 사용
- 이미지/파일 업로드 시 그에 맞는 결과물 보여주는 서비스

2. 방향성
- 팀원 모두가 DRF CRUD를 구현할 수 있다!
- 아이디어 보다 기능구현에 초점을 맞추자!
- 있던 기능에 추가적으로 활용해보자!


### 🤔 실용성 파악 및 프로젝트 선정
1. 유화 월드컵(ver.1.1) (구리다 너무 구려 / 너도나도 참여하는 온라인 그림 전시회)
-  사용자가 올린 이미지를 모아서 두개중에 한개씩 선택해서 최종선택 하는 서비스 (취향 찾기)

2. 📌유화 경매 사이트(ver.1.0)
- 이미지 업로드후 유화로 변환하여 상품등록
- 추억사진으로 상세설명 가능 입찰로 입찰시간및 입찰금액 조건으로 쿼리 가능 
- 핀터레스트의 기본 레이아웃을 가져 가고 싶음
- 사용자가 이미지 업로드한 유화 사진을 투표를 받고, 투표 수에 따라 일정 포인트 지급
- 특정 시간대에 1위에 선정된 이미지를 경매함.
- 투표를 아침

3. 유화 저작권 사이트 (영감을 얻는 사이트)

4. 유화일기

5. 변태유화 (이중 사진 합성 서비스)

6. 나만의 그림전시회 (유展)


### 🔥 아이디어 상세
나만의 유화전시회 유展 
- 그림 수집욕구를 불러일으키고 저작권을 보유하여 개인 전시회를 열고, 다른 사용자는 입장료를 내고 입장함 (무료 입장도 가능)
1. 핀터레스트 형 SNS
    - 유화 제작 서비스 모델을 활용하여, 업로드한 이미지(바꿀이미지, 스타일이미지)를 적용해 나만의 유화 이미지 생성 및 DB 저장
    - 소유하고 있는 사용자는 전시 활성/비활성 상태를 설정할 수 있다.
    - 물건을 구매하면, 워터마크 새기기/미판매 
    

2. 포인트 시스템(ver.1.1) ⭐
    - 그림 올릴때마다 포인트 수집
    - 그림을 판매한 것 또한 포인트 수집
    - 그림은 좋아요를 받을때마다 가격(포인트) 상승됨
    - 그림 전시회가 가능하며, 포인트를 통해 입장 또는 무료입장으로도 할 수 있음
    - 일정 수준 이상의 좋아요 눌리면, 등급이 레어로 바뀌고 전시하려면 포인트를 소모한다.
    

## 🚩 Ground Rule
### Hard Skill
1. 기술스택
- Django, DRF, HTML, CSS, JavaScript, AWS ec2, CloudFront, Nginx, S3, Gunicorn

2. 코드 컨벤션
- Python 기본 컨벤션
- [HTML 기본 컨벤션 w3school](w3school.com/html/html5_syntax.asp) 보고 따라해보기
- git commit message : **FEAT**, **ADD**, **FIX**, **STYLE**, **WIP** 등을 사용함 
    - FEAT : 명세에 작성된 백엔드 기능 하나가 완성되었을 때 사용
    - ADD : 기능, 스타일 등에서 상세하게 나누어 작업할 때 일단 추가했고, 분기로 나누고 싶을 때 주로 사용함
    - FIX : 버그 등과 같은 오류로 인해서 발생한 코드 수정 사항이 있을 때 사용
    - STYLE : 코드 누락, 스타일 변경 등과 같은 코드 전체에는 큰 변화가 없지만 수정 사항이 있을 때 사용함
    - WIP : 진행중? ㅇㅋ 대신 어디까지 했는지, 어딜 하고 있는지는 적어야함 함 (ex: 로그인 기능 진행중)

3. git 브랜치 전략
- ```add-feat-login```, ```fix-style-mainpage``` 등과 같이 사용

### Soft Skill
1. 복무신조 우리의 약속
- 서로 사랑하자
- 회의 9시, 1시, 7시 딱 5분만
- 정해진 공부시간에 최대한 진짜로 몰입하기!

## ✍ 기획
### 프로젝트 유展
- 이미지를 업로드하여 제작한 유화이미지를 수집하고, 전시하고, 판매하자!
- 핀터레스트형 SNS 아틀리에

## 🧩 목업(WIP)
- [FIGMA WIREFRAME](https://www.figma.com/file/grSqU88N398HLUf1sBt1xb/nbcamp_%EC%9C%A0%ED%99%94%EC%A0%9C%EC%9E%91?node-id=0%3A1)
![nbcamp_유화제작 – Figma - Chrome 2022-06-28 오후 5_00_55](https://user-images.githubusercontent.com/97969957/176126386-c4fac157-db9d-4b9b-a28e-538cc06f92ed.png)

## 📜 일정(WIP)
1. ver.1.0
    - 회원가입
    - 로그인(JWT)
    - 이미지 CRUD
    - 마이페이지 CRUD
    - 메인페이지 프론트엔드
    - 마이페이지 프론트엔드
2. ver.1.1
    - 포인트 적립

## 💾 ERD(WIP)
    
![스크린샷 2022-06-28 오후 4 17 19](https://user-images.githubusercontent.com/97969957/176123719-739766e3-0466-4887-99d8-4e573f78e4ad.png)

    1. UserModel
        - username : CharField(20)
        - password : CharField(128)
        - nickname : CharField(30)
        - email : EmailField()
        - join_date : DateTimeField(auto_now_add=True)

    2. PostModel
        - artist : FK(UserModel)
        - title : CharField(50)
        - image : ImgField
        - desc : TextField()
        - cost : IntegerField()
        - is_mine : BoolField() default=True
        - created_at : DateTimeField(auto_now_add=True)
        
    3. CollectionModel(ver.1.1)
        - artist : FK(UserModel)
        - owner : FK(UserModel)
        - post : FK(PostModel)
        - like : FK(LikeModel)
        - valueprice : IntegerField()

    4. CommentModel(ver.1.2)
        - author :FK(UseModelr)
        - post : FK(PostModel)
        - comment :CharField(128)
        - create_at : DateTimeField(auto_now_add=True)
        - update_at = DateTimeField(auto_now=True)
        
    5. PointModel(ver.1.1)
        - user : FK(UserModel)
        - point : IntegerField()

    6. LikeModel(ver.1.1)
        - user : FK(UserModel)
        - post : FK(PostModel)


## 📜 개발명세

![유화제작 서비스 - 유전 2022-06-28 오후 5_41_59](https://user-images.githubusercontent.com/97969957/176135075-1ae43e5e-eabc-4e95-be55-a05a8d4c507f.png)


## 🙋‍♂️ 역할분담

1. 김희정+김태인
- 회원가입, 로그인(JWT)
- 이미지 업로드, 이미지 보여주기, 마이페이지 내가 작성한 이미지 보여주기 

2. 이민기
- 프론트엔드 메인페이지(비로그인, 로그인), 마이페이지

3. 황영상
- 유화제작 모델 프로젝트 적용
- 마이페이지
- 배포 


# 👨‍💻 Patch
## 🚩 ver.1.1
1. 아이디어 발제
    - 그림에 좋아요를 누르면 그림의 가격 또한 올라감 (좋아요 1당 1포인트 예상)
    - 내 그림이 팔리면, is_mine이 False가 되면서 마이페이지에서 본인 그림 조회할 수 없음 (소유권 이전됨)
    - 그림을 올릴때 판매여부를 체크
    - 업로드하면 그림을 구매할 수 있는 포인트 획득 (10포인트) -> **UserModel**
    - 구매하면 컬렉션에 추가되고 마이페이지에서 볼 수 있음 
    - 내가 올린 그림들은 판매 여부를 체크 옵션으로 선택 가능하고, 체크로 표기할 시 메인페이지에 게시된다. 
    - 처음 그림이 업로드 될 때는 판매여부와 상관없이 메인페이지에 3일간 노출이 된다
    - 노출 여부를 체크로 옵션으로 확인해서 메인페이지에 등록

2. 모델 수정
    - UserModel 수정
        - 사용자 모델 포인트, 판매여부, 노출여부 필드 추가하기
    - PostModel 수정
        - 포스트 모델 가격 디폴트 5로 수정하기
        - 포스트 모델 like 필드 M2M 추가하기
    - LikeModel 추가
    
![내배캠_프로젝트 유전 - Chrome 2022-07-01 오전 10_57_00 (2)](https://user-images.githubusercontent.com/97969957/176808168-5044f489-58e3-4ae3-adfc-8b68ead778ff.png)

3. API 명세 추가
    - class LikeView 좋아요API (POST)
    - class PostView 포인트 모델 save 적용확인 (POST)
    - class PostView 가격 적용 (GET)
    
[ver.1.1.pdf](https://github.com/tunEmvegnomb/yujeon_be/files/9024522/ver.1.1.pdf)


