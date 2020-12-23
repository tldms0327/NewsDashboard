from fastapi import FastAPI
import uvicorn

from starlette.middleware.cors import CORSMiddleware
Hot_live_Data = [
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'image_url': "https://images.unsplash.com/random",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    }
]


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["Content-Type", "application/xml"],
)

@app.get("/")
async def root():
	return { "message" : "Hello World" }

@app.get("/test")
async def gogo(datetime:str,cate:str="Hot"):
    return Hot_live_Data

# @app.get("cate/live/")
# async def cate_live(datetime:str,cate:str="hot"):
#     print("first_route")
    
#     return

# @app.get("cate/day")
# async def cate_day(datetime=str,cate:str="hot"):
#     print("second_route")
#     return

# @app.get("word/live")
# async def word_live(cate:str,datetime=str):
#     print("third_route")
#     return

# @app.get("word/day")
# async def word_day(cate:str,datetime=str):
#     print("fourth_route")
#     return
# @app.on_event("startup")
# async def startup_db_client():
#     app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
#     app.mongodb = app.mongodb_client[settings.DB_NAME]


# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongodb_client.close()


# app.include_router(todo_router, tags=["tasks"], prefix="/task")

if __name__ == "__main__":
    uvicorn.run(
        "main.app", 
        host="localhost", 
        port=8000, 
        reload=True)