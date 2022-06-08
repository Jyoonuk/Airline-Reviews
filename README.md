# project1 ( 전세계의 인기 항공사에 대한 리뷰  )
+ 전 세계의 항공사들의 전체적인 데이터를 분석하고 
+ 각 항공사들의 상관계수를 이용하여 
+ 유사한 항공사를 추천해주는 웹 입니다.

데이터 출처 : https://www.kaggle.com/datasets/efehandanisman/skytrax-airline-reviews
웹 주소 : http://15.164.229.97:8502/

# 데이터 컬럼 설명 
+ airline: Name of the airline.
+ overall: Overall point given to the trip between 1 to 10.
+ author: Author of the trip
+ reviewdate: Date of the Review customerreview: Review of the customers in free text format
+ aircraft: Type of the aircraft
+ travellertype: Type of traveller (e.g. business, leisure) cabin: Cabin at the flight dateflown: Flight date
+ seatcomfort: Rated between 1-5 cabinservice: Rated between 1-5
+ foodbev: Rated between 1-5 entertainment: Rated between 1-5 groundservice: Rated between 1-5
+ valueformoney: Rated between 1-5

분석
평점,리뷰개수에 따라 항공사를 분석했다.

추천
항공사를 선택하고 그와 유사한 항공사를 5개 추천해준다.


