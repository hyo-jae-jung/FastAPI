HTTP[HyperText Transfer Protocol]  
문자 그래도 통신 규약인데 하이퍼텍스트로 서버와 클라이언트간 메시지 교환 규칙이다.  

Content-Type : 내가 보낼 데이터 형식  
Accept : 내가 받고 싶은 데이터 형식  

GET -> request header, Path Parameter, Query Parameter  
POST -> request body  


[RESTful API]  
HTTP를 지원하는 프로그램 언어.  
성능 향상이 목적이 아니라 일관적 컨벤션, API 이해도 및 호환성 상승이 목적  

***
mkdir -p [디렉토리 주소]  : hide a directory.  
cat /etc/issue : check an ubuntu version.  
***

[MongoDB]  

몽고DB 사용 여부 확인  
ps aux | grep mongod  

service mongod start   = systemctl start mongod  
service mongod stop    = systemctl stop mongod  
service mongod status  = systemctl status mongod  

몽고DB 인스턴스 실행
mongod --dbpath [주소]
exitCode:100 is a directory location error  

몽고DB admin 실행  
mongosh "mongodb://hostname:port"  

help 입력하면 정보 많음  
show dbs : db 목록조회  
use mydatabase : 특정 db 선택  
show tables : 선택된 db 테이블 목록확인  
CRUD 명령어 검색 ㄱㄱ  


[JWT : JSON Web Token]  
토큰을 사용하는 이유는 웹 환경에서 보안을 유지한 채 로그인 한 상태로 다양한 작업을 하기 위함  

클라이언트 계정 발급 시, 패스워드 해싱 후 서버가 저장  
발급된 계정으로 로그인 시, 토큰 발급(JWT)  
클라이언트는 발급된 토큰으로 다양한 데이터 요청  
서버는 토큰 확인 후 요청 데이터 전송  

