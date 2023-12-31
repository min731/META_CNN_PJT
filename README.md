# 📖 프로젝트명

### ✔️ 기상 상황에 따른 도로 노면 분류 프로젝트 (메티버스 아카데미 2기 AI반 CNN 개인 프로젝트)

![image](https://github.com/min731/META_CNN_PJT/assets/115389344/4ca9f8ec-bd46-4914-a166-3d2a48a484fa)

# 📃 프로젝트 소개

### ✔️ CNN(AlexNet, ResNet34, VGG16)과 Tag2Text 모델을 활용한 기상 상황에 따른 도로 노면 분류 프로젝트입니다.  

딥러닝 CNN 아키텍처 모델을 통해 차량 운행 중 빗길이나 눈길 등 안전을 위협하는 노면을 분류하는 프로젝트입니다.

정보통신산업진흥원의 2023년 ICT 기술 동향 보고서에 기재된 두가지 기술 키워드

1) 통합모빌리티 서비스의 확대
2) 차량 대 인프라 통신 기술의 확대

를 참고하여 주제를 선정하게 되었습니다.

[NIPA 글로벌 ICT 포털 자율주행차 시장동향 보고서 2023](https://www.globalict.kr/product/product_view.do?menuCode=030200&artclCode=DP0800&catNo=320&viewMode=view&knwldNo=142775)

# 👩‍🔧 팀원 소개 및 역할

### ✔️ 팀원(개인 프로젝트)
메타버스 아카데미 2기 임정민

### ✔️ 역할 분담(개인 프로젝트)
주제 선정 : 임정민<br>

데이터 수집 및 전처리 : 임정민<br>

모델링 및 평가 지표 비교 : 임정민<br>

발표 준비 및 PT 발표 : 임정민<br>

# 📅프로젝트 진행 기록

### ✔️ 수행 기간
2023.07.04 ~ 2023.07.06 (++07.13 Tag2Text 모델 보강, 07.14 전 전공 PT 발표 및 질의응답)

### ✔️ 세부 진행 기록
- 23-07-04 (9:00 ~ 12:00) : 아이디어 브레인스토밍/피드백, 프로젝트 주제 선정, 동영상 데이터 수집 (Youtube, AI-Hub)
- 23-07-04 (13:00 ~ 20:00) : 동영상 -> 이미지 데이터 전처리, 이미지 데이터 EDA 
- 23-07-05 (9:00 ~ 15:00) : Pytorch 활용 AlexNet, ResNet34, VGG16 모델 학습
- 23-07-05 (15:00 ~ 20:00) : Tensorboard 활용 평가 지표 비교(Accuarcy,Loss), 실전 데이터 Evaluate 원인/결과/개선점 분석
- 23-07-06 (9:00 ~ 12:00) : AI 전공 내부 PPT/대본 작성, 블로그/깃허브 정리
- 23-07-06 (13:00 ~ 18:00) : AI 전공 내부 PT 발표 및 질의응답

++
- 23-07-13 : Tag2Text 모델 도입, Pretrained된 Tag2Text 모델 활용 Evaluate, 평가 지표 확인
- 23-07-14 : 전 전공 PT 발표 및 질의응답


# 📊 데이터 소개
### ✔️ AI-Hub '다양한 기상 상황 주행 데이터' 와 Youtube '고속버스 주행 영상', '비오는 날 주행 영상', '눈오는 날 주행 영상' 등을 활용하였습니다.

![image](https://github.com/min731/META_CNN_PJT/assets/115389344/5c35d22f-55d7-4410-afc5-bdde17ddebf6)

[AI-hub 다양한 기상 상황 주행 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=630)

![image](https://github.com/min731/META_CNN_PJT/assets/115389344/61e96934-6151-490f-9632-16c215afa498)

[Youtube 고속도로 주행 영상](https://www.youtube.com/results?search_query=%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C+%EC%A3%BC%ED%96%89+%EC%98%81%EC%83%81)




### ✔️ 데이터 세부 사항

총 데이터 갯수 : 30000개 도로 노면 이미지 데이터(AI-Hub 10000개 + Youtube 도로 주행 20000개)<br>
클래스 : Normal(맑음), Rainy(빗길), Snowy(눈길) 3개 클래스

# 💡 주요 내용

### ✔️ 주제 선정 배경

1. 통합 모빌리티 서비스 (Mobility as a Service)의 확대 <br><br>
참고한 NIPA의 2023년 ICT 기술 동향 보고서에서 통합 모빌리티 서비스, '자율주행차를 기반으로 상업적인 서비스가 확대될 것이다' 라고 언급했습니다. 무인택시나 자율주행셔틀,무인 트럭 등이 예시입니다.
자율주행셔틀의 경우 현재에도 청계천,청와대 일대를 운영중입니다. 이 자율주행셔틀의 특징 중 한가지는 Level3 자율주행시스템으로 평시에는 시스템이 운전하다가 유사시에 운전자의 개입이 필요할 때에만 시스템이 
대기하고 있던 운전자에게 요청하여 조작하는 구조입니다. 이때, 비운전 상황에서 운전자가 안전에 관련한 요소들을 모니터링할 수 있는 시스템이 필요하지 않을까라는 생각에서 도로 노면 분류 모듈 개발에 대한 아이디어를 얻었습니다.

2. 차량 대 인프라 통신 (Vehicle for Infra)기술의 전망성  <br><br>
또한 참고한 보고서에 따르면 차량 대 인프라통신 기술이 확대될 것이라고 언급하였습니다. 차량 대 인프라통신 기술은 인근 도로를 주행하는 차량들끼리 수집한 정보들을 공유하면서 서로 안전하게 운행할 수 있게끔 도와주는 기술을 말합니다. 만약 광역버스, 고속버스처럼 주기적으로 왕복하는 차량에 카메라를 설치할 수 있다면 도로 구간별로 실시간 노면 상태 정보를 수집하여  카카오맵과 같은 지도상에 어느 구간이 빙결되어 있는지 표시하여 여행 중 안전에 유의할 수 있게 도와주는 서비스로 확장될 수 있습니다.

### ✔️ 데이터 전처리 

(1) AI-Hub, Yotube 영상 데이터 수집

(2) 영상 데이터 frame 단위 (20 frame 간격) 분할

(3) Pytorch Transform.Lambda() 활용 도로 노면 중심으로 Crop (Horizontal Crop)

### ✔️ CNN 모델 학습 및 Accuaracy

(1) AlexNet (optim = Adam, lr=1e-4, epoch = 1(Early Stop)) , Accuracy = 0.9997 

(2) ResNet34 (optim = Adam, lr=1e-4, epochs = 2(Early Stop)) , Accuracy = 0.9983

(3) VGG16 (optim = Adam, lr=1e-4, epoch = 1(Early Stop)) , Accuracy = 0.9800

### ✔️ Tag2Text 모델 Accuaracy

(1) Pretrained된 Tag2Text 모델 (Fine-Tunning 진행X)

(2) 평가 기준 : 이미지에 대한 묘사된 Caption 안의 'rainy' or 'snowy' 등의 단어 검출 시 해당 클래스로 분류

(3) Accuracy = 0.8696

💡Vision-Language Pretraining(VLP) 생성 모델의 이미지 분류 Task 가능성 확인

### ✔️ 결과

1. CNN 모델 중에서는 ResNet34이 테스트 데이터 6000개 기준 18개만 틀린 Accuaracy = 0.9997로 가장 높은 정확도를 보였습니다. 
2. 단, 실전 데이터 테스트 분석 결과 서비스에 도입하기 위해서는 터널/도심/야간 주행이 포함된 데이터셋까지 필요함을 깨달았습니다.
3. Accuracy = 0.8696를 보인 Pretrained Tag2Text와 같은 텍스트 생성 모델로 CNN을 대체할 수 있는 가능성을 볼 수 있었습니다.  

# 🛠 기술 스택
### ▪ 언어

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

### ▪ 주요 라이브러리

<img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/torchvision-29A7DF?style=for-the-badge&logo=torchvision&logoColor=white"> <img src="https://img.shields.io/badge/opencv-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"> <img src="https://img.shields.io/badge/tensorboard-FF6F00?style=for-the-badge&logo=tensorboard&logoColor=white"> <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/PIL-67C52A?style=for-the-badge&logo=PIL&logoColor=white"> <img src="https://img.shields.io/badge/matplotlib-0058CC?style=for-the-badge&logo=matplotlib&logoColor=white"> 

### ▪ 개발 툴
<img src="https://img.shields.io/badge/VS code-2F80ED?style=for-the-badge&logo=VS code&logoColor=white"> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white">
### ▪ 협업 툴

<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"> <img src="https://img.shields.io/badge/Google Slides-FFBB00?style=for-the-badge&logo=Google Slides&logoColor=white">

# 🔍 참고 자료
### ✔️ 데이터
  
[AI-hub 다양한 기상 상황 주행 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=realm&dataSetSn=630)
[Youtube 고속도로 주행 영상](https://www.youtube.com/results?search_query=%EA%B3%A0%EC%86%8D%EB%8F%84%EB%A1%9C+%EC%A3%BC%ED%96%89+%EC%98%81%EC%83%81)

### ✔️ 보고서
[NIPA 글로벌 ICT 포털 자율주행차 시장동향 보고서 2023](https://www.globalict.kr/product/product_view.do?menuCode=030200&artclCode=DP0800&catNo=320&viewMode=view&knwldNo=142775)
