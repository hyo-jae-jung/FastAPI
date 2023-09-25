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
