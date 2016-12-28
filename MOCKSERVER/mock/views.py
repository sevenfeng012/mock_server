#-*- coding: utf-8
from django.shortcuts import render,HttpResponse
from django.http import Http404, HttpResponseRedirect, HttpResponseServerError
from json import dumps
from django.core import serializers

from .models import API
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

import time
ISOTIMEFORMAT='%Y-%m-%d %X'

currentTime = time.strftime( ISOTIMEFORMAT, time.localtime() )

currentTime = 1477968610

def listAllFeeds(request,**kwargs):

    jsonData = []
    jsonData1 = []

    jsonTemplate = {}

    # for item in allFeedObjects:
    #     json = {}
    #     json['_id']=item._id
    #     json['createTime']=item.createTime
    #     summary = {}
    #     summary['content'] = item.summary.content
    #     # summary['viewCount'] = item.summary.viewCount
    #     summary['viewCount'] = 123
    #     # summary['replyCount'] = item.summary.replyCount
    #     summary['replyCount'] = 5647
    #     summary['threadImg'] = item.summary.threadImg
    #     # summary['topicId'] = item.summary.topicId
    #     summary['topicId'] = 4356435
    #     # summary['subType'] = item.summary.subType
    #     summary['subType'] = 8
    #     summary['subject'] = item.summary.subject
    #     summary['postTime'] = item.summary.postTime
    #
    #     user = {}
    #     # user['userId'] = item.summary.user.userId
    #     user['userId'] = 12345
    #     user['userName'] = item.summary.user.userName
    #     user['avatar'] = item.summary.user.avatar
    #     user['intro'] = item.summary.user.intro
    #     user['utPath'] = item.summary.user.utPath
    #     user['rankImg'] = item.summary.user.rankImg
    #
    #     summary['user'] = user
    #     summary['replyTime'] = item.summary.replyTime
    #     summary['topicTag'] = item.summary.topicTag
    #     summary['programName'] = item.summary.programName
    #     summary['programImg'] = item.summary.programImg
    #     summary['producer'] = item.summary.producer
    #
    #     attachList = {}
    #     # attachList['subject']=item.summary.audioAttachList.subject
    #     # attachList['liveUrl']=item.summary.audioAttachList.liveUrl
    #     # attachList['img']=item.summary.audioAttachList.img
    #     # attachList['duration']=item.summary.audioAttachList.duration
    #     # attachList['phId']=item.summary.audioAttachList.phId
    #     # attachList['count']=item.summary.audioAttachList.count
    #
    #     attachList['subject']='sfdfadsdf'
    #     attachList['liveUrl']='sdfdsfdsdf'
    #     attachList['img']='sdfdsfsd'
    #     attachList['duration']='fasfdd'
    #     attachList['phId']='fsdfds'
    #     attachList['count']='adfddsf'
    #
    #     summary['audioAttachList'] = attachList
    #
    #     summary['presenter'] = item.summary.presenter
    #     summary['topicType'] = item.summary.topicType
    #     summary['programId'] = item.summary.programId
    #
    #     shareInfo = {}
    #     shareInfo['acc']=item.summary.shareInfo.aac
    #     shareInfo['link']=item.summary.shareInfo.link
    #     shareInfo['title']=item.summary.shareInfo.title
    #     shareInfo['friendTitle']=item.summary.shareInfo.friendTitle
    #     shareInfo['content']=item.summary.shareInfo.content
    #     shareInfo['img']=item.summary.shareInfo.img
    #
    #     summary['shareInfo'] = shareInfo
    #
    #     json['summary']=summary
    #
    #     jsonTemplate = json
    #
    #     jsonData.append(json)


    for item in range(0,21,1):
        json = {}
        json['_id']=item
        json['createTime']='2016-11-01 10:50:10'
        summary = {}
        summary['content'] = ''
        summary['viewCount'] = 123
        summary['replyCount'] = 5647
        summary['threadImg'] = 'http://img-ossimg-test.ajmide.com/avatar/685306-1BHRMM.png'
        summary['topicId'] = 6347604
        summary['subType'] = item
        summary['subject'] = '万恶天天有'
        summary['postTime'] = '2016-10-13 13:39:27'

        user = {}
        user['userId'] = 10049
        user['userName'] = "王颖"
        user['avatar'] = 'http://img-ossimg.ajmide.com/avatar/10049.png'
        user['intro'] = ''
        user['utPath'] = ''
        user['rankImg'] = 'http://img-ossimg-test.ajmide.com/program/4141-level-1A8ETz.png'

        summary['user'] = user
        summary['replyTime'] = '2014-10-16 13:07:56'
        summary['topicTag'] = '官'
        summary['programName'] = '股市大家谈'
        summary['programImg'] = 'http://img-ossimg.ajmide.com/program/10114-1y4I2F.png'
        summary['producer'] = "第一财经广播"

        attachList = {}

        attachList['subject']='Tt'
        attachList['liveUrl']='http://media.live.ajmide.com/z1.ajmide.aj1477968610/20161101.m3u8'
        attachList['img']='http://img-ossimg.ajmide.com/program/10114-1y4I2F.png'
        attachList['duration']='153'
        attachList['phId']='6346623'
        attachList['count']='45'

        if item%3==0:
            summary['audioAttachList'] = [attachList]
            summary['contentAttachList']=[]
            summary['mediaAttachList'] = []

        elif item%3==1:
            summary['audioAttachList'] = []
            summary['contentAttachList'] = [
                {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'},
                {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'},
                {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'},
                {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'},
                {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'}]
            summary['mediaAttachList'] = []
        elif item%3==2:
            summary['audioAttachList'] = [attachList]
            summary['contentAttachList']=[]
            summary['mediaAttachList'] = [
                {
                    'url': 'http://media.live.ajmide.com/z1.ajmide.aj1477968610/20161101.m3u8',
                    'duration': 190
                },
                {
                    'url': 'http://media.live.ajmide.com/z1.ajmide.aj1477968610/20161101.m3u8',
                    'duration': 289
                },
                {
                    'url': 'http://media.live.ajmide.com/z1.ajmide.aj1477968610/20161101.m3u8',
                    'duration': 30
                },
            ]





        summary['presenter'] = "包嵘、王颖"
        summary['topicType'] = item
        summary['programId'] = '10114'

        shareInfo = {}
        shareInfo['acc']='http://m.ajmide.com/p.html?p=10114&t=801136'
        shareInfo['link']='http://m.ajmide.com/p.html?p=10114&t=10766'
        shareInfo['title']='JamesQIn：0906置顶贴_new1'
        shareInfo['friendTitle']='JamesQIn：0906置顶贴_new1'
        shareInfo['content']='0906置顶贴内容_new2'
        shareInfo['img']='http://img-ossimg.ajmide.com/program/10114-1y4I2F.png'

        summary['shareInfo'] = shareInfo

        json['summary']=summary

        jsonTemplate = json

        jsonData.append(json)

        jsonData1.append(summary)


    formatJson = {}
    formatJson['version']=0

    formatJson['carousels']=[
        {
        'statPosition':0,
        'img':'http://img-ossimg.ajmide.com/avatar/2424092-1C1MPv.png',
        'schema':'afddfas'
        },
        {
            'statPosition': 1,
            'img': 'http://img-ossimg.ajmide.com/avatar/3139618-1BZkfd.png',
            'schema': 'afddfas'
        },
        {
            'statPosition': 3,
            'img': 'http://img-ossimg.ajmide.com/avatar/2424092-1C1MPv.png',
            'schema': 'afddfas'
        }
    ]

    formatJson['hotTopics']=jsonData

    formatJson['feeds']=[
        {
            'type':0,
            'position':1,
            'programList':[
            ],
            'albumList':[],
            'voiceList':[jsonData1[0],jsonData1[5],jsonData1[2]],
            'activityList':[
            ]
        },
        {
            'type': 1,
            'position': 3,
            'programList': [

            ],
            'albumList': [jsonData1[0], jsonData1[4], jsonData1[2]],
            'voiceList': [],
            'activityList': [
            ]
        },
        {
            'type': 2,
            'position': 6,
            'programList': [
                {
                    'id': 3,
                    'producer': 'sffs',
                    'name': 'fdsadfsf',
                    'img': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'
                },
                {
                    'id': 4,
                    'producer': 'sffs',
                    'name': 'fdsadfsf',
                    'img': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'
                }
            ],
            'albumList': [],
            'voiceList': [],
            'activityList': [
            ]
        },
        {
            'type': 3,
            'position': 7,
            'programList': [
            ],
            'albumList': [],
            'voiceList': [],
            'activityList': [
                {
                    'actId': 0,
                    'subject': 'sdfadsf',
                    'content': 'fsdjkfdsl',
                    'contentAttachList': [{'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'},
                                          {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'}],
                    'beginTime': '2016-10-13 13:39:27',
                    'endTime': '2016-10-13 13:39:27',
                    'schema': 'fsdjkfdsl',
                    'topicTag': '精',
                    'pushType': 'fsdjkfdsl',
                    'user': {
                        'userId': '10019',
                        'userName': '的广告歌vhj',
                        'avatar': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png',
                        'intro': 'fsdjkfdsl',
                        'utPath': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png',
                        'rankImg': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png',
                    },
                },
                {
                    'actId': 12345556,
                    'subject': 'sdfadsf',
                    'content': 'fsdjkfdsl',
                    'contentAttachList': [{'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'},
                                          {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'}
                        , {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'}
                        , {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'}
                        , {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'}
                        , {'url': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png'}],

                    'beginTime': 'fsdjkfdsl',
                    'endTime': 'fsdjkfdsl',
                    'schema': 'fsdjkfdsl',
                    'topicTag': 'fsdjkfdsl',
                    'pushType': 'fsdjkfdsl',
                    'user': {
                        'userId': '685393',
                        'userName': 'tester昵称',
                        'avatar': 'http://img-ossimg-test.ajmide.com/avatar/10019-1AIGhn.png',
                        'intro': 'fsdjkfdsl',
                        'utPath': 'fsdjkfdsl',
                        'rankImg': 'http://img-ossimg-test.ajmide.com/program/6394-level-1AbGiv.png',
                    },
                }
            ]
        }
    ]


    context = {'code':'0',
               'key':'',
               'message':'No Datas',
               'time':currentTime,
               'data':{}
               }

    return HttpResponse(dumps(context),content_type='application/json')


def listPrograms(request,**kwargs):
    json = {
            "RollList": [
      {
        "imgPath": "http://img-ossimg-test.ajmide.com/upload/201611/15/000-1-582aa125cf50b_1080x544.png",
        "schema": "ajmide://wireless/toProgram?name=%E8%B7%B3%E8%BD%AC%E7%A4%BE%E5%8C%BA%E4%B8%93%E9%A2%98&programId=11646",
        "position": "轮播图,1|zid:3111@tp:zt,1"
      },
      {
        "imgPath": "http://img-ossimg-test.ajmide.com/upload/201611/10/000-1-5823e3abcde97_1020x330.png",
        "schema": "ajmide://wireless/toLink?url=http%3A%2F%2Fm.ajmide.com%2Fplugin%2Fsingle_audio%2Findex.html%3Faid%3D53",
        "position": "轮播图,1|zid:3047@tp:zt,2"
      },
      {
        "imgPath": "http://img-ossimg-test.ajmide.com/upload/201611/10/000-1-5823e3ce14210_1020x330.png",
        "schema": "ajmide://wireless/toLink?url=http%3A%2F%2Fm.ajmide.com%2Fplugin%2Fevent%2Findex.html%3Feid%3D76",
        "position": "轮播图,1|zid:3044@tp:zt,3"
      },
      {
        "imgPath": "http://img-ossimg-test.ajmide.com/upload/201611/10/000-1-5823e4448926b_1020x330.png",
        "schema": "ajmide://wireless/toLink?url=http%3A%2F%2Fm.ajmide.com%2Fplugin%2Fevent%2Findex.html%3Feid%3D75",
        "position": "轮播图,1|zid:3043@tp:zt,4"
      },
      {
        "imgPath": "http://img-ossimg-test.ajmide.com/upload/201611/10/000-1-5823e4879e593_1020x330.jpg",
        "schema": "ajmide://wireless/toLink?url=http%3A%2F%2Fm.ajmide.com%2Fplugin%2Fspecial%2Findex.html%3Fzid%3D3023",
        "position": "轮播图,1|zid:3023@tp:zt,5"
      }
    ],
    "rankingList": [

      {
        "configName": "节目点赞榜",
        "configImg": "http://img-ossimg.ajmide.com/program/6849-config-1AuT3P.jpg",
        "configUrl": "http://m.ajmide.com/ranklist/like/index.html",
        "configIconImg": ""
      },
      {
        "configName": "节目鲜花棒",
        "configImg": "http://img-ossimg.ajmide.com/program/9749-config-1AuT44.jpg",
        "configUrl": "http://m.ajmide.com/ranklist/flower/index.html",
        "configIconImg": ""
      },
      {
        "configName": "富豪榜",
        "configImg": "http://img-ossimg.ajmide.com/program/689-config-1AuT4m.jpg",
        "configUrl": "http://m.ajmide.com/ranklist/rich/index.html",
        "configIconImg": ""
      },
      {
        "configName": "意见领袖榜",
        "configImg": "http://img-ossimg.ajmide.com/program/6493-config-1AuT4z.jpg",
        "configUrl": "http://m.ajmide.com/ranklist/advice/index.html",
        "configIconImg": ""
      }
    ],
    "programList": [
      {
        "type": "3",
        "name": "本地电台",
        "list": [
          {
            "id": "3",
            "name": "上海交通广播",
            "position": "本地电台,2|上海交通广播,1"
          },
          {
            "id": "597",
            "name": "东上海之声",
            "position": "本地电台,2|东上海之声,2"
          },
          {
            "id": "697",
            "name": "解放日报",
            "position": "本地电台,2|解放日报,3"
          },
          {
            "id": "754",
            "name": "上海新闻综合频道",
            "position": "本地电台,2|上海新闻综合频道,4"
          },
          {
            "id": "755",
            "name": "上海娱乐频道",
            "position": "本地电台,2|上海娱乐频道,5"
          },
          {
            "id": "756",
            "name": "东方卫视",
            "position": "本地电台,2|东方卫视,6"
          },
          {
            "id": "768",
            "name": "浦东沸点100",
            "position": "本地电台,2|浦东沸点100,7"
          },
          {
            "id": "770",
            "name": " 网络电台",
            "position": "本地电台,2| 网络电台,8"
          },
          {
            "id": "771",
            "name": "上海广播电台",
            "position": "本地电台,2|上海广播电台,9"
          },
          {
            "id": "780",
            "name": "阿基米德",
            "position": "本地电台,2|阿基米德,10"
          },
          {
            "id": "781",
            "name": " 东方广播中心采访部",
            "position": "本地电台,2| 东方广播中心采访部,11"
          },
          {
            "id": "15",
            "name": "上海k98",
            "position": "本地电台,2|上海k98,12"
          },
          {
            "id": "14",
            "name": "东广新闻台",
            "position": "本地电台,2|东广新闻台,13"
          },
          {
            "id": "4",
            "name": "Love Radio",
            "position": "本地电台,2|Love Radio,14"
          },
          {
            "id": "5",
            "name": "上海故事广播",
            "position": "本地电台,2|上海故事广播,15"
          },
          {
            "id": "6",
            "name": "五星体育广播",
            "position": "本地电台,2|五星体育广播,16"
          },
          {
            "id": "7",
            "name": "第一财经广播",
            "position": "本地电台,2|第一财经广播,17"
          },
          {
            "id": "8",
            "name": "上海戏剧曲艺广播",
            "position": "本地电台,2|上海戏剧曲艺广播,18"
          },
          {
            "id": "9",
            "name": "上海新闻广播",
            "position": "本地电台,2|上海新闻广播,19"
          },
          {
            "id": "10",
            "name": "浦江之声广播",
            "position": "本地电台,2|浦江之声广播,20"
          },
          {
            "id": "11",
            "name": "899驾车调频",
            "position": "本地电台,2|899驾车调频,21"
          },
          {
            "id": "12",
            "name": "经典947",
            "position": "本地电台,2|经典947,22"
          },
          {
            "id": "13",
            "name": "动感101",
            "position": "本地电台,2|动感101,23"
          },
          {
            "id": "802",
            "name": "浦江之声广播电台1422",
            "position": "本地电台,2|浦江之声广播电台1422,24"
          }
        ]
      },
      {
        "type": "1",
        "name": "其他电台",
        "list": [
          {
            "id": "6",
            "name": "中央人民广播电台",
            "position": "其他电台,5|中央人民广播电台,1"
          },
          {
            "id": "7",
            "name": "中国国际广播电台",
            "position": "其他电台,5|中国国际广播电台,2"
          },
          {
            "id": "22",
            "name": "网络电台",
            "position": "其他电台,5|网络电台,3"
          },
          {
            "id": "8",
            "name": "其他省市台",
            "position": "其他电台,5|其他省市台,4"
          },
          {
            "id": "23",
            "name": "本地",
            "position": "其他电台,5|本地,5"
          }
        ]
      },
      {
        "type": "-1",
        "name": "内容分类",
        "list": [
          {
            "id": "127",
            "pid": "0",
            "position": "内容分类,3|音乐,1",
            "name": "音乐",
            "imgPath": "http://img-ossimg-test.ajmide.com/upload/201501/pic_sort01.jpg",
            "scategory_list": [
              {
                "id": "212",
                "pid": "127",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "134",
                "pid": "127",
                "name": "华语",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/134-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "135",
                "pid": "127",
                "name": "怀旧",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/135-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "131",
                "pid": "127",
                "name": "欧美",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/131-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "129",
                "pid": "127",
                "name": "排行榜",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/129-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "130",
                "pid": "127",
                "name": "古典",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/130-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "136",
                "pid": "127",
                "name": "民乐",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/136-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "137",
                "pid": "127",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/137-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "128",
            "pid": "0",
            "position": "内容分类,3|新闻,1",
            "name": "新闻",
            "imgPath": "http://img-ossimg-test.ajmide.com/upload/201501/pic_sort01.jpg",
            "scategory_list": [
              {
                "id": "213",
                "pid": "128",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "133",
                "pid": "128",
                "name": "地方",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/133-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "132",
                "pid": "128",
                "name": "综合",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/132-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "210",
                "pid": "128",
                "name": "读报",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/210-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "209",
                "pid": "128",
                "name": "军事",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/209-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "139",
            "pid": "0",
            "position": "内容分类,3|出行,1",
            "name": "出行",
            "imgPath": "http://img-ossimg-test.ajmide.com/upload/201501/pic_sort01.jpg",
            "scategory_list": [
              {
                "id": "214",
                "pid": "139",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "154",
                "pid": "139",
                "name": "晚高峰路况",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/154-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "153",
                "pid": "139",
                "name": "早高峰路况",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/153-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "155",
                "pid": "139",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/155-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "140",
            "pid": "0",
            "position": "内容分类,3|脱口秀,1",
            "name": "脱口秀",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "215",
                "pid": "140",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "156",
                "pid": "140",
                "name": "大咖",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/156-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "157",
                "pid": "140",
                "name": "特色",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/157-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "158",
                "pid": "140",
                "name": "校园",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/158-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "159",
                "pid": "140",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/159-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "141",
            "pid": "0",
            "position": "内容分类,3|财经,1",
            "name": "财经",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "216",
                "pid": "141",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "162",
                "pid": "141",
                "name": "股市",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/162-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "160",
                "pid": "141",
                "name": "新闻",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/160-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "161",
                "pid": "141",
                "name": "楼市",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/161-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "163",
                "pid": "141",
                "name": "理财",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/163-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "164",
                "pid": "141",
                "name": "公司",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/164-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "165",
                "pid": "141",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/165-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "142",
            "pid": "0",
            "position": "内容分类,3|服务,1",
            "name": "服务",
            "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/165-54cae0fe636bd_300x200.jpg",
            "scategory_list": [
              {
                "id": "217",
                "pid": "142",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "211",
                "pid": "142",
                "name": "民生",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/213-54cae0fe636bd_300x200.png"
              },
              {
                "id": "168",
                "pid": "142",
                "name": "维权",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/168-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "167",
                "pid": "142",
                "name": "法律",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/167-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "166",
                "pid": "142",
                "name": "问医",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/166-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "169",
                "pid": "142",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/169-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "143",
            "pid": "0",
            "position": "内容分类,3|体育,1",
            "name": "体育",
            "imgPath": "http://img-ossimg-test.ajmide.com/upload/201501/pic_sort01.jpg",
            "scategory_list": [
              {
                "id": "218",
                "pid": "143",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "173",
                "pid": "143",
                "name": "足球",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/173-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "170",
                "pid": "143",
                "name": "新闻",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/170-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "171",
                "pid": "143",
                "name": "访谈",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/171-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "175",
                "pid": "143",
                "name": "健身",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/175-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "172",
                "pid": "143",
                "name": "赛车",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/172-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "174",
                "pid": "143",
                "name": "篮球",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/174-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "176",
                "pid": "143",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/176-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "144",
            "pid": "0",
            "position": "内容分类,3|听书,1",
            "name": "听书",
            "imgPath": "http://img-ossimg-test.ajmide.com/upload/201611/15/000-1-582aa125cf50b_1080x544.png",
            "scategory_list": [
              {
                "id": "219",
                "pid": "144",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "177",
                "pid": "144",
                "name": "悬疑",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/177-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "179",
                "pid": "144",
                "name": "武侠",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/179-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "178",
                "pid": "144",
                "name": "综合",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/178-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "145",
            "pid": "0",
            "position": "内容分类,3|娱乐,1",
            "name": "娱乐",
            "imgPath": "http://img-ossimg-test.ajmide.com/upload/201611/15/000-1-582aa125cf50b_1080x544.png",
            "scategory_list": [
              {
                "id": "220",
                "pid": "145",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "182",
                "pid": "145",
                "name": "明星",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/182-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "181",
                "pid": "145",
                "name": "资讯",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/181-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "184",
                "pid": "145",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/184-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "146",
            "pid": "0",
            "position": "内容分类,3|公开课,1",
            "name": "公开课",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "221",
                "pid": "146",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "185",
                "pid": "146",
                "name": "讲座",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/185-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "186",
                "pid": "146",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/186-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "147",
            "pid": "0",
            "position": "内容分类,3|生活,1",
            "name": "生活",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "222",
                "pid": "147",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "189",
                "pid": "147",
                "name": "美食",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/189-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "187",
                "pid": "147",
                "name": "汽车",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/187-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "188",
                "pid": "147",
                "name": "旅游",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/188-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "190",
                "pid": "147",
                "name": "购物",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/190-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "191",
                "pid": "147",
                "name": "健康",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/191-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "192",
                "pid": "147",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/192-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "148",
            "pid": "0",
            "position": "内容分类,3|情感,1",
            "name": "情感",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "223",
                "pid": "148",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "194",
                "pid": "148",
                "name": "陪伴",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/194-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "193",
                "pid": "148",
                "name": "热线",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/193-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "195",
                "pid": "148",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/195-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "149",
            "pid": "0",
            "position": "内容分类,3|戏曲,1",
            "name": "戏曲",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "224",
                "pid": "149",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "197",
                "pid": "149",
                "name": "相声",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/197-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "198",
                "pid": "149",
                "name": "评书",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/198-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "196",
                "pid": "149",
                "name": "戏剧",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/196-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "199",
                "pid": "149",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/199-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "150",
            "pid": "0",
            "position": "内容分类,3|文化,1",
            "name": "文化",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "225",
                "pid": "150",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "201",
                "pid": "150",
                "name": "文学",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/201-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "200",
                "pid": "150",
                "name": "历史",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/200-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "202",
                "pid": "150",
                "name": "电影",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/202-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "203",
                "pid": "150",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/203-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "151",
            "pid": "0",
            "position": "内容分类,3|外语,1",
            "name": "外语",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "226",
                "pid": "151",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "204",
                "pid": "151",
                "name": "英语",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/204-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "205",
                "pid": "151",
                "name": "其他",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/205-54cae0fe636bd_300x200.jpg"
              }
            ]
          },
          {
            "id": "152",
            "pid": "0",
            "position": "内容分类,3|亲子,1",
            "name": "亲子",
            "imgPath": "",
            "scategory_list": [
              {
                "id": "227",
                "pid": "152",
                "name": "上周TOP50",
                "imgPath": "http://img-ossimg.ajmide.com/upload/201506/28/153-000-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "207",
                "pid": "152",
                "name": "育儿",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/207-54cae0fe636bd_300x200.jpg"
              },
              {
                "id": "206",
                "pid": "152",
                "name": "儿童故事",
                "imgPath": "http://img-ossimg-test.ajmide.com/upload/20150626/206-54cae0fe636bd_300x200.jpg"
              }
            ]
          }
        ]
      },
      {
        "type": "2",
        "name": "场景",
        "list": [
          {
            "id": "18",
            "name": "带孩子",
            "position": "场景,4|带孩子,1"
          },
          {
            "id": "16",
            "name": "跑步",
            "position": "场景,4|跑步,2"
          },
          {
            "id": "12",
            "name": "刚起床",
            "position": "场景,4|刚起床,3"
          },
          {
            "id": "14",
            "name": "醉了",
            "position": "场景,4|醉了,4"
          },
          {
            "id": "9",
            "name": "上班路",
            "position": "场景,4|上班路,5"
          },
          {
            "id": "15",
            "name": "学习",
            "position": "场景,4|学习,6"
          },
          {
            "id": "13",
            "name": "泡澡",
            "position": "场景,4|泡澡,7"
          },
          {
            "id": "17",
            "name": "想静静",
            "position": "场景,4|想静静,8"
          },
          {
            "id": "19",
            "name": "随便听听\n",
            "position": "场景,4|随便听听\n,9"
          },
          {
            "id": "11",
            "name": "准备睡",
            "position": "场景,4|准备睡,10"
          },
          {
            "id": "10",
            "name": "下班路",
            "position": "场景,4|下班路,11"
          }
        ]
      }
    ]
    }

    context = {'code':'0',
               'meta':'',
               'message':'',
               'data':json
               }

    return HttpResponse(dumps(context),content_type='application/json')

def programs(request,slug):
    api = None

    if slug ==None:
        slug = request.path_info[1:]

    try:
        allObjects = API.objects.all()
        for item in  allObjects:
            if item.slug == slug:
            # if cmp(item.slug,slug)==0:
                api = item
    except:
        return HttpResponse('没有找到内容')

    # html_parser = HTMLParser.HTMLParser()
    # infoContent = html_parser.unescape(api.content)

    if api == None:
        context = {'code': '0',
                   'meta': '',
                   'message': '',
                   'data': {}
                   }
    else:
        stream = BytesIO(api.content)
        infoContent = JSONParser().parse(stream)

        context = {'code': '0',
                   'meta': '',
                   'message': '',
                   'data': infoContent
                   }


    return HttpResponse(dumps(context), content_type='application/json')
