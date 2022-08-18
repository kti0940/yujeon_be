import os
import boto3
import datetime

def model_run():
        # os.system("dir") # 현재 위치에 존재하는 파일 확인
        os.chdir("deep_learning_with_images") # 터미널 cd 커맨드와 동일함 -> 폴더 이동
        # os.system("dir") # 폴더 이동했는지 한번 더 확인했음
        os.system('python main.py') # 머신러닝 모델 실행시키기
        os.chdir("..")
        os.remove('media/uploads/input.jpg')

def control_s3(image, user):
    s3 = boto3.client('s3')

    now = datetime.datetime.now()
    now = now.strftime('%Y%m%d_%H%M%S')
    bucket = "migdracios"
    key = f"images/{user}/{now}.jpg"
    
    s3.upload_file(
    image, bucket, key,
    ExtraArgs={
        'ACL': 'public-read',
        'ContentType': "image/jpeg"
               }
    )
    url = f"https://{bucket}.s3.ap-northeast-2.amazonaws.com/{key}"
    return url