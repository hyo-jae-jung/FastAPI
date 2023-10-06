[FastAPI를 사용한 파이썬 웹 개발 2회차]  

도커 사용 시, 이미지들 간 포트도 겹쳤을 때,  
실행중인 컨테이너의 포트를 실행하려고 하면 도커에서 막음  
사용중만 아니면 포트를 겹쳐서 만들고 실행이 가능하지만 연결오류남.  
그냥 포트는 완전히 배타적으로 설정하자.  

sample schema 공식문서보고 수정함(https://fastapi.tiangolo.com/tutorial/schema-extra-example/#examples-in-json-schema-openapi)  

Typing,mypy,pyright 찾아보기  

pydantic으로 모델 만들어서 입력 데이터 제한, response_model로 출력 데이터 제한  

***
[Example Schema]  
기본적으로 pydantic으로 만든 모델에 example schema를 설정하고 변수와 연결하면 스웨거에서도 출력 가능  
GET과 같은 변수없는 메소드는 response_model에 모델을 연결, POST등 변수가 있으면 라우터 인자 선언 시 연결  
fastapi의 Body클래스를 사용해서 라우터함수의 인자에 example schema를 추가 할 수 있긴 함  

이걸 알아본 이유는 모델 안에 추가했을 때 스웨거에 출력이 안되서인데 연결을 안해줘서 그런거  
위에 적어놓은대로 연결하면 스웨거에도 출력됨.  

라우터함수의 인자에 추가하면 기존 example schema를 덮어씌운다.
***

docker image build --tag [이미지이름] [주소 : 이미지 빌드 전 빌드할 위치로 이동 후 ., 아니면 주소입력]  
docker run -d -p 8000:8000 --name [컨테이너이름] [이미지이름]  
docker exec -it [컨테이너이름] /bin/sh  
docker container stop [컨테이너이름]  
docker container start [컨테이너이름]  

[response_model]  
함수의 return으로 출력되는 output의 형식을 제한한다.  
다양한 경우를 테스트 하니 자연스럽게 typing 라이브러리가 숙지된다.  
책에서는 응답모델 설명 후 오류처리가 나오는데 오류처리를 먼저 해야 응답모델 설정을 깔끔하게 할 수 있을 것 같다.  

