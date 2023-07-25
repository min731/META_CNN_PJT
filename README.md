# 📖 프로젝트명

### ✔️ 기상 상황에 따른 도로 노면 분류 프로젝트 (메티버스 아카데미 2기 AI반 CNN 개인 프로젝트)

# 📃 프로젝트 소개

### ✔️ CNN(AlexNet, ResNet34, VGG16)과 Tag2Text 모델을 활용한 기상 상황에 따른 도로 노면 분류 프로젝트입니다.  

딥러닝 CNN 아키텍처 모델을 통해 차량 운행 중 빗길이나 눈길 등 안전을 위협하는 노면을 분류하는 프로젝트입니다.

정보통신산업진흥원의 2023년 ICT 기술 동향 보고서에 기재된 두가지 기술 키워드

1) 자율주행차를 기반 상업적 서비스를 의미하는 통합모빌리티 서비스의 확대
2) 인근 도로를 주행하는 차량들끼리의 정보 공유를 통한 안전 사고 방지 통신 기술의 확대

를 참고하여 주제를 선정하게 되었습니다.

[NIPA 글로벌 ICT 포털 자율주행차 시장동향 보고서 2023](https://www.globalict.kr/product/product_view.do?menuCode=030200&artclCode=DP0800&catNo=320&viewMode=view&knwldNo=142775)

# 👩‍🔧 팀원 소개 및 역할

### ✔️ 팀원(개인 프로젝트)
메타버스 아카데미 2기 임정민

### ✔️ 역할 분담(개인 프로젝트)
주제 선정 : 임정민
데이터 수집 및 전처리 : 임정민
모델링 및 평가 지표 비교 : 임정민
발표 준비 및 PT 발표 : 임정민

# 📅프로젝트 진행 기록

### ✔️ 수행 기간
2023.07.04 ~ 2023.07.06 (++07.13 Tag2Text 모델 보강)

### ✔️ 세부 진행 기록
- 23-07-04 (9:00 ~ 12:00) : 아이디어 브레인스토밍/피드백, 프로젝트 주제 선정, 동영상 데이터 수집 (Youtube, AI-Hub)
- 23-07-04 (13:00 ~ 20:00) : 동영상 -> 이미지 데이터 전처리, 이미지 데이터 EDA 
- 23-07-05 (9:00 ~ 15:00) : Pytorch 활용 AlexNet, ResNet34, VGG16 모델 학습
- 23-07-05 (15:00 ~ 20:00) : Tensorboard 활용 평가 지표 비교(Accuarcy,Loss), 실전 데이터 Evaluate 원인/결과/개선점 분석
- 23-07-06 (9:00 ~ 12:00) : PPT/대본 작성, 블로그/깃허브 정리

++
- 23-07-13 : Tag2Text 모델 도입, Pretrained된 Tag2Text 모델 활용 Evaluate 
- 23-06-15 : 머신 러닝 회귀 모델링 (XGBoost/LightGBM, RandomForest, LinearRegression, Lasso)
- 23-06-16 : K-Fold 학습, GridSearchcv 하이퍼파라미터 튜닝 학습 후 비교
- 23-06-19 : GridSearchcv 하이퍼파라미터 튜닝, AutoML (Pycaret) 학습, PPT 수정
- 23-06-20 : AutoML(Optuna, Autogluon)학습, 각 모델별 MAE 비교, 인사이트 도출 , PPT 수정, 발표 대본 작성 
- 23-06-21 : PT 발표 및 질의응답


# 📊 데이터 소개
### ✔️ Dacon '데이콘 Basic 자동차 가격 예측 AI 경진대회' 데이터셋을 활용하였습니다.
[데이콘 Basic 자동차 가격 예측 AI 경진대회](https://dacon.io/competitions/official/236114/overview/description) <br><br>

![image](https://github.com/woojooc/ML_Car/assets/115389344/66e2a813-ab89-4802-92a7-8d49f6fe1173)


### ✔️ 데이터 세부 사항
데이터 갯수 : 57920개<br>
ID : 샘플 별 고유 id<br>
생산년도 : 차량이 생산된 연도<br>
모델출시년도 : 차량의 모델이 처음으로 출시된 연도<br>
브랜드<br>
차량모델명<br>
판매도시 : 3글자로 인코딩된 도시 이름<br>
판매구역 : 3글자로 인코딩된 구역 이름<br>
주행거리 : 총 주행 거리(km)<br>
배기량 : 내연기관에서 피스톤이 최대로 밀어내거나 빨아들이는 부피 (cc)<br>
압축천연가스(CNG) : 압축천연가스(CNG) 자동차 여부<br>
경유 : 경유 자동차 여부<br>
가솔린 : 가솔린 자동차 여부<br>
하이브리드 : 하이브리드 자동차 여부<br>
액화석유가스(LPG) : 액화석유가스(LPG) 자동차 여부<br>
가격 : 자동차 가격(백만원)<br>

# 💡 주요 내용

### ✔️ 사전 학습

주제 선정 배경
1. 국내 자동차 시장 중 신차 시장 대비 2배 이상의 규모에 해당하는 중고차 시장
2. 수입차(외제차)의 보편화로 인한 국내 수입차 점유율 증가 추이

도메인 학습
1. 국내/해외별 중고차 시장 가격 영향 요인이 다를 것이라 예상
2. 국내 중고 자동차 시장 가격 영향 요인 : 연식, 주행거리(km), 배기량(CC), 마력 순
3. 해외(튀르키예) 중고 자동차 시장 가격 영향 요인 : 브랜드, 주행거리(km), 연식, 변속기 순

### ✔️ 개요

1. 차량 번호를 조회하여 중고차 시세를 예측하는 서비스의 머신러닝 모델 기획
2. 소셜 데이터에 기반한 중고차 매매 관련 외부요인 탐색<br>
   (1) 크롤링/워드 클라우드 활용 네이버 블로그 '중고차,'중고차 하락' 검색 시 '수출','시세','사고','폐차','업체','국내' 등 키워드 도출
   (2) 해외 기준 국내 중고차 품질의 우수함을 인정받고 있지만 시스템의 부재로 걸맞는 가격을 받지 못하는 상황

### ✔️ 머신 러닝

1. 데이터 전처리<br>
   (1) 신차 / 중고차 분리 : 주행거리 < 200km 의 신차 데이터 drop
   (2) 이상치 데이터 제거 : 주행거리 >= 250만km (최댓값) 데이터 1개 관측/제거
   (3) 중복 Feature 통합 : get_dummies화된 연료 유형 통합
   (4) 불필요한 컬럼 제거 : 'ID'(데이터 고유 키값) , 'City','Area' : 모두 폴란드 지역/도시
   (5) 문자형 데이터 변환 : '브랜드','차량모델명','판매도시','판매구역' Label Encoding
   (6) (선택사항) MinMaxScaling : '연도','차량모델출시년도' MinMaxScaler 적용
2. 학습 결과 (MAE) <br>
   (1) LightGBM : 6.8398
   (2) RandomForest : 6.3714 (K-fold,cv=5,avg값 기준)
   (3) XGBoost : 6.4092
   (4) LinearRegression : 11.95
   (5) Lasso/LassoCV : 13.44 (alpha=1)

    💡MAE 기준 가장 낮은 RandomForest 의 Feature_importances : '생상년도','CC','주행거리','차량출시년도'

### ✔️ 결과

1. 이번 수입 중고차 가격 예측 프로젝트에서 MAE 기준 가장 최적화된 모델은 Optuna(AutoML)의 XGBoost 모델이고 '생산년도','주행거리','배기량','차량모델' 순으로 가격에 영향을 미쳤습니다.
2. 금리,나라별 가격,업체(딜러) 등을 독립변수로 추가할 수 있다면 더욱 정확한 예측 가능합니다.
3. 해당 모델/서비스를 통해 중고차 구매차 및 판매자들에게 여 중고치 시장의 활성화를 도모할 수 있습니다.

# 🛠 기술 스택

### ▪ 언어
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

### ▪ 주요 라이브러리
<img src="https://img.shields.io/badge/scikit learn-F7931E?style=for-the-badge&logo=scikit learn&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/seaborn-99CC00?style=for-the-badge&logo=seaborn&logoColor=white"> <img src="https://img.shields.io/badge/matplotlib-0058CC?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/wordcloud-FF4F8B?style=for-the-badge&logo=wordcloud&logoColor=white">
<img src="https://img.shields.io/badge/konlpy-FF0000?style=for-the-badge&logo=konlpy&logoColor=white"> <img src="https://img.shields.io/badge/collections-7FADF2?style=for-the-badge&logo=collections&logoColor=white">

### ▪ 개발 툴
<img src="https://img.shields.io/badge/VS code-2F80ED?style=for-the-badge&logo=VS code&logoColor=white"> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white">

### ▪ 협업 툴
<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"> <img src="https://img.shields.io/badge/Google Slides-FFBB00?style=for-the-badge&logo=Google Slides&logoColor=white">

# 🔍 참고 자료
### ✔️ 데이터
  
[데이콘 Basic 자동차 가격 예측 AI 경진대회](https://dacon.io/competitions/official/236114/overview/description)

### ✔️ 논문
1) 고찬영, 2021, 다중선형회귀분석을 이용한 중고차 가격 예측 연구 : A사의 사례를 중심으로』, 인하대학교 물류전문대학원 석사학위 논문
2) Sümeyra MUTİ1, Kazım YILDIZ2, 2023, Using Linear Regression For Used Car Price Prediction
,International Journal of Computational and
Experimental Science and ENgineering
,Vol. 9-No.1 (2023) pp. 11-16
