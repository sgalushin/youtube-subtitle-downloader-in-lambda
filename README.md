A simple AWS Lambda for downloading YouTube subtitles.
Uses [youtube-dl](https://github.com/ytdl-org/youtube-dl) underneath.

Subtitles are cached for the lifetime of a Lambda instance.

## Deployment

Requirements: 
 - [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
 - Python 3.8

Run `sam build && sam deploy --guided` in the project directory.

## Usage

HTTP GET request: `ENDPOINT_URL/LANGUAGE_CODE/VIDEO_ID` where Endpoint URL is a value of an output item of a deployed stack.

### Example

- Video: https://www.youtube.com/watch?v=hgg7lwi_xzc => `video id` is `hgg7lwi_xzc`
- Language: german => language code (according to [ISO 639-1:2002](https://en.wikipedia.org/wiki/ISO_639-1)) is `de`
- Endpoint URL: `https://75amc2323.execute-api.eu-west-1.amazonaws.com/Prod/`

Thus, to download german subtitles for this video, perform a GET request `https://75amc2323.execute-api.eu-west-1.amazonaws.com/Prod/de/hgg7lwi_xzc`.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](./LICENSE.txt) file.