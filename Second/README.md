[FastAPI를 사용한 파이썬 웹 개발 2회차]  

도커 사용 시, 이미지들 간 포트도 겹쳤을 때,  
실행중인 컨테이너의 포트를 실행하려고 하면 도커에서 막음  
사용중만 아니면 포트를 겹쳐서 만들고 실행이 가능하지만 연결오류남.  
그냥 포트는 완전히 배타적으로 설정하자.  

sample schema 공식문서보고 수정함(https://fastapi.tiangolo.com/tutorial/schema-extra-example/#examples-in-json-schema-openapi)  

Typing,mypy,pyright 찾아보기  
