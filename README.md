# Music Data Collection Using Python

This project provides a simple way to collect music chart data using Python. It automates the process of fetching and saving music data from various sources for further analysis or display in applications.

## Features

- Fetch music chart data (e.g., Apple Music, Melon, YouTube Music) from specified URLs.
- Save data in structured JSON format.
- Automate the data collection process for periodic updates.

## Prerequisites

- Python 3.8 or later installed.
- Required Python libraries: selenium, beautifulsoup4, requests, lxml, json.
- Chrome WebDriver installed and available in your system PATH.

Install dependencies using:

```
pip install selenium beautifulsoup4 lxml requests
```

## 🇰🇷 Korea Musci Chart

```
https://websseu.github.io/pythonMusic2/korea/bugs/bugsTop100_[current_date].json
https://websseu.github.io/pythonMusic2/korea/flo/floTop100_[current_date].json
https://websseu.github.io/pythonMusic2/korea/genie/genieTop100_[current_date].json
https://websseu.github.io/pythonMusic2/korea/melon/melonTop100_[current_date].json
https://websseu.github.io/pythonMusic2/korea/vibe/vibeTop100_[current_date].json
```

멜론(melon) 뮤직 순위 100  
지니(genie) 뮤직 순위 100  
벅스(bugs) 뮤직 순위 100  
플로(flo) 뮤직 순위 100  
바이브(vibe) 뮤직 순위 100

## 📹 유튜브 뮤직 전세계 챠트

```
https://websseu.github.io/pythonMusic2/youtube/[cuntry]/[cuntry]Top100_[current_date].json
```

유튜브 뮤직 🌏 글로벌(global) 순위 100  
유튜브 뮤직 🇦🇷 아르헨티나(ar) 순위 100  
유튜브 뮤직 🇦🇺 호주(au) 순위 100  
유튜브 뮤직 🇦🇹 오스트리아(at) 순위 100  
유튜브 뮤직 🇧🇴 볼리비아(bo) 순위 100  
유튜브 뮤직 🇧🇷 브라질(br) 순위 100  
유튜브 뮤직 🇨🇦 캐나다(ca) 순위 100  
유튜브 뮤직 🇨🇱 칠레(cl) 순위 100  
유튜브 뮤직 🇨🇴 콜롬비아(co) 순위 100  
유튜브 뮤직 🇨🇷 코스타리카(cr) 순위 100  
유튜브 뮤직 🇨🇿 체코(cr) 순위 100  
유튜브 뮤직 🇩🇰 덴마크(dk) 순위 100  
유튜브 뮤직 🇩🇴 도미니카 공화국(do) 순위 100  
유튜브 뮤직 🇪🇨 에콰도르(ec) 순위 100  
유튜브 뮤직 🇪🇬 이집트(eg) 순위 100  
유튜브 뮤직 🇸🇻 엘살바도르(sv) 순위 100  
유튜브 뮤직 🇪🇪 에스토니아(ee) 순위 100  
유튜브 뮤직 🇫🇮 핀란드(fi) 순위 100  
유튜브 뮤직 🇫🇷 프랑스(fr) 순위 100  
유튜브 뮤직 🇩🇪 독일(de) 순위 100  
유튜브 뮤직 🇬🇹 과테말라(gt) 순위 100  
유튜브 뮤직 🇬🇹 온두라스(hn) 순위 100  
유튜브 뮤직 🇭🇺 헝가리(hn) 순위 100  
유튜브 뮤직 🇮🇸 아이슬란드(is) 순위 100  
유튜브 뮤직 🇮🇳 인도(in) 순위 100  
유튜브 뮤직 🇮🇩 인도네시아(id) 순위 100  
유튜브 뮤직 🇮🇱 이스라엘(il) 순위 100  
유튜브 뮤직 🇮🇹 이탈리아(it) 순위 100  
유튜브 뮤직 🇯🇵 일본(jp) 순위 100  
유튜브 뮤직 🇰🇪 케냐(ke) 순위 100  
유튜브 뮤직 🇱🇺 룩셈부르크(lu) 순위 100  
유튜브 뮤직 🇲🇽 멕시코(lu) 순위 100  
유튜브 뮤직 🇳🇱 네덜란드(lu) 순위 100  
유튜브 뮤직 🇳🇿 뉴질랜드(nz) 순위 100  
유튜브 뮤직 🇳🇮 니카라과(ni) 순위 100  
유튜브 뮤직 🇳🇬 나이지리아(ng) 순위 100  
유튜브 뮤직 🇳🇴 노르웨이(no) 순위 100  
유튜브 뮤직 🇵🇦 파나마(no) 순위 100  
유튜브 뮤직 🇵🇾 파라과이(no) 순위 100  
유튜브 뮤직 🇵🇾 페루(pe) 순위 100  
유튜브 뮤직 🇵🇱 폴란드(pl) 순위 100  
유튜브 뮤직 🇵🇹 포르투갈(pt) 순위 100  
유튜브 뮤직 🇷🇴 루마니아(ro) 순위 100  
유튜브 뮤직 🇷🇺 러시아(ru) 순위 100  
유튜브 뮤직 🇸🇦 사우디아라비아(ru) 순위 100  
유튜브 뮤직 🇷🇸 세르비아(rs) 순위 100  
유튜브 뮤직 🇿🇦 남아프리카 공화국(za) 순위 100  
유튜브 뮤직 🇰🇷 대한민국(kr) 순위 100  
유튜브 뮤직 🇪🇸 스페인(es) 순위 100  
유튜브 뮤직 🇸🇪 스웨덴(se) 순위 100  
유튜브 뮤직 🇨🇭 스위스(ch) 순위 100  
유튜브 뮤직 🇹🇿 탄자니아(ch) 순위 100  
유튜브 뮤직 🇹🇷 튀르키예(tr) 순위 100  
유튜브 뮤직 🇺🇬 우간다(tr) 순위 100  
유튜브 뮤직 🇺🇦 우크라이나(ua) 순위 100  
유튜브 뮤직 🇦🇪 아랍에미리트(ae) 순위 100  
유튜브 뮤직 🇬🇧 영국(gb) 순위 100  
유튜브 뮤직 🇺🇸 미국(us) 순위 100  
유튜브 뮤직 🇺🇾 우루과이(uy) 순위 100  
유튜브 뮤직 🇿🇼 짐바브웨(zw) 순위 100

## 🍎 애플 뮤직 전세계 챠트

```
https://websseu.github.io/pythonMusic2/apple/[cuntry]/[cuntry]Top100_[current_date].json
```

애플 뮤직 🌏 글로벌(global) 순위 100  
애플 뮤직 🇺🇸 미국(usa) 순위 100  
애플 뮤직 🇬🇧 영국(uk) 순위 100  
애플 뮤직 🇲🇽 멕시코(mexico) 순위 100  
애플 뮤직 🇦🇺 호주(australia) 순위 100  
애플 뮤직 🇯🇵 일본(japan) 순위 100  
애플 뮤직 🇪🇸 스페인(spain) 순위 100  
애플 뮤직 🇫🇷 프랑스(france) 순위 100  
애플 뮤직 🇩🇪 독일(germany) 순위 100  
애플 뮤직 🇰🇷 한국(south-korea) 순위 100  
애플 뮤직 🇦🇬 앤티가 바부다 순위 100  
애플 뮤직 🇦🇷 아르헨티나(argentina) 순위 100  
애플 뮤직 🇦🇲 아르메니아(armenia) 순위 100  
애플 뮤직 🇦🇺 호주(austria) 순위 100  
애플 뮤직 🇦🇿 아제르바이잔(azerbaijan) 순위 100  
애플 뮤직 🇧🇭 바레인(bahrain) 순위 100  
애플 뮤직 🇧🇧 바베이도스(barbados) 순위 100  
애플 뮤직 🇧🇾 벨라루스(belarus) 순위 100  
애플 뮤직 🇧🇪 벨기에(belgium) 순위 100  
애플 뮤직 🇧🇧 벨리즈(belize) 순위 100  
애플 뮤직 🇧🇴 볼리비아(bolivia) 순위 100  
애플 뮤직 🇧🇼 보츠와나(botswana) 순위 100  
애플 뮤직 🇧🇷 브라질(brazil) 순위 100  
애플 뮤직 🇧🇬 불가리아(bulgaria) 순위 100  
애플 뮤직 🇰🇭 캄보디아(cambodia) 순위 100  
애플 뮤직 🇨🇻 카보베르데(cape-verde) 순위 100  
애플 뮤직 🇨🇱 칠레(chile) 순위 100  
애플 뮤직 🇨🇳 중국(china) 순위 100  
애플 뮤직 🇨🇴 콜로비아(colombia) 순위 100  
애플 뮤직 🇨🇷 코스타리카(costa-rica) 순위 100  
애플 뮤직 🇨🇾 키프로스(cyprus) 순위 100  
애플 뮤직 🇨🇿 체코 순위(czechia) 100  
애플 뮤직 🇩🇰 덴마크 순위(denmark) 100  
애플 뮤직 🇩🇲 도미니카(dominica) 순위 100  
애플 뮤직 🇩🇴 도미니카 공화국(dominican-republic) 순위 100  
애플 뮤직 🇪🇨 에콰도르(ecuador) 순위 100  
애플 뮤직 🇪🇬 이집트(egypt) 순위 100  
애플 뮤직 🇸🇻 엘살바도르(salvador) 순위 100  
애플 뮤직 🇪🇪 에스토니아(estonia) 순위 100  
애플 뮤직 🇫🇲 미크로네시아(micronesia) 순위 100  
애플 뮤직 🇫🇯 피지(fiji) 순위 100  
애플 뮤직 🇫🇮 핀란드(finland) 순위 100  
애플 뮤직 🇬🇲 감비아(gambia) 순위 100  
애플 뮤직 🇬🇭 가나(ghana) 순위 100  
애플 뮤직 🇬🇷 그리스(greece) 순위 100  
애플 뮤직 🇬🇩 그레나다(grenada) 순위 100  
애플 뮤직 🇬🇹 과테말라(guatemala) 순위 100  
애플 뮤직 🇬🇼 기니비사우(bissau) 순위 100  
애플 뮤직 🇭🇳 온두라스(honduras) 순위 100  
애플 뮤직 🇭🇰 홍콩(hong-kong) 순위 100  
애플 뮤직 🇭🇺 헝가리(hungary) 순위 100  
애플 뮤직 🇮🇳 인도(india) 순위 100  
애플 뮤직 🇮🇩 인도네시아(indonesia) 순위 100  
애플 뮤직 🇮🇱 이스라엘(israel) 순위 100  
애플 뮤직 🇮🇹 이탈리아(italy) 순위 100  
애플 뮤직 🇯🇴 요르단(jordan) 순위 100  
애플 뮤직 🇰🇿 카자흐스탄(kazakhstan) 순위 100  
애플 뮤직 🇰🇪 케냐(kenya) 순위 100  
애플 뮤직 🇰🇬 키르기스스탄(kyrgyzstan) 순위 100  
애플 뮤직 🇱🇦 라오스(laos) 순위 100  
애플 뮤직 🇱🇻 라트비아(latvia) 순위 100  
애플 뮤직 🇱🇧 레바논(lebanon) 순위 100  
애플 뮤직 🇱🇹 리투아니아(lithuania) 순위 100  
애플 뮤직 🇱🇺 룩셈부르크(luxembourg) 순위 100  
애플 뮤직 🇲🇾 말레이시아(malaysia) 순위 100  
애플 뮤직 🇲🇹 몰타(malta) 순위 100  
애플 뮤직 🇲🇺 모리셔스(mauritius) 순위 100  
애플 뮤직 🇲🇳 몽골(mongolia) 순위 100  
애플 뮤직 🇳🇵 네팔(nepal) 순위 100  
애플 뮤직 🇳🇱 네덜란드(netherlands) 순위 100  
애플 뮤직 🇳🇿 뉴질랜드(new-zealand) 순위 100  
애플 뮤직 🇳🇮 니카라과(nicaragua) 순위 100  
애플 뮤직 🇳🇪 니제르(niger) 순위 100  
애플 뮤직 🇳🇬 나이지리아(nigeriar) 순위 100  
애플 뮤직 🇳🇴 노르웨이(norway) 순위 100  
애플 뮤직 🇴🇲 오만(oman) 순위 100  
애플 뮤직 🇵🇦 파나마(panama) 순위 100  
애플 뮤직 🇵🇬 파푸아뉴기니(papua-new-guinea) 순위 100  
애플 뮤직 🇵🇾 파라과이(paraguay) 순위 100  
애플 뮤직 🇵🇪 페루(peru) 순위 100  
애플 뮤직 🇵🇭 필리핀(philippines) 순위 100  
애플 뮤직 🇵🇱 폴란드(poland) 순위 100  
애플 뮤직 🇵🇹 포르투갈(portugal) 순위 100  
애플 뮤직 🇲🇩 몰도바(moldova) 순위 100  
애플 뮤직 🇷🇴 루마니아(romania) 순위 100  
애플 뮤직 🇸🇦 사우디아라비아(saudi-arabia) 순위 100  
애플 뮤직 🇸🇬 싱가포르(singapore) 순위 100  
애플 뮤직 🇸🇰 슬로바키아(slovakia) 순위 100  
애플 뮤직 🇸🇮 슬로베니아(slovenia) 순위 100  
애플 뮤직 🇿🇦 남아프리카 공화국(south-africa) 순위 100  
애플 뮤직 🇱🇰 스리랑카(sri-lanka) 공화국 순위 100  
애플 뮤직 🇰🇳 세인트키츠 네비스 공화국(st-kitts-and-nevis) 순위 100  
애플 뮤직 🇸🇿 에스와티니(eswatini) 순위 100  
애플 뮤직 🇸🇪 스웨덴(sweden) 순위 100  
애플 뮤직 🇨🇭 스위스(switzerland) 순위 100  
애플 뮤직 🇹🇼 대만(taiwan) 순위 100  
애플 뮤직 🇹🇯 타지키스탄(tajikistan) 순위 100  
애플 뮤직 🇹🇭 태국(thailand) 순위 100  
애플 뮤직 🇹🇹 트리니다드 토바고(trinidad-and-tobago) 순위 100  
애플 뮤직 🇹🇲 투르크메니스탄(turkmenistan) 순위 100  
애플 뮤직 🇺🇬 우간다(uganda) 순위 100  
애플 뮤직 🇺🇦 우크라이나(ukraine) 순위 100  
애플 뮤직 🇦🇪 아랍에미리트(united-arab-emirates) 순위 100  
애플 뮤직 🇺🇿 우즈베키스탄(uzbekistan) 순위 100  
애플 뮤직 🇻🇪 베네수엘라(venezuela) 순위 100  
애플 뮤직 🇻🇳 베트남(vietnam) 순위 100  
애플 뮤직 🇿🇼 짐바브웨(Zimbabwe) 순위 100

## 스포티파이(spotify) 뮤직 전세계 챠트

```
https://websseu.github.io/pythonMusic2/spotify/[cuntry]/[cuntry]Top100_[current_date].json
```

스포티파이 뮤직 🌏 글로벌(global) 순위 100  
스포티파이 뮤직 🇦🇷 아르헨티나(ar) 순위 100  
스포티파이 뮤직 🇦🇺 호주(au) 순위 100  
스포티파이 뮤직 🇦🇹 오스트리아(at) 순위 100  
스포티파이 뮤직 🇧🇾 벨라루스(by) 순위 100  
스포티파이 뮤직 🇧🇪 벨기에(be) 순위 100  
스포티파이 뮤직 🇧🇴 볼리비아(bo) 순위 100  
스포티파이 뮤직 🇧🇷 브라질(br) 순위 100  
스포티파이 뮤직 🇧🇬 불가리아(bg) 순위 100  
스포티파이 뮤직 🇨🇦 캐나다(ca) 순위 100  
스포티파이 뮤직 🇨🇱 칠레(cl) 순위 100  
스포티파이 뮤직 🇨🇴 콜롬비아(co) 순위 100  
스포티파이 뮤직 🇨🇷 코스타리카(cr) 순위 100  
스포티파이 뮤직 🇨🇿 체코(cz) 순위 100  
스포티파이 뮤직 🇩🇰 덴마크(dk) 순위 100  
스포티파이 뮤직 🇩🇴 도미니카 공화국(do) 순위 100  
스포티파이 뮤직 🇪🇨 에콰도르(ec) 순위 100  
스포티파이 뮤직 🇪🇬 이집트(eg) 순위 100  
스포티파이 뮤직 🇸🇻 엘살바도르(sv) 순위 100  
스포티파이 뮤직 🇪🇪 에스토니아(ee) 순위 100  
스포티파이 뮤직 🇫🇮 핀란드(fi) 순위 100  
스포티파이 뮤직 🇫🇷 프랑스(fr) 순위 100  
스포티파이 뮤직 🇩🇪 독일(de) 순위 100  
스포티파이 뮤직 🇬🇷 그리스(gr) 순위 100  
스포티파이 뮤직 🇬🇹 과테말라(gt) 순위 100  
스포티파이 뮤직 🇭🇳 온두라스(hn) 순위 100  
스포티파이 뮤직 🇭🇰 홍콩(hk) 순위 100  
스포티파이 뮤직 🇭🇺 헝가리(hu) 순위 100  
스포티파이 뮤직 🇮🇸 아이슬란드(is) 순위 100  
스포티파이 뮤직 🇮🇱 이스라엘(il) 순위 100  
스포티파이 뮤직 🇮🇹 이탈리아(it) 순위 100  
스포티파이 뮤직 🇯🇵 일본(jp) 순위 100  
스포티파이 뮤직 🇰🇿 카자흐스탄(kz) 순위 100  
스포티파이 뮤직 🇱🇻 라트비아(lv) 순위 100  
스포티파이 뮤직 🇱🇹 리투아니아(lt) 순위 100  
스포티파이 뮤직 🇱🇺 룩셈부르크(lu) 순위 100  
스포티파이 뮤직 🇲🇾 말레이시아(my) 순위 100  
스포티파이 뮤직 🇲🇽 멕시코(mx) 순위 100  
스포티파이 뮤직 🇲🇦 모로코(ma) 순위 100  
스포티파이 뮤직 🇳🇱 네덜란드(nl) 순위 100  
스포티파이 뮤직 🇳🇿 뉴질랜드(nz) 순위 100  
스포티파이 뮤직 🇳🇮 니카라과(ni) 순위 100  
스포티파이 뮤직 🇳🇬 나이지리아(ng) 순위 100  
스포티파이 뮤직 🇳🇴 노르웨이(no) 순위 100  
스포티파이 뮤직 🇵🇰 파키스탄(pk) 순위 100  
스포티파이 뮤직 🇵🇦 파나마(pa) 순위 100  
스포티파이 뮤직 🇵🇾 파라과이(py) 순위 100  
스포티파이 뮤직 🇵🇪 페루(pe) 순위 100  
스포티파이 뮤직 🇵🇭 필리핀(ph) 순위 100  
스포티파이 뮤직 🇵🇱 폴란드(pl) 순위 100  
스포티파이 뮤직 🇵🇹 포르투갈(pt) 순위 100  
스포티파이 뮤직 🇷🇴 루마니아(ro) 순위 100  
스포티파이 뮤직 🇸🇦 사우디아라비아(sa) 순위 100  
스포티파이 뮤직 🇸🇬 싱가포르(sg) 순위 100  
스포티파이 뮤직 🇸🇰 슬로바키아(sk) 순위 100  
스포티파이 뮤직 🇿🇦 남아프리카공화국(za) 순위 100  
스포티파이 뮤직 🇰🇷 대한민국(kr) 순위 100  
스포티파이 뮤직 🇪🇸 스페인(es) 순위 100  
스포티파이 뮤직 🇸🇪 스웨덴(se) 순위 100  
스포티파이 뮤직 🇨🇭 스위스(ch) 순위 100  
스포티파이 뮤직 🇹🇼 대만(tw) 순위 100  
스포티파이 뮤직 🇹🇭 태국(th) 순위 100  
스포티파이 뮤직 🇹🇷 튀르키예(tr) 순위 100  
스포티파이 뮤직 🇦🇪 아랍에미리트(ae) 순위 100  
스포티파이 뮤직 🇺🇦 우크라이나(ua) 순위 100  
스포티파이 뮤직 🇬🇧 영국(gb) 순위 100  
스포티파이 뮤직 🇺🇸 미국(us) 순위 100  
스포티파이 뮤직 🇺🇾 우루과이(uy) 순위 100  
스포티파이 뮤직 🇻🇪 베네수엘라(ve) 순위 100  
스포티파이 뮤직 🇻🇳 베트남(vn) 순위 100
