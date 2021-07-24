A simple AWS Lambda for downloading YouTube subtitles.
Uses [youtube-dl](https://github.com/ytdl-org/youtube-dl) underneath.

## Deployment

Requirements: 
 - [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
 - Python 3.8

Run `sam build && sam deploy --guided` in the project directory.

## Usage

HTTP GET request: `ENDPOINT_URL/LANGUAGE/VIDEO_ID` where Endpoint URL is a value of an output item of a deployed stack.

### Example

- Video: https://www.youtube.com/watch?v=hgg7lwi_xzc => `video id` is `hgg7lwi_xzc`
- Langugage: german => language is `DE`
- Endpoint URL: `https://75amc2323.execute-api.eu-west-1.amazonaws.com/Prod/`

To download german subtitles for this video, perform a GET request `https://75amc2323.execute-api.eu-west-1.amazonaws.com/Prod/de/hgg7lwi_xzc`