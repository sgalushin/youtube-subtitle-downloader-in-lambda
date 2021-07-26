from download_subtitles import download_subtitles


def handler(event, context):
    lang = event['pathParameters']['lang']
    video_id = event['pathParameters']['videoId']
    result = download_subtitles(video_id, lang)
    if result:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/vtt; charset=utf-8",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS, GET"
            },
            "body": result
        }
    else:
        return {
            "statusCode": "404",
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS, GET"
            },
            "body": ""
        }