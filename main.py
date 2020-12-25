from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pymongo
from pymongo import MongoClient
# from bson import ObjectId
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()
url = 'mongodb://mongo-0.mongo,mongo-1.mongo,mongo-2.mongo:27017/'
client = MongoClient(url)

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

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/")
#에러뜰경우 root로

# @app.get("/")




@app.get("/cate/live/")
async def cate_live(datetime: str, cate: str="hot"):
    db = client['Real_time_Result']
    mycol = db[datetime]
    item = mycol.find_one({},{cate:1})
    result=[]
    for a in range(len(item[cate])):
        cur={}
        main_id=item[cate][str(i)]["id_list"][0]
        db=client['Info']
        main_news=db["Info"].find({"id":main_id})[0]
        cur['cluster_num']=i
        cur["img_url"]=main_news["img_url"]
        cur["title"]=main_news["title"]
        cur["url"]=main_news["url"]
        cur["press"]=main_news["press"]
        cur["keyword"]=item[cate][str(i)]["keyword_list"]
        cur["title_list"]=[]
        for now_id in item[cate][str(i)]["id_list"]:
            print(now_id)
            now_dic={}
            now_news=db["Info"].find({"id":now_id})
            now_dic["title"]=now_news["title"]
            now_dic["url"]=now_news["url"]
            now_dic["press"]=now_news["press"]
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

@app.get("/cate/live_nine/")
async def cate_live(datetime:str,cate:str="hot"):
    db=client['Real_time_Result']
    mycol=db[datetime]
    item=mycol.find_one({},{cate:1})
    result=[]
    num=0
    for a in range(len(item[cate])):
        num=num+1
        if num==10:
            break
        cur={}
        main_id=item[cate][str(i)]["id_list"][0]
        db=client['Info']
        main_news=db["Info"].find({"id":main_id})[0]
        cur['cluster_num']=i
        cur["img_url"]=main_news["img_url"]
        cur["title"]=main_news["title"]
        cur["url"]=main_news["url"]
        cur["press"]=main_news["press"]
        cur["keyword"]=item[cate][str(i)]["keyword_list"]
        cur["title_list"]=[]
        for now_id in item[cate][str(i)]["id_list"]:
            print(now_id)
            now_dic={}
            now_news=db["Info"].find({"id":now_id})
            now_dic["title"]=now_news["title"]
            now_dic["url"]=now_news["url"]
            now_dic["press"]=now_news["press"]
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

@app.get("/cate/day/")
async def cate_day(datetime:str,cate:str="hot"):
    db=client['Real_time_Result']
    mycol=db[datetime]
    item=mycol.find_one({},{cate:1})
    result=[]
    for a in range(len(item[cate])):
        cur={}
        main_id=item[cate][str(i)]["id_list"][0]
        db=client['Info']
        main_news=db["Info"].find({"id":main_id})[0]
        cur['cluster_num']=i
        cur["img_url"]=main_news["img_url"]
        cur["title"]=main_news["title"]
        cur["url"]=main_news["url"]
        cur["press"]=main_news["press"]
        cur["keyword"]=item[cate][str(i)]["keyword_list"]
        cur["title_list"]=[]
        for now_id in item[cate][str(i)]["id_list"]:
            print(now_id)
            now_dic={}
            now_news=db["Info"].find({"id":now_id})
            now_dic["title"]=now_news["title"]
            now_dic["url"]=now_news["url"]
            now_dic["press"]=now_news["press"]
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

@app.get("/cate/day_nine/")
async def cate_day(datetime:str,cate:str="hot"):
    db=client['Real_time_Result']
    mycol=db[datetime]
    item=mycol.find_one({},{cate:1})
    result=[]
    num=0
    for a in range(len(item[cate])):
        num=num+1
        if num==10:
            break
        cur={}
        main_id=item[cate][str(i)]["id_list"][0]
        db=client['Info']
        main_news=db["Info"].find({"id":main_id})[0]
        cur['cluster_num']=i
        cur["img_url"]=main_news["img_url"]
        cur["title"]=main_news["title"]
        cur["url"]=main_news["url"]
        cur["press"]=main_news["press"]
        cur["keyword"]=item[cate][str(i)]["keyword_list"]
        cur["title_list"]=[]
        for now_id in item[cate][str(i)]["id_list"]:
            print(now_id)
            now_dic={}
            now_news=db["Info"].find({"id":now_id})
            now_dic["title"]=now_news["title"]
            now_dic["url"]=now_news["url"]
            now_dic["press"]=now_news["press"]
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result