# Discord Cogs Application BoilerPlate
ext/cogs를 기반으로 한 디스코드 챗봇 소스 코드 템플릿입니다.

## Starting / Setting Application

### Prerequisite
이 프로젝트는 디스코드 챗봇 개발을 하는 프로그래머를 위해 제작되었습니다.

async와 await 구문 사용을 위해 3.7 이상의 파이썬 개발 환경이 필요합니다.

통합 개발 환경(IDE)는 [Visual Studio Code](https://code.visualstudio.com)를 권장합니다.
VSCode를 사용할 경우 워크스페이스 설정을 불러올수 있습니다.

```
$ cd .vscode
$ cp settings.example.json settings.json
```

### Installing
이 템플릿을 이용하기 위해서는 의존성 패키지를 설치해야 합니다.

```
$ pip install -r requirements.txt
```

또한 디스코드 봇 운영을 위해 디스코드 어플리케이션을 생성해야 합니다.
자세한 내용: [바로 가기](https://blog.naver.com/bainble0211/221955506407)

토큰을 발급 후 src/.env.example을 참고하여 .env를 작성합니다.

### Deployment
이 템플릿을 클론하고 src/main.py를 실행합니다.

```
$ git clone https://github.com/Bainble0211/dpy-cogs-boilerplate
# 혹은 다운로드
$ python src/main.py
```

## Built with
* [discord.py](https://discordpy.readthedocs.io/en/latest/) - 디스코드 봇 API 래퍼
* [Black](https://github.com/psf/black) - 파이썬 코드 포매터

### License
This project is licensed under the MIT License - see the
[LICENSE](https://github.com/Bainble0211/dpy-cogs-boilerplate/blob/main/LICENSE)

