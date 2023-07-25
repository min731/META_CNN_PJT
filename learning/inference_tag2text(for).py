'''
 * The Tag2Text Model
 * Written by Xinyu Huang
'''
import argparse
import numpy as np
import random

import torch

from PIL import Image
from ram.models import tag2text_caption
from ram import inference_tag2text as inference
from ram import get_transform


parser = argparse.ArgumentParser(
    description='Tag2Text inferece for tagging and captioning')
parser.add_argument('--image',
                    metavar='DIR',
                    help='path to dataset',
                    default='images/1641173_2291260800.jpg')
parser.add_argument('--pretrained',
                    metavar='DIR',
                    help='path to pretrained model',
                    default='pretrained/tag2text_swin_14m.pth')
parser.add_argument('--image-size',
                    default=384,
                    type=int,
                    metavar='N',
                    help='input image size (default: 448)')
parser.add_argument('--thre',
                    default=0.68,
                    type=float,
                    metavar='N',
                    help='threshold value')
parser.add_argument('--specified-tags',
                    default='None',
                    help='User input specified tags')


if __name__ == "__main__":

    args = parser.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print("device : ",device)
    transform = get_transform(image_size=args.image_size)

    # delete some tags that may disturb captioning
    # 127: "quarter"; 2961: "back", 3351: "two"; 3265: "three"; 3338: "four"; 3355: "five"; 3359: "one"
    delete_tag_index = [127,2961, 3351, 3265, 3338, 3355, 3359]

    #######load model
    model = tag2text_caption(pretrained=args.pretrained,
                             image_size=args.image_size,
                             vit='swin_b',
                             delete_tag_index=delete_tag_index)
    model.threshold = args.thre  # threshold for tagging
    model.eval()

    model = model.to(device)

    from glob import glob
    import pandas as pd
    import time
    from tqdm import tqdm

    class_names = ['Normal','Rainy','Snowy']
    # class_names = ['Snowy','Normal','Rainy']
    # class_names = ['Rainy','Snowy']
    # class_names = ['Snowy']
    # class_names = ['Rainy']
    preds_dict = {'rain':1,'Rain':1,'rainy':1,'Rainy':1,'wet':1,'Wet':1,
                  'snow':2,'Snow':2,'snowy':2,'Snowy':2
    }

    # preds_dict = {'rain':2,'Rain':2,'rainy':2,'Rainy':2,'wet':2,'Wet':2,'foggy':2,'Foggy':2,
    #                 'snow':0,'Snow':0,'snowy':0,'Snowy':0
    # }

    specified_tags = 'weather'
    data = []
    classes = []
    labels = []
    preds =[]

    tags = []
    spe_tags = []
    captions = []
    corr = []

    corr = 0    
    cnt = 0

    start = time.time()

    for class_name in class_names:

        images_path = 'D:/Weather conditions driving classification data (All)/images/'+class_name+'/'

        images = glob(images_path+'*.jpg')

        total_cor = len(images)
        label = class_names.index(class_name)

        for image in tqdm(images):
            # if cnt > 1000 :
            #     break
            data.append(image.split("/")[-1])

            image = transform(Image.open(image)).unsqueeze(0).to(device)

            res = inference(image, model, specified_tags)

            in_value = False

            tag = res[0].replace(" ","").split("|")
            caption = res[2].split()

            # print("tag : ",tag)
            # print("caption : ",caption)

            for k in preds_dict.keys():
                # tags에서 확인
                if k in tag:
                    in_value = True
                    pred = preds_dict[k]
                    preds.append(pred) 
                    break

                # caption에서 확인
                if k in caption:
                    in_value = True
                    pred = preds_dict[k]
                    preds.append(pred)
                    break
            
            # Rainy,Snowy 아니면 Normal
            if not in_value:
                pred = 0
                preds.append(pred)

            tags.append([res[0]])
            spe_tags.append(res[1])
            captions.append(res[2])
            classes.append(class_name)
            labels.append(label)

            if label == pred:
                corr += 1
            
            cnt += 1

    end = time.time()

    print("Test dataset :",cnt,"Total inference time : ",end-start)
    print("Inference 1 data per second : ",(end-start)/cnt)
    df = pd.DataFrame({'data':data,'class':classes,'label':labels,'pred':preds,'tag':tags,'spe_tag':spe_tags,'caption':captions})
    df = df[['class','data','tag','spe_tag','caption','label','pred']]
    df.to_csv('C:/backend_study/metaverse_academy/특강_Serving/recognize_anything/images_classification/tag2text_image_classification(road_surface).csv',index=False)

    total_corr = corr/cnt
    print("corr : ",corr)
    print("cnt : ",cnt)
    print("Accuracy : ",total_corr)

    f = open("log_07_13.txt", 'w')
    f.write("Test dataset : " + str(cnt) + " , Total inference time : " + str(end-start)+"\n")
    f.write("Inference 1 data per second : " + str((end-start)/cnt)+"\n")
    f.write("Accuracy : " + str(total_corr)+"\n")
    f.close()

    # conda activate ram
    # 실행 명령어
    # python inference_tag2text(for).py --pretrained D:/open_source_models/tag2text/tag2text_swin_14m.pth --specified-tags "weather"
    # python inference_tag2text.py  --image images/demo/demo11.jpg --pretrained D:/open_source_models/tag2text/tag2text_swin_14m.pth --specified-tags "princess"
    # python inference_tag2text.py  --image images/demo/demo9.jpg --pretrained D:/open_source_models/tag2text/tag2text_swin_14m.pth --specified-tags "road,surface"
    # python inference_tag2text(for).py --pretrained D:/open_source_models/tag2text/tag2text_swin_14m.pth --specified-tags "road,surface"